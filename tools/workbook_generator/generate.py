from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from artifact_tool import SpreadsheetFile, Workbook

from contract import field_help, load_yaml, merged_fields, validate_spec

NAVY = "#17365D"
BLUE = "#1F4E78"
LIGHT_BLUE = "#D9EAF7"
GREEN = "#E2F0D9"
AMBER = "#FFF2CC"
RED = "#FCE4D6"
WHITE = "#FFFFFF"
GRAY = "#F2F2F2"


def style_header(rng) -> None:
    rng.format.fill = BLUE
    rng.format.font = {"bold": True, "color": WHITE}
    rng.format.wrap_text = True
    rng.format.vertical_alignment = "center"


def build(root: Path, output: Path, git_commit: str | None = None) -> None:
    fields_schema = load_yaml(root / "schema/fields.yml")
    vertical_schema = load_yaml(root / "schema/tollebeek_vertical_slice.yml")
    datasets_schema = load_yaml(root / "schema/datasets.yml")
    spec = load_yaml(root / "schema/artifacts/tollebeek_vertical_slice_workbook.yml")

    fields = merged_fields(fields_schema, vertical_schema)
    datasets = datasets_schema["datasets"]
    errors = validate_spec(spec, fields, datasets)
    if errors:
        raise ValueError("Workbook spec invalid:\n- " + "\n- ".join(errors))

    workbook = Workbook.create()
    artifact = spec["artifact"]

    # 00_METADATA
    sheet = workbook.worksheets.add("00_METADATA")
    sheet.merge_cells("A1:D2")
    sheet.get_range("A1").values = [[
        "Bodemverdichting kosten — Tollebeek vertical slice workbook"
    ]]
    sheet.get_range("A1").format.fill = NAVY
    sheet.get_range("A1").format.font = {
        "bold": True,
        "color": WHITE,
        "size": 18,
    }
    metadata = [
        ["project_id", artifact["project_id"]],
        ["artifact_id", artifact["artifact_id"]],
        ["artifact_class", artifact["artifact_class"]],
        ["artifact_version", artifact["artifact_version"]],
        ["framework_version", "Status-A-light / data-model v0.2"],
        ["schema_version", artifact["schema_version"]],
        ["generated_on", date.today().isoformat()],
        ["git_commit", git_commit or ""],
        ["purpose", artifact["purpose"]],
        ["scope", artifact["scope"]],
        ["intended_audience", artifact.get("intended_audience", "")],
        ["canonical_status", artifact["canonical_status"]],
        [
            "input_datasets",
            "; ".join(item["dataset_id"] for item in spec["datasets"]),
        ],
        ["known_limitations", artifact.get("known_limitations", "")],
        ["owner", artifact.get("owner", "")],
        ["repository", "https://github.com/abhedwig-cell/Bodemverdichting_kosten"],
    ]
    sheet.get_range(f"A4:B{3 + len(metadata)}").values = metadata
    sheet.get_range("A4:A19").format.fill = LIGHT_BLUE
    sheet.get_range("A4:A19").format.font = {"bold": True, "color": NAVY}
    sheet.get_range("A4:B19").format.wrap_text = True
    sheet.get_range("A:A").format.column_width = 28
    sheet.get_range("B:B").format.column_width = 92
    sheet.freeze_panes.freeze_rows(3)

    # 01_GUIDE
    sheet = workbook.worksheets.add("01_GUIDE")
    sheet.merge_cells("A1:H2")
    sheet.get_range("A1").values = [["How to read this workbook"]]
    sheet.get_range("A1").format.fill = NAVY
    sheet.get_range("A1").format.font = {
        "bold": True,
        "color": WHITE,
        "size": 18,
    }
    guide = [
        ["Principle", "Meaning"],
        [
            "Canonical meaning",
            "The repository schema, documentation and code are canonical. "
            "This workbook is a generated review interface.",
        ],
        [
            "Unknowns",
            "Blank scientific values mean unknown/not supplied. Blank is never "
            "interpreted as zero.",
        ],
        [
            "Dataset grain",
            "Every data sheet declares what one row represents before the table.",
        ],
        [
            "Header help",
            "Select a column header to see a compact field definition as an Excel "
            "input message.",
        ],
        [
            "Full definitions",
            "DATA_DICTIONARY contains the longer canonical field descriptions and "
            "guardrails.",
        ],
        [
            "Views",
            "VIEW_STATUS is a view only. It is not a source table.",
        ],
        [
            "Current scientific status",
            "The source→transfer→dispatch architecture is implemented, but Tollebeek "
            "hydrological attribution and current pump-cost estimates remain externally "
            "data-gated.",
        ],
    ]
    sheet.get_range(f"A4:B{3 + len(guide)}").values = guide
    style_header(sheet.get_range("A4:B4"))
    sheet.get_range(f"A4:B{3 + len(guide)}").format.wrap_text = True
    sheet.get_range("A:A").format.column_width = 30
    sheet.get_range("B:B").format.column_width = 96
    sheet.freeze_panes.freeze_rows(3)

    # DATA_DICTIONARY
    used_fields: list[str] = []
    for dataset_spec in spec["datasets"]:
        for field_id in dataset_spec["fields"]:
            if field_id not in used_fields:
                used_fields.append(field_id)
    rows = [[
        "field_id",
        "label",
        "description",
        "entity",
        "datatype",
        "unit",
        "nullable",
        "allowed_values",
        "guardrail",
    ]]
    for field_id in used_fields:
        definition = fields[field_id]
        rows.append([
            field_id,
            definition.get("label", ""),
            definition.get("description", ""),
            definition.get("entity", ""),
            definition.get("datatype", ""),
            definition.get("unit") or "",
            str(definition.get("nullable", "")),
            ", ".join(map(str, definition.get("allowed_values", []))),
            definition.get("guardrail", ""),
        ])
    sheet = workbook.worksheets.add("DATA_DICTIONARY")
    sheet.get_range(f"A1:I{len(rows)}").values = rows
    style_header(sheet.get_range("A1:I1"))
    sheet.get_range(f"A1:I{len(rows)}").format.wrap_text = True
    for column, width in {
        "A": 30,
        "B": 34,
        "C": 72,
        "D": 28,
        "E": 16,
        "F": 18,
        "G": 14,
        "H": 48,
        "I": 72,
    }.items():
        sheet.get_range(f"{column}:{column}").format.column_width = width
    sheet.tables.add(f"A1:I{len(rows)}", True, "DataDictionaryTable")
    sheet.freeze_panes.freeze_rows(1)

    # Dataset template sheets.
    for dataset_spec in spec["datasets"]:
        dataset_id = dataset_spec["dataset_id"]
        sheet_name = dataset_spec["sheet_name"]
        dataset = datasets[dataset_id]
        sheet = workbook.worksheets.add(sheet_name)
        sheet.merge_cells("A1:H1")
        sheet.get_range("A1").values = [[dataset_id]]
        sheet.get_range("A1").format.fill = NAVY
        sheet.get_range("A1").format.font = {
            "bold": True,
            "color": WHITE,
            "size": 15,
        }
        metadata_rows = [
            ["dataset_id", dataset_id],
            ["entity", dataset.get("entity", "")],
            ["role", dataset.get("role", "")],
            ["grain", dataset.get("grain", "")],
            ["primary_key", ", ".join(dataset.get("primary_key", []))],
            ["canonical_status", "MIGRATION_BASELINE"],
        ]
        sheet.get_range("A2:B7").values = metadata_rows
        sheet.get_range("A2:A7").format.fill = LIGHT_BLUE
        sheet.get_range("A2:A7").format.font = {"bold": True, "color": NAVY}
        sheet.get_range("A2:B7").format.wrap_text = True

        header_row = 9
        field_ids = dataset_spec["fields"]
        labels = [fields[field_id].get("label", field_id) for field_id in field_ids]
        sheet.get_range_by_indexes(header_row - 1, 0, 1, len(field_ids)).values = [labels]
        header = sheet.get_range_by_indexes(header_row - 1, 0, 1, len(field_ids))
        style_header(header)

        # Header prompts are generated from canonical field definitions.
        for index, field_id in enumerate(field_ids):
            cell = sheet.get_cell(header_row - 1, index)
            definition = fields[field_id]
            cell.data_validation = {
                "rule": {"type": "custom", "formula1": "=TRUE"},
                "prompt": {
                    "title": definition.get("label", field_id)[:32],
                    "message": field_help(field_id, definition),
                },
            }

        # A blank template row exposes the editable shape without inventing values.
        sheet.get_range_by_indexes(header_row, 0, 1, len(field_ids)).values = [
            [None for _ in field_ids]
        ]
        if len(field_ids) <= 26:
            end_column = chr(ord("A") + len(field_ids) - 1)
            table_name = ("T_" + sheet_name.replace("-", "_"))[:28]
            sheet.tables.add(
                f"A{header_row}:{end_column}{header_row + 1}", True, table_name
            )
        sheet.freeze_panes.freeze_rows(header_row)
        for index, field_id in enumerate(field_ids):
            column = chr(ord("A") + index)
            definition = fields[field_id]
            width = 18
            if definition.get("datatype") == "string":
                width = 24
            if field_id.endswith("_id"):
                width = 26
            if definition.get("datatype") == "enum":
                width = 24
            sheet.get_range(f"{column}:{column}").format.column_width = width
        sheet.get_range("A:B").format.column_width = 30
        sheet.get_range("A1:Z12").format.wrap_text = True

    # VIEW_STATUS is explicitly a view, not a source table.
    sheet = workbook.worksheets.add("VIEW_STATUS")
    sheet.merge_cells("A1:F2")
    sheet.get_range("A1").values = [["Vertical-slice readiness view"]]
    sheet.get_range("A1").format.fill = NAVY
    sheet.get_range("A1").format.font = {
        "bold": True,
        "color": WHITE,
        "size": 18,
    }
    status_rows = [
        ["Stage", "Dataset", "Status", "Why", "Next evidence/action"],
        [
            "Source/evidence",
            "SOURCE / EVIDENCE",
            "TEMPLATE_READY",
            "Workbook interface exists; source/evidence records are not populated here.",
            "Populate from canonical evidence registers.",
        ],
        [
            "Spatial source",
            "SPATIAL_UNIT",
            "WAIT_DATA",
            "Current OT.02 geometry/routing zones are not admitted in this workbook.",
            "Admit current spatial units.",
        ],
        [
            "Hydrological response",
            "HYDRO_RESPONSE",
            "BLOCKED_DATA",
            "Current/reference SWAP attribution is not yet qualified.",
            "Current soil/drainage state + paired runs.",
        ],
        [
            "Transfer",
            "TRANSFER_EVENT",
            "BLOCKED_DATA",
            "Delivery/routing is event-conditioned and cannot be defaulted.",
            "Event transfer evidence/routing model.",
        ],
        [
            "Pump assets",
            "PUMP_ASSET",
            "WAIT_DATA",
            "Installed/nominal values need canonical asset/evidence records before population.",
            "Reconcile asset register.",
        ],
        [
            "Dispatch",
            "PUMP_DISPATCH",
            "BLOCKED_DATA",
            "Assist, availability, head and efficiency have no defaults.",
            "Operational telemetry/control data.",
        ],
    ]
    sheet.get_range(f"A4:E{3 + len(status_rows)}").values = status_rows
    style_header(sheet.get_range("A4:E4"))
    sheet.get_range(f"A4:E{3 + len(status_rows)}").format.wrap_text = True
    sheet.get_range("C5:C10").conditional_formats.add_custom(
        '=ISNUMBER(SEARCH("READY",C5))', {"fill": GREEN}
    )
    sheet.get_range("C5:C10").conditional_formats.add_custom(
        '=ISNUMBER(SEARCH("WAIT",C5))', {"fill": AMBER}
    )
    sheet.get_range("C5:C10").conditional_formats.add_custom(
        '=ISNUMBER(SEARCH("BLOCKED",C5))', {"fill": RED}
    )
    for column, width in {
        "A": 28,
        "B": 30,
        "C": 22,
        "D": 72,
        "E": 72,
    }.items():
        sheet.get_range(f"{column}:{column}").format.column_width = width
    sheet.freeze_panes.freeze_rows(4)

    # Compact structural verification before export.
    print(
        workbook.inspect(
            {
                "kind": "table",
                "range": "00_METADATA!A1:B19",
                "include": "values,formulas",
                "table_max_rows": 20,
                "table_max_cols": 4,
            }
        ).ndjson
    )
    print(
        workbook.inspect(
            {
                "kind": "table",
                "range": "PUMP_DISPATCH!A1:M10",
                "include": "values,formulas",
                "table_max_rows": 12,
                "table_max_cols": 16,
            }
        ).ndjson
    )
    print(
        workbook.inspect(
            {
                "kind": "match",
                "search_term": "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
                "options": {"use_regex": True, "max_results": 100},
                "summary": "workbook generator formula scan",
            }
        ).ndjson
    )
    SpreadsheetFile.export_xlsx(workbook).save(str(output))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--git-commit", default="")
    args = parser.parse_args()
    build(args.root.resolve(), args.output.resolve(), args.git_commit or None)


if __name__ == "__main__":
    main()
