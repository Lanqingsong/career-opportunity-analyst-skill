# Company Research Reference

## Research sequence

1. Resolve identity using the legal or full company name, city, industry, official domain, and the hiring entity. Keep ambiguous entities separate.
2. Search the official website, investor or regulatory material, product pages, and official recruitment pages.
3. Search independent reporting for financing, financial or operating changes, layoffs, litigation, penalties, product adoption, and industry position.
4. Open the pages and record the exact claim each page supports. Do not rely on a search snippet alone.
5. Compare the job with the company's products and growth direction. Distinguish a core product role from internal support, delivery, outsourcing, or speculative hiring.
6. Audit coverage before assigning confidence.

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

If these conditions fail, set research status to `incomplete`, confidence to `low`, and state the missing evidence. Never turn missing information into a negative company fact.

## Source ledger schema

```json
{
  "company_name": "Full company name",
  "identity_status": "resolved",
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
