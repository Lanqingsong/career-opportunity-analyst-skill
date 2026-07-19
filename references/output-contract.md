# Output Contract

## Complete package

Use the headings in `assets/report-template.md`. Keep the report usable without requiring another agent to reconstruct context.

Include:

- input inventory, field-mapping confidence, omissions, and stale data;
- user-needs profile, preferences, concerns, hard filters, and deal-breakers;
- candidate fact and evidence ledger with source and disclosure state;
- company first-gate results and company due-diligence ledger;
- job clusters, shared requirements, differentiators, and sample size;
- one to three direction decisions with current and reachable fit;
- shortlisted roles with company and role judgments kept separate;
- typed gaps with 30/90/180-day horizons;
- minimum resume set and complete resume text when requested;
- interview question tree, safe evidence, and confidentiality boundaries;
- executable plan with deliverables and acceptance criteria;
- unresolved questions, sources, and audit results.

## Quick direction mode

Return input quality, user-needs summary, candidate evidence summary, company first-gate results, job clusters, direction decision, critical gaps, and at most three next questions. State which complete-package sections were intentionally deferred.

## Update modes

For resume updates, preserve facts and change only claims affected by new evidence or a changed target cluster. For plan updates, preserve completed-task history and modify only dependent gaps and tasks.

## Confidence language

Use `high` only when evidence and coverage support the conclusion. Use `medium`, `low`, or `incomplete` otherwise. A successful model or search call is not evidence by itself.

## Delivery files

Prefer:

- `career-analysis.md` for the complete readable package;
- `resume-<target>.docx` or `.md` for each resume family;
- `delivery-manifest.json` for deterministic audit;
- canonical contract JSON files when another agent will continue the work.
