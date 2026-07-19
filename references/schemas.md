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
- `salary_period`
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
- `notes`
- `raw_text_hash`
- `field_mapping`
- `normalization_warnings`

## Manual CSV Header

For a simple manually prepared job file, use this header:

```csv
job_id,title,company_name,city,source_platform,source_url,collected_at,salary_min,salary_max,salary_period,experience_min,experience_max,education,responsibilities,required_skills,preferred_skills,description_raw,company_text_raw,notes
```

The absolute minimum compatible CSV is:

```csv
job_id,title,company_name
job-001,AI产品经理,示例科技
```

## Field Mapping Aliases

```yaml
job_id: ["编号", "岗位编号", "职位编号", "job_id", "id", "role_id"]
title: ["岗位", "职位", "岗位名称", "职位名称", "title", "job_title", "position", "role"]
company_name: ["公司", "企业", "公司名称", "企业名称", "company", "company_name", "employer"]
city: ["城市", "地点", "工作地点", "location", "city", "work_place"]
source_platform: ["来源平台", "平台", "source_platform", "platform", "source"]
source_url: ["链接", "URL", "url", "source_url", "job_url"]
collected_at: ["收集时间", "采集时间", "收藏时间", "collected_at", "saved_at"]
salary_min: ["最低薪资", "salary_min", "min_salary"]
salary_max: ["最高薪资", "salary_max", "max_salary"]
salary_period: ["薪资周期", "salary_period", "period"]
salary: ["薪资", "工资", "salary", "compensation"]
experience_min: ["最低经验", "经验下限", "experience_min", "min_experience"]
experience_max: ["最高经验", "经验上限", "experience_max", "max_experience"]
experience: ["经验", "工作经验", "experience", "years_experience"]
education: ["学历", "education", "degree"]
responsibilities: ["职责", "岗位职责", "工作内容", "responsibilities", "duties"]
description_raw: ["JD", "岗位描述", "职位描述", "description", "detail", "job_description", "description_raw"]
required_skills: ["要求", "任职要求", "必备技能", "required_skills", "requirements", "must_have"]
preferred_skills: ["加分项", "优先", "preferred_skills", "nice_to_have"]
company_text_raw: ["公司介绍", "企业介绍", "company_text_raw", "company_description"]
notes: ["备注", "个人备注", "notes", "user_notes"]
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
