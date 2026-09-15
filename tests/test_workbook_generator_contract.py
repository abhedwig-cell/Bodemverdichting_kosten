from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/workbook_generator"))

from contract import field_help, load_yaml, merged_fields, validate_spec


def load_all():
    base = load_yaml(ROOT / "schema/fields.yml")
    overlay = load_yaml(ROOT / "schema/tollebeek_vertical_slice.yml")
    datasets = load_yaml(ROOT / "schema/datasets.yml")["datasets"]
    spec = load_yaml(ROOT / "schema/artifacts/tollebeek_vertical_slice_workbook.yml")
    return merged_fields(base, overlay), datasets, spec


class WorkbookGeneratorContractTests(unittest.TestCase):
    def test_artifact_spec_resolves(self):
        fields, datasets, spec = load_all()
        self.assertEqual(validate_spec(spec, fields, datasets), [])

    def test_help_contains_guardrail(self):
        fields, _, _ = load_all()
        text = field_help("delta_runoff_mm", fields["delta_runoff_mm"])
        self.assertIn("not field-edge", text)
        self.assertIn("mm/event", text)

    def test_no_unknown_field_names(self):
        fields, _, spec = load_all()
        for dataset in spec["datasets"]:
            for field_id in dataset["fields"]:
                self.assertIn(field_id, fields)


if __name__ == "__main__":
    unittest.main()
