# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

A local-agent skill for career opportunity analysis. It can be used with Codex, WorkBuddy, Claude Code, or any local agent that can read repository files. Codex is one supported environment, not the whole point of the project.

The job is simple: help a user understand who they are, what they want, which companies are worth joining, whether the role has a future, how many resume versions are needed, and how to prepare for interviews without leaking confidential work.

## Positioning

This is not a resume-polishing template and not a generic job scorecard. It is a local career analysis workflow with three priorities:

1. Discover the user's real needs and experience: goals, preferences, concerns, actual contribution, public evidence, and confidentiality boundaries.
2. Research company and career outlook first: business prospects, role future, work pressure, promotion room, growth environment, and team culture.
3. Then decide role fit: target directions, shortlisted opportunities, resume versions, interview preparation, and 30/90/180-day improvement plan.

Company research here does not mean only checking whether the company legally exists. That is only a small baseline check. The useful question is whether the company and role are worth the user's time and whether joining would help or hurt the user's career.

## Recommended Companion Tool

Recommended companion tool: the Chrome extension [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor).

The extension is not meant for blind bulk scraping. The intended workflow is human-in-the-loop: the user browses job boards, adds personally interesting roles to a candidate pool, and exports that pool as CSV/JSON. The local agent then does the deeper analysis.

Recommended flow:

1. Browse job boards normally.
2. Add interesting roles to the candidate pool with the `job-page-extractor` Chrome extension.
3. Export candidate roles as CSV/JSON.
4. Give the job file, resume, notes, preferences, and confidentiality boundaries to the local agent.
5. Ask the agent to run `$analyze-career-opportunities`.

The extension is optional. A manually prepared CSV also works. Start from [assets/job-input-template.csv](assets/job-input-template.csv).

## Invocation Name

```text
analyze-career-opportunities
```

Example prompt:

```text
Use $analyze-career-opportunities. Read my job CSV, resume, and candidate notes.
First clarify my real needs, experience, preferences, and confidentiality boundaries. Then research company and career outlook for the roles in the job file, focusing on business prospects, role growth, work pressure, promotion room, learning environment, team culture, and forum/community feedback. After that, summarize the market, choose suitable directions, shortlist roles, decide how many resume versions are needed, draft those versions, prepare interview material, and create a 30/90/180-day improvement plan.
Do not present planned work as completed experience. Keep confidential work safely abstract.
```

## What It Delivers

A complete run usually includes:

1. User needs profile: location, industry, compensation, workload, company preference, and deal-breakers.
2. Experience discovery: what the user actually did, responsibility boundary, public evidence, and private evidence.
3. Job input check: CSV/JSON field mapping, missing fields, source links, and notes.
4. Company and career-outlook research: business prospects, role future, work pressure, promotion room, learning environment, and team culture.
5. Job-market summary: role clusters, common requirements, differentiators, and hard filters.
6. Suitable directions: one to three directions worth serious effort.
7. Target opportunities: company outlook, work environment, and role fit kept separate.
8. Resume set: the minimum number of targeted resume versions and the actual drafts.
9. Interview preparation: HR questions, technical depth, project explanation, and confidentiality-safe answers.
10. 30/90/180-day plan: deliverables, acceptance criteria, resume-use gates, and fallback scopes.

## Company And Career-Outlook Research

The local agent should do this work instead of handing it back to the user.

The focus is not only whether the company exists. The useful questions are:

- Business prospects: growing, shrinking, pivoting, or unclear.
- Career prospects: whether the role builds experience recognized by the next employer.
- Role position: core business, growth business, support function, outsourcing delivery, or temporary experiment.
- Work pressure: overtime, delivery pressure, turnover, management style.
- Promotion room: levels, internal mobility, mentoring, and promotion path.
- Growth environment: tech stack, mentor resources, business complexity, and chance to produce visible results.
- Team culture: communication style, stability, management feedback, and cross-team friction.

Useful sources include official pages and news, but also forums, employee reviews, social posts, recruiting-platform comments, Maimai, Kanzhun, Glassdoor, Zhihu, Xiaohongshu, Reddit, and other public discussions. Official sources are better for business facts. Forum and community sources are better for pressure, culture, promotion, and management signals.

Handle community sources carefully. Look for repeated patterns across independent posts; do not treat a single complaint as a conclusion. If coverage is weak, mark the result as `incomplete` or `watch`.

## Job CSV Format

The minimum CSV needs only three columns:

```csv
job_id,title,company_name
job-001,AI Product Manager,Example Tech
```

For better analysis, use the full header:

```csv
job_id,title,company_name,city,source_platform,source_url,collected_at,salary_min,salary_max,salary_period,experience_min,experience_max,education,responsibilities,required_skills,preferred_skills,description_raw,company_text_raw,notes
```

Field guide:

- `job_id`: Unique role ID. Required.
- `title`: Role title. Required.
- `company_name`: Company name. Required.
- `city`: Work location.
- `source_platform`: Source platform, such as BOSS, Lagou, Liepin, LinkedIn, or company website.
- `source_url`: Job posting URL.
- `collected_at`: Collection date. Prefer `YYYY-MM-DD`.
- `salary_min` / `salary_max`: Salary range.
- `salary_period`: `month`, `year`, or `day`.
- `experience_min` / `experience_max`: Experience requirement in years.
- `education`: Education requirement.
- `responsibilities`: Main responsibilities.
- `required_skills`: Must-have skills.
- `preferred_skills`: Nice-to-have skills.
- `description_raw`: Original JD text.
- `company_text_raw`: Company description from the job page.
- `notes`: User notes, such as "very interested", "salary unclear", or "long commute".

Field names do not need to match exactly, but the English headers above reduce mapping errors.

## Install For Local Agents

This repository uses the Codex Skill folder format. For Codex, install it under:

```text
analyze-career-opportunities
```

Windows PowerShell:

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" | Out-Null
Copy-Item -Recurse -Force ".\career-opportunity-analyst-skill\*" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

macOS / Linux:

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
mkdir -p ~/.codex/skills/analyze-career-opportunities
cp -R career-opportunity-analyst-skill/* ~/.codex/skills/analyze-career-opportunities/
```

For WorkBuddy, Claude Code, or other local agents, load this repository as a local knowledge or tool folder and tell the agent to read `SKILL.md` first, then use `references/` and `scripts/` as needed.

Agent-oriented installation instructions are in [AI_INSTALL.md](AI_INSTALL.md).

## Local Scripts

Profile a job file:

```powershell
python scripts/profile_job_input.py path\to\jobs.csv
```

Audit a company source ledger:

```powershell
python scripts/audit_company_sources.py company-sources.json
```

Audit a complete delivery manifest:

```powershell
python scripts/audit_career_delivery.py delivery-manifest.json
```

The scripts check structure and evidence rules. They do not replace human judgment.

## Privacy

Candidate material stays local by default. Do not upload resumes, job files, project details, internal data, or confidential work material to unrelated services.

For confidential experience, ask only for: problem class, responsibility boundary, constraints, trade-offs, validation method, and generalized outcomes. Do not request source code, internal datasets, logs, model weights, customer identities, unreleased algorithms, or sensitive internal metrics.

## License

Apache-2.0.
