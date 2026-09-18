from pathlib import Path
import sys
import unittest
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from acquire_onsite_maize_soil_sources import (
    BRP_FILTER,
    atom_gpkg_url,
    build_brp_first_url,
    next_link,
    target_feature_errors,
)


class OnsiteMaizeSoilSourceAcquisitionTests(unittest.TestCase):
    def test_brp_url_pins_cql_target(self):
        url = build_brp_first_url(limit=500)
        parsed = urllib.parse.urlparse(url)
        q = urllib.parse.parse_qs(parsed.query)
        self.assertEqual(q["filter"], [BRP_FILTER])
        self.assertEqual(q["filter-lang"], ["cql2-text"])
        self.assertEqual(q["limit"], ["500"])
        self.assertEqual(q["f"], ["json"])

    def test_target_feature_semantics(self):
        good = {
            "id": "x",
            "properties": {"gewascode": 259, "jaar": 2025, "status": "Definitief"},
            "geometry": {"type": "Point", "coordinates": [5, 52]},
        }
        self.assertEqual(target_feature_errors(good), [])

        bad = {
            "id": "y",
            "properties": {"gewascode": 260, "jaar": 2024, "status": "Concept"},
            "geometry": None,
        }
        errors = target_feature_errors(bad)
        self.assertEqual(len(errors), 4)

    def test_next_link_can_be_relative(self):
        payload = {
            "links": [
                {"rel": "self", "href": "?page=1"},
                {"rel": "next", "href": "?cursor=abc"},
            ]
        }
        self.assertEqual(
            next_link(payload, "https://example.test/items?page=1"),
            "https://example.test/items?cursor=abc",
        )

    def test_atom_prefers_canonical_gpkg(self):
        xml = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <link href="downloads/other.gpkg"/>
          <link href="downloads/BRO_DownloadBodemkaart.gpkg"/>
        </feed>"""
        self.assertEqual(
            atom_gpkg_url(xml, "https://service.example/atom/index.xml"),
            "https://service.example/atom/downloads/BRO_DownloadBodemkaart.gpkg",
        )

    def test_atom_without_gpkg_fails_closed(self):
        xml = b"""<?xml version="1.0"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <link href="metadata.xml"/>
        </feed>"""
        with self.assertRaises(ValueError):
            atom_gpkg_url(xml, "https://service.example/atom/index.xml")


if __name__ == "__main__":
    unittest.main()
