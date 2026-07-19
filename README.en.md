# Career Opportunity Analyst Skill

[简体中文](README.md) | English

A career opportunity research and decision-support Skill for job seekers.

Most recruiting platforms are designed to help employers filter candidates—not to help candidates decide which companies are genuinely worth joining. Job seekers are often left to answer difficult questions on their own:

* Is this company actually a good fit for me?
* Does the role offer meaningful long-term growth?
* Will the work build valuable experience or simply consume my time?
* Which gaps should I close first?
* How should I present my experience without exaggerating or exposing confidential information?
* Which opportunities deserve a tailored résumé and serious interview preparation?

Career Opportunity Analyst brings these questions into one structured workflow.

It is designed for Codex, WorkBuddy, Claude Code, and other local Agent environments that can read files, research public information, and generate structured deliverables.

The Skill helps an Agent analyze:

* who you are;
* what kind of work you are looking for;
* which companies and roles are worth pursuing;
* whether an opportunity supports healthy career development;
* how many résumé versions you need;
* how to prepare for interviews;
* and what to improve over the next 30, 90, and 180 days.

---

## What This Skill Is

Career Opportunity Analyst is not a generic résumé-polishing template, and it is not a simplistic job-scoring tool.

It acts more like a career research and decision-support assistant.

Its work focuses on three areas:

1. **Understanding the candidate**

   It identifies the candidate’s goals, preferences, concerns, real experience, public evidence, and confidentiality boundaries.

2. **Researching companies and career prospects**

   It examines business quality, industry outlook, financing, role positioning, growth potential, workload, promotion opportunities, learning conditions, and team environment.

3. **Matching the candidate to opportunities**

   It groups relevant roles, identifies stronger directions, prioritizes target opportunities, plans tailored résumé versions, prepares interview materials, and creates practical improvement roadmaps.

Company research should answer more than whether a company looks attractive from the outside.

The real questions are:

* Is the company worth applying to?
* Does the business appear sustainable?
* Is the position close to the company’s core business?
* Can the role produce transferable career value?
* Is the workload likely to be reasonable?
* Does the organization appear capable of supporting growth?

All company research is based on public information available on the internet or through tools accessible to the Agent.

The results are not an audit, guarantee, or substitute for direct verification. They are intended to organize signals, reduce information asymmetry, and help the user make better-informed decisions.

---

## Recommended Companion Tool

This Skill works well with the Chrome extension:

[Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor)

The extension allows users to collect interesting jobs while browsing recruiting platforms and export them as CSV or JSON.

This creates a useful division of labor:

* the user performs the first-pass interest filter;
* the browser extension builds a candidate pool;
* the local Agent performs deeper research and analysis.

### Recommended Workflow

1. Browse recruiting websites.
2. Add interesting roles to the candidate pool with `job-page-extractor`.
3. Export the collected jobs as CSV or JSON.
4. Provide the job file, résumé, background notes, preferences, and confidentiality boundaries to the local Agent.
5. Run `$analyze-career-opportunities`.
6. Review the company research, opportunity priorities, résumé strategy, interview materials, and improvement plan.

The browser extension is optional.

You may also create a job CSV manually by copying the header from:

```text
assets/job-input-template.csv
```

---

## Skill Name

```text
analyze-career-opportunities
```

### Example Prompt

```text
Use $analyze-career-opportunities to review my job CSV, résumé, and background notes.

First, identify my actual goals, experience, preferences, concerns, and confidentiality boundaries.

Then research the companies and career prospects represented in the job list. Pay particular attention to business outlook, financing, institutional assessments, role growth potential, workload, promotion opportunities, team environment, and public employee or community feedback.

Next, summarize the job market, identify the directions that fit me best, prioritize the strongest opportunities, determine the minimum number of tailored résumé versions I need, generate those versions, prepare interview materials, and create a 30/90/180-day improvement plan.

Do not describe planned projects as completed experience. Abstract confidential work safely and do not expose internal information.
```

---

## What It Produces

A complete analysis will typically include the following deliverables.

### 1. Candidate Requirements Profile

A structured summary of:

* preferred cities;
* target industries;
* salary expectations;
* acceptable workload;
* company preferences;
* role preferences;
* career goals;
* and non-negotiable constraints.

### 2. Experience Discovery

A grounded review of:

* what the candidate actually worked on;
* what responsibilities they personally owned;
* how far their decision-making authority extended;
* what outcomes can be supported with public evidence;
* what can be discussed in interviews;
* and what must remain abstract because of confidentiality.

### 3. Job Input Validation

Checks for:

* CSV or JSON field mapping;
* missing fields;
* duplicate jobs;
* incomplete descriptions;
* source links;
* collection dates;
* and candidate notes.

### 4. Company and Career-Prospect Research

Research into:

* business outlook;
* financing history;
* investor quality;
* institutional opinions;
* product and market maturity;
* commercial traction;
* customer cases;
* role positioning;
* career growth potential;
* workload;
* promotion opportunities;
* learning environment;
* and team culture.

### 5. Job-Market Summary

A structured view of:

* major job clusters;
* recurring requirements;
* role-specific requirements;
* hard qualification barriers;
* common technical expectations;
* and differences between similar positions.

### 6. Recommended Career Directions

One to three directions that deserve the candidate’s time and investment, together with the reasoning behind each recommendation.

### 7. Priority Opportunities

A shortlist that evaluates three dimensions separately:

* company outlook;
* work environment;
* candidate-role fit.

The Skill avoids hiding these dimensions behind a single opaque score.

### 8. Résumé Strategy

The Skill determines the smallest useful number of tailored résumé versions and generates a clear positioning strategy for each one.

Possible distinctions may include:

* technical versus product-oriented roles;
* research versus engineering roles;
* platform versus application roles;
* management-oriented versus individual-contributor roles;
* or industry-specific résumé variants.

### 9. Interview Materials

Preparation may include:

* HR interview questions;
* technical deep-dive questions;
* project narratives;
* experience-boundary explanations;
* confidentiality-safe answers;
* motivation statements;
* company-specific questions;
* and risk-response strategies.

### 10. 30/90/180-Day Improvement Plan

Each improvement item should include:

* a concrete task;
* a deliverable;
* an acceptance criterion;
* the condition under which it may be added to a résumé;
* and a fallback plan when the full target cannot be completed.

---

## How Company and Career Research Works

Company research should separate **business-development signals** from **employee-experience signals**.

These categories answer different questions and should not be merged carelessly.

| Signal Category       | What to Examine                                                                                   | Why It Matters                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Institutional views   | Brokerage reports, consulting firms, research institutions, industry associations, sector reports | Helps assess industry direction and company prospects                                 |
| Financing and capital | Funding rounds, investors, shareholder structure, IPO progress, merger or acquisition activity    | Provides indirect evidence of company stage, capital support, and external confidence |
| Commercial traction   | Customer cases, partners, government projects, contracts, tenders, deployments                    | Indicates whether the business has real adoption and commercialization                |
| Role position         | Core business, growth business, support function, outsourcing delivery, temporary exploration     | Determines whether the role is likely to build valuable experience                    |
| Work experience       | Overtime, delivery pressure, employee turnover, management style                                  | Helps assess whether the workload and pressure are acceptable                         |
| Growth environment    | Technology stack, mentorship, business complexity, promotion path                                 | Shows whether the role can support learning and advancement                           |
| Team environment      | Communication style, stability, management reputation, cross-team collaboration                   | Helps estimate long-term working conditions                                           |

Recommended research sources may include:

* official company websites;
* official announcements;
* investor disclosures;
* financing databases;
* shareholder information;
* industry reports;
* government procurement records;
* tender and contract records;
* product documentation;
* customer case studies;
* business news;
* recruiting platforms;
* employee-review websites;
* professional forums;
* social platforms;
* Maimai;
* Kanzhun;
* Glassdoor;
* Zhihu;
* Xiaohongshu;
* Reddit;
* and other public discussions.

Different sources are useful for different purposes.

Official websites are useful for confirming products, services, customers, and formal company claims.

Financing records, investor announcements, industry reports, and customer cases are stronger signals for business development.

Forums, employee reviews, and social platforms are more useful for identifying possible issues related to workload, management, promotion, communication, and team culture.

All internet information must be used carefully.

Funding does not guarantee future success. Institutional opinions may be outdated or influenced by commercial interests. Employee discussions may be incomplete, emotional, or unrepresentative.

The Skill should therefore:

* distinguish facts from interpretations;
* record source dates;
* compare multiple independent sources;
* avoid conclusions based on a single complaint;
* identify conflicting evidence;
* and clearly state uncertainty.

Its purpose is to collect and organize signals so that candidates can partially overcome the information disadvantage common in recruitment.

---

## Job CSV Format

The minimum recommended input contains three columns:

```csv
job_id,title,company_name
job-001,AI Product Manager,Example Technology
```

For more complete analysis, use the following header:

```csv
job_id,title,company_name,city,source_platform,source_url,collected_at,salary_min,salary_max,salary_period,experience_min,experience_max,education,responsibilities,required_skills,preferred_skills,description_raw,company_text_raw,notes
```

### Field Reference

* `job_id`: Unique job identifier. Required. Example: `job-001`.
* `title`: Job title. Required.
* `company_name`: Company name. Required.
* `city`: Job location.
* `source_platform`: Source platform, such as BOSS Zhipin, Lagou, Liepin, LinkedIn, or the company website.
* `source_url`: Original job-posting URL.
* `collected_at`: Date the role was collected. Recommended format: `YYYY-MM-DD`.
* `salary_min`: Minimum salary.
* `salary_max`: Maximum salary.
* `salary_period`: Salary period, such as `month`, `year`, or `day`.
* `experience_min`: Minimum required years of experience.
* `experience_max`: Maximum stated years of experience.
* `education`: Education requirement.
* `responsibilities`: Main responsibilities.
* `required_skills`: Required skills or qualifications.
* `preferred_skills`: Preferred qualifications or bonus skills.
* `description_raw`: Complete original job description.
* `company_text_raw`: Company introduction shown on the job page.
* `notes`: Personal notes, such as `high interest`, `salary unclear`, or `commute too long`.

Field names do not have to match exactly, but the English header above is recommended because it reduces ambiguity and mapping errors.

---

## Installation for Local Agents

This repository follows the Codex Skill format.

When installing it for Codex, the target directory name must be:

```text
analyze-career-opportunities
```

### Windows PowerShell

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git

New-Item -ItemType Directory -Force `
  "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" |
  Out-Null

Copy-Item -Recurse -Force `
  ".\career-opportunity-analyst-skill\*" `
  "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

### macOS and Linux

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git

mkdir -p ~/.codex/skills/analyze-career-opportunities

cp -R career-opportunity-analyst-skill/* \
  ~/.codex/skills/analyze-career-opportunities/
```

For WorkBuddy, Claude Code, or another local Agent environment, you may provide the repository URL and ask the Agent to install the Skill in its supported Skill or instruction directory.

Installation instructions intended for AI Agents are available in:

[AI_INSTALL.md](AI_INSTALL.md)

---

## Local Validation Scripts

### Inspect a Job Input File

```powershell
python scripts/profile_job_input.py path\to\jobs.csv
```

This script checks the structure and basic quality of a job CSV.

### Audit the Company Source Ledger

```powershell
python scripts/audit_company_sources.py company-sources.json
```

This script checks the company-research source ledger, including source structure and evidence requirements.

### Audit the Complete Delivery Manifest

```powershell
python scripts/audit_career_delivery.py delivery-manifest.json
```

This script checks whether the expected deliverables and supporting evidence have been recorded correctly.

These scripts validate structure and evidence constraints only. They do not replace human judgment.

---

## Privacy and Confidentiality

Candidate materials should remain local by default.

Do not upload confidential project details, internal company data, source code, logs, model weights, customer information, proprietary algorithms, unpublished metrics, or other sensitive materials to external AI services.

Confidential experience should be abstracted to the following level:

* problem category;
* personal responsibility boundary;
* operating constraints;
* technical or business trade-offs;
* validation method;
* and generalized outcome.

The Skill should never require:

* internal source code;
* raw internal datasets;
* private logs;
* model weights;
* customer identities;
* unpublished algorithms;
* confidential architecture details;
* or sensitive internal performance metrics.

Planned work must not be represented as completed experience.

Inferred achievements must not be presented as verified facts.

When evidence is incomplete, the Skill should state the limitation clearly rather than filling gaps with assumptions.

---

## Limitations

Career Opportunity Analyst is a decision-support tool, not a guarantee of employment or company quality.

Its conclusions may be limited by:

* incomplete job descriptions;
* outdated public information;
* inaccurate company claims;
* missing financing data;
* biased employee reviews;
* inaccessible recruiting-platform content;
* weak or contradictory sources;
* and changes that occur after the research date.

Users should verify important findings through:

* direct interviews;
* conversations with current or former employees;
* official company disclosures;
* employment contracts;
* written compensation details;
* and their own professional judgment.

---

## License

Licensed under the [Apache License 2.0](LICENSE).
