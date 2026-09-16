# Tollebeek drainage data request v0.1

Related readiness item: `DR_SM_DRAINAGE`

Status: `PARTIAL_EVIDENCE`

## Purpose

Obtain the missing source-native drainage information required to turn the qualified OT.02 drainage-data route into a current source-model drainage configuration.

## Already known

The owner `zzl_Drainage` inventory contains 74 drainage polygons intersecting the admitted OT.02 geometry and covering about 95.27% of the polygon by clipped union area. The service exposes fields for spacing, installation date and depth, but all 74 intersecting records currently return spacing `0` and null depth/date values.

The owner NOP watersystem-legger service provides much newer open-water/water-system topology, including afvoervakken, culverts, stuwen and other structures. This does not fill the missing parcel-drain geometry/parameter fields.

## Requested records

For each selected source-model drainage unit or parcel, request where available:

- stable asset/drainage-unit ID;
- parcel/spatial-unit link or geometry;
- coordinate reference system;
- drain spacing or drain-density equivalent;
- drain depth/elevation and vertical datum/reference;
- installation or renewal date;
- drainage material/type if it affects hydraulic interpretation;
- outlet point or receiving ditch/watercourse;
- operational or maintenance status where relevant;
- source system/version and extraction date;
- missing-value semantics and QC/status flags.

If only design drawings or drainage plans are available, preserve the source document/asset ID and do not transcribe missing values as zero.

## Qualified source-holder route

Waterschap Zuiderzeeland publishes a dedicated **waterinformatie aanvragen** route for information not available through its public maps/GEO information. The form explicitly accepts location-specific requests for kaartmateriaal and meetresultaten and states that information requests are taken into treatment within one week, with an answer depending on complexity normally within two weeks.

Use the ordinary water-information request before a formal Woo request. Zuiderzeeland's Woo guidance explicitly recommends first submitting an information request because many documents can be supplied without a formal disclosure decision.

The request must identify the target unambiguously:

- peilgebied: `OT.02` / `TOLLEBEEK_OT02_CURRENT`;
- canonical owner drainage route: `zzl_Drainage`;
- observed public issue: 74 intersecting polygons, all with spacing `0`, and null depth/installation date;
- requested purpose: scientific source-model parameterisation and audit, not asset-operation control;
- preferred output: source-native GIS/table export plus field definitions/codebook and extraction/version date;
- if public sharing of parcel-level drainage detail is restricted, request a privacy-preserving OT.02-selected extract or a holder-side join to the supplied canonical OT.02 polygon.

If the ordinary information route cannot resolve the records or confirms that relevant documents require a formal disclosure procedure, escalate to the published Woo-contact route. A Woo request is therefore a secondary legal/document route, not the default first step.

## Acceptance criteria

The drainage gate can move beyond `PARTIAL_EVIDENCE` only when the selected model units have a reproducible current or explicitly dated drainage representation with provenance.

At minimum, the evidence must support the actual representation chosen in the source model. If SWAP uses explicit subsurface drainage, the evidence or separately qualified derivation must support the relevant drain level/depth and spacing/density or equivalent drainage relation.

A model drainage resistance is **not** accepted solely because it matches historical NOP practice or produces plausible model output. The mapping from physical evidence to model parameter must be documented and independently reviewable.

Receipt of owner records alone is not automatic admission: field semantics, temporal applicability, missingness and spatial relation to the chosen model units still require qualification.

## Explicitly unacceptable substitutions

- `0` spacing from the incomplete `zzl_Drainage` attributes as a physical value;
- historical 1946–1955 installation values as current asset state without evidence;
- the historical FutureWater 100 d tile resistance as a current default;
- the historical FutureWater ~30 d surface-drainage resistance as a current default;
- open-water line density as a proxy for subsurface drain spacing;
- target peil as drain elevation;
- missing values converted to zero.

## Next processing step after receipt

1. validate source/version and field semantics;
2. spatially join records to `TOLLEBEEK_OT02_CURRENT` and the selected source-model units;
3. retain raw source-native values and missing flags;
4. classify temporal applicability;
5. derive any model-specific parameter only through an explicit qualified mapping;
6. update `DR_SM_DRAINAGE` only after qualification.
