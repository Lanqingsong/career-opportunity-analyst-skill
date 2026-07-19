# Company Research Reference

## Principle

Company due diligence is a first gate, not an optional appendix after role ranking. A local agent should actively research companies with public sources instead of asking the user to do the background check.

The goal is not to write a long company profile. The goal is to decide whether the company deserves the user's time, whether the role is close to real business, and what risks or unknowns should affect application priority.

## Research sequence

1. Resolve company identity using legal or full company name, city, industry, official domain, hiring entity, and source platform. Keep ambiguous entities separate.
2. Run a first-gate check for every company in the user's candidate pool:
   - identity clarity;
   - business or product clarity;
   - hiring entity versus work entity;
   - obvious public risk signals;
   - whether the job appears close to core business.
3. Deep-research high-interest, high-fit, unclear, or risky companies before final ranking.
4. Search official website, investor or regulatory material, product pages, and official recruitment pages.
5. Search independent reporting for financing, financial or operating changes, layoffs, litigation, penalties, product adoption, and industry position.
6. Open pages and record the exact claim each page supports. Do not rely on a search snippet alone.
7. Compare the job with the company's products and growth direction. Distinguish core product work from internal support, delivery, outsourcing, or speculative hiring.
8. Audit coverage before assigning confidence.

## First-gate labels

Use these labels before detailed role matching:

- `pass`: company identity and basic business are clear; no obvious blocking risk found.
- `watch`: company may be viable, but there are important unknowns or weak source coverage.
- `deprioritize`: company is real but risk, business mismatch, role ambiguity, or preference conflict makes it lower priority.
- `block`: company identity, hiring entity, legal/risk issue, or user hard filter makes it inappropriate unless the user explicitly overrides.
- `incomplete`: public information is not enough to judge.

Never turn missing information into a negative fact. Use `incomplete` or `watch` when evidence is weak.

## Query plan

Use the exact company identity and vary the intent:

- official site, about, products, customers, careers
- annual report, regulatory filing, financing, revenue, profitability
- latest product launch, commercialization, customer adoption
- layoffs, litigation, penalty, shutdown, business contraction
- technical team, engineering blog, open-source work, patents
- exact job title plus business unit or product name

Prefer current sources for changeable facts. Record publication date and access date separately.

## Source hierarchy

1. Regulatory disclosure, exchange filing, audited report, government record.
2. Company website, investor relations, official product or recruitment page.
3. Reputable independent business, technology, or industry publication.
4. Specialist databases and established research organizations.
5. Recruitment aggregators, social posts, forums, and anonymous reviews.

Lower-tier sources can identify questions but cannot alone support a high-confidence negative or positive conclusion.

## Minimum evidence

For a high-confidence company conclusion require:

- at least two reachable sources from different domains;
- at least one official, regulatory, or audited source;
- at least one independent source for material development or risk claims;
- a publication date for time-sensitive claims;
- a written claim-to-source mapping.

If these conditions fail, set research status to `incomplete`, confidence to `low`, and state the missing evidence.

## Source ledger schema

```json
{
  "company_name": "Full company name",
  "identity_status": "resolved",
  "first_gate": "pass",
  "sources": [
    {
      "title": "Page title",
      "url": "https://example.com/page",
      "published_at": "2026-01-01",
      "accessed_at": "2026-07-17",
      "source_class": "official",
      "claim": "The exact fact supported by this page"
    }
  ]
}
```

Allowed `source_class` values are `regulatory`, `official`, `independent`, `aggregator`, and `community`.

## Decision language

Separate:

- verified fact;
- inference based on multiple facts;
- uncertainty or conflicting evidence;
- verification action needed before applying or accepting an offer.

Do not describe general industry growth as proof that a particular company is healthy.
