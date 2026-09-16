# Tollebeek model-configuration authority route v0.1

Status: **SWAP5 EXECUTION AUTHORITY QUALIFIED; TOLLEBEEK CONFIGURATION NOT ADMITTED**

## Decision

`DR_SM_MODEL_CONFIG` advances from `MISSING` to `PARTIAL_EVIDENCE`. The project now has an explicit, reproducible SWAP5 authority chain for designing the first paired source-model experiment, but not yet the full run configuration.

## Authority roles

The executable scientific pin is SWAP5 `50346642bd565f79134ea17d5462e544b354998c` (production tree `3b085d7d...`). The Status-A acceptance authority is `992a5c657bfe10a10100f92e0cb77c4825ae65b6`. The later live canonical head `80c6faaa...` is governance/status context and is deliberately not used as a moving executable pin.

## Why configuration remains open

A model configuration is more than a software commit. It binds model structure, boundary, drainage, initial state, land-use/crop treatment, forcing conversion, numerical choices and controlled CURRENT/REFERENCE dimensions. Several of those project inputs remain partial. Creating a runnable configuration now would hide missing science behind defaults.

No model_configuration dataset/row and no CURRENT/REFERENCE model run is admitted by this workunit.
