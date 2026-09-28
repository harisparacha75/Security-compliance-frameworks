# Risk Treatment Plan

## 1. Purpose

This illustrative plan records treatment decisions, control mappings, accountable role, and follow-up for the risks in the risk register.

## 2. Scope

This plan covers the eight sample risks documented in `risk-register.csv`. Control references point to ISO/IEC 27001:2022 Annex A controls selected for this portfolio example.

## 3. Risk Treatment Register

| Risk ID | Risk Description | Treatment Decision | Annex A Control Mapping | Planned Controls | Risk Owner | Target Date | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | Unauthorized access to privileged accounts | Mitigate | A.8.5; A.5.18; A.8.2 | Enforce MFA and review privileged access rights | IT Security | TBD | Planned |
| RISK-002 | Data loss due to ransomware | Mitigate | A.8.13; A.8.7 | Implement protected backups and endpoint malware protection | IT Operations | TBD | Planned |
| RISK-003 | Exposure of sensitive data in cloud storage | Mitigate | A.5.15; A.5.23; A.8.16 | Review cloud storage permissions and monitor access | IT Security | TBD | Planned |
| RISK-004 | Phishing and credential compromise | Mitigate | A.6.3; A.8.7 | Implement email security and malware protection controls and phishing awareness training | IT Security | TBD | Planned |
| RISK-005 | Loss of critical business data | Mitigate | A.8.13 | Perform scheduled backups and restoration tests | IT Operations | TBD | Planned |
| RISK-006 | Unauthorized changes to production systems | Mitigate | A.8.32; A.8.16 | Require change approval, testing, and change records; monitor privileged activities | IT Operations | TBD | Planned |
| RISK-007 | Service disruption due to network failure | Mitigate | A.8.14; A.8.20; A.8.22 | Address single points of failure through redundancy, network segmentation, and availability monitoring | IT Operations | TBD | Planned |
| RISK-008 | Improper handling of classified information | Mitigate | A.5.12; A.5.15 | Classify and label information and apply access/handling restrictions | IT Security | TBD | Planned |

| RISK-009 | Supplier or third-party compromise | Mitigate | A.5.19; A.5.20; A.5.21; A.5.22; A.5.23 | Perform supplier due diligence, define security clauses, and review assurance evidence | Vendor Management; IT Security | TBD | Planned |
| RISK-010 | Exploitation of unpatched vulnerability | Mitigate | A.8.8; A.8.9; A.8.16 | Maintain asset coverage, prioritize vulnerabilities, and track remediation | IT Security | TBD | Planned |
| RISK-011 | Security monitoring or logging failure | Mitigate | A.8.15; A.8.16; A.8.17 | Monitor log pipeline health, protect logs, and validate coverage and time synchronization | SOC | TBD | Planned |
| RISK-012 | Sensitive data leakage | Mitigate | A.5.12; A.5.14; A.8.12; A.8.16 | Classify information, restrict transfers and sharing, and monitor data movement | IT Security | TBD | Planned |

## 4. Implementation and Monitoring

- Risk owners coordinate treatment implementation and maintain supporting records.
- Progress is reviewed periodically; evidence references are maintained in the ISO evidence register.
- Residual likelihood and impact are reassessed after controls are implemented.
- Residual risk is compared with the illustrative acceptance criteria in the risk assessment methodology.
- Risks above the defined acceptance threshold are escalated; no risk is considered accepted while its decision is `Pending`.

## 5. Approval

| Role | Name | Approval Date |
|---|---|---|
| Risk Owner | TBD | TBD |
| Information Security | TBD | TBD |
| Management Approver | TBD | TBD |

---

**Disclaimer:** This is a fictional portfolio example. Risk owners, dates, approvals, risk ratings, and treatment decisions require validation by an actual organization. It is not evidence of ISO 27001 compliance.
