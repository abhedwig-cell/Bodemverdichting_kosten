# Tollebeek drainage access v0.1 — RECONCILE

Capability: `DR_SM_DRAINAGE`

Phase: `RECONCILE → QUALIFY → CLOSE`

Canonical start:
- branch: `main`
- head: `a02e0810e2a1bfd9d4d8c5c5f418a012c8d55206`

Reused immutable evidence:
- owner `zzl_Drainage` intersection: 74 polygons, ~95.27% clipped union coverage;
- all intersecting records: spacing `0`, depth/date null;
- newer owner watersystem-legger topology;
- historical FutureWater drainage resistances retained as method priors only.

New access-route evidence:
- Waterschap Zuiderzeeland publishes a dedicated water-information request route for unavailable map/information records;
- the owner advises ordinary information requests before formal Woo requests because many records can be supplied directly;
- Woo remains a secondary escalation route if documents require formal disclosure.

Decision:
`OWNER_DRAINAGE_INVENTORY_KNOWN — PHYSICAL_DETAIL_ATTRIBUTES_UNRESOLVED`

Readiness mutation:
- none; `DR_SM_DRAINAGE` remains `PARTIAL_EVIDENCE`;
- no drainage parameter or model configuration is admitted.

Mutations:
- strengthen `data_requests/tollebeek_drainage_data_request_v0_1.md`;
- add `docs/39_tollebeek_drainage_access_route_v0_1.md`;
- add this resumable checkpoint.

Next permitted action:
- qualify documentation/governance delta with normal CI;
- request the source-native owner records;
- after receipt, open a separate bounded data-qualification workunit.

Exclusions:
- no spacing=0 interpretation as physical zero;
- no FutureWater default transfer;
- no open-water density proxy;
- no target peil as drain level;
- no null→0;
- no SWAP run.
