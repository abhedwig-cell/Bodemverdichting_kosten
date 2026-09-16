# Source-model input baseline v0.1 — IMPLEMENT checkpoint

## Branch state

- branch: `work/source-model-input-baseline-v0.1`
- base authority: `main` at `f6e605b9cbf2d8c0dfa8f8df2b3ebc7a31644a0b`
- phase: IMPLEMENT complete, QUALIFY next

## Implemented canonical contract

- added input-readiness controlled vocabularies for requirement kind and readiness status;
- added `schema/data_request_fields.yml` for machine-readable request semantics;
- bound `data_request_register` to `data_requests/data_request_register.csv`;
- populated a bounded first-source-model prerequisite register with exactly ten roles:
  - spatial geometry;
  - soil profile context;
  - current soil state;
  - reference soil state;
  - drainage configuration;
  - event forcing;
  - initial hydrological state;
  - managed boundary;
  - land-use/crop context;
  - model configuration;
- linked requests only to already canonical evidence/claims/capabilities where such links exist;
- added explicit acceptance criteria, blocking reason and next action for each request;
- added `tools/validate_input_readiness.py` and a unit test;
- integrated readiness validation into `tools/validate_project.py` and CI compilation;
- documented register semantics and the scientific boundary in `data_requests/README.md` and `docs/23_source_model_input_baseline_v0_1.md`.

## Scientific boundary preserved

No requested input was populated with an invented value. No row is marked `ADMITTED`. Existing discovery routes, theory relations and historical method priors are represented as `PARTIAL_EVIDENCE` where appropriate, not as current project inputs.

Transfer/routing, pump operation and costs are deliberately excluded from the first source-model prerequisite set.

## Qualification required

QUALIFY must establish:

1. register/schema validation passes;
2. all evidence/claim/capability references resolve;
3. exactly the bounded ten prerequisite roles are represented once;
4. central project integrity gate passes;
5. existing unit/contract suite remains green;
6. diff contains no new hydrological/economic parameter, Tollebeek numerical result, source-model output or hidden default.

## Next permitted action

Open one PR from this branch and run GitHub CI. Do not merge on a failing gate.
