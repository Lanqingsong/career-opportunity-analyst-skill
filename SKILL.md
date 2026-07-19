---
name: analyze-career-opportunities
description: "Turn job CSV/JSON or job-page-extractor exports plus a resume, free-form introduction, project materials, portfolio links, preferences, or corrections into an evidence-grounded career delivery package: candidate profile, market and role clusters, suitable directions, shortlisted opportunities, minimum tailored resume set, interview evidence preparation, and executable 30/90/180-day improvement plan. Use for job selection, career-direction analysis, resume targeting or rewriting, interview preparation, capability-gap assessment, and career learning plans. Research shortlisted companies with Codex's built-in web tools without asking the user to configure a search API."
---

# Analyze Career Opportunities

## Outcome

Deliver a usable career package, not only a ranking. Accept a job file plus any combination of a resume, natural-language or voice-transcribed introduction, projects, publications, patents, portfolio links, preferences, concerns, and later corrections. A resume is optional.

Produce these outputs when the available material supports them:

1. candidate fact and evidence ledger;
2. job-market clusters and requirement map;
3. one to three suitable career directions;
4. target companies and roles;
5. hard, reachable, evidence, expression, preference, and unknown gaps;
6. the minimum useful set of targeted resumes, normally one to three;
7. interview and confidentiality preparation;
8. a 30/90/180-day evidence-producing plan;
9. structured handoff artifacts when requested or when another agent will continue the work.

## Non-Negotiable Rules

- Never request work source code, internal datasets, credentials, private logs, model weights, client identities, unreleased algorithms, or confidential metrics.
- Preserve `confirmed`, `evidence_available`, `evidence_private`, `in_progress`, `planned`, `unknown`, and `disallowed` states. Never present planned work as completed or missing information as inability.
- Ask no more than three high-decision-value questions per round. Do not repeat answered questions. Continue partial analysis with unresolved items marked `unknown`.
- Trace every important recommendation and resume claim to candidate facts, job requirements, preferences, or public company sources.
- Show concise auditable reasoning summaries. Do not expose or claim to expose private chain-of-thought.
- Keep company quality, current fit, six-month reachable fit, evidence strength, and preference compatibility separate.
- Use Codex web tools directly for public company research. Never ask the user for a search engine, endpoint, or search API key.
- Prefer Chinese output unless the user asks for another language.

## Workflow

### 1. Inventory and normalize inputs

Record every input source and disclosure boundary. Prefer `job-page-extractor` exports. For generic CSV/JSON, map headers and report uncertain mappings; never silently discard salary, location, experience, education, description, company, or source URL fields.

Run `scripts/profile_job_input.py` for unfamiliar or large job files. Read `references/schemas.md` for field aliases and fact statuses.

### 2. Build the evidence ledger

Convert candidate material into fact, responsibility, technical action, result, evidence, and disclosure boundary. Keep independent contribution separate from listed authorship or team attribution. Treat the latest explicit correction as current while retaining the contradiction as an audit note.

Read `references/candidate-interview.md` for follow-up selection and `references/privacy.md` for confidential work.

### 3. Build market and direction clusters

Group jobs by responsibility and capability combination rather than title alone. Extract shared requirements, differentiators, hard filters, compensation and location constraints, and evidence expectations. Base direction recommendations on clusters, not one unusual job.

Read `references/scoring.md` for score separation, gap classes, and direction gates.

### 4. Research only the shortlist

Shortlist locally before browsing. Resolve company identity, then research only companies that could remain viable. Use official or regulatory sources plus independent coverage for high-confidence conclusions. Mark weak coverage as incomplete rather than negative.

Read `references/company-research.md` and run `scripts/audit_company_sources.py` before a high-confidence company claim.

### 5. Decide directions, opportunities, and gaps

For every direction, state current evidence, distinctive advantage, hard limitations, 90-day reachability, 180-day reachability, and why it fits the user's preferences. For every shortlisted role, separate company thesis from role fit. Classify each gap and attach a target horizon.

### 6. Produce the resume set

Determine the smallest number of resumes that covers the viable job clusters. Define each resume's target cluster, central narrative, project order, evidence emphasis, exclusions, and keyword boundary before drafting it. Use only public or `abstract_only` facts whose status permits resume use.

Read `references/resume-delivery.md`. When `.docx` is requested, use the available document-generation capability and render the document for visual verification before delivery.

### 7. Produce interview preparation

Generate likely HR challenges, technical-depth questions, evidence requests, and safe confidentiality answers. Distinguish what the candidate can disclose, describe abstractly, demonstrate through an open reproduction, or must decline to disclose.

Read `references/interview-delivery.md`.

### 8. Produce the growth plan

Create 30-, 90-, and 180-day tasks only after direction and gap decisions. Attach every task to a gap and require a public deliverable, acceptance criteria, resume-use gate, dependencies, and fallback. Do not return a generic course list.

Read `references/growth-plan.md`.

### 9. Audit and deliver

Use `assets/report-template.md` for the human-readable package. Read `references/output-contract.md` for required sections and modes. When structured artifacts are requested, follow `references/handoff-contract.md` and validate repository contracts when available.

Create a delivery manifest following `references/delivery-manifest.md`, then run:

```powershell
python scripts/audit_career_delivery.py delivery-manifest.json
```

Fix errors rather than weakening the facts, sources, or audit rules. Clearly label any section that remains incomplete.

## Delivery Modes

- **Quick direction**: candidate ledger, job clusters, direction decision, critical gaps, and next questions.
- **Complete package**: all nine outputs, including targeted resumes and 30/90/180-day plan.
- **Resume update**: preserve the existing ledger and direction decision; revise only affected resumes and interview evidence.
- **Plan update**: ingest new evidence or execution results; revise affected gaps and tasks without rewriting completed history.

Default to the complete package when the user asks for a full analysis, final materials, resumes, or guidance and supplies a job file.

## Reference Routing

- Input fields and fact states: `references/schemas.md`
- Candidate discovery: `references/candidate-interview.md`
- Privacy and confidential work: `references/privacy.md`
- Direction, scores, and gaps: `references/scoring.md`
- Company sources: `references/company-research.md`
- Resume strategy and claims: `references/resume-delivery.md`
- Interview and disclosure preparation: `references/interview-delivery.md`
- 30/90/180-day planning: `references/growth-plan.md`
- Human-readable output: `references/output-contract.md`
- Delivery manifest audit: `references/delivery-manifest.md`
- Structured handoff: `references/handoff-contract.md`
