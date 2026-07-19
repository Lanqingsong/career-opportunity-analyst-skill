# Scoring Reference

Keep scores separate.

## Required Score Dimensions

- company development outlook
- institutional and capital signal
- commercial adoption signal
- role career value
- work pressure and culture risk
- promotion and growth environment
- current role fit
- future reachable fit
- evidence coverage
- preference compatibility

Hard filters and risk flags must remain visible and must not be hidden by a high aggregate score.

Company and career-outlook research comes before role-fit ranking. A strong role match does not compensate for poor career value, unmanageable pressure, weak growth environment, a user deal-breaker, or a material unresolved risk.

## Gap Types

- `hard_filter`: structural condition unlikely to change soon.
- `learnable`: skill or evidence can be improved in 1-3 or 3-6 months.
- `evidence_gap`: ability may exist but public or safe evidence is weak.
- `expression_gap`: experience exists but is not explained convincingly.
- `preference_conflict`: role fits ability but violates preferences.
- `unknown`: needs clarification.

## Ranking Rule

Use preferences to weight scores, but preserve component scores. When weights change, explain why ranking changes.

## Direction Gate

Recommend a direction only when sampled roles form a meaningful cluster and the candidate has either current evidence or a realistic six-month evidence path. For each direction record:

- sample role count and representative role IDs;
- shared and differentiating requirements;
- current evidence and evidence quality;
- hard filters and preference conflicts;
- 90-day and 180-day reachability;
- uncertainty that could change the decision.

Do not recommend a direction only because it has many vacancies or shares generic terms such as Python or AI.
