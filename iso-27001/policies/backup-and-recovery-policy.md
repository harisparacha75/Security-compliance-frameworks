# Backup and Recovery Policy

**Document ID:** ISO-POL-007  
**Version:** 0.2  
**Status:** Draft — Portfolio Example  
**Owner:** IT Operations  
**Review Cycle:** Annually and after significant change

## 1. Purpose

Ensure in-scope information can be restored after deletion, corruption, ransomware, or system failure within the recovery objectives defined for the illustrative continuity and recovery scenario.

## 2. Scope

All in-scope systems and data listed in `asset-inventory.csv`, including production servers (AST-003), cloud file storage (AST-002), identity data (AST-001), logging data (AST-006), and the backup service itself (AST-007).

## 3. Policy requirements

1. **Coverage.** Every in-scope asset is assigned a recovery tier (Tier 1, 2, or 3) in the continuity plan. An asset may be excluded from backup only with a documented decision by its owner and IT Security.
2. **Frequency.** Tier 1: hourly snapshots or continuous replication. Tier 2: daily. Tier 3: weekly.
3. **Copies.** Keep at least three copies on two different storage services, with one copy offline, immutable, or logically isolated from production credentials (3-2-1 rule).
4. **Protection.** Encrypt backups at rest and in transit (see A.8.24). Backup administration uses accounts separate from production administration, protected by MFA (A.8.2, A.8.5). Immutable or retention-locked copies are kept for at least 30 days.
5. **Retention.** Daily backups for 35 days, monthly backups for 12 months, and longer only where the records retention schedule (A.5.33) requires it. Expired backups are deleted and media sanitized (A.8.10, A.7.14).
6. **Monitoring.** Failed or missed backup jobs alert the SOC and are triaged within one business day. A weekly job-success report is reviewed by IT Operations; the illustrative target is at least 98% of scheduled jobs succeeding.
7. **Restore testing.** Restore a sample of Tier 1 data quarterly, Tier 2 semi-annually, and Tier 3 annually. Measure restore time against the tier RTO and data age against the tier RPO. Failed tests raise a corrective action (see `governance/nonconformity-corrective-action-register.csv`).
8. **Ransomware resilience.** Restore into an isolated environment and verify that restored data is free of malware before reconnecting it to production.
9. **Exceptions.** Documented, time-limited (maximum 90 days), approved by the asset owner and IT Security, and tracked until closed.

## 4. Roles

| Role | Responsibility |
|---|---|
| IT Operations | Operate backups, run restore tests, report results |
| IT Security | Review backup protection and approve exceptions |
| Asset owners | Confirm tier, retention, and restore test results for their assets |
| SOC | Triage backup failure alerts |

## 5. Records and metrics

Retain backup job reports, restore test results, exception records, and corrective actions (ISO-EV-012). Metrics: backup job success rate, restore tests completed on schedule (OBJ-003), and restore time versus RTO.

## Related references

- Annex A: A.8.13, A.8.14, A.8.10, A.8.24, A.5.30
- SOC 2: A1.2, A1.3
- Risks: RISK-002, RISK-005, RISK-013
- Related documents: Illustrative continuity and recovery requirements

## Approval

**Approver:** TBD  
**Approval date:** TBD  
**Next review:** TBD

---
**Disclaimer:** Draft illustrative portfolio document only. All numeric targets, tiers, and timeframes are example values for the fictional scenario; a real organization must set its own from its risk assessment, legal duties, and business needs. It is not approved, adopted, or evidence of ISO/IEC 27001 compliance.
