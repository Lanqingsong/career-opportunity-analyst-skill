# Career Intelligence Handoff

Use the canonical repository schemas when another agent or the future Career Growth Agent will continue the work.

## Canonical contracts

The repository root `schemas/` directory is the source of truth:

- `candidate-brief.schema.json`
- `target-role-package.schema.json`
- `evidence-record.schema.json`
- `gap-record.schema.json`
- `career-plan.schema.json`

Preserve every identifier across artifacts. Do not invent candidate facts to satisfy a required field. Preserve disclosure policy and exclude `local_only`, private, and disallowed material from web research or public resumes.

## Recommended export order

1. Candidate Brief: stable candidate facts, preferences, constraints, disclosure policy, and uncertainties.
2. Target Role Package: viable directions, roles, companies, requirements, initial gaps, sources, and decision uncertainty.
3. Evidence Records: inspectable or safely summarized proof linked to candidate facts and requirements.
4. Gap Records: hard filters, learnable gaps, evidence gaps, expression gaps, preference conflicts, and unknowns.
5. Career Plan: 30/90/180-day tasks linked to gaps, dependencies, deliverables, acceptance criteria, and review points.

A successful model or web call is not evidence that a company is verified or a candidate fact is confirmed.

## Validation

When the repository is available, validate every artifact:

```powershell
python -m career_decision_agent.cli contract --input candidate-brief.json --type candidate_brief
python -m career_decision_agent.cli contract --input target-role-package.json --type target_role_package
python -m career_decision_agent.cli contract --input evidence-record.json --type evidence_record
python -m career_decision_agent.cli contract --input gap-record.json --type gap_record
python -m career_decision_agent.cli contract --input career-plan.json --type career_plan
```

Fix invalid references or data rather than weakening schemas. The standalone `delivery-manifest.json` supports Skill-level claim auditing but does not replace canonical contracts.
