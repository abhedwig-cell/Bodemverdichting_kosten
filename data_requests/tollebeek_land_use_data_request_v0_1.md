# Tollebeek 1998 land-use / crop data request v0.1

Purpose: resolve `DR_SM_LAND_USE` for `EVT_TOL_1998_OCT` without a representative-crop convenience default.

Preferred evidence is field/parcel-level crop or vegetation identity for the 1998 growing season, spatially linkable to the historical Tollebeek control areas and ultimately to selected source-model units. Preserve parcel/field ID, geometry/coordinates and CRS, crop code/name, reference date/year, source provenance and any management/phenology information needed by the chosen source model.

Qualified context routes:
- LGN3: 25 m pre-event context; Flevoland agricultural classification is 1995;
- LGN4: post-event context based on 1999/2000 imagery;
- public BRP/Gewaspercelen historical annual archive: 2009 onward, so it does not resolve 1998;
- official 2006 Tollebeek documentation: broad arable/forest context only.

Do not interpolate crop identity across LGN map years because crop changes can reflect rotation. Do not assume one representative crop for OT.02 or bare soil from the October event date. If direct 1998 evidence cannot be recovered, any crop-independent or scenario-based model design must be reviewed separately and labelled as a scientific scenario rather than observation.
