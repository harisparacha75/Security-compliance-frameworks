# Risk Treatment Plan

## 1. Purpose

This illustrative plan records treatment decisions, control mappings, accountable role, and follow-up for the risks in the risk register.

## 2. Scope

This plan covers all 19 sample risks documented in `risk-register.csv`. Control references point to ISO/IEC 27001:2022 Annex A controls selected for this portfolio example.

## 3. Risk Treatment Register

| Risk ID | Risk Description | Treatment Decision | Annex A Control Mapping | Planned Controls | Risk Owner | Target Date | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | Unauthorized access to privileged accounts | Mitigate | A.8.5; A.5.18; A.8.2 | Enforce MFA and review privileged access rights | IT Security | TBD | Planned |
| RISK-002 | Data loss due to ransomware | Mitigate | A.8.13; A.8.7 | Implement tested offline or immutable backups and endpoint protection | IT Operations | TBD | Planned |
| RISK-003 | Exposure of sensitive data | Mitigate | A.5.15; A.5.23; A.8.16; A.8.3 | Review cloud storage permissions and monitor access to sensitive data | IT Security | TBD | Planned |
| RISK-004 | Phishing and credential compromise | Mitigate | A.6.3; A.8.7; A.6.8; A.8.23 | Implement email security and malware protection controls, enable event reporting, and deliver phishing awareness training | IT Security | TBD | Planned |
| RISK-005 | Loss of critical business data | Mitigate | A.8.13 | Implement regular backups and conduct restoration tests | IT Operations | TBD | Planned |
| RISK-006 | Unauthorized changes to production systems | Mitigate | A.8.32; A.8.16; A.5.3; A.8.19 | Enforce change approval, segregate duties, control software installation, and monitor privileged activities | IT Operations | TBD | Planned |
| RISK-007 | Service disruption due to network failure | Mitigate | A.8.14; A.8.20; A.8.22; A.8.6 | Implement redundancy, segment networks, manage capacity, and monitor network availability | IT Operations | TBD | Planned |
| RISK-008 | Improper handling of classified information | Mitigate | A.5.12; A.5.13; A.5.15 | Classify and label information and apply handling restrictions | IT Security | TBD | Planned |
| RISK-009 | Supplier or third-party compromise | Mitigate | A.5.19; A.5.20; A.5.21; A.5.22; A.5.23 | Perform supplier due diligence, define security clauses, review service changes and assurance evidence | Vendor Management; IT Security | TBD | Planned |
| RISK-010 | Exploitation of unpatched vulnerability | Mitigate | A.8.8; A.8.9; A.8.16 | Maintain asset coverage, scan and prioritize vulnerabilities, track remediation and exceptions | IT Security | TBD | Planned |
| RISK-011 | Security monitoring or logging failure | Mitigate | A.8.15; A.8.16; A.8.17 | Monitor log pipeline health, protect logs, validate time synchronization, and review coverage | SOC | TBD | Planned |
| RISK-012 | Sensitive data leakage | Mitigate | A.5.12; A.5.14; A.8.12; A.8.16 | Classify information, restrict transfers and sharing, and monitor for suspicious data movement | IT Security | TBD | Planned |
| RISK-013 | Prolonged outage or failed recovery after a disruption | Mitigate | A.5.29; A.5.30; A.8.13; A.8.14 | Define recovery objectives, maintain the continuity and recovery plan, and exercise it annually | IT Operations | TBD | Planned |
| RISK-014 | Insider misuse of access or data | Mitigate | A.6.1; A.6.2; A.6.4; A.6.5; A.5.3; A.5.11; A.8.3 | Screen personnel, bind them to security terms, separate duties, return assets and revoke access on exit, and apply disciplinary process | IT Security; HR | TBD | Planned |
| RISK-015 | Non-compliance with legal, regulatory, or contractual requirements | Mitigate | A.5.31; A.5.33; A.5.34; A.5.36 | Maintain a requirements register, retention schedule, and privacy records, and review compliance periodically | Legal/Compliance | TBD | Planned |
| RISK-016 | Loss or theft of equipment or storage media | Mitigate | A.7.9; A.7.10; A.7.14; A.8.1; A.8.24 | Encrypt endpoints, control removable media, enable remote wipe, and sanitize equipment before disposal | IT Operations | TBD | Planned |
| RISK-017 | Physical intrusion or environmental event at the supplier-managed facility | Transfer | A.5.19; A.5.20; A.5.22; A.5.29 | Rely on contractual physical-security commitments, review provider assurance reports, and plan for facility loss | Vendor Management | TBD | Planned |
| RISK-018 | Exposure of data in transit or at rest through weak cryptography or key management | Mitigate | A.8.24; A.5.14; A.8.21 | Define cryptography and key management rules, encrypt in transit and at rest, and manage key lifecycle | IT Security | TBD | Planned |
| RISK-019 | Delayed or ineffective incident handling | Mitigate | A.5.24; A.5.25; A.5.26; A.5.27; A.5.28; A.6.8 | Triage events consistently, preserve evidence, respond per plan, and review incidents for lessons learned | SOC | TBD | Planned |

## 4. Implementation and Monitoring

- Risk owners coordinate treatment implementation and maintain supporting records.
- Progress is reviewed periodically; evidence references are maintained in the ISO evidence register.
- Residual likelihood and impact in the register are illustrative target values that assume the planned controls are implemented; they must be reassessed with real evidence after implementation.
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
