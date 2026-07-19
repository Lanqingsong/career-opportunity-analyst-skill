# Career Opportunity Analyst Skill

[简体中文](README.md) | [English](README.en.md)

这是一个面向求职者职业机会选择分析的 Skill。现在的招聘软件对求职者并不公平：一方面很难判断哪些公司真的适合自己，另一方面也很少有人告诉你，怎样在有限时间内补齐岗位差距、把经历讲清楚、把简历投到更值得投的地方。

这个 Skill 适合放进 Codex、WorkBuddy、Claude Code 或其他能读取本地文件的 Agent 工作流里

它帮你把“我是谁、我想找什么、哪些公司值得去、对你发展是否健康、简历怎么写、面试怎么讲”放到同一张桌子上判断。

## 先说清楚定位

这个 Skill 不做专业的简历润色模板，也不是岗位打分器。它更像一个求职分析助理，重点有三件事：

1. 挖清楚用户需求和经历：目标、偏好、顾虑、真实经历、可公开证据、保密边界。
2. 先看公司和职业前景：发展空间、业务质量、岗位前途、职业压力、晋升空间、成长环境、团队氛围。
3. 再做岗位匹配：方向、机会、简历版本、面试材料和 30/90/180 天补强计划。

这里说的“公司调研”不是查一下公司真假。互联网资料本身很难证明一家公司的全部真实情况，所以不要把它写成审计结论。更合理的做法是收集多类信号：机构观点、融资记录、投资方、产业报告、客户案例、招聘变化、论坛反馈、员工评价。它们共同帮助判断“这家公司值不值得投、进去以后能不能成长、会不会消耗很大、岗位是不是有前途”。

## 推荐配套工具

推荐配合 Chrome 浏览器插件 [Lanqingsong/job-page-extractor](https://github.com/Lanqingsong/job-page-extractor) 使用。

这个插件的定位是让用户在浏览招聘网站时，把自己感兴趣的岗位加入候选池，然后导出 CSV/JSON。人的兴趣先筛一遍，本地 Agent 再做深度分析。

推荐流程：

1. 正常浏览招聘网站。
2. 遇到感兴趣的岗位，用 `job-page-extractor` Chrome 插件加入候选池。
3. 从插件导出候选岗位 CSV/JSON。
4. 把岗位文件、简历、补充介绍、偏好和保密边界交给本地 Agent。
5. 本地 Agent 使用 `$analyze-career-opportunities` 完成公司与职业前景调研、机会筛选、简历版本规划、面试准备和提升计划。

不使用插件也可以。你可以手工整理一个岗位 CSV，直接复制 [assets/job-input-template.csv](assets/job-input-template.csv) 的表头。

## 调用名称

```text
analyze-career-opportunities
```

示例提示词：

```text
使用 $analyze-career-opportunities，读取我的岗位CSV、简历和补充介绍。
先挖掘我的真实需求、经历、偏好和保密边界；再调研岗位里的公司与职业前景，重点看机构观点、融资记录、投资方、产业报告、客户案例、发展前途、岗位成长性、职业压力、晋升空间、团队氛围和论坛/社区反馈；然后归纳岗位市场和适合方向，筛选目标机会，判断需要多少份简历并生成对应版本，同时准备面试材料和30/90/180天提升计划。
不要把计划中的项目写成已完成经历，涉及工作保密内容只做安全抽象。
```

## 它会交付什么

完整分析通常包括：

1. 用户需求画像：目标城市、行业、薪资、工作强度、公司偏好、不能接受的条件。
2. 经历挖掘：真实做过什么、负责到什么边界、哪些能公开证明、哪些只能抽象讲。
3. 岗位输入检查：CSV/JSON 字段映射、缺失字段、来源和备注。
4. 公司与职业前景调研：机构观点、融资和投资方、产业报告、客户案例、发展前途、岗位成长性、压力强度、晋升空间、学习环境、团队氛围。
5. 岗位市场归纳：岗位簇、共性要求、差异化要求、硬性门槛。
6. 适合方向：1-3 个更值得投入的方向，并说明为什么。
7. 目标机会：把公司前景、工作环境和岗位匹配分开写，不用一个总分糊过去。
8. 简历版本：判断最少需要几份定向简历，并生成对应版本。
9. 面试材料：HR 问题、技术深挖、项目讲法、保密问题回答。
10. 30/90/180 天计划：每项任务有交付物、验收标准、简历使用门槛和降级方案。

## 公司与职业前景怎么调研

本地 Agent 应该主动做这部分，不要把“你自己去查查公司”丢给用户。

互联网背调的真实性有限，所以它的目标不是证明“绝对真相”，而是建立一个可解释的信号组合：

- 机构观点：券商、咨询机构、研究机构、行业协会、产业报告怎么看这个赛道和公司。
- 资本信号：融资轮次、投资方质量、融资时间、并购、上市进展、股东背景。
- 商业信号：客户案例、合作伙伴、政府项目、中标记录、产品落地、商业化进展。
- 发展前途：业务是在增长、收缩、转型，还是长期不清楚。
- 职业前景：这个岗位能不能积累下一份工作认可的经验。
- 岗位位置：岗位在核心业务、增长业务、边缘支持、外包交付，还是临时探索。
- 职业压力：加班强度、交付压力、人员流动、管理风格。
- 晋升空间：是否有清晰职级、成长路径、内部转岗或培养机制。
- 成长环境：团队技术栈、导师资源、业务复杂度、能不能做出可展示成果。
- 团队氛围：沟通方式、稳定性、管理评价、跨部门协作成本。

不同来源回答不同问题。机构观点、融资记录和客户案例是公司发展前景的强信号；官网适合确认业务事实；论坛、员工评价、社交平台、招聘平台评论、脉脉、看准、Glassdoor、知乎、小红书、Reddit 等公开讨论，更适合发现压力、氛围、晋升和管理问题。

使用时要克制：融资不是公司一定成功的证明，机构观点也可能滞后或有立场；论坛信息更不能靠单条吐槽下结论。好的表达应该是“强信号”“侧面证明”“需要面试验证”，而不是“已经证明”。

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

如果是 WorkBuddy、Claude Code 或其他本地 Agent，可以把这个仓库链接发给他们，让他们自己安装。

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

候选人材料默认留在本地。请不要将项目细节、内部数据或公司保密内容上传给AI。

保密经历只抽象到这个层级：问题类型、个人职责边界、约束条件、技术取舍、验证方法、泛化结果。不要要求源码、内部数据、日志、模型权重、客户身份、未公开算法或内部敏感指标。

## License

Apache-2.0.
