"""Summarize paired published HYDRUS outputs; no HYDRUS model is run.

Usage: python tools/check_pinza_water_balance.py 3-HYDRUS_Simulations.zip
Source: https://doi.org/10.5281/zenodo.16940365
Differences are compacted minus non-compacted, in mm per adjusted year.
"""
import csv
import hashlib
import io
import json
import math
import statistics
import sys
import zipfile
from collections import defaultdict
from datetime import datetime, timedelta


def summarize(path):
    results = []
    seasonal_results = []
    with zipfile.ZipFile(path) as archive:
        for parameter in (1, 2, 3):
            name = next(n for n in archive.namelist() if n.endswith(
                f"Scenario_Analyses_HYDRUS_Parameterization{parameter}.csv"))
            records = defaultdict(dict)
            for row in csv.DictReader(io.TextIOWrapper(archive.open(name), encoding="utf-8-sig")):
                key = (row["Scenario"], row["Year_new"], row["Date"])
                case = row["Case"]
                if case in records[key]:
                    raise ValueError(f"Duplicate case/date: {key} {case}")
                records[key][case] = row
            yearly = defaultdict(lambda: defaultdict(float))
            seasonal = defaultdict(lambda: defaultdict(float))
            dates = defaultdict(set)
            for (scenario, year, date), pair in records.items():
                if set(pair) != {"compacted", "noncompacted"}:
                    raise ValueError(f"Unpaired date: {scenario} {date}")
                comp = pair["compacted"]
                ref = pair["noncompacted"]
                day, month, label_year = map(int, date.split("/"))
                # Future labels retain the historical calendar shifted 100 years,
                # including 29 February 2100. Preserve all source rows.
                offset = 0 if scenario == "Historical" else 100
                parsed = datetime(label_year - offset, month, day).date()
                expected_year = label_year + (month == 12)
                if int(year) != expected_year:
                    raise ValueError(f"Incorrect adjusted year: {date} {year}")
                dates[(scenario, str(int(year)-offset))].add(parsed)
                season = ("DJF", "MAM", "JJA", "SON")[(parsed.month % 12) // 3]
                for col in ("Precipitation_mm", "Evapotranspiration_potential_mm"):
                    if abs(float(comp[col]) - float(ref[col])) > 1e-8:
                        raise ValueError(f"Unmatched forcing: {date} {col}")
                for row in pair.values():
                    for col in ("Precipitation_mm", "Evapotranspiration_potential_mm",
                                "Evapotranspiration_actual_mm", "Evaporation_mm",
                                "Transpiration_actual_mm", "Deep_percolation_mm", "Runoff_mm"):
                        if not math.isfinite(float(row[col])):
                            raise ValueError(f"Nonfinite value: {date} {col}")
                    if abs(float(row["Evapotranspiration_actual_mm"]) -
                           float(row["Evaporation_mm"]) -
                           float(row["Transpiration_actual_mm"])) > 1e-5:
                        raise ValueError(f"ET decomposition mismatch: {date}")
                totals = yearly[(scenario, year)]
                totals["days"] += 1
                for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm"):
                    totals[col] += float(comp[col]) - float(ref[col])
                    seasonal[(scenario, year, season)][col] += float(comp[col]) - float(ref[col])
            for (scenario, year), actual_dates in dates.items():
                first = datetime(int(year) - 1, 12, 1).date()
                last = datetime(int(year), 12, 1).date()
                expected_dates = {first + timedelta(days=i) for i in range((last-first).days)}
                if actual_dates != expected_dates:
                    raise ValueError(f"Missing calendar dates: {scenario} {year}")
            for scenario in sorted({key[0] for key in yearly}):
                years = [v for (s, y), v in yearly.items() if s == scenario]
                if len(years) != 29 or any(v["days"] not in (365, 366) for v in years):
                    raise ValueError(f"Incomplete adjusted years: {scenario}")
                dp = [v["Deep_percolation_mm"] for v in years]
                runoff_year = max(years, key=lambda v: v["Runoff_mm"])
                results.append({"parameterization": parameter, "scenario": scenario,
                    "paired_years": len(years), **{
                        "delta_" + col: round(sum(v[col] for v in years) / len(years), 4)
                        for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm")},
                    "delta_percolation_annual_median_mm": round(statistics.median(dp), 4),
                    "delta_percolation_annual_min_mm": round(min(dp), 4),
                    "delta_percolation_annual_max_mm": round(max(dp), 4),
                    "years_positive_delta_percolation": sum(v > 0 for v in dp),
                    "mean_delta_percolation_without_max_runoff_year_mm": round(
                        (sum(dp) - runoff_year["Deep_percolation_mm"]) / (len(dp)-1), 4)})
                for season in ("DJF", "MAM", "JJA", "SON"):
                    values = [v for (s, y, t), v in seasonal.items() if s == scenario and t == season]
                    seasonal_results.append({"parameterization": parameter, "scenario": scenario,
                        "season": season, "paired_seasons": len(values), **{
                            "delta_"+col: round(sum(v[col] for v in values)/len(values), 4)
                            for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm")}})
                for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm"):
                    seasonal_sum = sum(r["delta_"+col] for r in seasonal_results
                                       if r["parameterization"] == parameter and r["scenario"] == scenario)
                    if abs(seasonal_sum - sum(v[col] for v in years)/len(years)) > 0.0003:
                        raise ValueError("Seasonal totals do not reproduce annual totals")
    with open(path, "rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    return {"source_doi": "10.5281/zenodo.16940365", "archive_sha256": digest,
            "checks": "exact case pairs, finite fluxes, identical forcing, exact December-November source calendars, ET=E+T, seasonal sums reproduce annual means",
            "calendar_note": "Future labels retain historical leap days shifted by 100 years, including 29/02/2100. Calendar checks map future labels back 100 years; no rows dropped.",
            "limitation": "Published outputs only; full storage balance and HYDRUS rerun not verified.",
            "results": results, "seasonal_results": seasonal_results}


if __name__ == "__main__":
    print(json.dumps(summarize(sys.argv[1]), indent=2))
