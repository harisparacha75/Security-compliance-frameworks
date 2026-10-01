# Business Continuity and Disaster Recovery Plan

**Document ID:** ISO-PLAN-001  
**Version:** 0.2  
**Status:** Draft — Portfolio Example  
**Owner:** IT Operations  
**Review Cycle:** Annually and after significant change

## 1. Purpose and scope

Define how the organization keeps critical services running or restores them after a disruption such as a ransomware event, supplier outage, or loss of the supplier-managed facility. The plan covers the in-scope assets in `asset-inventory.csv`.

## 2. Recovery tiers

| Tier | Recovery time objective (RTO) | Recovery point objective (RPO) | Assets (examples) |
|---|---|---|---|
| Tier 1 | 4 hours | 1 hour | Identity service (AST-001), production servers (AST-003), network infrastructure (AST-005) |
| Tier 2 | 24 hours | 24 hours | Cloud file storage (AST-002), central logging and SIEM (AST-006), email and collaboration (AST-013), backup service (AST-007) |
| Tier 3 | 5 business days | 7 days | Employee endpoints (AST-004) and supporting tools |

Tiers come from a business impact analysis that asset owners review annually and after major change.

## 3. Activation

The plan is activated by the Incident Commander (IT Operations lead or delegate) when an incident or outage is expected to exceed the RTO of any Tier 1 asset, or when the facility provider declares a site-level event. Activation is recorded with time, trigger, and decision-maker.

## 4. Roles

| Role | Responsibility |
|---|---|
| Incident Commander | Declares activation, directs recovery, approves return to normal operations |
| IT Operations | Executes technical recovery in tier order |
| IT Security / SOC | Confirms the environment is clean before restoration; preserves evidence (A.5.28) |
| Management | Approves customer and authority communications; accepts recovery trade-offs |
| Vendor Management | Engages suppliers and facility provider under contract |

## 5. Recovery sequence

1. Contain the cause and confirm scope with SOC.
2. Restore Tier 1 assets in dependency order: network, identity, then production servers.
3. Restore Tier 2 assets; validate integrity and access controls.
4. Restore Tier 3 assets as capacity allows.
5. Confirm security controls (MFA, logging, monitoring) are active before declaring recovery complete (A.5.29).

## 6. Communication

Internal updates at least every two hours during activation. Customer, supplier, and authority notifications are approved by Management and follow the communication plan (`governance/communication-plan.md`) and any contractual or legal deadlines identified under A.5.31.

## 7. Exercises and maintenance

Run at least one recovery exercise per year, alternating between a tabletop and a technical restore of a Tier 1 asset. Record objectives, results versus RTO/RPO, issues, and corrective actions. Update the plan after each exercise, after significant change, and after any activation.

## Related references

- Annex A: A.5.29, A.5.30, A.8.13, A.8.14
- SOC 2: CC7.5, CC9.1, A1.2, A1.3
- Risks: RISK-013, RISK-017
- Related documents: [Backup and Recovery Policy](../policies/backup-and-recovery-policy.md), [Incident Response Policy](../policies/incident-response-policy.md)

## Approval

**Approver:** TBD  
**Approval date:** TBD  
**Next review:** TBD

---
**Disclaimer:** Draft illustrative portfolio document only. All numeric targets, tiers, and timeframes are example values for the fictional scenario; a real organization must set its own from its risk assessment, legal duties, and business needs. It is not approved, adopted, or evidence of ISO/IEC 27001 compliance.
