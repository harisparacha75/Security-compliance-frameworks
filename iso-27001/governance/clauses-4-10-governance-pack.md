# ISO/IEC 27001 Clauses 4–10 Governance Pack

**Document ID:** ISO-GOV-001  
**Version:** 0.2  
**Status:** Draft — Portfolio Example  
**Owner:** IT Security  
**Review Cycle:** Annually and after significant change

## 1. Purpose

This pack shows how the repository's documents map to the management-system requirements in clauses 4–10 of ISO/IEC 27001:2022, defines ISMS roles, and sets the rules for controlled documents. It does not claim an operating ISMS; every record remains an illustrative draft.

## 2. Clause-to-document map

| Clause | Requirement | Where it is addressed |
|---|---|---|
| 4.1 | Understand the organization and its context | [Context register](context-and-interested-parties-register.csv) (CTX items) |
| 4.2 | Understand needs of interested parties | [Context register](context-and-interested-parties-register.csv) (IP items) |
| 4.3 | Determine the scope of the ISMS | [ISMS scope](../isms-scope.md) |
| 4.4 | Information security management system | This pack; [iso-27001 README](../README.md) |
| 5.1 | Leadership and commitment | [Information Security Policy](../policies/information-security-policy.md); roles in section 3 below |
| 5.2 | Policy | [Information Security Policy](../policies/information-security-policy.md) |
| 5.3 | Organizational roles, responsibilities, authorities | Section 3 below |
| 6.1.1 | Actions to address risks and opportunities | [Risk assessment methodology](../risk-assessment/risk-assessment-methodology.md) |
| 6.1.2 | Information security risk assessment | [Methodology](../risk-assessment/risk-assessment-methodology.md); [Risk register](../risk-assessment/risk-register.csv) |
| 6.1.3 | Information security risk treatment | [Treatment plan](../risk-assessment/risk-treatment-plan.md); [Statement of Applicability](../statement-of-applicability/soa-register.csv) |
| 6.2 | Security objectives and planning to achieve them | [Objectives register](security-objectives-register.csv) |
| 6.3 | Planning of changes | Change management control A.8.32; section 4 below |
| 7.1 | Resources | [Management review template](management-review-template.md) (resource inputs and outputs) |
| 7.2 | Competence | [Competence and awareness plan](competence-and-awareness-plan.md) |
| 7.3 | Awareness | [Competence and awareness plan](competence-and-awareness-plan.md); control A.6.3 |
| 7.4 | Communication | [Communication plan](communication-plan.md) |
| 7.5 | Documented information | Section 4 below |
| 8.1 | Operational planning and control | Procedure and implementation documentation; [Control register](../control-implementation/control-register.csv) |
| 8.2 | Risk assessment at planned intervals | Methodology section 8 (annual and after significant change) |
| 8.3 | Risk treatment implementation | [Treatment plan](../risk-assessment/risk-treatment-plan.md) |
| 9.1 | Monitoring, measurement, analysis, evaluation | [Objectives register](security-objectives-register.csv); metrics in each procedure |
| 9.2 | Internal audit | [Internal audit program](internal-audit-program.md) |
| 9.3 | Management review | [Management review template](management-review-template.md) |
| 10.1 | Continual improvement | Management review outputs; [corrective action register](nonconformity-corrective-action-register.csv) |
| 10.2 | Nonconformity and corrective action | [Corrective action register](nonconformity-corrective-action-register.csv) |

## 3. ISMS roles and authorities

| Role | Held by (fictional) | Responsibilities |
|---|---|---|
| Top management | Management | Approve policy, scope, objectives, risk acceptance for High and Critical risks, and resources; chair management review |
| ISMS owner | IT Security lead | Maintain the ISMS, risk process, SoA, and objectives; report ISMS performance |
| Risk owners | As named in the risk register | Own treatment decisions and residual risk for assigned risks |
| Control owners | As named in the control register | Operate controls and keep evidence |
| SOC lead | SOC | Detect, triage, and coordinate incident response |
| HR | HR | Screening, terms of employment, disciplinary process, joiner/leaver notifications |
| Legal/Compliance | Legal/Compliance | Legal, contractual, and privacy requirements; authority contact |
| Vendor Management | Vendor Management | Supplier due diligence, contracts, and reviews |

## 4. Documented information rules (clause 7.5)

- **Document IDs** are unique across the repository: `ISO-POL-###` policies, `ISO-STD-###` standards, `ISO-PROC-###` procedures, `ISO-PLAN-###` plans, `ISO-GOV-###` governance documents, and `ISMS-SCOPE-001` for the scope. SOC 2 documents use `SOC2-POL-###` and `SOC2-SYS-###`.
- Each controlled document records version, status, owner, review cycle, and approval. Drafts show `Approver: TBD`.
- Changes are made by pull request, reviewed by the document owner, and recorded in the [CHANGELOG](../../CHANGELOG.md).
- Registers use fixed vocabularies, and `scripts/validate_repo.py` checks ID uniqueness, register cross-references, and counts on every change.

## 5. Completion gates before claiming an operating ISMS

Approved scope and policy; completed and approved risk assessment; approved SoA; implemented controls with retained evidence; completed internal audit; completed management review; and corrective actions tracked to closure.

---
**Disclaimer:** Illustrative portfolio template only. It is not approved, adopted, or evidence of ISO/IEC 27001 compliance.
