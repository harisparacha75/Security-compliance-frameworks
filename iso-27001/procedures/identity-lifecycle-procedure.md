# Identity Lifecycle Procedure

**Document ID:** ISO-PROC-001  
**Version:** 0.2  
**Status:** Draft — Portfolio Example  
**Owner:** IT Security  
**Review Cycle:** Annually and after significant change

## 1. Purpose and scope

Define how user and privileged identities are created, changed, reviewed, and removed so access matches current role and employment status. Applies to employees, contractors, service accounts, and administrators of in-scope systems.

## 2. Joiner

1. HR or the sponsoring manager submits an access request naming role and start date.
2. Access is granted from the role baseline; anything beyond the baseline needs the data or system owner's approval.
3. MFA is enrolled before access to in-scope systems is enabled (A.8.5).
4. Provisioning completes within one business day of approval; the request and approval are retained.

## 3. Mover

1. The manager notifies IT Operations of a role change.
2. New access is approved as for joiners; access no longer needed is removed within two business days.

## 4. Leaver

1. HR notifies IT Operations of the termination date and whether it is voluntary or involuntary.
2. Accounts are disabled within four hours of the effective time; for involuntary or privileged departures, immediately.
3. Sessions and tokens are revoked, MFA devices are unenrolled, and shared secrets the person knew are rotated.
4. Assets are returned and recorded (A.5.11). Disabled accounts are deleted after 90 days unless retention is required.

## 5. Contractors and service accounts

- Contractor accounts have a named sponsor and an end date no more than 12 months out; extension needs sponsor approval.
- Service and shared accounts have a named owner, a documented purpose, credentials held in a secrets vault, and are reviewed with user accounts.

## 6. Privileged access

Administrators use separate privileged accounts with MFA, approval for elevation, and logging of privileged activity (A.8.2, A.8.15). Privileged accounts are reviewed quarterly.

## 7. Reviews

| Review | Frequency | Reviewer | Revocation deadline |
|---|---|---|---|
| Privileged accounts | Quarterly | IT Security | 5 business days |
| Cloud storage permissions | Quarterly | Data owners | 5 business days |
| Standard user access | Semi-annual | Line managers | 10 business days |
| Dormant accounts (no sign-in 45 days) | Monthly | IT Operations | Disable on detection |

Reviewers cannot approve their own access. Review records show reviewer, date, decisions, and completion of revocations.

## 8. Records and metrics

Retain requests, approvals, termination tickets, and review results (ISO-EV-004, ISO-EV-005, ISO-EV-019). Metric: percentage of privileged accounts reviewed on schedule (OBJ-002).

## Related references

- Annex A: A.5.15, A.5.16, A.5.18, A.8.2, A.8.3, A.5.11, A.6.5
- SOC 2: CC6.1, CC6.2, CC6.3
- Risks: RISK-001, RISK-003, RISK-014
- Related documents: [Access Control Policy](../policies/access-control-policy.md), [Authentication Policy](../policies/authentication-policy.md)

## Approval

**Approver:** TBD  
**Approval date:** TBD  
**Next review:** TBD

---
**Disclaimer:** Draft illustrative portfolio document only. All numeric targets, tiers, and timeframes are example values for the fictional scenario; a real organization must set its own from its risk assessment, legal duties, and business needs. It is not approved, adopted, or evidence of ISO/IEC 27001 compliance.
