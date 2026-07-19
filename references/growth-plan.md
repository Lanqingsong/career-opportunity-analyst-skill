# Growth Plan

## Plan from gaps, not topics

Create a task only when it references a viable target direction and one or more identified gaps. Reject generic entries such as “learn LangChain” or “study deployment.”

## Required task fields

Each task must include:

- `task_id` and title;
- target direction and linked gap IDs;
- rationale from sampled job requirements;
- prerequisite tasks;
- horizon: 30, 90, or 180 days;
- estimated effort;
- concrete public or safely shareable deliverable;
- acceptance criteria;
- evidence level after completion;
- resume-use gate;
- fallback or reduced-scope version.

## Horizon roles

- 30 days: close expression gaps, inventory evidence, reproduce one narrow capability, and establish baselines.
- 90 days: deliver one end-to-end project or substantial extension with evaluation, tests, deployment, documentation, and failure analysis.
- 180 days: deepen the chosen direction through a second hard project, real users or contributions, a research artifact, or constrained-device/production validation.

Avoid planning three large projects in parallel. Prefer one flagship artifact plus smaller evidence tasks.

## Project quality gate

A flagship project should demonstrate:

- a real user or operational problem;
- explicit scope and architecture;
- non-trivial technical decisions;
- reproducible setup;
- evaluation dataset or scenario and baseline;
- failure cases and limitations;
- tests and observability;
- deployable interface or demo;
- documentation suitable for an interviewer;
- a clear distinction between completed and future work.

## Resume-use gate

A task becomes resume-ready only after its acceptance criteria pass and supporting artifacts exist. Repository creation, a design document, model download, or unfinished experiment is not completion.

## Replanning

Preserve completed history. When a target direction changes, mark orphaned tasks explicitly and explain whether their deliverables remain useful. When a task fails, use its fallback before adding a new large project.
