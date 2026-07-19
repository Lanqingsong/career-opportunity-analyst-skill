# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

A Codex Skill for evidence-grounded career opportunity analysis. It turns job CSV/JSON files, resumes, candidate notes, project material, preferences, and corrections into a complete career delivery package.

## Recommended Upstream Tool

Use [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) first to collect job pages and export them as CSV/JSON.

Recommended workflow:

1. Use `job-page-extractor` to collect or organize job pages.
2. Export a job file such as `jobs.csv` or `jobs.json`.
3. Provide the job file, resume, candidate notes, preferences, and confidentiality boundaries to `$analyze-career-opportunities`.
4. Let this Skill produce target directions, shortlisted roles, resume-version planning, interview material, and a growth plan.

The Skill can also read ordinary CSV/JSON job tables that were not produced by `job-page-extractor`, as long as the fields contain enough title, company, location, responsibility, requirement, and source information.

## Skill Invocation Name

```text
analyze-career-opportunities
```

Use it in Codex like this:

```text
Use $analyze-career-opportunities. Read my job CSV, resume, preferences, and project notes.
Produce a complete career package: candidate evidence ledger, market clusters, suitable directions,
shortlisted roles, minimum targeted resume set, interview preparation, confidentiality-safe answers,
and a 30/90/180-day growth plan. Do not present planned work as completed experience.
```

Chinese example:

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍，请完成完整职业交付：评估当前能力，归纳岗位市场和适合方向，筛选目标机会，判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

## What Problem It Solves

Many job-matching workflows collapse too many questions into one vague score:

- Is the company worth attention?
- Does the role fit the candidate today?
- Can the candidate become competitive in three to six months?
- Is the candidate actually missing a capability, or only missing public evidence?
- Does a planned project accidentally get written as completed experience?
- Can confidential work be discussed safely without exposing code, data, clients, logs, model weights, or internal metrics?

This Skill separates those judgments. It keeps company quality, current fit, reachable future fit, evidence strength, preference compatibility, and hard filters visible as different dimensions.

It also preserves fact states such as:

```text
confirmed
evidence_available
evidence_private
in_progress
planned
unknown
disallowed
```

This helps prevent an AI from turning unknown information into weakness or future plans into completed experience.

## What It Produces

When the input material supports a complete package, the Skill produces:

1. Input inventory and job-file field mapping.
2. Candidate fact and evidence ledger.
3. Job-market clusters and requirement map.
4. One to three suitable career directions.
5. Target companies and roles, with company quality separated from role fit.
6. Gap analysis across hard, reachable, evidence, expression, preference, and unknown gaps.
7. Minimum useful resume set, usually one to three versions instead of one resume per job.
8. HR, technical, project-deep-dive, and confidentiality-safe interview material.
9. A 30/90/180-day improvement plan with deliverables, acceptance criteria, resume-use gates, and fallback scopes.
10. An audit-ready `delivery-manifest.json`.

## Key Features

- Supports job CSV/JSON exports from `job-page-extractor` and ordinary job tables.
- Treats resumes as optional; candidate notes, project material, portfolio links, preferences, and corrections are first-class inputs.
- Clusters jobs by responsibility and capability patterns rather than title alone.
- Researches only shortlisted companies to avoid unnecessary investigation.
- Requires source-backed company claims and marks weak coverage as incomplete or low confidence instead of inventing conclusions.
- Separates public resume evidence from private evidence that can only be discussed safely in interviews.
- Prevents planned or in-progress work from being written as completed experience.
- Produces the minimum useful set of targeted resume versions.
- Converts gaps into concrete tasks with deliverables, acceptance criteria, dependencies, and fallback scopes.
- Includes local audit scripts for job input profiling, company-source coverage, and delivery-manifest consistency.

## Repository Layout

```text
.
|-- SKILL.md
|-- README.md
|-- README.en.md
|-- AI_INSTALL.md
|-- LICENSE
|-- agents/
|-- assets/
|-- references/
`-- scripts/
```

## Install For Codex

This repository is one installable Skill. The target directory name must be:

```text
analyze-career-opportunities
```

If another AI agent is installing it, give the agent [AI_INSTALL.md](AI_INSTALL.md). That file contains an agent-oriented installation and verification procedure.

### Windows PowerShell

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" | Out-Null
Copy-Item -Recurse -Force ".\career-opportunity-analyst-skill\*" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

Then start a new Codex task so the Skill metadata is loaded.

### macOS / Linux

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
mkdir -p ~/.codex/skills/analyze-career-opportunities
cp -R career-opportunity-analyst-skill/* ~/.codex/skills/analyze-career-opportunities/
```

Then start a new Codex task.

## Detailed Usage

### 1. Prepare Job Data

Use [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) to convert job pages into CSV/JSON. Common fields may include:

- company
- title
- location
- salary
- responsibilities
- requirements
- source_url
- published_at
- notes

Field names do not need to match exactly. The Skill begins by mapping fields and checking input quality.

### 2. Prepare Candidate Material

Good inputs include:

- Resume.
- Free-form candidate introduction.
- Project summaries.
- Portfolio, paper, patent, GitHub, blog, or public profile links.
- Preferences about location, industry, compensation, work intensity, and company type.
- Corrections to previous facts.
- Disclosure boundaries: what can be public, what can be safely abstracted, and what cannot be mentioned.

Do not provide:

- Work source code.
- Internal datasets.
- Credentials, cookies, tokens, or API keys.
- Production logs.
- Model weights.
- Client identities.
- Unreleased algorithms.
- Sensitive internal metrics.

### 3. Ask Codex To Use The Skill

Recommended prompt:

```text
Use $analyze-career-opportunities. Read the provided job CSV/JSON, resume or candidate notes,
project material, public profile links, and career preferences.

Produce the complete career package:
1. Input inventory and field mapping.
2. Candidate fact and evidence ledger.
3. Job-market clusters and requirement map.
4. One to three suitable directions.
5. Shortlisted target companies and roles.
6. Gap analysis across hard, reachable, evidence, expression, preference, and unknown gaps.
7. Minimum useful tailored resume set and the corresponding resume versions.
8. HR, technical, and confidentiality-safe interview preparation.
9. 30/90/180-day improvement plan.
10. delivery-manifest.json plus audit-script verification.

Do not turn planned or in-progress work into completed experience. Keep confidential work safely abstract.
Do not request source code, internal datasets, logs, model weights, client identities, or unreleased metrics.
```

## Audit Scripts

Profile an unfamiliar job file:

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

The audit scripts do not prove that every career recommendation is correct. They check whether the delivery follows the evidence contract: reference consistency, unsafe resume claims, missing task gates, and company-source coverage.

## Privacy Model

The Skill is local-first. Candidate material should stay local unless the user explicitly asks Codex to research public company information or authorizes a specific external operation.

For confidential work, the Skill should ask only for safe abstract information:

- Problem class.
- Personal responsibility boundary.
- Constraints.
- Trade-offs.
- Validation method.
- Generalized outcomes.

It should not request source code, internal datasets, logs, model weights, customer names, unreleased algorithms, or sensitive internal metrics.

## License

Apache-2.0.
