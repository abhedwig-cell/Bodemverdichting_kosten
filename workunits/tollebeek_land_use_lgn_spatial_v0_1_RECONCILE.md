# Tollebeek land-use LGN spatial acquisition v0.1 — RECONCILE

Capability: `DR_SM_LAND_USE`

Phase: `RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → CLOSE`

Canonical start after branch reconciliation:
- branch: `main`
- head: `3dfeea52bac5bcee3d31b6d023cce355ff1eea69`
- work branch: `work/tollebeek-land-use-lgn-spatial-v0.1`

Existing canonical state:
- `DR_SM_LAND_USE = PARTIAL_EVIDENCE`;
- LGN3 is qualified pre-event context; Flevoland agricultural classification is 1995;
- LGN4 is qualified post-event context based on 1999/2000 information;
- public BRP/Gewaspercelen annual archive starts much later and does not resolve 1998;
- one representative crop, bare soil, majority-crop substitution or interpolation between map years is prohibited.

Recovered branch-local acquisition history:
- public LGN3/LGN4 MapServer endpoints were probed on the earlier branch lineage;
- WCS 2.0.1 `GetCoverage` with `SUBSET=x(...)`, `SUBSET=y(...)` and `FORMAT=image/tiff` returned bounded OT.02 clips;
- later encoding checks established that these TIFFs are rendered three-band RGB products rather than source class-value rasters;
- therefore the earlier provisional interpretation of band-1 values as LGN class codes is rejected and is not carried into the reconciled branch.

Goal of the reconciled workunit:
- retain only reproducible source-hosted spatial-rendering evidence and immutable fingerprints;
- classify the WCS/FeatureInfo/Styles route honestly;
- prevent rendered RGB values from being admitted as crop classes;
- leave exact October-1998 crop identity data-gated.

Scientific boundary:
- LGN3/4 do not become observations of the exact 1998 crop;
- RGB tuple frequencies are rendering diagnostics, not class frequencies unless an authoritative RGB→LGN mapping is recovered;
- no model input or SWAP run is created;
- no readiness status is promoted.

Next permitted action:
- persist the bounded ACQUIRE/CLASSIFY findings and their run IDs/checksums;
- remove all temporary acquisition workflows from the candidate diff;
- qualify only the route/context decision on normal CI.
