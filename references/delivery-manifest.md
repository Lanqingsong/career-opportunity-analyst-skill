# Delivery Manifest

Use a UTF-8 JSON object to connect facts, requirements, decisions, resumes, and tasks. The bundled audit script checks semantic references and unsafe claims.

## Shape

```json
{
  "candidate_facts": [
    {
      "fact_id": "fact-1",
      "statement": "Built and deployed an ONNX/TensorRT inference path",
      "status": "confirmed",
      "disclosure_level": "public",
      "source_refs": ["resume"]
    }
  ],
  "job_requirements": [
    {
      "requirement_id": "req-1",
      "statement": "Production model deployment",
      "role_ids": ["role-1"]
    }
  ],
  "directions": [
    {
      "direction_id": "direction-1",
      "title": "AI model deployment",
      "requirement_ids": ["req-1"],
      "evidence_fact_ids": ["fact-1"],
      "gap_ids": []
    }
  ],
  "gaps": [],
  "resumes": [
    {
      "resume_id": "resume-1",
      "target_direction_ids": ["direction-1"],
      "claims": [
        {"text": "Deployed ONNX/TensorRT inference", "fact_ids": ["fact-1"]}
      ]
    }
  ],
  "learning_tasks": [],
  "companies": [],
  "sources": []
}
```

## Enumerations

Fact status:

- `confirmed`
- `evidence_available`
- `evidence_private`
- `in_progress`
- `planned`
- `unknown`
- `disallowed`

Disclosure level:

- `public`
- `abstract_only`
- `private`
- `disallowed`

Gap type:

- `hard_filter`
- `learnable`
- `evidence_gap`
- `expression_gap`
- `preference_conflict`
- `unknown`

Company confidence:

- `high`
- `medium`
- `low`
- `incomplete`

Source class:

- `regulatory`
- `official`
- `institutional`
- `capital`
- `customer`
- `independent`
- `aggregator`
- `community`

## Audit expectations

- Every reference ID must resolve.
- Resume claims may use only eligible facts and safe disclosure levels.
- Every learning task must reference a gap and contain a deliverable, acceptance criteria, and resume-use gate.
- Every high-confidence company business claim must have at least two sources from different domains, including official/regulatory and independent, institutional, capital, or customer coverage. Workplace, pressure, promotion, and culture claims may use community sources, but must be phrased as patterns or signals unless strongly corroborated. Financing, investor, and institutional views are strong development signals, not proof of future success.
- Unknown or planned facts may inform questions and plans but cannot support completed resume claims.
