from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/workbook_generator"))

from contract import field_help, load_yaml, merged_fields, validate_spec


def load_all():
    base = load_yaml(ROOT / "schema/fields.yml")
    overlay = load_yaml(ROOT / "schema/tollebeek_vertical_slice.yml")
    datasets = load_yaml(ROOT / "schema/datasets.yml")["datasets"]
    spec = load_yaml(ROOT / "schema/artifacts/tollebeek_vertical_slice_workbook.yml")
    return merged_fields(base, overlay), datasets, spec


def test_artifact_spec_resolves():
    fields, datasets, spec = load_all()
    assert validate_spec(spec, fields, datasets) == []


def test_help_contains_guardrail():
    fields, _, _ = load_all()
    text = field_help("delta_runoff_mm", fields["delta_runoff_mm"])
    assert "not field-edge" in text
    assert "mm/event" in text


def test_no_unknown_field_names():
    fields, _, spec = load_all()
    for dataset in spec["datasets"]:
        for field_id in dataset["fields"]:
            assert field_id in fields
