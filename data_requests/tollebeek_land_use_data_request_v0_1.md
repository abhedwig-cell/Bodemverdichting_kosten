# Tollebeek 1998 land-use / crop data request v0.1

Purpose: resolve `DR_SM_LAND_USE` for `EVT_TOL_1998_OCT` without a representative-crop convenience default.

Preferred evidence is field/parcel-level crop or vegetation identity for the 1998 growing season, spatially linkable to the historical Tollebeek control areas and ultimately to selected source-model units. Preserve parcel/field ID, geometry/coordinates and CRS, crop code/name, reference date/year, source provenance and any management/phenology information needed by the chosen source model.

Qualified context routes:
- LGN3: 25 m pre-event context; Flevoland agricultural classification is 1995;
- LGN4: post-event context based on 1999/2000 imagery;
- public BRP/Gewaspercelen historical annual archive: 2009 onward, so it does not resolve 1998;
- official 2006 Tollebeek documentation: broad arable/forest context only.

## Public LGN spatial-rendering route reviewed 2026-09-16

The public LGN3/LGN4 MapServer WCS can reproducibly return bounded OT.02 TIFF responses, but the returned files are three-band rendered RGB products rather than source class-value rasters. WMS GetFeatureInfo returned no underlying class attribute and GetStyles returned no color-map rules. The route is therefore useful as source-hosted spatial context only; it does not provide a reproducible RGB→LGN-class mapping for canonical crop statistics.

Do not interpret TIFF band values or RGB frequencies as LGN class codes. Do not derive crop shares/hectares from this rendering route unless a source-authoritative class-value mapping/export is separately recovered. See `docs/42_tollebeek_lgn_spatial_context_v0_1.md`.

## Historical 1998 source-holder route reviewed 2026-09-16

The 1998 event predates the modern Gecombineerde Opgave route, which CBS describes as part of the Landbouwtelling from 2002 onward. CBS does publish historical municipality-level Landbouwtelling data for 1980-2000, but municipality statistics are context and cannot identify the crop on an OT.02 parcel. The standard CBS older-LBT research-microdata catalog currently lists 2006/2007 rather than 1998; this is an access/catalog fact, not proof that 1998 source records no longer exist.

Two source-holder enquiries are therefore qualified:

1. **CBS historical Landbouwtelling / maatwerk** — ask whether 1998 source or preserved microdata can support a research-safe spatial selection below municipality level for Noordoostpolder/Tollebeek, and obtain the applicable crop-code dictionary, reference date, spatial identifiers and disclosure constraints.
2. **RVO/LVVN historical administration / LASER chain** — ask whether 1998 agricultural scheme records contained crop identity linked to fields/parcels, whether those records survive, and if transferred, obtain the exact archive collection/inventory reference and access conditions.

Minimum useful return fields are: source-native record/parcel ID; 1998 crop code/name with source codebook; explicit reference date/year; spatial identifier/geometry or traceable parcel-location relation; source-system/archive authority; missingness/disclosure treatment; and enough provenance to assign records reproducibly to the historical Tollebeek domain without revealing farmer identity where that is unnecessary.

See `docs/43_tollebeek_1998_land_use_sourceholder_route_v0_1.md`.

Do not interpolate crop identity across LGN map years because crop changes can reflect rotation. Do not assume one representative crop for OT.02 or bare soil from the October event date. If direct 1998 evidence cannot be recovered, any crop-independent or scenario-based model design must be reviewed separately and labelled as a scientific scenario rather than observation.
