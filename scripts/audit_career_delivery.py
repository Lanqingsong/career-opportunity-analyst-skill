#!/usr/bin/env python3
"""Audit career delivery references, resume claims, plans, and company sources."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


FACT_STATUSES = {
    "confirmed", "evidence_available", "evidence_private", "in_progress",
    "planned", "unknown", "disallowed",
}
DISCLOSURES = {"public", "abstract_only", "private", "disallowed"}
RESUME_STATUSES = {"confirmed", "evidence_available", "evidence_private"}
RESUME_DISCLOSURES = {"public", "abstract_only"}
GAP_TYPES = {
    "hard_filter", "learnable", "evidence_gap", "expression_gap",
    "preference_conflict", "unknown",
}
SOURCE_CLASSES = {"regulatory", "official", "institutional", "capital", "customer", "independent", "aggregator", "community"}


def _items(value: dict[str, Any], key: str, issues: list[dict[str, str]]) -> list[dict[str, Any]]:
    raw = value.get(key, [])
    if not isinstance(raw, list):
        issues.append({"severity": "error", "path": key, "message": "must be a list"})
        return []
    result = []
    for index, item in enumerate(raw):
        if isinstance(item, dict):
            result.append(item)
        else:
            issues.append({"severity": "error", "path": f"{key}[{index}]", "message": "must be an object"})
    return result


def _index(items: list[dict[str, Any]], key: str, path: str, issues: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(items):
        identifier = str(item.get(key, "")).strip()
        if not identifier:
            issues.append({"severity": "error", "path": f"{path}[{index}].{key}", "message": "missing identifier"})
        elif identifier in result:
            issues.append({"severity": "error", "path": f"{path}[{index}].{key}", "message": "duplicate identifier"})
        else:
            result[identifier] = item
    return result


def _refs(item: dict[str, Any], key: str) -> list[str]:
    value = item.get(key, [])
    return [str(entry).strip() for entry in value if str(entry).strip()] if isinstance(value, list) else []


def _check_refs(
    items: list[dict[str, Any]], field: str, known: set[str], path: str, issues: list[dict[str, str]],
    *, required: bool = False,
) -> None:
    for index, item in enumerate(items):
        refs = _refs(item, field)
        if required and not refs:
            issues.append({"severity": "error", "path": f"{path}[{index}].{field}", "message": "at least one reference required"})
        for ref in refs:
            if ref not in known:
                issues.append({"severity": "error", "path": f"{path}[{index}].{field}", "message": f"unknown reference: {ref}"})


def audit_delivery(value: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    facts = _items(value, "candidate_facts", issues)
    requirements = _items(value, "job_requirements", issues)
    directions = _items(value, "directions", issues)
    gaps = _items(value, "gaps", issues)
    resumes = _items(value, "resumes", issues)
    tasks = _items(value, "learning_tasks", issues)
    companies = _items(value, "companies", issues)
    sources = _items(value, "sources", issues)

    fact_map = _index(facts, "fact_id", "candidate_facts", issues)
    requirement_map = _index(requirements, "requirement_id", "job_requirements", issues)
    direction_map = _index(directions, "direction_id", "directions", issues)
    gap_map = _index(gaps, "gap_id", "gaps", issues)
    source_map = _index(sources, "source_id", "sources", issues)

    for index, fact in enumerate(facts):
        status = str(fact.get("status", ""))
        disclosure = str(fact.get("disclosure_level", ""))
        if status not in FACT_STATUSES:
            issues.append({"severity": "error", "path": f"candidate_facts[{index}].status", "message": "invalid fact status"})
        if disclosure not in DISCLOSURES:
            issues.append({"severity": "error", "path": f"candidate_facts[{index}].disclosure_level", "message": "invalid disclosure level"})

    _check_refs(directions, "requirement_ids", set(requirement_map), "directions", issues, required=True)
    _check_refs(directions, "evidence_fact_ids", set(fact_map), "directions", issues)
    _check_refs(directions, "gap_ids", set(gap_map), "directions", issues)
    _check_refs(gaps, "requirement_ids", set(requirement_map), "gaps", issues, required=True)
    _check_refs(gaps, "evidence_fact_ids", set(fact_map), "gaps", issues)

    for index, gap in enumerate(gaps):
        if str(gap.get("gap_type", "")) not in GAP_TYPES:
            issues.append({"severity": "error", "path": f"gaps[{index}].gap_type", "message": "invalid gap type"})

    for resume_index, resume in enumerate(resumes):
        direction_ids = _refs(resume, "target_direction_ids")
        if not direction_ids:
            issues.append({"severity": "error", "path": f"resumes[{resume_index}].target_direction_ids", "message": "at least one target direction required"})
        for direction_id in direction_ids:
            if direction_id not in direction_map:
                issues.append({"severity": "error", "path": f"resumes[{resume_index}].target_direction_ids", "message": f"unknown reference: {direction_id}"})
        claims = resume.get("claims", [])
        if not isinstance(claims, list):
            issues.append({"severity": "error", "path": f"resumes[{resume_index}].claims", "message": "must be a list"})
            continue
        for claim_index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                issues.append({"severity": "error", "path": f"resumes[{resume_index}].claims[{claim_index}]", "message": "must be an object"})
                continue
            fact_ids = _refs(claim, "fact_ids")
            if not fact_ids:
                issues.append({"severity": "error", "path": f"resumes[{resume_index}].claims[{claim_index}].fact_ids", "message": "resume claim has no supporting fact"})
            for fact_id in fact_ids:
                fact = fact_map.get(fact_id)
                if not fact:
                    issues.append({"severity": "error", "path": f"resumes[{resume_index}].claims[{claim_index}].fact_ids", "message": f"unknown reference: {fact_id}"})
                elif fact.get("status") not in RESUME_STATUSES or fact.get("disclosure_level") not in RESUME_DISCLOSURES:
                    issues.append({"severity": "error", "path": f"resumes[{resume_index}].claims[{claim_index}]", "message": f"fact {fact_id} is not eligible for a completed resume claim"})

    for index, task in enumerate(tasks):
        task_gap_ids = _refs(task, "gap_ids")
        if not task_gap_ids:
            issues.append({"severity": "error", "path": f"learning_tasks[{index}].gap_ids", "message": "at least one reference required"})
        for gap_id in task_gap_ids:
            if gap_id not in gap_map:
                issues.append({"severity": "error", "path": f"learning_tasks[{index}].gap_ids", "message": f"unknown reference: {gap_id}"})
        for field in ("deliverable", "resume_use_gate"):
            if not str(task.get(field, "")).strip():
                issues.append({"severity": "error", "path": f"learning_tasks[{index}].{field}", "message": "required"})
        criteria = task.get("acceptance_criteria", [])
        if not isinstance(criteria, list) or not any(str(item).strip() for item in criteria):
            issues.append({"severity": "error", "path": f"learning_tasks[{index}].acceptance_criteria", "message": "at least one criterion required"})

    source_domains: dict[str, str] = {}
    source_classes: dict[str, str] = {}
    for index, source in enumerate(sources):
        source_id = str(source.get("source_id", ""))
        parsed = urlparse(str(source.get("url", "")))
        source_class = str(source.get("source_class", ""))
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            issues.append({"severity": "error", "path": f"sources[{index}].url", "message": "invalid URL"})
        else:
            source_domains[source_id] = parsed.netloc.lower().removeprefix("www.")
        if source_class not in SOURCE_CLASSES:
            issues.append({"severity": "error", "path": f"sources[{index}].source_class", "message": "invalid source class"})
        else:
            source_classes[source_id] = source_class
        if not str(source.get("claim", "")).strip():
            issues.append({"severity": "error", "path": f"sources[{index}].claim", "message": "missing claim mapping"})

    for index, company in enumerate(companies):
        refs = _refs(company, "source_ids")
        for ref in refs:
            if ref not in source_map:
                issues.append({"severity": "error", "path": f"companies[{index}].source_ids", "message": f"unknown reference: {ref}"})
        if company.get("confidence") == "high":
            domains = {source_domains.get(ref) for ref in refs if source_domains.get(ref)}
            classes = {source_classes.get(ref) for ref in refs if source_classes.get(ref)}
            if len(refs) < 2 or len(domains) < 2 or not classes & {"official", "regulatory"} or "independent" not in classes:
                issues.append({"severity": "error", "path": f"companies[{index}]", "message": "high-confidence company lacks independent multi-source coverage"})

    error_count = sum(issue["severity"] == "error" for issue in issues)
    return {
        "valid": error_count == 0,
        "error_count": error_count,
        "warning_count": sum(issue["severity"] == "warning" for issue in issues),
        "counts": {
            "facts": len(facts), "requirements": len(requirements), "directions": len(directions),
            "gaps": len(gaps), "resumes": len(resumes), "learning_tasks": len(tasks),
            "companies": len(companies), "sources": len(sources),
        },
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a career delivery manifest")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    value = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Delivery manifest must be a JSON object")
    result = audit_delivery(value)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    sys.exit(main())
