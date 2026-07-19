# Company And Career-Outlook Research

## Principle

Company research is valuable only when it answers the user's real career questions. Do not reduce it to "is this company real" or "does the business exist." Basic identity checks are useful, but they are not the point.

The point is to judge whether the company and role are worth the user's time:

- development prospects;
- career prospects of the role;
- work pressure;
- promotion room;
- growth environment;
- team culture;
- management and collaboration style;
- whether the role can produce useful evidence for the user's next move.

## Research sequence

1. Start from the user's priorities. If the user cares about stability, growth, compensation, low pressure, technical depth, promotion, or team culture, make those dimensions visible in the research.
2. Resolve the basic company identity and hiring entity. Keep this short unless ambiguity affects the decision.
3. Research business and development prospects:
   - product or business line;
   - growth, contraction, financing, profitability, commercialization, or market position;
   - whether the role belongs to core business, growth business, internal support, outsourcing delivery, or temporary exploration.
4. Research career environment:
   - overtime and delivery pressure;
   - employee turnover;
   - management style;
   - promotion room and internal mobility;
   - learning environment, mentorship, technical depth, and ownership;
   - team stability and communication style.
5. Compare company and role findings with the user's preferences and deal-breakers.
6. Write the conclusion as a career decision, not a company profile.

## Useful sources

Use different source types for different questions:

- Official website, product pages, investor relations, annual reports, regulatory filings: business facts, products, financing, strategy, hiring entity.
- Independent business, technology, or industry media: growth, layoffs, financing, product adoption, market position, risk events.
- Forums and communities: work pressure, team atmosphere, management style, promotion, turnover, interview process, hidden job expectations.
- Recruiting platforms and anonymous employee-review sites: compensation bands, overtime patterns, role scope, team comments.
- Social platforms such as Maimai, Kanzhun, Glassdoor, Zhihu, Xiaohongshu, Reddit, LinkedIn, and similar public discussions: repeated signals about environment and reputation.

Community and forum sources are especially useful for user-interest dimensions, but they are noisy. Treat them as signals. Look for repeated patterns across independent posts and platforms.

## Query plan

Use exact company identity plus career-intent queries:

- company name + development prospects / growth / financing / layoffs / business contraction
- company name + overtime / work pressure / employee review / turnover
- company name + promotion / internal transfer / career growth
- company name + team atmosphere / management style / technical team
- company name + exact role title + interview / role scope / team
- company name + business unit or product name + hiring

For Chinese companies, also try Chinese-language queries:

- 公司名 + 加班 / 强度 / 压力
- 公司名 + 晋升 / 成长 / 培养
- 公司名 + 氛围 / 领导 / 管理
- 公司名 + 脉脉 / 看准 / 知乎 / 小红书
- 公司名 + 裁员 / 融资 / 业务 / 前景

Prefer current sources for changeable facts. Record publication date and access date separately when available.

## Evidence handling

Separate:

- verified business facts;
- repeated workplace signals;
- single-person anecdotes;
- inference based on multiple sources;
- uncertainty or missing coverage.

Do not present one anonymous post as fact. Better wording:

- "Several community posts suggest heavy delivery pressure, but coverage is limited."
- "Official material shows the product line exists; independent coverage of commercial traction is weak."
- "Employee-review signals are mixed, so treat team culture as an interview-verification item."

## Research labels

Use these labels before detailed role matching:

- `strong_watch`: company and role appear promising for the user's goals.
- `watch`: viable, but important unknowns remain.
- `caution`: useful opportunity, but pressure, culture, promotion, business, or preference risks are visible.
- `deprioritize`: career value looks weaker than alternatives.
- `block`: violates a user hard filter or has a serious unresolved risk.
- `incomplete`: public information is not enough to judge.

Never turn missing information into a negative fact. Use `incomplete` or `watch` when evidence is weak.

## Source hierarchy

1. Regulatory disclosure, exchange filing, audited report, government record.
2. Company website, investor relations, official product or recruitment page.
3. Reputable independent business, technology, or industry publication.
4. Recruiting platforms, employee-review sites, professional communities, forums, and public social posts.
5. Anonymous single posts and comments.

Lower-tier sources can be very useful for pressure and culture, but they need pattern matching and careful wording.

## Source ledger schema

```json
{
  "company_name": "Full company name",
  "identity_status": "resolved",
  "career_outlook_label": "watch",
  "research_dimensions": {
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
      "source_class": "community",
      "claim": "The exact signal supported by this page"
    }
  ]
}
```

Allowed `source_class` values are `regulatory`, `official`, `independent`, `aggregator`, and `community`.

## Decision language

Separate:

- company development outlook;
- role career value;
- pressure and culture risk;
- promotion and growth opportunity;
- fit with user preferences;
- verification questions to ask in interviews.

Do not describe general industry growth as proof that a particular company is healthy. Do not describe a single forum complaint as proof that a team is bad.
