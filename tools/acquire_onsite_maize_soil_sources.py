from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import BinaryIO


BRP_API = "https://api.pdok.nl/rvo/gewaspercelen/ogc/v1/collections/brpgewas/items"
BRP_FILTER = "gewascode = 259 AND jaar = 2025 AND status = 'Definitief'"
BRO_ATOM = "https://service.pdok.nl/bzk/bro-bodemkaart/atom/index.xml"
USER_AGENT = "Bodemverdichting-kosten-source-acquisition/0.1"
TARGET = {"gewascode": "259", "jaar": "2025", "status": "definitief"}


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def request(url: str, timeout: int = 120):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=timeout)


def build_brp_first_url(limit: int = 1000) -> str:
    query = urllib.parse.urlencode(
        {
            "filter": BRP_FILTER,
            "filter-lang": "cql2-text",
            "limit": str(limit),
            "f": "json",
        }
    )
    return f"{BRP_API}?{query}"


def target_feature_errors(feature: dict) -> list[str]:
    errors: list[str] = []
    props = feature.get("properties") or {}
    if str(props.get("gewascode", "")).strip() != TARGET["gewascode"]:
        errors.append(f"gewascode={props.get('gewascode')!r}")
    if str(props.get("jaar", "")).strip() != TARGET["jaar"]:
        errors.append(f"jaar={props.get('jaar')!r}")
    if str(props.get("status", "")).strip().casefold() != TARGET["status"]:
        errors.append(f"status={props.get('status')!r}")
    if not feature.get("geometry"):
        errors.append("geometry missing")
    return errors


def next_link(payload: dict, current_url: str) -> str | None:
    for link in payload.get("links") or []:
        if str(link.get("rel", "")).casefold() == "next" and link.get("href"):
            return urllib.parse.urljoin(current_url, str(link["href"]))
    return None


def atom_gpkg_url(xml_bytes: bytes, base_url: str) -> str:
    root = ET.fromstring(xml_bytes)
    candidates: list[str] = []
    for elem in root.iter():
        href = elem.attrib.get("href")
        if href:
            candidates.append(urllib.parse.urljoin(base_url, href))
    gpkg = [url for url in candidates if urllib.parse.urlparse(url).path.lower().endswith(".gpkg")]
    if not gpkg:
        raise ValueError(
            "BRO Atom feed exposes no direct .gpkg link; "
            f"found {len(candidates)} link(s). Inspect/pin the feed before acquisition."
        )
    # Prefer the canonical current download filename if present.
    gpkg.sort(key=lambda url: ("BRO_DownloadBodemkaart.gpkg" not in url, url))
    return gpkg[0]


def download_stream(url: str, destination: Path) -> dict:
    destination.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    with request(url) as response, destination.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
            h.update(chunk)
        headers = {
            "content_type": response.headers.get("Content-Type"),
            "content_length": response.headers.get("Content-Length"),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }
        final_url = response.geturl()
    return {
        "url": url,
        "final_url": final_url,
        "path": str(destination),
        "sha256": h.hexdigest(),
        "size_bytes": destination.stat().st_size,
        "headers": headers,
    }


def acquire_brp(raw_dir: Path, interim_dir: Path, limit: int, max_pages: int) -> dict:
    page_dir = raw_dir / "brp_2025_silage_maize_pages"
    page_dir.mkdir(parents=True, exist_ok=True)
    output = interim_dir / "brp_2025_silage_maize.geojson"
    output.parent.mkdir(parents=True, exist_ok=True)

    url: str | None = build_brp_first_url(limit)
    pages: list[dict] = []
    feature_count = 0
    number_matched: int | None = None
    seen_ids: set[str] = set()
    first_feature = True

    with output.open("w", encoding="utf-8") as merged:
        merged.write('{"type":"FeatureCollection","features":[')

        page_no = 0
        while url:
            page_no += 1
            if page_no > max_pages:
                raise RuntimeError(
                    f"BRP pagination exceeded max_pages={max_pages}; aborting before silent truncation."
                )

            with request(url) as response:
                raw = response.read()
                final_url = response.geturl()
                headers = {
                    "content_type": response.headers.get("Content-Type"),
                    "etag": response.headers.get("ETag"),
                    "last_modified": response.headers.get("Last-Modified"),
                }

            page_path = page_dir / f"page_{page_no:05d}.json"
            page_path.write_bytes(raw)
            page_sha = hashlib.sha256(raw).hexdigest()

            payload = json.loads(raw)
            if payload.get("type") != "FeatureCollection":
                raise ValueError(f"BRP page {page_no} is not a FeatureCollection")

            if number_matched is None and isinstance(payload.get("numberMatched"), int):
                number_matched = payload["numberMatched"]

            features = payload.get("features")
            if not isinstance(features, list):
                raise ValueError(f"BRP page {page_no} has no features list")

            for feature in features:
                errors = target_feature_errors(feature)
                if errors:
                    raise ValueError(
                        f"BRP page {page_no} contains non-target/invalid feature "
                        f"{feature.get('id')!r}: {errors}"
                    )
                feature_id = str(feature.get("id", "")).strip()
                if not feature_id:
                    raise ValueError(f"BRP page {page_no} feature without stable id")
                if feature_id in seen_ids:
                    raise ValueError(f"duplicate BRP feature id across pages: {feature_id}")
                seen_ids.add(feature_id)

                if not first_feature:
                    merged.write(",")
                json.dump(feature, merged, ensure_ascii=False, separators=(",", ":"))
                first_feature = False
                feature_count += 1

            pages.append(
                {
                    "page": page_no,
                    "requested_url": url,
                    "final_url": final_url,
                    "raw_path": str(page_path),
                    "sha256": page_sha,
                    "size_bytes": len(raw),
                    "feature_count": len(features),
                    "headers": headers,
                }
            )
            url = next_link(payload, final_url)

        merged.write('],"source_query":')
        json.dump(
            {
                "endpoint": BRP_API,
                "filter": BRP_FILTER,
                "filter_lang": "cql2-text",
                "page_limit": limit,
            },
            merged,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        merged.write("}")

    if feature_count == 0:
        raise RuntimeError("BRP CQL query returned zero definitive 2025 silage-maize features")
    if number_matched is not None and feature_count != number_matched:
        raise RuntimeError(
            f"BRP pagination closure failed: collected={feature_count}, numberMatched={number_matched}"
        )

    return {
        "source": "SRC_BRP2025_PDOK",
        "endpoint": BRP_API,
        "filter": BRP_FILTER,
        "filter_lang": "cql2-text",
        "page_limit": limit,
        "raw_pages": pages,
        "page_count": len(pages),
        "feature_count": feature_count,
        "number_matched": number_matched,
        "derived_geojson": str(output),
        "derived_geojson_sha256": sha256_path(output),
        "derived_geojson_size_bytes": output.stat().st_size,
        "status": "ACQUIRED_AND_TARGET_SEMANTICS_VERIFIED_NOT_ADMITTED",
    }


def acquire_bro(raw_dir: Path) -> dict:
    raw_dir.mkdir(parents=True, exist_ok=True)
    atom_path = raw_dir / "bro_bodemkaart_atom_index.xml"
    with request(BRO_ATOM) as response:
        atom_raw = response.read()
        atom_final_url = response.geturl()
    atom_path.write_bytes(atom_raw)
    gpkg_url = atom_gpkg_url(atom_raw, atom_final_url)

    gpkg_path = raw_dir / Path(urllib.parse.urlparse(gpkg_url).path).name
    download = download_stream(gpkg_url, gpkg_path)
    return {
        "source": "SRC_BRO_SGM",
        "atom_url": BRO_ATOM,
        "atom_final_url": atom_final_url,
        "atom_path": str(atom_path),
        "atom_sha256": hashlib.sha256(atom_raw).hexdigest(),
        "resolved_gpkg_url": gpkg_url,
        "download": download,
        "status": "ACQUIRED_RAW_VERSIONED_NOT_ADMITTED",
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Materialize source-native inputs for the 2025 silage-maize × BRO soil crosswalk. "
            "Raw inputs are written under gitignored data/raw; derived BRP target geometry under "
            "data/interim. Acquisition is not scientific admission."
        )
    )
    p.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/onsite_maize_soil_v0_1"),
    )
    p.add_argument(
        "--interim-dir",
        type=Path,
        default=Path("data/interim/onsite_maize_soil_v0_1"),
    )
    p.add_argument(
        "--manifest",
        type=Path,
        default=Path("data/interim/onsite_maize_soil_v0_1/acquisition_manifest.json"),
    )
    p.add_argument("--page-limit", type=int, default=1000)
    p.add_argument("--max-pages", type=int, default=10000)
    p.add_argument("--skip-brp", action="store_true")
    p.add_argument("--skip-bro", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.skip_brp and args.skip_bro:
        raise SystemExit("Nothing to acquire: both --skip-brp and --skip-bro supplied.")

    result = {
        "artifact_id": "ONSITE_MAIZE_SOIL_SOURCE_MATERIALIZATION_V0_1",
        "scientific_status": "ACQUISITION_OUTPUT_NOT_SCIENTIFICALLY_ADMITTED",
        "run_authorized": False,
        "guardrails": [
            "Raw source responses/files are preserved before transformation.",
            "BRP target semantics are revalidated feature by feature.",
            "Pagination must close; silent truncation is prohibited.",
            "BRO download URL is resolved from the official Atom feed.",
            "Acquisition does not qualify BRO→CCNL6 mappings or compaction exposure.",
        ],
    }

    if not args.skip_brp:
        result["brp"] = acquire_brp(
            args.raw_dir,
            args.interim_dir,
            limit=args.page_limit,
            max_pages=args.max_pages,
        )
    if not args.skip_bro:
        result["bro"] = acquire_bro(args.raw_dir)

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote local acquisition manifest: {args.manifest}")
    print("Scientific admission remains false.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
