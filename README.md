# Career Opportunity Analyst Skill

A Codex Skill for evidence-grounded career opportunity analysis.

This repository contains one installable Codex Skill:

```text
analyze-career-opportunities
```

It turns job CSV/JSON files plus candidate material into a complete career delivery package: candidate evidence ledger, job-market clusters, suitable directions, shortlisted opportunities, minimum targeted resume set, interview preparation, confidentiality-safe answers, and an executable 30/90/180-day growth plan.

## What Problem It Solves

Most job matching workflows collapse too many questions into one vague score:

- Is the company worth attention?
- Does the role fit the candidate today?
- Can the candidate become competitive in three to six months?
- Is the candidate actually missing a capability, or only missing public evidence?
- Does a planned project already count as experience? It should not.
- Can private work be discussed safely without exposing code, data, clients, logs, model weights, or internal metrics?

This Skill separates those judgments. It keeps company quality, current role fit, reachable future fit, evidence strength, preference compatibility, and hard filters visible as different dimensions. It also preserves fact states such as `confirmed`, `evidence_available`, `evidence_private`, `in_progress`, `planned`, `unknown`, and `disallowed`, so an AI does not accidentally turn missing information into weakness or future plans into completed experience.

## What It Produces

When the input supports a complete package, the Skill produces:

1. Input inventory and job-file field mapping.
2. Candidate fact and evidence ledger.
3. Job-market clusters and requirement map.
4. One to three suitable career directions.
5. Target companies and roles, with company judgment separated from role fit.
6. Gap analysis with hard, reachable, evidence, expression, preference, and unknown gaps.
7. The minimum useful resume set, normally one to three versions.
8. Interview question tree and confidentiality-safe answer frames.
9. A 30/90/180-day evidence-producing plan.
10. A delivery manifest that can be audited by the included scripts.

## Key Features

- Works with CSV/JSON job exports, including generic job tables and `job-page-extractor` style exports.
- Treats a resume as optional; free-form candidate notes, project material, portfolio links, and corrections are first-class input.
- Groups jobs by responsibility and capability pattern rather than title alone.
- Researches only shortlisted companies, using Codex's built-in web tools. It does not ask the user for a search API key.
- Requires source-backed company claims and marks weak coverage as incomplete instead of negative.
- Separates private evidence from public resume claims.
- Prevents planned or in-progress projects from being written as completed experience.
- Determines the smallest useful set of targeted resumes instead of creating one resume per job.
- Converts gaps into tasks with deliverables, acceptance criteria, resume-use gates, dependencies, and fallback scopes.
- Includes local audit scripts for job input profiling, company-source coverage, and delivery-manifest consistency.

## Repository Layout

```text
.
├── SKILL.md
├── README.md
├── AI_INSTALL.md
├── LICENSE
├── agents/
├── assets/
├── references/
└── scripts/
```

## Install For Codex

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

If you are asking another AI agent to install it, use [AI_INSTALL.md](AI_INSTALL.md). That file is written as an agent-executable installation and verification procedure.

## How To Use In Codex

Use the Skill name directly in your request:

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍。
请完成完整职业交付：评估当前能力，归纳岗位市场和适合方向，筛选目标机会，
判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。
不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

English example:

```text
Use $analyze-career-opportunities. Read my job CSV, resume, preferences, and project notes.
Produce a complete career package: candidate evidence ledger, market clusters, suitable directions,
shortlisted roles, minimum targeted resume set, interview preparation, confidentiality-safe answers,
and a 30/90/180-day growth plan. Do not present planned work as completed experience.
```

## Input Guidance

Good inputs include job CSV/JSON files, resumes, free-form career notes, project summaries, publications, patents, portfolio links, location and compensation preferences, corrections to earlier facts, and confidentiality boundaries.

Do not provide work source code, internal datasets, credentials, cookies, tokens, private chat logs, production logs, model weights, client identities, unreleased algorithms, or sensitive internal metrics.

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

The audit scripts do not prove career recommendations are correct. They check reference consistency, unsafe resume claims, missing task gates, and source coverage rules so another agent cannot silently weaken the evidence contract.

## Privacy Model

The Skill is local-first. Candidate material should remain local unless the user explicitly asks Codex to research public company information or authorizes a specific external operation.

For confidential work, the Skill should ask only for safe abstract information: problem class, responsibility boundary, constraints, trade-offs, validation method, and generalized outcomes. It should not request source code, datasets, logs, weights, customer names, or internal metrics.

## License

Apache-2.0.
