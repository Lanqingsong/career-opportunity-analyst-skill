# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

面向 Codex 的职业机会分析 Skill。它把岗位 CSV/JSON、简历、补充介绍、项目材料、偏好约束和修正信息，整理成一套证据驱动的职业交付包。

## 推荐前置工具

推荐配合 Chrome 浏览器插件 [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) 使用。

它不是要求用户一次性批量抓取全网岗位，而是用于用户浏览招聘网站时，把自己感兴趣的岗位纳入候选池，并导出候选岗位 CSV/JSON。这样可以先由人完成“我对哪些岗位有兴趣”的选择，再由本 Skill 完成职业判断、简历版本规划和面试准备。

推荐工作流：

1. 用户在招聘网站正常浏览岗位。
2. 遇到感兴趣的岗位时，用 `job-page-extractor` Chrome 插件加入候选池。
3. 从插件导出候选岗位 CSV/JSON。
4. 把岗位文件、简历、补充介绍、偏好条件和保密边界一起交给 `$analyze-career-opportunities`。
5. 由本 Skill 完成职业方向判断、岗位筛选、简历版本规划、面试材料和 30/90/180 天提升计划。

不使用插件也可以。你可以手工整理一个岗位 CSV，推荐从 [assets/job-input-template.csv](assets/job-input-template.csv) 复制表头。

## Skill 调用名称

```text
analyze-career-opportunities
```

在 Codex 里这样调用：

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍，请完成完整职业交付：评估当前能力，归纳岗位市场和适合方向，筛选目标机会，判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

## 解决的问题

很多求职分析会把所有问题压成一个模糊匹配分数，但真正影响决策的是一组不同的问题：

- 这家公司是否值得投入时间？
- 这个岗位是否匹配候选人当前能力？
- 候选人是否能在三到六个月内补齐关键差距？
- 是真的缺能力，还是缺可以公开展示的证据？
- 计划中的项目是否被误写成已完成经历？
- 工作中涉及保密的内容，能否安全抽象成面试可讲的表达？

这个 Skill 会把公司质量、当前岗位匹配度、未来可达匹配度、证据强度、偏好兼容度和硬性筛选条件拆开判断，而不是藏在一个总分里。

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

## 交付内容

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

## 项目特点

- 支持 `job-page-extractor` Chrome 插件导出的候选岗位 CSV/JSON，也支持用户手工整理的岗位表格。
- 提供最小 CSV 输入格式，用户不依赖插件也能快速准备岗位资料。
- 不只依赖简历；补充介绍、项目材料、作品链接、偏好条件和修正信息都可以作为输入。
- 按职责和能力模式聚类岗位，而不是只按岗位标题归类。
- 只对进入候选范围的公司做公开资料核查，减少无效研究。
- 公司判断必须有来源支撑；资料不足时标记为 incomplete 或 low confidence，而不是编造结论。
- 区分“可公开写进简历的证据”和“只能面试安全抽象表达的私有证据”。
- 防止 planned / in_progress 项目被写成 completed 经历。
- 生成最小必要简历版本，避免为了每个岗位机械复制一份简历。
- 把能力差距转成具体提升任务，每项任务包含交付物、验收标准、依赖关系和 fallback scope。
- 附带本地审计脚本，用于检查岗位输入、公司来源覆盖和交付清单一致性。

## 仓库结构

```text
.
|-- SKILL.md
|-- README.md
|-- README.en.md
|-- AI_INSTALL.md
|-- LICENSE
|-- agents/
|-- assets/
|   |-- job-input-template.csv
|   `-- report-template.md
|-- references/
`-- scripts/
```

## 安装到 Codex

这个仓库本身就是一个 Skill。安装目标目录名必须是：

```text
analyze-career-opportunities
```

如果是让另一个 AI Agent 安装，建议直接把 [AI_INSTALL.md](AI_INSTALL.md) 发给它。那个文件是面向 AI 的安装与验证流程。

### Windows PowerShell

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" | Out-Null
Copy-Item -Recurse -Force ".\career-opportunity-analyst-skill\*" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

然后新开一个 Codex 任务，让 Skill 元数据被重新加载。

### macOS / Linux

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
mkdir -p ~/.codex/skills/analyze-career-opportunities
cp -R career-opportunity-analyst-skill/* ~/.codex/skills/analyze-career-opportunities/
```

然后新开一个 Codex 任务。

## 详细使用方法

### 1. 准备岗位数据

有两种方式。

方式 A：使用 Chrome 插件

1. 安装并打开 [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor)。
2. 正常浏览招聘网站。
3. 对自己感兴趣的岗位，用插件加入候选池。
4. 从插件导出候选岗位 CSV/JSON。
5. 把导出的文件交给 `$analyze-career-opportunities`。

方式 B：手工准备 CSV

最简单的岗位 CSV 只需要三列：

```csv
job_id,title,company_name
job-001,AI产品经理,示例科技
```

更推荐使用下面的完整表头，复制自 [assets/job-input-template.csv](assets/job-input-template.csv)：

```csv
job_id,title,company_name,city,source_platform,source_url,collected_at,salary_min,salary_max,salary_period,experience_min,experience_max,education,responsibilities,required_skills,preferred_skills,description_raw,company_text_raw,notes
```

字段说明：

- `job_id`：岗位唯一编号，必填。可以自己写 `job-001`、`job-002`。
- `title`：岗位名称，必填。
- `company_name`：公司名称，必填。
- `city`：工作城市。
- `source_platform`：来源平台，例如 BOSS、拉勾、猎聘、LinkedIn、官网。
- `source_url`：岗位链接。
- `collected_at`：收集日期，建议使用 `YYYY-MM-DD`。
- `salary_min` / `salary_max`：薪资下限和上限。
- `salary_period`：薪资周期，例如 `month`、`year`、`day`。
- `experience_min` / `experience_max`：经验年限要求。
- `education`：学历要求。
- `responsibilities`：岗位职责。
- `required_skills`：必备技能或硬性要求。
- `preferred_skills`：加分项。
- `description_raw`：原始 JD 文本。
- `company_text_raw`：岗位页里的公司介绍文本。
- `notes`：你的个人备注，例如“很感兴趣”“薪资不明确”“通勤较远”。

字段名不必完全一致。本 Skill 会先做字段映射和输入质量检查。但为了减少误判，建议优先使用上面的英文表头。

### 2. 准备候选人材料

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

### 3. 让 Codex 使用 Skill

推荐提示词：

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

## 审计脚本

查看岗位文件结构：

```powershell
python scripts/profile_job_input.py path\to\jobs.csv
```

审计公司来源台账：

```powershell
python scripts/audit_company_sources.py company-sources.json
```

审计完整交付清单：

```powershell
python scripts/audit_career_delivery.py delivery-manifest.json
```

这些脚本不能证明职业建议一定正确。它们检查的是交付物是否遵守证据约束，例如引用一致性、简历中是否出现不安全声明、提升任务是否缺少使用门槛、公司来源覆盖是否不足等。

## 隐私边界

这个 Skill 默认本地优先。候选人材料应该保留在本地，除非用户明确要求 Codex 查询公开公司信息，或明确授权某个外部操作。

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
