# Tollebeek scenario/reconstruction admissibility v0.1

Status: **DECISION-SURFACE QUALIFIED; NO INPUT ADMISSION**

Canonical basis: `main` @ `8ef90b123dbce0b9c855cd9a008405806ad6451b`.

## 1. Why this document exists

After the P1 readiness baseline, every required source-model input has an explicit route, but seven roles remain `PARTIAL_EVIDENCE`. This document defines which of those open roles are fundamentally dependent on new external observations, which may eventually be reconstructed, and which may support explicit scenario analysis.

The purpose is to allow productive next work without eroding the distinction between:

- observed or source-native historical evidence;
- bounded reconstruction;
- explicit scientific scenario;
- convenience default.

A convenience default is not an admissible scientific category.

## 2. Governing claim boundary

The canonical attribution equation compares CURRENT and REFERENCE under controlled forcing, crop/land use, geometry and boundary/system context. A modelled reference or reconstructed context is scientifically possible, but its provenance and uncertainty become part of the causal claim.

Therefore:

- **historical attribution** asks what happened, or what is defensibly reconstructable, for the real Tollebeek event/context;
- **scenario analysis** asks what would happen under explicitly declared conditions;
- scenario results must not be back-labelled as observed 1998 Tollebeek conditions.

## 3. Admissibility matrix

| P1 role | Historical closure | Reconstruction/scenario route | Minimum admission prerequisites | Claim boundary |
| --- | --- | --- | --- | --- |
| `CURRENT_SOIL_STATE` | New local/source-native evidence required for a historical/measured Tollebeek claim. | Synthetic compaction states are permitted only as separate scenario/sensitivity states. | Explicit layer grain; state variables; provenance; physical plausibility; no SoilPhys modal density relabelled as CURRENT; scenario ID and uncertainty. | May say “response under scenario state X”; may not say “current/actual Tollebeek compaction” without admitted evidence. |
| `REFERENCE_SOIL_STATE` | No independent external dataset is inherently mandatory, but construction depends on the admitted CURRENT state. | Evidence-based modelled counterfactual is permissible. Candidate forms include measured control, locally lower-compaction state, qualified agronomic reference or modelled decompacted state. | Same profile/layer grain as CURRENT; explicit variables changed; rationale/evidence; equality of all non-state dimensions; sensitivity to reference choice where material. | May estimate soil-state attribution only for the explicitly defined reference concept. No universal “uncompacted” claim. |
| `DRAINAGE_CONFIGURATION` | Source-native drainage evidence required to claim actual/current/historical configuration. | Explicit drainage scenarios are permissible for sensitivity. Historical reconstruction is only permissible if physical constraints narrow spacing/depth/resistance defensibly. | Geometry/applicability; depth/spacing or explicitly qualified equivalent relation; temporal applicability; uncertainty range; no zero-as-missing; no historical resistance used as current fact. | Scenario outputs are conditional on drainage scenario. They do not establish observed drainage configuration. |
| `INITIAL_HYDROLOGICAL_STATE` | Direct shallow observation preferred but not strictly mandatory if a reproducible initialization can be qualified. | Warm-up/restart reconstruction may be admissible. | Model configuration; forcing/warm-up period; boundary; drainage; crop/land use; convergence/stability criterion; same/equivalent initialization rule for CURRENT and REFERENCE; sensitivity to initialization. | May say “reconstructed initial state from protocol X”; may not say “observed initial groundwater/soil moisture” without observations. |
| `MANAGED_BOUNDARY` | Telemetry/operator records are required to call the boundary observed. | Bounded historical reconstruction may be admissible using historical topology, target levels, nominal capacities, event reports and emergency intervention constraints. | Historical topology only; event window; operating-rule hypotheses; plausible bounds; alternative reconstructions/ensemble where non-identifiable; sensitivity; no current IJsvogel backcast. | May say “historically constrained reconstruction”; may not say “observed 1998 hydrograph/control sequence” without telemetry. |
| `LAND_USE_CROP_CONTEXT` | Dated field/parcel evidence required to claim actual 1998 crop identity. | Crop scenarios are permissible. A crop-independent design is permissible only if crop-sensitive terms are genuinely excluded/neutralized by the scientific question and this is demonstrated, not assumed. | Explicit crop/scenario identity; phenology/rooting assumptions where relevant; identical scenario across CURRENT/REFERENCE pair; sensitivity across plausible crop classes if response is crop-sensitive. | May say “conditional on crop scenario X”; may not infer 1998 crop from LGN3/LGN4 or late-October timing. |
| `MODEL_CONFIGURATION` | No new external datum is inherently required for software authority; concrete configuration depends on all bound inputs. | One or more explicitly versioned historical-reconstruction or scenario configurations may be built after their dependencies are qualified. | SWAP5 executable pin; configuration ID; input references; forcing conversion; timestep/numerical controls; boundary/drainage/initial/crop semantics; outputs/sign/units; pair-equality rule. | Configuration identity does not upgrade the evidentiary class of its inputs. A scenario config remains a scenario config. |

## 4. Permitted sequencing

### 4.1 Work that can proceed before new external data

The following design work is scientifically useful now:

1. define candidate REFERENCE-state construction families without assigning numerical state values;
2. define a managed-boundary reconstruction protocol and uncertainty structure without choosing a single realized 1998 hydrograph;
3. define warm-up/restart qualification criteria without running them yet;
4. define crop-scenario semantics and claim labels;
5. define the schema needed to distinguish `OBSERVED`, `RECONSTRUCTED` and `SCENARIO` configuration inputs.

This work prepares later qualification but does not close any input gate.

### 4.2 Work that remains blocked on external evidence

The historical-attribution path still materially needs:

- source-native/local compaction measurements for CURRENT state;
- actual parcel drainage information if actual drainage is claimed;
- 1998 crop/vegetation evidence if actual crop is claimed;
- preferably 1998 managed-boundary telemetry/operator records;
- preferably shallow groundwater/soil-water observations near event start.

The final two items have a possible reconstruction path if direct data remain unavailable. CURRENT compaction state does not have an equivalent historical-reconstruction shortcut from the presently admitted evidence.

## 5. Reconstruction qualification requirements

A reconstruction may only move beyond `PARTIAL_EVIDENCE` when all of the following are explicit:

1. **target quantity** — exactly what historical variable/state is being reconstructed;
2. **constraints** — source-native facts that bound it;
3. **free assumptions** — quantities not identified by evidence;
4. **uncertainty representation** — interval, alternatives, ensemble or other explicit structure;
5. **identifiability statement** — what cannot be recovered uniquely;
6. **sensitivity test** — whether the project outcome materially changes across admissible reconstructions;
7. **claim language** — “reconstructed”, never “observed” unless it is observed;
8. **pair consistency** — the same reconstructed context must apply to CURRENT and REFERENCE unless the research question explicitly includes that dimension.

A single plausible number chosen from a broad range without the above structure is not a qualified reconstruction.

## 6. Scenario qualification requirements

A scenario must have:

- stable scenario ID and version;
- explicit scientific purpose;
- declared values/relations and provenance class `SCENARIO_ASSUMPTION` where applicable;
- bounded parameter ranges rather than hidden defaults where uncertainty is material;
- identical non-soil-state scenario dimensions across a simple CURRENT/REFERENCE pair;
- result labels that retain `SCENARIO_ONLY` semantics through downstream transfer and valuation.

A scenario may be highly useful for sensitivity, mechanism exploration, stress testing or acquisition prioritization. It is not evidence that the scenario occurred historically.

## 7. Recommended two-track programme

### Track H — historical attribution

Retain the current 1998 event as the target and continue acquiring source-native evidence. Use reconstruction only for quantities where the historical system is sufficiently constrained and uncertainty can be propagated honestly.

### Track S — bounded scenario experiment

A separate future workunit may define a minimal scenario experiment using admitted geometry/profile/forcing plus explicitly scenario-labelled CURRENT/REFERENCE state, drainage, boundary, initial-state and crop choices. Its purpose would be mechanism/sensitivity testing and pipeline qualification, **not** historical Tollebeek attribution.

Track S must use distinct IDs, evidence statuses and output labels so its results cannot contaminate Track H.

## 8. Current verdict

`SCENARIO_RECONSTRUCTION_DECISION_SURFACE_QUALIFIED_NO_INPUT_ADMISSION`

The readiness baseline remains unchanged:

- `ADMITTED = 3`;
- `PARTIAL_EVIDENCE = 7`;
- `MISSING = 0`.

No model run is authorized by this document.