# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

这是一个给本地 Agent 使用的职业机会分析 Skill。它适合放进 Codex、WorkBuddy、Claude Code 或其他能读取本地文件的 Agent 工作流里。Codex 只是其中一种运行环境。

它做的事很朴素：帮你把“我是谁、我想找什么、这些公司靠不靠谱、哪些岗位值得投、简历应该怎么写、面试怎么讲”放到同一张桌子上判断。

## 先说清楚定位

这个 Skill 不是简历润色模板，也不是岗位打分器。它更像一个本地求职分析助理，重点有三件事：

1. 挖清楚用户需求和经历：目标、偏好、顾虑、真实经历、可公开证据、保密边界。
2. 先做公司背调：公司是否真实、业务是否成立、岗位是否在核心业务里、近期有没有明显风险。
3. 再做岗位匹配：方向、机会、简历版本、面试材料和 30/90/180 天补强计划。

公司背调不是“筛出候选岗位以后顺手查一下”。它是第一道闸门。公司不值得看，后面的岗位匹配和简历定制就不应该浪费时间。

## 推荐配套工具

推荐配合 Chrome 浏览器插件 [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) 使用。

这个插件的定位不是批量抓取全网岗位，而是让用户在浏览招聘网站时，把自己感兴趣的岗位加入候选池，然后导出 CSV/JSON。人的兴趣先筛一遍，本地 Agent 再做深度分析。

推荐流程：

1. 用户正常浏览招聘网站。
2. 遇到感兴趣的岗位，用 `job-page-extractor` Chrome 插件加入候选池。
3. 从插件导出候选岗位 CSV/JSON。
4. 把岗位文件、简历、补充介绍、偏好和保密边界交给本地 Agent。
5. 本地 Agent 使用 `$analyze-career-opportunities` 完成公司背调、机会筛选、简历版本规划、面试准备和提升计划。

不使用插件也可以。你可以手工整理一个岗位 CSV，直接复制 [assets/job-input-template.csv](assets/job-input-template.csv) 的表头。

## 调用名称

```text
analyze-career-opportunities
```

示例提示词：

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍。
先挖掘我的真实需求、经历、偏好和保密边界；再对岗位里的公司做背调，判断哪些公司值得优先看；然后归纳岗位市场和适合方向，筛选目标机会，判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。
不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

## 它会交付什么

完整分析通常包括：

1. 用户需求画像：目标城市、行业、薪资、工作强度、公司偏好、不能接受的条件。
2. 经历挖掘：真实做过什么、负责到什么边界、哪些能公开证明、哪些只能抽象讲。
3. 岗位输入检查：CSV/JSON 字段映射、缺失字段、来源和备注。
4. 公司背调：公司身份、业务、产品、融资或财务、公开风险、岗位是否接近核心业务。
5. 岗位市场归纳：岗位簇、共性要求、差异化要求、硬性门槛。
6. 适合方向：1-3 个更值得投入的方向，并说明为什么。
7. 目标机会：把公司判断和岗位匹配分开写，不用一个总分糊过去。
8. 简历版本：判断最少需要几份定向简历，并生成对应版本。
9. 面试材料：HR 问题、技术深挖、项目讲法、保密问题回答。
10. 30/90/180 天计划：每项任务有交付物、验收标准、简历使用门槛和降级方案。

## 公司背调怎么做

本地 Agent 应该主动完成公司背调，而不是把这部分丢给用户。

背调至少看这些问题：

- 公司主体是否明确，岗位发布方和实际用工方是否一致。
- 公司做什么产品或业务，岗位是否接近核心业务。
- 近期是否有融资、增长、裁员、处罚、诉讼、经营收缩等信号。
- 招聘岗位像核心团队扩张、内部支持、外包交付，还是试探性招聘。
- 公开资料是否足够支撑判断；资料不够时标记为 `incomplete`，不要编结论。

高置信公司判断需要至少两个不同域名来源，其中应包含官方、监管、年报或审计类来源，并尽量有独立媒体或行业报道交叉验证。

## 岗位 CSV 输入格式

最简单只需要三列：

```csv
job_id,title,company_name
job-001,AI产品经理,示例科技
```

更推荐使用完整表头：

```csv
job_id,title,company_name,city,source_platform,source_url,collected_at,salary_min,salary_max,salary_period,experience_min,experience_max,education,responsibilities,required_skills,preferred_skills,description_raw,company_text_raw,notes
```

字段说明：

- `job_id`：岗位编号，必填。可以写 `job-001`、`job-002`。
- `title`：岗位名称，必填。
- `company_name`：公司名称，必填。
- `city`：工作城市。
- `source_platform`：来源平台，例如 BOSS、拉勾、猎聘、LinkedIn、官网。
- `source_url`：岗位链接。
- `collected_at`：收集日期，建议 `YYYY-MM-DD`。
- `salary_min` / `salary_max`：薪资下限和上限。
- `salary_period`：薪资周期，例如 `month`、`year`、`day`。
- `experience_min` / `experience_max`：经验年限要求。
- `education`：学历要求。
- `responsibilities`：岗位职责。
- `required_skills`：必备技能。
- `preferred_skills`：加分项。
- `description_raw`：原始 JD 文本。
- `company_text_raw`：岗位页里的公司介绍。
- `notes`：你的个人备注，例如“很感兴趣”“薪资不明确”“通勤太远”。

字段名不必完全一致，但建议优先使用上面的英文表头，减少误判。

## 安装给本地 Agent

这个仓库是 Codex Skill 格式，安装到 Codex 时目录名必须是：

```text
analyze-career-opportunities
```

Windows PowerShell：

```powershell
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills\analyze-career-opportunities" | Out-Null
Copy-Item -Recurse -Force ".\career-opportunity-analyst-skill\*" "$env:USERPROFILE\.codex\skills\analyze-career-opportunities\"
```

macOS / Linux：

```bash
git clone https://github.com/Lanqingsong/career-opportunity-analyst-skill.git
mkdir -p ~/.codex/skills/analyze-career-opportunities
cp -R career-opportunity-analyst-skill/* ~/.codex/skills/analyze-career-opportunities/
```

如果是 WorkBuddy、Claude Code 或其他本地 Agent，可以把这个仓库作为本地知识库或工具目录加载，并要求 Agent 先读取 `SKILL.md`，再按 `references/` 和 `scripts/` 执行。

面向 AI 的安装说明见 [AI_INSTALL.md](AI_INSTALL.md)。

## 本地脚本

检查岗位文件：

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

脚本只检查结构和证据约束，不能替代人的判断。

## 隐私边界

候选人材料默认留在本地。不要把简历、岗位文件、项目细节、内部数据或公司保密内容上传到无关服务。

保密经历只抽象到这个层级：问题类型、个人职责边界、约束条件、技术取舍、验证方法、泛化结果。不要要求源码、内部数据、日志、模型权重、客户身份、未公开算法或内部敏感指标。

## License

Apache-2.0.
