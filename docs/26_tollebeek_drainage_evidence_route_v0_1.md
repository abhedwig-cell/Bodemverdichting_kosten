# Tollebeek drainage evidence route v0.1

Status: `DRAINAGE_ROUTE_QUALIFIED_CONFIGURATION_BLOCKED`

## Purpose

This note defines what is and is not currently known about drainage configuration for the first Tollebeek OT.02 source-model experiment.

The project needs to distinguish four objects that must not be collapsed into one parameter:

1. subsurface parcel drainage geometry;
2. kavelsloten and other open-water drainage topology;
3. managed receiving-water level/control context;
4. model parameters such as drainage resistance.

## Owner evidence

### Parcel-drainage inventory

Waterschap Zuiderzeeland publishes `zzl_Drainage`, service item `dd48ed818ae44b6d9a64d189036511dc`.

A reproducible intersection with the admitted `TOLLEBEEK_OT02_CURRENT` polygon found 74 drainage polygons. Their clipped union covers about 1425.81 ha, approximately 95.27% of the admitted OT.02 polygon.

The layer exposes fields for:

- drainage identifier;
- heart-to-heart spacing;
- installation date;
- depth;
- remarks;
- global ID.

However, for all 74 intersecting features:

- spacing is returned as `0`;
- depth is null;
- installation date is null.

The layer data-last-edit timestamp is 2021-06-27.

The project therefore interprets this layer as an owner drainage-inventory / acquisition route, not as a complete current source-model parameter set. A zero spacing is treated as unavailable/sentinel-like in this context, not as a physical zero spacing.

### Open-water and water-system topology

The owner `Legger_watersysteem_2024_Noord_oostpolder__WFL1` service, item `cf10c95387724cf0b3f3af0339dc87b5`, was last edited 2025-08-27.

Within the admitted OT.02 polygon the screening found:

- 127 `Afvoervak` lines, about 55.57 km clipped length;
- 258 culvert features, about 3.06 km clipped line length;
- 12 stuw points;
- 5 put points.

This provides strong owner-backed water-system topology context. It does not define parcel tile-drain spacing, drain depth or SWAP drainage resistance.

A separate `leggerkavelsloten` owner layer contains 77 features intersecting OT.02 with about 44.22 km clipped length, but its data-last-edit timestamp is 2019-07-05. It is retained as supporting topology/history rather than the freshest water-system authority.

The public Zuiderzeeland notice found for the 2024 watersystem-legger programme describes the second design/draft legger during the March–May 2025 consultation. Therefore this workunit uses the current owner service for data/topology acquisition without claiming that every feature has independently verified final legal status.

## Historical context

The Noordoostpolder was systematically drained after reclamation. Owner heritage documentation records extensive subsurface parcel drainage installed mainly during 1946–1955, with spacing varying by soil conditions.

This is useful structural context only. Historical installation geometry cannot be treated as an unchanged current asset register.

Likewise the existing FutureWater SWAP values of 100 d tile-drain resistance and about 30 d surface-drainage resistance remain bounded historical method priors. They are not OT.02 calibration values.

## Scientific decision

The present evidence is sufficient to qualify the **owner drainage-data route and managed/open-water topology**, but not sufficient to admit a current source-model drainage configuration.

`DR_SM_DRAINAGE` therefore remains `PARTIAL_EVIDENCE`.

A current configuration may only be admitted after evidence supplies the relevant parcel-drain dimensions or a separately qualified derivation. At minimum the selected modelling units need reviewable evidence for the drainage representation actually used, including drainage depth/elevation and spacing or an equivalent hydraulic description.

Any drainage resistance used in SWAP must have a documented relation to the admitted geometry/state and may not be copied from historical precedent merely because it produces a plausible hydrograph.

## Required next evidence

For selected OT.02 source-model units acquire, where applicable:

- stable parcel/drainage-unit identifier;
- geometry or explicit spatial applicability;
- drain spacing or equivalent density;
- drain depth/elevation and reference datum;
- installation/renewal date or known asset-state information;
- outlet/receiving-water relation;
- maintenance/operational qualification where it materially affects function;
- provenance and observation/reference date;
- uncertainty and missing-data flags.

Potential routes include owner asset records, landholder drainage plans, KLIC/contract records where legally and technically appropriate, or a separately qualified field/remote derivation.

## Guardrails

- `IWS_AFSTAND_HART_OP_HART = 0` is not interpreted as physical zero spacing.
- Null owner fields remain null.
- Historical NOP spacing/depth values are not silently promoted to current OT.02 values.
- Open-water topology is not subsurface drainage geometry.
- Target surface-water level is not drain depth.
- Drainage geometry is not drainage resistance.
- No current SWAP drainage parameter is admitted by this note.
