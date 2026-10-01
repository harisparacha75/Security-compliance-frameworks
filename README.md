# Security Compliance Frameworks

A cybersecurity portfolio project demonstrating sample security controls, risk assessment, policy documentation, and evidence-tracking approaches for ISO/IEC 27001:2022 and SOC 2.

This repository is intended for learning, practical documentation, and portfolio development. All examples use fictional assumptions and require organization-specific review.

## Project Status

- **ISO/IEC 27001:2022:** Illustrative scope, risk assessment (19 risks), risk treatment plan, a decided 93-control Statement of Applicability (76 applicable, 17 excluded with rationale), control and evidence registers, seven policies, seven procedures and standards, an asset inventory linked to risks, and draft clause 4–10 governance documents with a clause-to-document map. Every control is `Planned`; nothing is approved or implemented, so this is an example ISMS design, not an operating ISMS.
- **SOC 2:** An illustrative control matrix and evidence register covering all 36 Security (CC1.1–CC9.2) and Availability (A1.1–A1.3) criteria, twelve draft policies, Trust Services Criteria notes, and an unchecked planning checklist. The checklist is not an assessment.
- **Crosswalk:** 78 illustrative ISO/IEC 27001 to SOC 2 relationships (156 rows, both directions) covering all 36 criteria.
- **Validation:** `scripts/validate_repo.py` checks IDs, counts, cross-references, and links; it runs in GitHub Actions on every push and pull request.

No evidence of control implementation, testing, certification, SOC 2 examination, or audit readiness is claimed.

## Objectives

- Document sample security controls and implementation approaches.
- Develop risk assessment and risk treatment documentation.
- Maintain control registers and evidence-tracking templates.
- Explore relationships between ISO/IEC 27001 and SOC 2 without treating the frameworks as interchangeable.
- Demonstrate practical governance, risk management, and compliance documentation skills.

## Repository Structure

```text
Security-compliance-frameworks/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── SECURITY.md
├── .github/workflows/validate.yml
├── scripts/validate_repo.py
├── control-mapping/
├── iso-27001/
│   ├── isms-scope.md
│   ├── asset-inventory.csv
│   ├── control-implementation/
│   ├── evidence/
│   ├── governance/
│   ├── policies/
│   ├── procedures/
│   ├── risk-assessment/
│   └── statement-of-applicability/
├── soc-2/
│   ├── system-description.md
│   ├── management-assertion-template.md
│   ├── audit-readiness/
│   ├── control-matrix/
│   ├── evidence/
│   ├── policies/
│   └── trust-services-criteria/
└── templates/
```

## Validation

```bash
python3 scripts/validate_repo.py
```

The script uses only the Python standard library and exits non-zero if any check fails.

## Disclaimer

This is an educational portfolio project. It is not legal advice, an audit report, an attestation, or an assurance opinion, and it does not demonstrate ISO 27001 certification or SOC 2 compliance.
