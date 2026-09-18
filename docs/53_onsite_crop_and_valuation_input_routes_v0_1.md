# On-site crop crosswalk and valuation input routes v0.1

Status: **QUALIFIED INPUT ROUTES — NUMERIC INPUTS NOT YET ADMITTED**  
Parent calculation surface: `52_onsite_bounded_calculation_surface_v0_1.md`

## 1. Purpose

The bounded calculation surface exposed two immediate input gaps after current compaction exposure:

1. the amount of silage maize within the relevant sandy-soil reporting strata;
2. crop-specific economic values with a clearly defined valuation perspective.

This document fixes reproducible acquisition routes for both gaps without inventing values.

## 2. Silage-maize crop × soil crosswalk

### 2.1 Primary spatial crop source

The primary route is:

`BRP Gewaspercelen 2025 definitief`

Source ID:

`SRC_BRP2025_PDOK`

The definitive 2025 dataset was published through PDOK on 17 March 2026.

It contains agricultural parcel geometry and the declared cultivated crop. It is available through public spatial services/API.

This makes it suitable for:

```text
BRP crop parcel
  ∩ compatible soil-class geometry
  → crop area by soil stratum
```

### 2.2 What it solves

For the maize calculation rows, it can replace:

`crop_share = unknown`

with a reproducible crop area/share after the soil overlay is qualified.

### 2.3 What it does not solve

BRP does not provide:

- soil class;
- compaction exposure;
- depth/severity;
- crop response;
- economic damage.

Those remain independent inputs.

### 2.4 National closure source

CBS table `85636NED` is retained as national crop context.

At the public state reviewed on 18 September 2026:

- 2025 cultivated silage-maize area: 183,191 ha;
- 2025 gross yield: 47.3 t/ha;
- 2025 values are definitive in the current CBS table;
- 2026 preliminary cultivated area: 182,587 ha.

This is useful as a closure/sanity check after spatial aggregation.

It is **not** a rule for distributing maize over sandy/clay/other soil classes.

## 3. Required soil side of the crosswalk

The crop layer alone is not enough.

The next spatial design task is to select a versioned soil-class layer that can reproduce the reporting classes used by the calculation surface.

The overlay must document:

- soil source and version;
- classification rule;
- CRS;
- crop data year;
- intersection method;
- treatment of multipart/sliver geometry;
- total crop-area closure;
- unmapped/excluded area.

No crop share is admitted until this crosswalk closes reproducibly.

## 4. Economic valuation routes

### 4.1 KWIN-AGV 2025

Source:

`SRC_KWIN_AGV2025`

KWIN-AGV provides current crop-level economic data including gross money returns, allocated/direct costs and other production-cost information.

It is the preferred route for a consistent normative crop-specific accounting framework.

However, the detailed numeric tables require paid/subscription access in the currently identified route.

Therefore:

`KWIN_NUMERIC_INPUT = NOT_YET_ACQUIRED`

The method/source route is qualified; no KWIN number is currently admitted.

### 4.2 BINternet

Source:

`SRC_BINTERNET_2025`

BINternet is a public Wageningen Social & Economic Research interface with technical results, prices and balances for represented farm/crop groups.

It is useful for:

- empirical current context;
- price/technical-result plausibility;
- checking whether normative KWIN values are representative;
- multi-year sensitivity.

It is not automatically equivalent to crop-specific marginal compaction damage.

## 5. Valuation perspectives remain separate

### Gross revenue/accounting

Possible calculation:

```text
affected ha
 × response fraction
 × gross money yield per ha
```

This is transparent but not automatically the farmer's net damage.

### Farmer-private marginal damage

Preferred for "cost to farmer" where data permit:

```text
lost output revenue
 - genuinely avoided yield-dependent costs
 + additional compaction-related operating costs
```

### Societal production/welfare

Requires a separate welfare interpretation.

The project must not sum gross production value and private farm loss as though they were independent damages.

## 6. Grassland valuation is a separate case

Grass is not simply a marketed crop with one observable product price in the same sense as many arable crops.

A grass-yield change can affect:

- purchased feed;
- silage stocks;
- herd feed balance;
- milk production;
- land/feed substitution;
- farm-management decisions.

Therefore the grassland route should not copy the maize/arable gross-revenue formula without an explicit forage-value or farm-feed-balance interpretation.

For grass, the likely lowest-computation route is first to search for a defensible forage replacement/opportunity-cost value or a directly applicable farm-economic relationship.

## 7. Data hierarchy for the next calculation step

For silage maize:

```text
BRP 2025 parcel crop geometry
  + qualified soil-class geometry
  → maize ha by soil stratum

current CC-NL depth×severity exposure
  → affected maize ha

ENS_O1_MAIZE_SAND scenario member
  → response scenario

KWIN/BINternet economic input
  → explicitly defined accounting/private-cost result
```

For grass:

```text
grassland soil-stratum area
  + current CC-NL depth×severity exposure
  → affected grassland ha

ENS_O1_GRASS_SAND scenario/context member
  → response scenario

qualified forage/farm valuation
  → explicitly defined private/accounting result
```

## 8. Current verdict

The crop-area and valuation **routes** are now substantially clearer than the numerical inputs.

The immediate remaining gates are:

- current CC-NL exposure;
- versioned soil geometry compatible with the 12-domain reporting scheme;
- BRP × soil overlay for maize;
- acquired/selected economic values;
- response/reference matching.

No new modelling is required to address any of these four gates.
