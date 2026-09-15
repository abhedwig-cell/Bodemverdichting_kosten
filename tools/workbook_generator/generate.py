from __future__ import annotations

import argparse
import csv
from datetime import date, datetime
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


def excel_column(index_zero_based: int) -> str:
    value = index_zero_based + 1
    letters = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters


def coerce_value(raw: str | None, definition: dict) -> object:
    if raw is None or raw == "":
        return None
    datatype = definition.get("datatype")
    if datatype == "integer":
        return int(raw)
    if datatype == "float":
        return float(raw)
    if datatype == "date":
        return datetime.strptime(raw, "%Y-%m-%d")
    return raw


def load_dataset_rows(
    root: Path,
    data_file: str,
    field_ids: list[str],
    fields: dict[str, dict],
) -> list[list[object]]:
    path = root / data_file
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        available = set(reader.fieldnames or [])
        missing = [field_id for field_id in field_ids if field_id not in available]
        if missing:
            raise ValueError(
                f"{data_file}: missing canonical columns required by workbook spec: {missing}"
            )
        return [
            [coerce_value(row[field_id], fields[field_id]) for field_id in field_ids]
            for row in reader
        ]


def build(root: Path, output: Path, git_commit: str | None = None) -> None:
    fields_schema = load_yaml(root / "schema/fields.yml")
    vertical_schema = load_yaml(root / "schema/tollebeek_vertical_slice.yml")
    evidence_schema = load_yaml(root / "schema/evidence_fields.yml")
    datasets_schema = load_yaml(root / "schema/datasets.yml")
    spec = load_yaml(root / "schema/artifacts/tollebeek_vertical_slice_workbook.yml")

    fields = merged_fields(fields_schema, vertical_schema)
    fields = merged_fields({"fields": fields}, evidence_schema)
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
    metadata_end = 3 + len(metadata)
    sheet.get_range(f"A4:B{metadata_end}").values = metadata
    sheet.get_range(f"A4:A{metadata_end}").format.fill = LIGHT_BLUE
    sheet.get_range(f"A4:A{metadata_end}").format.font = {"bold": True, "color": NAVY}
    sheet.get_range(f"A4:B{metadata_end}").format.wrap_text = True
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
            "The repository schema, evidence registers, documentation and code are canonical. This workbook is a generated review interface.",
        ],
        [
            "Unknowns",
            "Blank scientific values mean unknown/not supplied. Blank is never interpreted as zero.",
        ],
        [
            "Evidence chain",
            "SOURCE → EVIDENCE → CLAIMS → QUALIFICATION distinguishes source facts from project interpretation and intended-use qualification.",
        ],
        [
            "Dataset grain",
            "Every data sheet declares what one row represents before the table.",
        ],
        [
            "Header help",
            "Select a column header to see a compact field definition as an Excel input message.",
        ],
        [
            "Full definitions",
            "DATA_DICTIONARY contains the longer canonical field descriptions and guardrails.",
        ],
        [
            "Views",
            "VIEW_STATUS is a view only. It is not a source table.",
        ],
        [
            "Current scientific status",
            "Canonical Tollebeek evidence is now populated, but current/reference hydrological attribution, event transfer and current pump-cost estimates remain data-gated.",
        ],
    ]
    guide_end = 3 + len(guide)
    sheet.get_range(f"A4:B{guide_end}").values = guide
    style_header(sheet.get_range("A4:B4"))
    sheet.get_range(f"A4:B{guide_end}").format.wrap_text = True
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

    # Dataset sheets. Canonical CSV-backed datasets are populated; unresolved model
    # datasets remain one-row templates with explicit blanks.
    for dataset_spec in spec["datasets"]:
        dataset_id = dataset_spec["dataset_id"]
        sheet_name = dataset_spec["sheet_name"]
        dataset = datasets[dataset_id]
        data_file = dataset_spec.get("data_file")
        field_ids = dataset_spec["fields"]

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
            ["source_file", data_file or "generated template / not yet populated"],
        ]
        sheet.get_range("A2:B8").values = metadata_rows
        sheet.get_range("A2:A8").format.fill = LIGHT_BLUE
        sheet.get_range("A2:A8").format.font = {"bold": True, "color": NAVY}
        sheet.get_range("A2:B8").format.wrap_text = True

        header_row = 10
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

        data_rows = (
            load_dataset_rows(root, data_file, field_ids, fields)
            if data_file
            else []
        )
        if not data_rows:
            data_rows = [[None for _ in field_ids]]
        sheet.get_range_by_indexes(header_row, 0, len(data_rows), len(field_ids)).values = data_rows

        end_column = excel_column(len(field_ids) - 1)
        end_row = header_row + len(data_rows)
        table_name = ("T_" + sheet_name.replace("-", "_"))[:28]
        sheet.tables.add(
            f"A{header_row}:{end_column}{end_row}", True, table_name
        )
        sheet.freeze_panes.freeze_rows(header_row)

        for index, field_id in enumerate(field_ids):
            column = excel_column(index)
            definition = fields[field_id]
            width = 18
            if definition.get("datatype") == "string":
                width = 28
            if field_id.endswith("_id") or field_id == "evidence_ids":
                width = 28
            if definition.get("datatype") == "enum":
                width = 24
            if field_id in {
                "source_title",
                "source_notes",
                "evidence_statement",
                "intended_use",
                "guardrail",
                "claim_statement",
                "dependencies",
                "test_or_review",
                "qualification_notes",
            }:
                width = 42
            sheet.get_range(f"{column}:{column}").format.column_width = width
            if definition.get("datatype") == "date":
                sheet.get_range(f"{column}{header_row + 1}:{column}{end_row}").format.number_format = "yyyy-mm-dd"
        sheet.get_range(f"A1:{end_column}{end_row}").format.wrap_text = True

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
            "SOURCE / EVIDENCE / CLAIMS / QUALIFICATION",
            "CANONICAL_POPULATED",
            "The first Tollebeek source → evidence → claim → qualification slice is populated from canonical CSV registers.",
            "Extend the same pattern to soil, drainage and event evidence as those data arrive.",
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
            "PARTIAL_EVIDENCE",
            "Capacity/topology evidence exists, but canonical pump-asset configuration records are not yet populated here.",
            "Create versioned asset records after current Kievit/operation data are obtained.",
        ],
        [
            "Dispatch",
            "PUMP_DISPATCH",
            "BLOCKED_DATA",
            "Assist, availability, head and efficiency have no defaults.",
            "Operational telemetry/control data.",
        ],
    ]
    status_end = 3 + len(status_rows)
    sheet.get_range(f"A4:E{status_end}").values = status_rows
    style_header(sheet.get_range("A4:E4"))
    sheet.get_range(f"A4:E{status_end}").format.wrap_text = True
    sheet.get_range(f"C5:C{status_end}").conditional_formats.add_custom(
        '=OR(ISNUMBER(SEARCH("POPULATED",C5)),ISNUMBER(SEARCH("READY",C5)))',
        {"fill": GREEN},
    )
    sheet.get_range(f"C5:C{status_end}").conditional_formats.add_custom(
        '=OR(ISNUMBER(SEARCH("WAIT",C5)),ISNUMBER(SEARCH("PARTIAL",C5)))',
        {"fill": AMBER},
    )
    sheet.get_range(f"C5:C{status_end}").conditional_formats.add_custom(
        '=ISNUMBER(SEARCH("BLOCKED",C5))', {"fill": RED}
    )
    for column, width in {
        "A": 28,
        "B": 38,
        "C": 24,
        "D": 76,
        "E": 76,
    }.items():
        sheet.get_range(f"{column}:{column}").format.column_width = width
    sheet.freeze_panes.freeze_rows(4)

    # Compact structural verification before export.
    print(
        workbook.inspect(
            {
                "kind": "table",
                "range": f"00_METADATA!A1:B{metadata_end}",
                "include": "values,formulas",
                "table_max_rows": 24,
                "table_max_cols": 4,
            }
        ).ndjson
    )
    print(
        workbook.inspect(
            {
                "kind": "table",
                "range": "EVIDENCE!A1:K15",
                "include": "values,formulas",
                "table_max_rows": 16,
                "table_max_cols": 12,
            }
        ).ndjson
    )
    print(
        workbook.inspect(
            {
                "kind": "table",
                "range": "PUMP_DISPATCH!A1:M11",
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
