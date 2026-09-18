# On-site maize × soil source materialization v0.1

Status: **EXECUTABLE ACQUISITION CONTRACT — RAW SOURCES NOT YET MATERIALIZED**  
Parent workunits: `54_onsite_maize_soil_crosswalk_v0_1.md`, `55_bro_ccnl6_rule_proposals_v0_1.md`

## 1. Purpose

Turn the qualified public BRP and BRO source routes into one reproducible local acquisition step.

The key rule is:

> preserve source-native bytes before transformation, hash them, verify the selected semantics, and only then create derived geometry for the crosswalk.

Raw files remain outside Git under the already ignored `data/raw/` tree.

## 2. Executable tool

`tools/acquire_onsite_maize_soil_sources.py`

Default command:

```bash
python tools/acquire_onsite_maize_soil_sources.py
```

Default local outputs:

```text
data/raw/onsite_maize_soil_v0_1/
  brp_2025_silage_maize_pages/page_00001.json
  ...
  bro_bodemkaart_atom_index.xml
  BRO_DownloadBodemkaart.gpkg

data/interim/onsite_maize_soil_v0_1/
  brp_2025_silage_maize.geojson
  acquisition_manifest.json
```

Both directories are gitignored.

## 3. BRP acquisition

The current PDOK OGC API supports CQL filtering.

The source query is pinned to:

```text
gewascode = 259
AND jaar = 2025
AND status = 'Definitief'
```

The tool requests this through the official BRP OGC API Features endpoint.

### Raw-page preservation

Every response page is written unchanged before it is parsed.

For each page the local acquisition manifest records:

- requested/final URL;
- page number;
- SHA-256;
- byte size;
- feature count;
- selected HTTP provenance headers.

### Semantic verification

Every returned feature must independently satisfy:

- `gewascode = 259`;
- `jaar = 2025`;
- `status = Definitief`;
- geometry is present;
- stable feature ID is present.

A single violating feature aborts acquisition.

### Pagination closure

The tool follows `rel=next` links until none remains.

If the API supplies `numberMatched`, collected feature count must equal that number.

A `max_pages` guard prevents silent infinite or unexpectedly truncated pagination.

### Derived BRP geometry

Only after raw pages are persisted, the exact selected features are streamed into one local GeoJSON for the spatial overlay.

This GeoJSON is derived convenience input. The raw API pages remain the provenance authority.

## 4. BRO acquisition

The soil model is acquired through the official BRO/PDOK Atom route.

The tool:

1. downloads and preserves the Atom XML;
2. hashes the Atom response;
3. resolves a direct GeoPackage link from the feed;
4. prefers the canonical `BRO_DownloadBodemkaart.gpkg` filename when present;
5. streams the GPKG unchanged into `data/raw/`;
6. computes SHA-256 while downloading;
7. records response metadata and final URL.

If the Atom feed does not expose a direct GPKG, the tool fails closed instead of guessing a download URL.

## 5. Why BRP is filtered server-side

The project does not need all Dutch crop parcels for this workunit.

Server-side filtering:

- reduces transfer/storage;
- makes the scientific target explicit in the acquisition request itself;
- still preserves every returned source response page;
- avoids transforming the full BRP before provenance capture.

The independent CBS national maize figure remains a later closure/context check, not a source-selection mechanism.

## 6. Scientific admission boundary

Acquisition statuses are deliberately:

- BRP: `ACQUIRED_AND_TARGET_SEMANTICS_VERIFIED_NOT_ADMITTED`;
- BRO: `ACQUIRED_RAW_VERSIONED_NOT_ADMITTED`;
- whole manifest: `ACQUISITION_OUTPUT_NOT_SCIENTIFICALLY_ADMITTED`.

Acquiring files does not:

- qualify a BRO→CC-NL6 mapping;
- admit a maize-by-soil area;
- supply compaction exposure;
- select a yield-response member;
- create a damage or monetary result.

## 7. Sequence after acquisition

```text
ACQUIRE + HASH
  ↓
first fail-closed BRP × BRO crosswalk run
  ↓
unmapped-code diagnostic
  ↓
official-legend proposals
  ↓
explicit soil-code review / QUALIFY
  ↓
rerun overlay
  ↓
area-closure check
  ↓
CBS national crop-context comparison
  ↓
qualify/admit crop × soil shares
```

## 8. Current execution boundary

The repository now contains the executable acquisition code and network-free contract tests.

The raw public datasets themselves have **not** been materialized in this ChatGPT execution environment. Direct binary source download is therefore still an external/local execution step.

This is a technical environment boundary, not a scientific permission to substitute another source.

## 9. Verdict

`SOURCE_MATERIALIZATION_EXECUTABLE_RAW_DATA_NOT_YET_ACQUIRED`

The next colleague action is now a command, not a research question:

```bash
python tools/acquire_onsite_maize_soil_sources.py
```

After it completes, proceed directly with the already canonical fail-closed crosswalk workflow.
