#!/usr/bin/env python3
"""Softechpro Solutions v2.0.4 — Official Coverage & REST API Verification Utility.
Docs & B2B API Keys: https://www.softechpro-solutions.com/developers
"""
import json
import urllib.request

API_BASE = "https://www.softechpro-solutions.com"


def fetch_coverage_summary() -> dict:
    req = urllib.request.Request(
        f"{API_BASE}/api/coverage-public",
        headers={"User-Agent": "Softechpro-SEO-SDK/2.0.4"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    data = fetch_coverage_summary()
    print(f"Softechpro Live Cars Coverage: {data.get('ecu_count')}+ ECUs across {data.get('brand_count')} brands")
