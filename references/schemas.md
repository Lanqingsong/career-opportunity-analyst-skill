# Schemas Reference

Use this reference when mapping job files, resumes, and candidate facts.

## JobRecord v1

Required:

- `job_id`
- `title`
- `company_name`

Recommended:

- `source_platform`
- `source_url`
- `collected_at`
- `extractor_version`
- `salary_min`
- `salary_max`
- `salary_periods`
- `city`
- `experience_min`
- `experience_max`
- `education`
- `description_raw`
- `responsibilities`
- `required_skills`
- `preferred_skills`
- `company_text_raw`
- `address`
- `raw_text_hash`
- `field_mapping`
- `normalization_warnings`

## Field Mapping Aliases

```yaml
title: ["岗位", "职位", "岗位名称", "title", "job_title", "position", "role"]
company_name: ["公司", "企业", "公司名称", "company", "company_name", "employer"]
city: ["城市", "地点", "工作地点", "location", "city", "work_place"]
description_raw: ["JD", "岗位描述", "职位描述", "description", "detail", "job_description"]
required_skills: ["要求", "任职要求", "required_skills", "requirements", "must_have"]
preferred_skills: ["加分项", "优先", "preferred_skills", "nice_to_have"]
salary_min: ["最低薪资", "salary_min", "min_salary"]
salary_max: ["最高薪资", "salary_max", "max_salary"]
source_url: ["链接", "URL", "source_url", "job_url"]
```

## Candidate Fact Status

- `confirmed`: user confirmed with factual basis.
- `evidence_available`: public or safely shareable evidence exists.
- `evidence_private`: fact is true but evidence is confidential.
- `in_progress`: currently underway.
- `planned`: planned only.
- `unknown`: missing or conflicting.
- `disallowed`: must not be used externally.

Never convert `unknown` to inability. Never convert `planned` to completed work.

