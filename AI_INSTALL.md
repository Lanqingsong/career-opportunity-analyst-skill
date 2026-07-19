# AI Installation Guide

This file is written for a local AI agent that has shell access and has been asked to install or load this Skill.

The repository uses the Codex Skill folder format, but the workflow can also be loaded by WorkBuddy, Claude Code, or another local agent that can read `SKILL.md`, `references/`, `assets/`, and `scripts/`.

The goal is to install or load the Skill without copying private career files, resumes, job CSVs, local analysis reports, or unrelated project history.

## Skill Identity

- Repository: `https://github.com/Lanqingsong/career-opportunity-analyst-skill.git`
- Skill directory name for Codex: `analyze-career-opportunities`
- Invocation name: `$analyze-career-opportunities`
- Required file at install root: `SKILL.md`
- Optional job CSV template: `assets/job-input-template.csv`

## Safety Rules For The Installing AI

1. Clone only this repository.
2. Do not scan unrelated folders for resumes, job files, source code, or private documents.
3. Do not upload candidate material anywhere.
4. Do not ask the user for work source code, internal datasets, credentials, logs, model weights, client names, or unreleased algorithms.
5. If installing for Codex, start a new Codex task after installation because Skill discovery happens when task context is built.
6. If loading for WorkBuddy, Claude Code, or another local agent, register or attach the repository as a local knowledge/tool folder and instruct the agent to read `SKILL.md` first.
7. If the target directory already exists, inspect it before overwriting. Do not delete unrelated user-created files without explicit permission.

## Codex Installation: Windows PowerShell

```powershell
$repo = "https://github.com/Lanqingsong/career-opportunity-analyst-skill.git"
$work = Join-Path $env:TEMP "career-opportunity-analyst-skill"
$target = Join-Path $env:USERPROFILE ".codex\skills\analyze-career-opportunities"

if (Test-Path -LiteralPath $work) {
  Remove-Item -Recurse -Force -LiteralPath $work
}

git clone $repo $work

if (-not (Test-Path -LiteralPath (Join-Path $work "SKILL.md"))) {
  throw "SKILL.md not found at repository root"
}

New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Recurse -Force -LiteralPath (Join-Path $work "*") -Destination $target

Get-ChildItem -Force -LiteralPath $target
```

Verify:

```powershell
Get-Content -LiteralPath "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\SKILL.md" -TotalCount 20
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\profile_job_input.py" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\assets\job-input-template.csv"
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\audit_career_delivery.py" --help
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\audit_company_sources.py" --help
```

## Codex Installation: macOS / Linux

```bash
repo="https://github.com/Lanqingsong/career-opportunity-analyst-skill.git"
work="${TMPDIR:-/tmp}/career-opportunity-analyst-skill"
target="$HOME/.codex/skills/analyze-career-opportunities"

rm -rf "$work"
git clone "$repo" "$work"

test -f "$work/SKILL.md" || {
  echo "SKILL.md not found at repository root" >&2
  exit 1
}

mkdir -p "$target"
cp -R "$work"/. "$target"/
ls -la "$target"
```

Verify:

```bash
sed -n '1,20p' "$HOME/.codex/skills/analyze-career-opportunities/SKILL.md"
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/profile_job_input.py" "$HOME/.codex/skills/analyze-career-opportunities/assets/job-input-template.csv"
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/audit_career_delivery.py" --help
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/audit_company_sources.py" --help
```

## Loading For Other Local Agents

For WorkBuddy, Claude Code, or another local agent:

1. Clone this repository to a local folder.
2. Register or attach the repository as a local knowledge/tool folder.
3. Instruct the agent to read `SKILL.md` before acting.
4. Let the agent load reference files only as needed:
   - `references/candidate-interview.md` for user-needs and experience discovery.
   - `references/company-research.md` for company outlook, role future, pressure, promotion, growth environment, team culture, and community-signal research.
   - `references/schemas.md` for CSV/JSON job input mapping.
   - `references/privacy.md` for confidential work.
5. Let the agent run scripts locally when useful.

## Smoke Test Prompt

After installation or loading, ask the local agent:

```text
使用 $analyze-career-opportunities，说明这个 Skill 需要哪些输入、会交付哪些内容、它如何调研公司发展前途、职业前景、职业压力、晋升空间、成长环境、团队氛围和论坛/社区反馈，如何挖掘用户需求和经历，以及如何避免把 planned 工作写成 completed 经历。不要读取我的本地私人文件。
```

The expected answer should mention job CSV/JSON, candidate material, preferences, confidentiality boundaries, user-needs discovery, experience mining, company and career-outlook research, community-signal handling, evidence ledger, job clusters, directions, shortlisted roles, minimum resume set, interview preparation, 30/90/180-day plan, delivery manifest audit, and the rule that planned work remains planned.

## Full Task Prompt Template

```text
使用 $analyze-career-opportunities，读取我提供的岗位 CSV/JSON、简历或补充介绍、项目材料、公开主页和职业偏好。
请完成完整职业分析：
1. 盘点输入和字段映射；
2. 挖掘我的真实需求、偏好、顾虑、硬性条件和经历边界；
3. 建立候选人事实与证据台账；
4. 调研岗位里的公司与职业前景，重点看发展前途、岗位成长性、职业压力、晋升空间、团队氛围和论坛/社区反馈；
5. 归纳岗位市场画像和岗位簇；
6. 推荐 1-3 个适合方向；
7. 筛选目标公司和岗位，并分开写公司判断与岗位匹配；
8. 区分 hard / learnable / evidence / expression / preference / unknown gaps；
9. 判断最少需要多少份定向简历并生成对应版本；
10. 准备 HR、技术和保密回答；
11. 制定 30/90/180 天提升计划；
12. 创建 delivery-manifest.json 并运行审计脚本。
不要把 planned 或 in_progress 写成 completed。涉及工作保密内容只做安全抽象，不要要求源码、内部数据、日志、模型权重、客户身份或未公开指标。
```

## Troubleshooting

If Codex does not see the Skill, check that this path exists:

```text
~/.codex/skills/analyze-career-opportunities/SKILL.md
```

Then start a new Codex task.

If another local agent does not follow the workflow, explicitly ask it to read `SKILL.md` first and to use `references/company-research.md` before ranking roles.

If company or career-outlook research is weak, do not invent claims. Mark the research status as incomplete, watch, or low confidence. Official sources are useful for business facts; forums, employee reviews, and community discussions are useful for pressure, promotion, growth environment, and culture signals, but require pattern-based wording rather than single-post certainty.

If resume claims fail audit, fix the claim or the fact state. Completed resume claims may use only facts whose state and disclosure level allow resume use.
