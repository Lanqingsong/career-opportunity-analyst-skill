# Company And Career-Outlook Research

## Principle

Company research is valuable only when it answers the user's real career questions. Do not reduce it to "is this company real" or "does the business exist." Basic identity checks are useful, but they are not the point.

Internet research has limited truthfulness. Treat it as signal collection, not forensic verification. The goal is to judge whether the company and role are worth the user's time by combining:

- institutional views;
- funding and investor signals;
- customer, partner, tender, government-project, and commercialization signals;
- business development prospects;
- career prospects of the role;
- work pressure;
- promotion room;
- growth environment;
- team culture;
- management and collaboration style;
- whether the role can produce useful evidence for the user's next move.

Institutional views and financing records can be strong evidence of company development prospects. They are often more useful than shallow web-page checks, but they still need careful wording. Funding does not guarantee future success. Institutional opinions may be stale, biased, or based on different assumptions.

## Research sequence

1. Start from the user's priorities. If the user cares about stability, growth, compensation, low pressure, technical depth, promotion, or team culture, make those dimensions visible.
2. Resolve the basic company identity and hiring entity. Keep this short unless ambiguity affects the decision.
3. Research institutional and capital signals:
   - financing rounds, financing time, investors, shareholder background;
   - M&A, IPO, listed-company filings, major strategic investment;
   - brokerage, consulting, research-institute, industry-association, or think-tank views;
   - public awards, government projects, industrial-policy support, public tenders.
4. Research business and development prospects:
   - product or business line;
   - growth, contraction, commercialization, profitability, or market position;
   - customer cases, partnerships, adoption signals, and public deployment evidence;
   - whether the role belongs to core business, growth business, internal support, outsourcing delivery, or temporary exploration.
5. Research career environment:
   - overtime and delivery pressure;
   - employee turnover;
   - management style;
   - promotion room and internal mobility;
   - learning environment, mentorship, technical depth, and ownership;
   - team stability and communication style.
6. Compare company and role findings with the user's preferences and deal-breakers.
7. Write the conclusion as a career decision, not a company profile.

## Useful sources

Use different source types for different questions:

- Official website, product pages, investor relations, annual reports, regulatory filings: business facts, products, financing, strategy, hiring entity.
- Institutional sources: brokerage reports, consulting reports, market research, industry association reports, think-tank articles, analyst views.
- Capital sources: financing databases, investor announcements, fund portfolio pages, shareholder disclosures, IPO or M&A materials.
- Commercial sources: customer cases, partner pages, government projects, tender records, product adoption stories, public deployment references.
- Independent business, technology, or industry media: growth, layoffs, financing, product adoption, market position, risk events.
- Forums and communities: work pressure, team atmosphere, management style, promotion, turnover, interview process, hidden job expectations.
- Recruiting platforms and anonymous employee-review sites: compensation bands, overtime patterns, role scope, team comments.
- Social platforms such as Maimai, Kanzhun, Glassdoor, Zhihu, Xiaohongshu, Reddit, LinkedIn, and similar public discussions: repeated signals about environment and reputation.

Institutional, capital, and commercial sources are strong signals for development prospects. Community and forum sources are especially useful for user-interest dimensions, but they are noisy. Treat them as signals. Look for repeated patterns across independent posts and platforms.

## Query plan

Use exact company identity plus career-intent and capital-intent queries:

- company name + development prospects / growth / financing / investors / shareholders
- company name + brokerage report / research report / industry report / market share
- company name + customer case / partnership / tender / government project / commercialization
- company name + layoffs / business contraction / profitability / IPO / M&A
- company name + overtime / work pressure / employee review / turnover
- company name + promotion / internal transfer / career growth
- company name + team atmosphere / management style / technical team
- company name + exact role title + interview / role scope / team
- company name + business unit or product name + hiring

For Chinese companies, also try Chinese-language queries:

- 公司名 + 融资 / 投资方 / 股东 / 上市 / 并购
- 公司名 + 券商研报 / 行业报告 / 机构观点 / 市场份额
- 公司名 + 客户案例 / 中标 / 政府项目 / 商业化 / 合作伙伴
- 公司名 + 加班 / 强度 / 压力
- 公司名 + 晋升 / 成长 / 培养
- 公司名 + 氛围 / 领导 / 管理
- 公司名 + 脉脉 / 看准 / 知乎 / 小红书
- 公司名 + 裁员 / 业务 / 前景

Prefer current sources for changeable facts. Record publication date and access date separately when available.

## Evidence handling

Separate:

- verified business facts;
- institutional or analyst opinions;
- capital and financing signals;
- commercial adoption signals;
- repeated workplace signals;
- single-person anecdotes;
- inference based on multiple sources;
- uncertainty or missing coverage.

Do not present one anonymous post as fact. Do not present one financing event as proof that the company will succeed. Better wording:

- "Recent financing from named investors is a strong positive signal, but does not prove long-term stability."
- "Institutional reports support the market-space thesis; direct evidence of this company's execution is still limited."
- "Several community posts suggest heavy delivery pressure, but coverage is limited."
- "Official material shows the product line exists; independent coverage of commercial traction is weak."
- "Employee-review signals are mixed, so treat team culture as an interview-verification item."

## Research labels

Use these labels before detailed role matching:

- `strong_watch`: company and role appear promising for the user's goals, with institutional, capital, commercial, or repeated independent support.
- `watch`: viable, but important unknowns remain.
- `caution`: useful opportunity, but pressure, culture, promotion, business, or preference risks are visible.
- `deprioritize`: career value looks weaker than alternatives.
- `block`: violates a user hard filter or has a serious unresolved risk.
- `incomplete`: public information is not enough to judge.

Never turn missing information into a negative fact. Use `incomplete` or `watch` when evidence is weak.

## Source hierarchy

1. Regulatory disclosure, exchange filing, audited report, government record.
2. Investor relations, official product or recruitment page, company website.
3. Institutional reports, brokerage or consulting views, industry association material.
4. Financing records, investor announcements, fund portfolio pages, shareholder or M&A information.
5. Customer cases, tenders, government projects, partnerships, public deployment references.
6. Reputable independent business, technology, or industry publication.
7. Recruiting platforms, employee-review sites, professional communities, forums, and public social posts.
8. Anonymous single posts and comments.

Lower-tier sources can be very useful for pressure and culture, but they need pattern matching and careful wording.

## Source ledger schema

```json
{
  "company_name": "Full company name",
  "identity_status": "resolved",
  "career_outlook_label": "watch",
  "research_dimensions": {
    "institutional_view": "medium",
    "capital_signal": "strong",
    "commercial_signal": "medium",
    "business_prospects": "medium",
    "role_future": "medium",
    "work_pressure": "watch",
    "promotion_room": "incomplete",
    "growth_environment": "medium",
    "team_culture": "watch"
  },
  "sources": [
    {
      "title": "Page title",
      "url": "https://example.com/page",
      "published_at": "2026-01-01",
      "accessed_at": "2026-07-17",
      "source_class": "institutional",
      "claim": "The exact signal supported by this page"
    }
  ]
}
```

Allowed `source_class` values are `regulatory`, `official`, `institutional`, `capital`, `customer`, `independent`, `aggregator`, and `community`.

## Decision language

Separate:

- company development outlook;
- institutional and capital support;
- commercial adoption;
- role career value;
- pressure and culture risk;
- promotion and growth opportunity;
- fit with user preferences;
- verification questions to ask in interviews.

Do not describe general industry growth as proof that a particular company is healthy. Do not describe a single forum complaint as proof that a team is bad. Do not describe financing or institutional views as proof that the company will succeed; describe them as strong supporting signals.
