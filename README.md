# Career Opportunity Analyst Skill

面向 Codex 的职业机会分析 Skill。它把岗位 CSV/JSON、简历、补充介绍、项目材料、偏好约束和修正信息，整理成一套证据驱动的职业交付包。

English: A Codex Skill for evidence-grounded career opportunity analysis. It turns job exports plus candidate material into market clusters, target directions, shortlisted roles, tailored resume versions, interview preparation, and a practical 30/90/180-day growth plan.

## Recommended Upstream Tool / 推荐前置工具

建议先使用岗位采集工具 [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) 批量读取招聘页面，并导出岗位 CSV/JSON。

推荐工作流：

1. 用 `job-page-extractor` 抓取或整理招聘页面。
2. 导出岗位文件，例如 `jobs.csv` 或 `jobs.json`。
3. 把岗位文件、简历、补充介绍、偏好条件和保密边界一起交给 `$analyze-career-opportunities`。
4. 由本 Skill 完成职业方向判断、岗位筛选、简历版本规划、面试材料和成长计划。

English workflow:

1. Use `job-page-extractor` to collect job pages and export CSV/JSON.
2. Provide the job export together with resume material, candidate notes, preferences, and confidentiality boundaries.
3. Invoke `$analyze-career-opportunities` in Codex to generate the complete career delivery package.

This Skill can also read ordinary CSV/JSON job tables that were not produced by `job-page-extractor`, as long as the fields contain enough role, company, location, requirement, and responsibility information.

## Skill Name / 调用名称

```text
analyze-career-opportunities
```

在 Codex 里这样调用：

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍，请完成完整职业交付：评估当前能力，归纳岗位市场和适合方向，筛选目标机会，判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

English example:

```text
Use $analyze-career-opportunities. Read my job CSV, resume, preferences, and project notes.
Produce a complete career package: candidate evidence ledger, market clusters, suitable directions,
shortlisted roles, minimum targeted resume set, interview preparation, confidentiality-safe answers,
and a 30/90/180-day growth plan. Do not present planned work as completed experience.
```

## What Problem It Solves / 解决的问题

很多求职分析会把所有问题压成一个模糊匹配分数，但真正影响决策的是一组不同的问题：

- 这家公司是否值得投入时间？
- 这个岗位是否匹配候选人当前能力？
- 候选人是否能在三到六个月内补齐关键差距？
- 是真的缺能力，还是缺可以公开展示的证据？
- 计划中的项目是否被误写成已完成经历？
- 工作中涉及保密的内容，能否安全抽象成面试可讲的表达？

This Skill separates these judgments instead of hiding them behind a single score. It keeps company quality, current fit, reachable future fit, evidence strength, preference compatibility, and hard filters visible as different dimensions.

它还会保留事实状态，例如：

```text
confirmed
evidence_available
evidence_private
in_progress
planned
unknown
disallowed
```

这样可以避免 AI 把“未知信息”写成缺点，也避免把“未来计划”写成已经完成的项目经历。

## What It Produces / 交付内容

当输入材料足够时，本 Skill 会生成：

1. 输入清单和岗位字段映射。
2. 候选人事实与证据台账。
3. 岗位市场画像、岗位簇和能力要求地图。
4. 1-3 个适合的职业方向。
5. 目标公司和目标岗位筛选结果，并区分公司质量与岗位匹配度。
6. 差距分析，包括 hard / reachable / evidence / expression / preference / unknown gaps。
7. 最小必要简历版本数量，通常是 1-3 份，而不是每个岗位一份。
8. HR、技术面、项目深挖和保密场景回答材料。
9. 30/90/180 天提升计划，每项任务包含可交付物、验收标准、简历使用门槛和降级方案。
10. 可由脚本审计的 `delivery-manifest.json`。

English output summary:

- Candidate evidence ledger.
- Job-market clusters and role requirement map.
- Suitable target directions.
- Shortlisted opportunities.
- Minimum useful tailored resume set.
- Interview preparation and confidentiality-safe answer frames.
- 30/90/180-day growth plan.
- Audit-ready delivery manifest.

## Key Features / 项目特点

- 支持 `job-page-extractor` 导出的岗位 CSV/JSON，也支持普通岗位表格。
- 不只依赖简历；补充介绍、项目材料、作品链接、偏好条件和修正信息都可以作为输入。
- 按职责和能力模式聚类岗位，而不是只按岗位标题归类。
- 只对进入候选范围的公司做公开资料核查，减少无效研究。
- 公司判断必须有来源支撑；资料不足时标记为 incomplete 或 low confidence，而不是编造结论。
- 区分“可公开写进简历的证据”和“只能面试安全抽象表达的私有证据”。
- 防止 planned / in_progress 项目被写成 completed 经历。
- 生成最小必要简历版本，避免为了每个岗位机械复制一份简历。
- 把能力差距转成具体提升任务，每项任务包含交付物、验收标准、依赖关系和 fallback scope。
- 附带本地审计脚本，用于检查岗位输入、公司来源覆盖和交付清单一致性。

## Repository Layout / 仓库结构

```text
.
|-- SKILL.md
|-- README.md
|-- AI_INSTALL.md
|-- LICENSE
|-- agents/
|-- assets/
|-- references/
`-- scripts/
```

## Install For Codex / 安装到 Codex

This repository is designed to be installed by an AI agent or manually by a user. If another AI agent is doing the installation, give it [AI_INSTALL.md](AI_INSTALL.md); that file contains agent-oriented install and verification steps.

这个仓库本身就是一个 Skill。安装目标目录名必须是：

```text
analyze-career-opportunities
```

### Windows PowerShell

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" | Out-Null
Copy-Item -Recurse -Force ".\career-opportunity-analyst-skill\*" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

Then start a new Codex task so the Skill metadata is loaded.

### macOS / Linux

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
mkdir -p ~/.codex/skills/analyze-career-opportunities
cp -R career-opportunity-analyst-skill/* ~/.codex/skills/analyze-career-opportunities/
```

Then start a new Codex task.

## Detailed Usage / 详细使用方法

### 1. Prepare job data / 准备岗位数据

推荐使用：

[Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor)

把招聘页面整理成 CSV/JSON。常见字段可以包括：

- company / 公司
- title / 岗位名称
- location / 地点
- salary / 薪资
- responsibilities / 职责
- requirements / 要求
- source_url / 来源链接
- published_at / 发布时间
- notes / 备注

字段名不必完全一致。本 Skill 会先做字段映射和输入质量检查。

### 2. Prepare candidate material / 准备候选人材料

可以提供：

- 简历。
- 补充自我介绍。
- 项目经历说明。
- 作品集、论文、专利、GitHub、博客或公开主页链接。
- 城市、行业、薪资、工作强度、公司类型等偏好。
- 对历史信息的修正。
- 哪些内容能公开写、哪些内容只能抽象讲、哪些内容不能提。

请不要提供：

- 工作源代码。
- 内部数据集。
- 账号、密钥、cookie、token。
- 生产日志。
- 模型权重。
- 客户身份。
- 未公开算法。
- 内部经营指标或敏感指标。

### 3. Ask Codex to run the Skill / 让 Codex 使用 Skill

推荐中文提示词：

```text
使用 $analyze-career-opportunities，读取我提供的岗位 CSV/JSON、简历或补充介绍、项目材料、公开主页和职业偏好。
请完成完整职业交付：
1. 盘点输入和字段映射；
2. 建立候选人事实与证据台账；
3. 归纳岗位市场画像和岗位簇；
4. 推荐 1-3 个适合方向；
5. 筛选目标公司和岗位；
6. 区分 hard / reachable / evidence / expression / preference / unknown gaps；
7. 判断最少需要多少份定向简历并生成对应版本；
8. 准备 HR、技术和保密回答；
9. 制定 30/90/180 天提升计划；
10. 创建 delivery-manifest.json 并运行审计脚本。
不要把 planned 或 in_progress 写成 completed。涉及工作保密内容只做安全抽象，不要要求源码、内部数据、日志、模型权重、客户身份或未公开指标。
```

Recommended English prompt:

```text
Use $analyze-career-opportunities. Read the provided job CSV/JSON, resume or candidate notes,
project material, public profile links, and career preferences.

Produce the complete career package:
1. Input inventory and field mapping.
2. Candidate fact and evidence ledger.
3. Job-market clusters and requirement map.
4. One to three suitable directions.
5. Shortlisted target companies and roles.
6. Gap analysis across hard, reachable, evidence, expression, preference, and unknown gaps.
7. Minimum useful tailored resume set and the corresponding resume versions.
8. HR, technical, and confidentiality-safe interview preparation.
9. 30/90/180-day improvement plan.
10. delivery-manifest.json plus audit-script verification.

Do not turn planned or in-progress work into completed experience. Keep confidential work safely abstract.
Do not request source code, internal datasets, logs, model weights, client identities, or unreleased metrics.
```

## Audit Scripts / 审计脚本

Profile an unfamiliar job file:

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

The audit scripts do not prove that every career recommendation is correct. They check whether the delivery follows the evidence contract: reference consistency, unsafe resume claims, missing task gates, and company-source coverage.

## Privacy Model / 隐私边界

The Skill is local-first. Candidate material should stay local unless the user explicitly asks Codex to research public company information or authorizes a specific external operation.

对于保密工作，本 Skill 只应该要求安全抽象信息：

- 问题类型。
- 个人职责边界。
- 约束条件。
- 技术取舍。
- 验证方法。
- 泛化后的结果。

它不应该要求源代码、内部数据、日志、模型权重、客户名称、未公开算法或内部敏感指标。

## License

Apache-2.0.
