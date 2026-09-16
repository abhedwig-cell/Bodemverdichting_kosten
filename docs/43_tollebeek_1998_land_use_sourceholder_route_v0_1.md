# Tollebeek 1998 land-use source-holder route v0.1

Status: **qualification candidate — access route only**

Governing readiness item: `DR_SM_LAND_USE`

## 1. Purpose

Identify a defensible source-holder path for crop/vegetation information from the 1998 growing season that could eventually be linked to the historical Tollebeek system and, if spatial identity is sufficient, to the admitted OT.02 analysis domain.

This workunit does not create a 1998 crop state.

## 2. CBS historical Landbouwtelling route

CBS publishes `Landbouw; gemeente, 1980 - 2000`, which contains historical municipality-level data on agricultural businesses, crops, livestock, land use, labour and related subjects.

This route is useful for historical Noordoostpolder context, but it is not parcel evidence:
- municipality statistics do not identify which crop occupied a particular OT.02 field;
- aggregated crop shares cannot be assigned to soil profiles or model columns;
- a municipality average or dominant crop is not an observed Tollebeek crop.

CBS's current methodology description states that agricultural structure censuses have been conducted for more than a century and that the Landbouwtelling became part of the Gecombineerde Opgave from 2002. Thus 1998 predates the modern Gecombineerde Opgave collection route.

The standard CBS research-microdata page for the older `LBT: Landbouwtellingen` product currently lists files for 2006 and 2007, not 1998. This is an access/catalog observation only. It does not establish that older source records have been destroyed or are unavailable through maatwerk or archival channels.

### CBS source-holder request

Ask CBS whether source or preserved microdata underlying the 1998 Landbouwtelling can be accessed for research/maatwerk in a form that can answer any of the following without violating disclosure rules:

1. whether 1998 crop records exist below municipality level for Noordoostpolder;
2. whether records contain farm/location identifiers or spatial/kadastral/perceel references;
3. whether a research-safe spatial selection for the historical Tollebeek area can be performed by CBS without releasing identifying farm data;
4. which 1998 crop-code dictionary, reference date and unit definitions apply;
5. whether any preserved linkage exists to ministry/LASER administrative source records;
6. if source microdata are unavailable, whether a custom historical tabulation for a smaller spatial unit than municipality can be produced legitimately.

Any returned aggregate remains context unless its spatial grain is sufficient for the intended model unit.

## 3. RVO/LVVN–LASER administrative archive route

Nationaal Archief institutional records show LASER as a Ministry of Agriculture implementation service in the relevant period. Later institutional succession runs through Dienst Regelingen and ultimately RVO.

This organizational continuity makes RVO/LVVN records management a defensible enquiry route, but it does **not** prove that the desired 1998 parcel/crop records survive.

### Administrative source-holder request

Ask RVO/LVVN records management or the appropriate historical-data contact:

1. whether LASER or predecessor systems in 1998 collected crop identity linked to individual agricultural parcels or cadastral/field identifiers in Noordoostpolder;
2. which 1998 national/EU agricultural schemes required crop/parcel declarations;
3. whether those records were retained, migrated, destroyed under a selection schedule, or transferred to an archive;
4. if retained, which system/dataset/archive series contains them;
5. what spatial identifiers were used (coordinates, cadastral parcels, field sketches, farm parcel numbers, map sheets or other references);
6. what crop-code list and reference date applied;
7. whether a privacy-preserving research extract or spatial aggregate for the historical Tollebeek control areas can be supplied;
8. if records were transferred, provide the exact archival institution, collection/inventory number and access conditions.

Do not start from a Woo disclosure assumption. The first question is provenance and existence. Access can then follow the appropriate research, archival, privacy or public-information procedure.

## 4. Minimum admissible historical crop record

A future record can support `DR_SM_LAND_USE` only if it preserves at minimum:
- source-native record or parcel ID;
- crop code/name and source codebook;
- explicit reference year/date for the 1998 growing season;
- spatial identifier sufficient for reproducible assignment to the historical Tollebeek domain;
- CRS/geometry or a traceable archival parcel-location relation where applicable;
- source system / archive authority;
- missingness and disclosure treatment;
- any transformations used to map the source crop taxonomy to a model crop representation.

A record need not reveal farmer identity to be scientifically usable.

## 5. Context-only routes

The following may support plausibility or scenario design but cannot independently close the historical crop gate:
- CBS Noordoostpolder municipality crop totals/shares;
- LGN3 1995 crop context;
- LGN4 1999/2000 context;
- later BRP/Gewaspercelen archives;
- generic statements that Noordoostpolder was dominated by arable rotations.

These sources can inform a future scenario envelope, but they cannot be relabelled as observations of a specific field in October 1998.

## 6. Current verdict

The source-holder route is classified:

`QUALIFIED_CBS_PLUS_RVO_LASER_ARCHIVE_ENQUIRY_ROUTE_NO_1998_CROP_ADMISSION`

`DR_SM_LAND_USE` remains `PARTIAL_EVIDENCE`.

Next material progress requires a response from a source holder or an independently authoritative 1998 parcel/crop archive. If no spatial historical crop records survive, a separate Track-S crop-envelope/scenario workunit may be designed, but it must remain scenario-only.
