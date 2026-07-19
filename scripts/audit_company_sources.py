#!/usr/bin/env python3
"""Audit a company source ledger without network access or third-party packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


TRUSTED_CLASSES = {"regulatory", "official"}
OUTLOOK_CLASSES = {"institutional", "capital", "customer"}
ALLOWED_CLASSES = TRUSTED_CLASSES | OUTLOOK_CLASSES | {"independent", "aggregator", "community"}


def audit_company(company: dict) -> dict:
    issues: list[str] = []
    warnings: list[str] = []
    valid_sources: list[dict] = []
    domains: set[str] = set()
    classes: set[str] = set()
    urls: set[str] = set()
    for index, source in enumerate(company.get("sources", []), start=1):
        if not isinstance(source, dict):
            issues.append(f"source {index}: not an object")
            continue
        url = str(source.get("url", "")).strip()
        parsed = urlparse(url)
        source_class = str(source.get("source_class", "")).strip()
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            issues.append(f"source {index}: invalid URL")
            continue
        if url in urls:
            issues.append(f"source {index}: duplicate URL")
            continue
        urls.add(url)
        domains.add(parsed.netloc.lower().removeprefix("www."))
        if source_class not in ALLOWED_CLASSES:
            issues.append(f"source {index}: invalid source_class")
        else:
            classes.add(source_class)
        if not str(source.get("title", "")).strip():
            issues.append(f"source {index}: missing title")
        if not str(source.get("claim", "")).strip():
            issues.append(f"source {index}: missing claim mapping")
        if not str(source.get("accessed_at", "")).strip():
            issues.append(f"source {index}: missing accessed_at")
        valid_sources.append(source)

    high_confidence = (
        len(valid_sources) >= 2
        and len(domains) >= 2
        and bool(classes & TRUSTED_CLASSES)
        and "independent" in classes
        and not issues
    )
    if len(valid_sources) < 2:
        issues.append("fewer than two valid sources")
    if len(domains) < 2:
        issues.append("sources do not cover two independent domains")
    if not classes & TRUSTED_CLASSES:
        issues.append("missing official or regulatory source")
    if "independent" not in classes:
        issues.append("missing independent source")
    if not classes & OUTLOOK_CLASSES:
        warnings.append("missing institutional, capital, or customer source; company development outlook should remain cautious")
    if "community" not in classes and "aggregator" not in classes:
        warnings.append("missing community, forum, recruiting-platform, or employee-review source; workplace pressure, promotion, and culture claims should remain low confidence")
    return {
        "company_name": company.get("company_name", ""),
        "identity_status": company.get("identity_status", "unknown"),
        "career_outlook_label": company.get("career_outlook_label", company.get("first_gate", "unknown")),
        "valid_source_count": len(valid_sources),
        "domain_count": len(domains),
        "outlook_signal_count": sum(
            1 for source in valid_sources if str(source.get("source_class", "")).strip() in OUTLOOK_CLASSES
        ),
        "community_signal_count": sum(
            1 for source in valid_sources if str(source.get("source_class", "")).strip() in {"community", "aggregator"}
        ),
        "high_confidence_ready": high_confidence,
        "research_status": "complete" if high_confidence else "incomplete",
        "issues": list(dict.fromkeys(issues)),
        "warnings": list(dict.fromkeys(warnings)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit company research source ledgers")
    parser.add_argument("input", type=Path, help="JSON file containing one company or a companies list")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    value = json.loads(args.input.read_text(encoding="utf-8"))
    companies = value.get("companies", []) if isinstance(value, dict) else []
    if isinstance(value, dict) and "company_name" in value:
        companies = [value]
    if not isinstance(companies, list):
        raise ValueError("Input must contain a companies list")
    result = {"companies": [audit_company(item) for item in companies if isinstance(item, dict)]}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0 if all(item["high_confidence_ready"] for item in result["companies"]) else 2


if __name__ == "__main__":
    sys.exit(main())
