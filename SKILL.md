---
name: analyze-career-opportunities
description: "Guide a local AI agent through career opportunity analysis from job CSV/JSON, manually prepared job tables, or candidate-role exports from the job-page-extractor Chrome extension plus resume material, candidate notes, projects, preferences, concerns, and corrections. Use for job selection, company and career-outlook research, user-needs and experience discovery, career-direction analysis, resume targeting or rewriting, interview preparation, capability-gap assessment, and 30/90/180-day career plans. Research institutional views, funding, investors, industry reports, customer cases, company prospects, role future, work pressure, promotion room, growth environment, team culture, and public forum or community signals before final role ranking."
---

# Analyze Career Opportunities

## Outcome

Deliver a usable career package, not only a ranking. This Skill is written for a local agent. Codex, WorkBuddy, Claude Code, or another local agent may use it if they can read the repository files and run the scripts. Accept a job file plus any combination of a resume, natural-language or voice-transcribed introduction, projects, publications, patents, portfolio links, preferences, concerns, and later corrections. A resume is optional.

Produce these outputs when the available material supports them:

1. user-needs profile and decision constraints;
2. candidate fact and evidence ledger;
3. company and career-outlook research ledger;
4. job-market clusters and requirement map;
5. one to three suitable career directions;
6. target companies and roles;
7. hard, reachable, evidence, expression, preference, and unknown gaps;
8. the minimum useful set of targeted resumes, normally one to three;
9. interview and confidentiality preparation;
10. a 30/90/180-day evidence-producing plan;
11. structured handoff artifacts when requested or when another agent will continue the work.

## Non-Negotiable Rules

- Never request work source code, internal datasets, credentials, private logs, model weights, client identities, unreleased algorithms, or confidential metrics.
- Preserve `confirmed`, `evidence_available`, `evidence_private`, `in_progress`, `planned`, `unknown`, and `disallowed` states. Never present planned work as completed or missing information as inability.
- Ask no more than three high-decision-value questions per round. Do not repeat answered questions. Continue partial analysis with unresolved items marked `unknown`.
- Trace every important recommendation and resume claim to candidate facts, job requirements, preferences, or public company sources.
- Show concise auditable reasoning summaries. Do not expose or claim to expose private chain-of-thought.
- Keep company outlook, career prospects, work environment, current fit, six-month reachable fit, evidence strength, and preference compatibility separate.
- Research company and career outlook before final role ranking. Do not reduce company research to legal identity or business verification; include institutional views, funding and investors, industry reports, customer cases, development prospects, role future, pressure, promotion, learning environment, team culture, and community feedback.
- Use the current local agent's available web or browser tools for public company research. Never ask the user for a search engine, endpoint, or search API key.
- Prefer Chinese output unless the user asks for another language.

## Workflow

### 1. Inventory and normalize inputs

Record every input source and disclosure boundary. Treat `job-page-extractor` as a Chrome extension that exports roles the user has personally added to a candidate pool. Also accept manually prepared CSV/JSON files; map headers and report uncertain mappings. Never silently discard salary, location, experience, education, description, company, source URL, or user-note fields.

Run `scripts/profile_job_input.py` for unfamiliar or large job files. Read `references/schemas.md` for field aliases and fact statuses.

### 2. Discover user needs and experience

Before ranking jobs, understand what the user is optimizing for and what they can truthfully claim. Extract target direction, disliked work, preferred company type, compensation, location, learning appetite, risk tolerance, timing, and deal-breakers. Mine the user's experience for responsibility boundaries, hard decisions, tools used, validation methods, measurable or safely generalized results, public evidence, private evidence, and missing evidence.

Ask at most three high-value questions when a missing answer would change company ranking, direction choice, resume claims, or confidentiality handling. Continue with unknowns marked when the user does not answer.

Read `references/candidate-interview.md` for follow-up selection and `references/privacy.md` for confidential work.

### 3. Build the evidence ledger

Convert candidate material into fact, responsibility, technical action, result, evidence, and disclosure boundary. Keep independent contribution separate from listed authorship or team attribution. Treat the latest explicit correction as current while retaining the contradiction as an audit note.

### 4. Research company and career outlook

Research every company that appears in the user's candidate pool before final ranking. Basic identity and hiring-entity checks are only the baseline. Internet research has limited truthfulness, so build a signal set rather than pretending to audit reality. Judge institutional recognition, capital backing, customer or commercialization evidence, development prospects, role future, career pressure, promotion room, growth environment, team culture, and role-business alignment.

Use official and independent sources for business facts. Use institutional reports, investor announcements, funding records, customer cases, government projects, and public tenders as strong signals for company prospects. Use forums, employee reviews, social posts, recruiting-platform comments, and other public community signals for pressure, promotion, management, growth, and team-culture patterns. Treat all sources as signals; funding and institutional views are strong supporting evidence, not proof of future success. Mark weak coverage as incomplete or watch rather than negative. Read `references/company-research.md` and run `scripts/audit_company_sources.py` before a high-confidence company claim.

### 5. Build market and direction clusters

Group jobs by responsibility and capability combination after company and career-outlook research, not by title alone. Extract shared requirements, differentiators, hard filters, compensation and location constraints, and evidence expectations. Base direction recommendations on clusters, not one unusual job.

Read `references/scoring.md` for score separation, gap classes, and direction gates.

### 6. Decide directions, opportunities, and gaps

For every direction, state current evidence, distinctive advantage, hard limitations, 90-day reachability, 180-day reachability, and why it fits the user's preferences. For every shortlisted role, separate company thesis from role fit. Classify each gap and attach a target horizon.

### 7. Produce the resume set

Determine the smallest number of resumes that covers the viable job clusters. Define each resume's target cluster, central narrative, project order, evidence emphasis, exclusions, and keyword boundary before drafting it. Use only public or `abstract_only` facts whose status permits resume use.

Read `references/resume-delivery.md`. When `.docx` is requested, use the available document-generation capability and render the document for visual verification before delivery.

### 8. Produce interview preparation

Generate likely HR challenges, technical-depth questions, evidence requests, and safe confidentiality answers. Distinguish what the candidate can disclose, describe abstractly, demonstrate through an open reproduction, or must decline to disclose.

Read `references/interview-delivery.md`.

### 9. Produce the growth plan

Create 30-, 90-, and 180-day tasks only after direction and gap decisions. Attach every task to a gap and require a public deliverable, acceptance criteria, resume-use gate, dependencies, and fallback. Do not return a generic course list.

Read `references/growth-plan.md`.

### 10. Audit and deliver

Use `assets/report-template.md` for the human-readable package. Read `references/output-contract.md` for required sections and modes. When structured artifacts are requested, follow `references/handoff-contract.md` and validate repository contracts when available.

Create a delivery manifest following `references/delivery-manifest.md`, then run:

```powershell
python scripts/audit_career_delivery.py delivery-manifest.json
```

Fix errors rather than weakening the facts, sources, or audit rules. Clearly label any section that remains incomplete.

## Delivery Modes

- **Quick direction**: user-needs profile, candidate ledger, company and career-outlook summary, job clusters, direction decision, critical gaps, and next questions.
- **Complete package**: all nine outputs, including targeted resumes and 30/90/180-day plan.
- **Resume update**: preserve the existing ledger and direction decision; revise only affected resumes and interview evidence.
- **Plan update**: ingest new evidence or execution results; revise affected gaps and tasks without rewriting completed history.

Default to the complete package when the user asks for a full analysis, final materials, resumes, or guidance and supplies a job file.

## Reference Routing

- Input fields and fact states: `references/schemas.md`
- Candidate discovery: `references/candidate-interview.md`
- Privacy and confidential work: `references/privacy.md`
- Direction, scores, and gaps: `references/scoring.md`
- Company and career-outlook research: `references/company-research.md`
- Resume strategy and claims: `references/resume-delivery.md`
- Interview and disclosure preparation: `references/interview-delivery.md`
- 30/90/180-day planning: `references/growth-plan.md`
- Human-readable output: `references/output-contract.md`
- Delivery manifest audit: `references/delivery-manifest.md`
- Structured handoff: `references/handoff-contract.md`
