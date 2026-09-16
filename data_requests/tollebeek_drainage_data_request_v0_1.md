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

## Acceptance criteria

The drainage gate can move beyond `PARTIAL_EVIDENCE` only when the selected model units have a reproducible current or explicitly dated drainage representation with provenance.

At minimum, the evidence must support the actual representation chosen in the source model. If SWAP uses explicit subsurface drainage, the evidence or separately qualified derivation must support the relevant drain level/depth and spacing/density or equivalent drainage relation.

A model drainage resistance is **not** accepted solely because it matches historical NOP practice or produces plausible model output. The mapping from physical evidence to model parameter must be documented and independently reviewable.

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
