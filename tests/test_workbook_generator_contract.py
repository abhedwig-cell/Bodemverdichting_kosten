from pathlib import Path
import csv
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/workbook_generator"))

from contract import (
    DATASET_METADATA_FIELDS,
    dataset_metadata_rows,
    field_help,
    load_yaml,
    merged_fields,
    validate_spec,
)


def load_all():
    base = load_yaml(ROOT / "schema/fields.yml")
    vertical = load_yaml(ROOT / "schema/tollebeek_vertical_slice.yml")
    evidence = load_yaml(ROOT / "schema/evidence_fields.yml")
    datasets = load_yaml(ROOT / "schema/datasets.yml")["datasets"]
    spec = load_yaml(ROOT / "schema/artifacts/tollebeek_vertical_slice_workbook.yml")
    fields = merged_fields(base, vertical)
    fields = merged_fields({"fields": fields}, evidence)
    return fields, datasets, spec


class WorkbookGeneratorContractTests(unittest.TestCase):
    def test_artifact_spec_resolves(self):
        fields, datasets, spec = load_all()
        self.assertEqual(validate_spec(spec, fields, datasets), [])

    def test_help_contains_guardrail(self):
        fields, _, _ = load_all()
        text = field_help("delta_runoff_mm", fields["delta_runoff_mm"])
        self.assertIn("not field-edge", text)
        self.assertIn("mm/event", text)

    def test_evidence_help_is_defined(self):
        fields, _, _ = load_all()
        text = field_help("evidence_statement", fields["evidence_statement"])
        self.assertIn("Atomic fact", text)

    def test_no_unknown_field_names(self):
        fields, _, spec = load_all()
        for dataset in spec["datasets"]:
            self.assertTrue(dataset.get("canonical_status"))
            for field_id in dataset["fields"]:
                self.assertIn(field_id, fields)

    def test_dataset_metadata_contract_matches_generator(self):
        workbook_contract = load_yaml(ROOT / "schema/workbook_contract.yml")
        required = tuple(
            workbook_contract["workbook"]["dataset_metadata"]["required"]
        )
        self.assertEqual(required, DATASET_METADATA_FIELDS)

        _, datasets, spec = load_all()
        sample_spec = spec["datasets"][0]
        sample_id = sample_spec["dataset_id"]
        rows = dataset_metadata_rows(sample_id, datasets[sample_id], sample_spec)
        self.assertEqual(tuple(row[0] for row in rows), DATASET_METADATA_FIELDS)

    def test_git_commit_is_required_artifact_metadata(self):
        workbook_contract = load_yaml(ROOT / "schema/workbook_contract.yml")
        required = set(workbook_contract["workbook"]["metadata_fields"]["required"])
        self.assertIn("git_commit", required)
        self.assertIn("schema_version", required)

    def test_csv_backed_datasets_have_required_columns(self):
        _, _, spec = load_all()
        for dataset in spec["datasets"]:
            data_file = dataset.get("data_file")
            if not data_file:
                continue
            with (ROOT / data_file).open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                available = set(reader.fieldnames or [])
            self.assertTrue(
                set(dataset["fields"]).issubset(available),
                msg=f"{data_file} does not expose the artifact's canonical field set",
            )


if __name__ == "__main__":
    unittest.main()
