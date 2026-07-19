# AI Installation Guide

This file is written for an AI agent that has shell access and has been asked to install this Skill for Codex.

The goal is to install the Skill under the user's Codex skill directory without copying private career files, resumes, job CSVs, local analysis reports, or unrelated project history.

## Skill Identity

- Repository: `https://github.com/Lanqingsong/career-opportunity-analyst-skill.git`
- Install directory name: `analyze-career-opportunities`
- Invocation name: `$analyze-career-opportunities`
- Required file at install root: `SKILL.md`

## Safety Rules For The Installing AI

1. Clone only this repository.
2. Do not scan the user's unrelated folders for resumes, job files, source code, or private documents.
3. Do not upload candidate material anywhere.
4. Do not ask the user for work source code, internal datasets, credentials, logs, model weights, client names, or unreleased algorithms.
5. After installation, start a new Codex task or tell the user to start one, because Skill discovery happens when task context is built.
6. If the target directory already exists, inspect it before overwriting. Do not delete unrelated user-created files without explicit permission.

## Windows PowerShell Procedure

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
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\profile_job_input.py" --help
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\audit_career_delivery.py" --help
python "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\scripts\audit_company_sources.py" --help
```

## macOS / Linux Procedure

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
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/profile_job_input.py" --help
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/audit_career_delivery.py" --help
python "$HOME/.codex/skills/analyze-career-opportunities/scripts/audit_company_sources.py" --help
```

## Smoke Test Prompt

After installation, open a new Codex task and ask:

```text
使用 $analyze-career-opportunities，说明这个 Skill 需要哪些输入、会交付哪些文件、
以及它如何避免把 planned 工作写成 completed 经历。不要读取我的本地私人文件。
```

The expected answer should mention job CSV/JSON, candidate material, preferences, confidentiality boundaries, evidence ledger, job clusters, directions, shortlisted roles, minimum resume set, interview preparation, 30/90/180-day plan, delivery manifest audit, and the rule that planned work remains planned.

## Full Task Prompt Template

```text
使用 $analyze-career-opportunities，读取我提供的岗位 CSV/JSON、简历或补充介绍、
项目材料、公开主页和职业偏好。

请完成完整职业交付：
1. 盘点输入和字段映射；
2. 建立候选人事实与证据账本；
3. 归纳岗位市场画像和岗位簇；
4. 推荐 1-3 个适合方向；
5. 筛选目标公司和岗位；
6. 区分 hard / learnable / evidence / expression / preference / unknown gaps；
7. 判断最少需要多少份定向简历并生成对应版本；
8. 准备 HR、技术和保密回答；
9. 制定 30/90/180 天提升计划；
10. 创建 delivery-manifest.json 并运行审计脚本。

不要把 planned 或 in_progress 写成 completed。
涉及工作保密内容只做安全抽象，不要要求源码、内部数据、日志、模型权重、
客户身份或未公开指标。
```

## Troubleshooting

If Codex does not see the Skill, check that this path exists:

```text
~/.codex/skills/analyze-career-opportunities/SKILL.md
```

Then start a new Codex task.

If company research is weak, do not invent company quality claims. Mark the research status as incomplete or low confidence. A high-confidence company conclusion needs at least two reachable sources from different domains, including official or regulatory material and independent coverage.

If resume claims fail audit, fix the claim or the fact state. Completed resume claims may use only facts whose state and disclosure level allow resume use.
