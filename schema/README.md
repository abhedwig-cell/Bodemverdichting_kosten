# Canonical schema

This directory contains the machine-readable semantic contracts for the project data model.

Current status: **composite Status-A-light baseline**.

There is deliberately no single global schema version that can be inferred from the highest component number. Core files and later bounded extensions matured at different moments. Their component versions remain visible, while validators merge them into one current semantic contract and reject incompatible duplicate definitions.

## Main components

- `entities.yml`: generic scientific and project entities and their grain;
- `relationships.yml`: cross-entity relations and foreign-key semantics;
- `datasets.yml`: stable dataset IDs, roles, grains, primary keys and storage mappings where applicable;
- `fields.yml`: core field definitions;
- `domain_fields_v0_3.yml`: later generic domain/run-control extensions;
- `evidence_fields.yml`: evidence/claim/qualification fields;
- `formal_traceability_fields.yml`: equation and capability-traceability fields;
- `profile_fields_v0_1.yml`, `event_forcing_fields_v0_1.yml`, `hydraulic_parameterization_fields_v0_1.yml`: bounded domain extensions;
- `controlled_vocabularies.yml`: controlled statuses and classifications;
- `workbook_contract.yml`: downstream workbook metadata and separation rules;
- `artifacts/`: artifact-specific compositions. These select canonical semantics but do not redefine them;
- `tollebeek_vertical_slice.yml`: bounded pilot overlay. Tollebeek-specific fields must not silently become generic project concepts.

## Authority rule

A field or dataset does not become scientifically admitted merely because it exists in the schema. Scientific use still requires the relevant source/evidence/claim/qualification route.

Dataset identity, grain and keys belong here rather than in workbook layout. Excel, dashboards and future application views consume the schema. They are not allowed to become a parallel semantic source.

`soil_state_id` is the current generic identifier introduced by the v0.3 domain extension. Legacy `state_id` references may remain during migration, but they must not create a second identity for the same soil-state object.

Run `python tools/validate_domain_schema.py` or the project-wide `python tools/validate_project.py` to check the merged contract.