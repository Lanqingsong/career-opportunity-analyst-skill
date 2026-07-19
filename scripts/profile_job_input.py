#!/usr/bin/env python3
"""Profile CSV/JSON job input without third-party dependencies."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


ALIASES = {
    "title": ["岗位", "职位", "岗位名称", "title", "job_title", "position", "role"],
    "company_name": ["公司", "企业", "公司名称", "company", "company_name", "employer"],
    "city": ["城市", "地点", "工作地点", "location", "city", "work_place"],
    "description_raw": ["jd", "岗位描述", "职位描述", "description", "detail", "job_description"],
    "required_skills": ["要求", "任职要求", "required_skills", "requirements", "must_have"],
    "preferred_skills": ["加分项", "优先", "preferred_skills", "nice_to_have"],
    "salary_min": ["最低薪资", "salary_min", "min_salary"],
    "salary_max": ["最高薪资", "salary_max", "max_salary"],
    "salary": ["薪资", "工资", "salary", "compensation"],
    "experience": ["经验", "工作经验", "experience", "years_experience"],
    "education": ["学历", "education", "degree"],
    "source_url": ["链接", "url", "source_url", "job_url"],
}
REQUIRED = {"title", "company_name"}


def _normalize(value: Any) -> str:
    return str(value or "").strip().lower().replace(" ", "").replace("-", "_")


def _read_text(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(encoding), encoding
        except UnicodeDecodeError:
            pass
    raise ValueError("Input is not valid UTF-8, UTF-8 BOM, or GB18030 text")


def load_records(path: Path) -> tuple[list[dict[str, Any]], str]:
    text, encoding = _read_text(path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return [dict(row) for row in csv.DictReader(text.splitlines())], encoding
    if suffix == ".json":
        value = json.loads(text)
        if isinstance(value, list):
            records = value
        elif isinstance(value, dict):
            records = value.get("jobs") or value.get("items") or value.get("data") or []
        else:
            records = []
        if not isinstance(records, list) or not all(isinstance(item, dict) for item in records):
            raise ValueError("JSON must be a list of objects or contain jobs/items/data list")
        return records, encoding
    raise ValueError("Only .csv and .json job files are supported")


def infer_mapping(headers: list[str]) -> dict[str, dict[str, Any]]:
    normalized = {_normalize(header): header for header in headers}
    result: dict[str, dict[str, Any]] = {}
    for canonical, aliases in ALIASES.items():
        candidates = [_normalize(canonical), *(_normalize(alias) for alias in aliases)]
        source = next((normalized[item] for item in candidates if item in normalized), None)
        if source:
            result[canonical] = {
                "source_header": source,
                "confidence": "high" if _normalize(source) == _normalize(canonical) else "medium",
            }
    return result


def profile(path: Path) -> dict[str, Any]:
    records, encoding = load_records(path)
    headers = list(dict.fromkeys(key for record in records for key in record))
    mapping = infer_mapping(headers)
    warnings: list[str] = []
    if not records:
        warnings.append("job file contains no records")
    for field in sorted(REQUIRED):
        if field not in mapping:
            warnings.append(f"required field not mapped: {field}")
    coverage: dict[str, dict[str, Any]] = {}
    for canonical, details in mapping.items():
        source = details["source_header"]
        populated = sum(1 for record in records if str(record.get(source, "")).strip())
        coverage[canonical] = {
            **details,
            "populated": populated,
            "coverage": round(populated / len(records), 4) if records else 0.0,
        }
        if canonical in REQUIRED and populated < len(records):
            warnings.append(f"{canonical} missing in {len(records) - populated} records")
    unmapped = [header for header in headers if header not in {item["source_header"] for item in mapping.values()}]
    return {
        "path": str(path),
        "format": path.suffix.lower().removeprefix("."),
        "encoding": encoding,
        "record_count": len(records),
        "headers": headers,
        "field_mapping": coverage,
        "unmapped_headers": unmapped,
        "warnings": warnings,
        "ready": bool(records) and not any(message.startswith("required field not mapped") for message in warnings),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile a career job CSV/JSON input")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = profile(args.input)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0 if result["ready"] else 2


if __name__ == "__main__":
    sys.exit(main())
