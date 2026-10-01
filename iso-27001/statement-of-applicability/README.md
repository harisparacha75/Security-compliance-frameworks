# Statement of Applicability

The `soa-register.csv` records an applicability decision for each of the 93 ISO/IEC 27001:2022 Annex A controls. Of these, **76 are applicable** (`Yes`) and **17 are excluded** (`No`) with a documented rationale. No control is left undecided.

All 76 applicable controls have status `Planned`, a control-register entry, and an evidence-register reference. This does not mean any control is implemented. Decisions follow the fictional [ISMS scope](../isms-scope.md) and the [risk register](../risk-assessment/risk-register.csv), and require approval and validation by a real organization.

## Exclusions

| Controls | Reason |
|---|---|
| A.7.1–A.7.6, A.7.11, A.7.12 | Building-level physical security, utilities, and cabling are provided by the facility provider and treated as a supplier-managed dependency; reliance is addressed through supplier assurance (A.5.19, A.5.22; RISK-017) |
| A.8.4, A.8.25–A.8.31 | Product engineering and software development are outside the scope |
| A.8.11 | No routine use of production personal data in non-production environments is assumed |

Each exclusion states when to reassess. If scope changes, revisit the matching SoA rows, the control register, the evidence register, and the risk register.
