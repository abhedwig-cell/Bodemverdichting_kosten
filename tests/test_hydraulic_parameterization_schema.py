from pathlib import Path
import sys
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_domain_schema import validate


class HydraulicParameterizationSchemaTests(unittest.TestCase):
    def test_domain_schema_integrity(self):
        self.assertEqual(validate(), [])

    def test_hydraulic_entity_dataset_and_relationships_exist(self):
        entities = yaml.safe_load((ROOT / "schema/entities.yml").read_text(encoding="utf-8"))["entities"]
        datasets = yaml.safe_load((ROOT / "schema/datasets.yml").read_text(encoding="utf-8"))["datasets"]
        rel = yaml.safe_load((ROOT / "schema/relationships.yml").read_text(encoding="utf-8"))["relationships"]
        fields = yaml.safe_load((ROOT / "schema/hydraulic_parameterization_fields_v0_1.yml").read_text(encoding="utf-8"))["fields"]
        self.assertIn("hydraulic_parameterization", entities)
        self.assertEqual(datasets["hydraulic_parameterization_register"]["primary_key"], ["hydraulic_parameterization_id"])
        self.assertEqual(rel["state_hydraulic_parameterization"]["foreign_key"], "hydraulic_parameterization.soil_state_id")
        self.assertEqual(rel["hydraulic_parameterization_run"]["foreign_key"], "model_run.hydraulic_parameterization_id")
        self.assertIn("hydraulic_parameterization_id", fields)
        self.assertIn("hydraulic_method_class", fields)
        self.assertIn("hydraulic_representation", fields)

    def test_no_numerical_parameterization_dataset_is_admitted(self):
        ds = yaml.safe_load((ROOT / "schema/datasets.yml").read_text(encoding="utf-8"))["datasets"]["hydraulic_parameterization_register"]
        self.assertNotIn("storage", ds)


if __name__ == "__main__":
    unittest.main()
