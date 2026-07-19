# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

A Skill for job seekers who want to make better career-opportunity decisions. Recruiting platforms are not very fair to candidates: it is hard to tell which companies are actually suitable, and even harder to know how to close role gaps, explain experience clearly, and spend application effort on roles that deserve it.

This Skill can be used inside Codex, WorkBuddy, Claude Code, or any local Agent workflow that can read local files.

It puts the core questions in one place: who you are, what you want, which companies are worth considering, whether the opportunity is healthy for your development, how the resume should be written, and how the interview story should be prepared.

## Positioning

This Skill is not a professional resume-polishing template and not a simple job scorecard. It works more like a career-analysis assistant, with three priorities:

1. Clarify user needs and experience: goals, preferences, concerns, real experience, public evidence, and confidentiality boundaries.
2. Look at company and career outlook first: development space, business quality, role future, work pressure, promotion room, growth environment, and team culture.
3. Then handle role matching: directions, opportunities, resume versions, interview material, and a 30/90/180-day improvement plan.

Company research here answers the questions candidates actually care about: is this company worth applying to, can I grow after joining, will the work consume too much, and does the role have a future?

The research is limited to public internet information and what the Agent can access. Its truthfulness still needs to be checked by the user. It is not an audit or a guarantee; it is a way to organize multiple signals into a clearer decision.

## Recommended Companion Tool

Recommended companion tool: the Chrome extension [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor).

The extension lets users add interesting roles to a candidate pool while browsing job sites, then export that pool as CSV/JSON. Human interest filters the first layer; the local Agent does the deeper analysis.

Recommended flow:

1. Browse job sites normally.
2. Add interesting roles to the candidate pool with the `job-page-extractor` Chrome extension.
3. Export the candidate roles as CSV/JSON.
4. Give the job file, resume, notes, preferences, and confidentiality boundaries to the local Agent.
5. Use `$analyze-career-opportunities` to research company and career outlook, screen opportunities, plan resume versions, prepare interviews, and build an improvement plan.

The extension is optional. A manually prepared CSV also works. Start from [assets/job-input-template.csv](assets/job-input-template.csv).

## Invocation Name

```text
analyze-career-opportunities
```

Example prompt:

```text
Use $analyze-career-opportunities. Read my job CSV, resume, and candidate notes.
First clarify my real needs, experience, preferences, and confidentiality boundaries. Then research company and career outlook for the roles in the job file, focusing on business prospects, funding, institutional views, role growth, work pressure, promotion room, team culture, and forum/community feedback. After that, summarize the job market, choose suitable directions, shortlist roles, decide how many resume versions are needed, draft those versions, prepare interview material, and create a 30/90/180-day improvement plan.
Do not present planned work as completed experience. Keep confidential work safely abstract.
```

## What It Delivers

A complete run usually includes:

1. User needs profile: target city, industry, compensation, workload, company preference, and deal-breakers.
2. Experience discovery: what the user actually did, responsibility boundary, public evidence, and private evidence.
3. Job input check: CSV/JSON field mapping, missing fields, source links, and notes.
4. Company and career-outlook research: development prospects, funding and institutional views, business quality, role growth, work pressure, promotion room, learning environment, and team culture.
5. Job-market summary: role clusters, common requirements, differentiators, and hard filters.
6. Suitable directions: one to three directions worth serious effort, with reasons.
7. Target opportunities: company outlook, work environment, and role fit kept separate instead of merged into one vague score.
8. Resume set: the minimum number of targeted resume versions and the corresponding drafts.
9. Interview preparation: HR questions, technical depth, project story, and confidentiality-safe answers.
10. 30/90/180-day plan: deliverables, acceptance criteria, resume-use gates, and fallback scopes.

## Company And Career-Outlook Research

Company research is not only about whether a company exists. It separates development signals from work-experience signals.

| Signal Type | What It Looks At | Why It Matters |
| --- | --- | --- |
| Institutional views | Brokerages, consulting firms, research organizations, industry associations, industry reports | Helps judge the market and company outlook |
| Funding and capital | Funding rounds, investor quality, shareholder background, IPO or M&A progress | Gives side evidence for capital recognition and stage potential |
| Commercial adoption | Customer cases, partners, government projects, tender records, product deployment | Shows whether the business has real-world traction |
| Role position | Core business, growth business, support function, outsourcing delivery, temporary experiment | Helps judge whether the role can build useful experience |
| Work experience | Overtime, delivery pressure, turnover, management style | Helps judge whether the pressure is acceptable |
| Growth environment | Tech stack, mentor resources, business complexity, promotion path | Helps judge whether the user can grow after joining |
| Team culture | Communication style, stability, management reviews, cross-team collaboration | Helps judge whether the long-term work environment is healthy |

Useful sources include official pages, news, funding information, investor announcements, industry reports, customer cases, forums, employee reviews, social posts, recruiting-platform comments, Maimai, Kanzhun, Glassdoor, Zhihu, Xiaohongshu, Reddit, and other public discussions.

Different sources answer different questions. Official pages are useful for business facts; institutional views, funding records, and customer cases are strong signals for company outlook; forums and communities are better for pressure, culture, promotion, and management issues.

All internet information should be handled carefully. Funding does not prove a company will succeed. Institutional views may be stale or biased. A single forum complaint is not a conclusion. Better wording is "strong signal", "supporting evidence", and "needs interview verification", not "proven fact".

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

For WorkBuddy, Claude Code, or other local Agents, share this repository link with them and let them install it.

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

## Push Helper

If the GitHub remote already has new commits, a plain `git push` may stop at a rebase conflict or detached HEAD state. This repository includes a Windows push helper for common cases:

- Adds the repository to Git `safe.directory`.
- Checks rebase and conflict state.
- Commits current local changes.
- Fetches the remote branch and rebases local commits on top of it.
- Pushes to `origin/main`.

Run from the repository root:

```powershell
.\push.cmd
```

With a custom commit message:

```powershell
.\push.cmd -Message "docs: update readme"
```

If there is a real content conflict, the helper stops and lists the conflicted files. Fix them manually, then run `.\push.cmd` again.

## Privacy

Candidate material stays local by default. Please do not upload project details, internal data, or confidential company material to AI services.

For confidential experience, keep the abstraction at this level: problem type, personal responsibility boundary, constraints, trade-offs, validation method, and generalized result. Do not request source code, internal datasets, logs, model weights, customer identities, unreleased algorithms, or sensitive internal metrics.

## License

Apache-2.0.
