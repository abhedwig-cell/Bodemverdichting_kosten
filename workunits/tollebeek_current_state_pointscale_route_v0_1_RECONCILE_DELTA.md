# Tollebeek CURRENT-state point/field publication recovery v0.1 — RECONCILE DELTA

Capability: `DR_SM_CURRENT_STATE`

Phase: `RECONCILE`

Original workunit base: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`

Latest concurrent canonical main reconciled during finalization:

`494d7e841f18ede0e93a4ec5a89c3b3d45a5eec7`

## Relevant state delta only

Since the original checkpoint, canonical `main` gained a broader CURRENT-state source-holder access package and a separate soil-state→hydraulic-parameterization architecture.

Relevant current-main facts:

- qualified source-holder route for the WER3382 / `Flevo - land in beweging` 2020–2021 raw point dataset;
- Aeres/WUR/Actieplan contact and referral routes;
- privacy-preserving holder-side OT.02 selection option when exact farm coordinates cannot be shared;
- DOI/public-metadata recovery review;
- explicit rule that related 2018 project data must not be conflated with the WER3382 regional campaign;
- soil-state→hydraulic transformation architecture is now qualified but all numerical Tollebeek hydraulic parameterization remains data-gated;
- `DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`; no numerical CURRENT state has been admitted.

## Collision decision

The workunit's earlier draft modification of `data_requests/tollebeek_current_state_data_request_v0_1.md` is superseded by the richer current-main version and is **not** carried forward.

The incremental scientific value retained from this workunit is narrower:

- exact identification of the related article: Van Orsouw et al. (2022), DOI `10.3390/agronomy12071669`;
- exact project-family funding link `RAAK.PRO02.021`;
- explicit 25-location single-field design;
- autumn-2018 sampling after a 2017 compaction event;
- source-native location description limited to eastern Flevoland / Noordoostpolder / edge of Emmeloord;
- data available on request;
- no public source-native coordinates or downloadable data object recovered;
- therefore classification `PROJECT_LINK_CONFIRMED_DISTINCT_2018_FIELD_DATA_ON_REQUEST`.

## Integration rule

Preserve current main unchanged except for the new detailed point/field publication classification note and resumable workunit checkpoints.

Do not replace or regress the source-holder handoff, DOI review, privacy rules, hydraulic transformation architecture or readiness state.

No readiness/evidence/schema/model-input mutation is authorized.

Next permitted action: merge current main into the existing workunit branch using a tree based on this latest main plus only the retained classification files; then qualify the clean delta.