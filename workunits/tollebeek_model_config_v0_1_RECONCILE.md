# Tollebeek model configuration v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_MODEL_CONFIG`
Protocol phase: RECONCILE / CLASSIFY

## Canonical project authority

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical start: `main` @ `f6aba17c016a4b860f750a17678cc4ec51875a3f`
- branch: `work/tollebeek-model-config-v0.1`
- fixed event: `EVT_TOL_1998_OCT`
- readiness at start: `DR_SM_MODEL_CONFIG = MISSING`

No materially equivalent open model-config branch or PR was found before branch creation.

## What the project already commits to

The project formal model defines paired CURRENT/REFERENCE runs as one common source model `M(...)` with identical or explicitly equivalent controlled forcing, crop/land-use context, hydrological boundary, drainage and numerical/model configuration. The conceptual Tollebeek mapping explicitly uses a `paired SWAP run` as the implementation example.

This establishes SWAP as the intended source-model family for the first Tollebeek vertical slice, but it does **not** select an executable version, commit, numerical configuration, boundary option, crop model, drainage parameterization or initialization method.

The canonical schema already defines a `model_configuration` entity and register, but no concrete Tollebeek model-configuration row/storage authority is admitted.

## Live SWAP5 authority reconciliation

Live-checked against `abhedwig-cell/SWAP5` on 2026-09-16:

- live canonical branch: `integration/f-ci-canonical`
- live canonical head: `80c6faaa8a277d9596a6da7bc5d2244c0df1bb82`
- Status-A acceptance authority documented by current canonical: `992a5c657bfe10a10100f92e0cb77c4825ae65b6`
- scientific production baseline: `50346642bd565f79134ea17d5462e544b354998c`
- scientific production tree: `3b085d7dea3d3f3fce42ad9d8f259a8350205846`

The SWAP5 current-status contract explicitly states that the Status-A authority is later than the scientific production baseline but does not change its scientific production postimage. Later canonical work may advance governance/capability closure without changing the scientific production tree.

For cross-project execution pinning, these authorities therefore have different roles:

1. `50346642...` — **candidate scientific executable authority** for a reproducible first Tollebeek source-model experiment;
2. `992a5c657...` — **Status-A acceptance/documentation authority** for the admitted capability denominator around that production baseline;
3. `80c6faaa...` — **live canonical/governance head**, useful for current status and later closure records but not a substitute for explicitly pinning the scientific production commit;
4. SWAP 4.3.1 — **legacy/reference authority** for scientific preservation and comparison, not automatically the selected Tollebeek execution authority.

## Relevant admitted SWAP5 capability surface

Status-A documents the Richards/soil-water core, drainage and surface evaporation as admitted production capabilities within their bounded contracts. Restart v1 is available as a bounded committed-state capability. These are potentially relevant to the Tollebeek event experiment.

This checkpoint does not import unrelated capabilities or claim that all SWAP functionality is admitted. In particular, a bounded WOFOST runtime admission does not solve the missing 1998 crop-state problem, and no crop model is selected here.

## Why no model configuration is admitted yet

A reproducible Tollebeek model configuration must still declare at minimum:

- executable scientific authority and build/runtime provenance;
- selected profile/unit mapping;
- CURRENT/REFERENCE soil-state parameter sets;
- meteorological variable mapping/conversion from the admitted KNMI forcing to source-model inputs;
- event start/end and time-step/control policy;
- initial-state or warm-up/restart semantics;
- drainage representation and parameters;
- managed-boundary formulation and its historical 1998 mapping;
- crop/vegetation treatment or an explicitly qualified crop-independent/scenario design;
- output variables and sign/unit conventions used for attribution;
- equality/equivalence rule proving that the pair differs only in the admitted soil-state contrast.

Several of those dependencies remain `PARTIAL_EVIDENCE`, so writing a concrete configuration now would create convenience defaults or hide missing scientific inputs.

## Classification

- SWAP source-model family: **PROJECT-INTENDED / CONCEPTUALLY ESTABLISHED**
- SWAP5 scientific production baseline `50346642...`: **QUALIFIED CANDIDATE EXECUTABLE AUTHORITY, NOT YET PROJECT-ADMITTED**
- SWAP5 Status-A acceptance `992a5c657...`: **QUALIFIED CANDIDATE ACCEPTANCE AUTHORITY, NOT AN EXECUTABLE SUBSTITUTE**
- live SWAP5 canonical `80c6faaa...`: **CURRENT GOVERNANCE/STATUS CONTEXT**
- SWAP 4.3.1: **REFERENCE / PRESERVATION COMPARATOR**
- Tollebeek `model_configuration`: **NOT ADMITTED**
- `DR_SM_MODEL_CONFIG`: remains **MISSING** at this checkpoint.

## Next permitted action

A follow-up qualification may register the SWAP5 authority chain as evidence and advance `DR_SM_MODEL_CONFIG` only to `PARTIAL_EVIDENCE` if the project wants to formally qualify the executable-authority route before all run inputs are available.

Do not create a concrete model-configuration record until the unresolved drainage, managed-boundary, initial-state and land-use/crop decisions are either admitted or explicitly represented by separately qualified scenario/reconstruction semantics.

## Explicit exclusions

- no automatic SWAP5 selection merely because another repository exists;
- no live canonical head used as a moving executable pin;
- no SWAP 4.3.1 → SWAP5 equivalence claim beyond the accepted SWAP5 Status-A documentation;
- no numerical defaults;
- no boundary option selection;
- no drainage parameter defaults;
- no crop model/default crop;
- no initial-state convenience profile;
- no production run;
- missing remains missing.
