"""Summarize paired published HYDRUS outputs; no HYDRUS model is run.

Usage: python tools/check_pinza_water_balance.py 3-HYDRUS_Simulations.zip
Source: https://doi.org/10.5281/zenodo.16940365
Differences are compacted minus non-compacted, in mm per adjusted year.
"""
import csv
import hashlib
import io
import json
import sys
import zipfile
from collections import defaultdict


def summarize(path):
    results = []
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
            for (scenario, year, date), pair in records.items():
                if len(pair) != 2 or "compacted" not in pair:
                    raise ValueError(f"Unpaired date: {scenario} {date}")
                comp = pair["compacted"]
                ref = next(row for case, row in pair.items() if case != "compacted")
                for col in ("Precipitation_mm", "Evapotranspiration_potential_mm"):
                    if abs(float(comp[col]) - float(ref[col])) > 1e-8:
                        raise ValueError(f"Unmatched forcing: {date} {col}")
                for row in pair.values():
                    if abs(float(row["Evapotranspiration_actual_mm"]) -
                           float(row["Evaporation_mm"]) -
                           float(row["Transpiration_actual_mm"])) > 1e-5:
                        raise ValueError(f"ET decomposition mismatch: {date}")
                totals = yearly[(scenario, year)]
                totals["days"] += 1
                for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm"):
                    totals[col] += float(comp[col]) - float(ref[col])
            for scenario in sorted({key[0] for key in yearly}):
                years = [v for (s, y), v in yearly.items() if s == scenario]
                if len(years) != 29 or any(v["days"] not in (365, 366) for v in years):
                    raise ValueError(f"Incomplete adjusted years: {scenario}")
                results.append({"parameterization": parameter, "scenario": scenario,
                    "paired_years": len(years), **{
                        "delta_" + col: round(sum(v[col] for v in years) / len(years), 4)
                        for col in ("Deep_percolation_mm", "Evapotranspiration_actual_mm", "Runoff_mm")}})
    with open(path, "rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    return {"source_doi": "10.5281/zenodo.16940365", "archive_sha256": digest,
            "checks": "paired dates, identical forcing, complete adjusted years, ET=E+T",
            "limitation": "Published outputs only; full storage balance and HYDRUS rerun not verified.",
            "results": results}


if __name__ == "__main__":
    print(json.dumps(summarize(sys.argv[1]), indent=2))
