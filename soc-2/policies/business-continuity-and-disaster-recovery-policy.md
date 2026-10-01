# Business Continuity and Disaster Recovery Policy

**Document ID:** SOC2-POL-006  
**Version:** 0.1  
**Status:** Draft — Portfolio Example  
**Policy Owner:** IT Operations  
**Review Frequency:** Annually and after significant changes

## 1. Purpose and scope

Sets requirements for assessing disruption risk, maintaining recovery plans, and testing recovery for the in-scope system.

## 2. Requirements

1. Perform a business impact analysis at least annually and assign each system component a recovery tier with a recovery time objective (RTO) and recovery point objective (RPO). Example: Tier 1 RTO 4 hours and RPO 1 hour.
2. Maintain a documented continuity and disaster recovery plan with activation criteria, roles, recovery sequence, and communication steps.
3. Back up in-scope data according to its tier, keep one copy isolated from production credentials, and encrypt backups.
4. Monitor backup jobs and investigate failures within one business day.
5. Test restoration of sample data at least quarterly for Tier 1 and exercise the full plan at least annually.
6. Document test results, compare them with RTO and RPO, and track corrective actions to closure.
7. Review the plan after incidents, significant change, and each exercise.

## 3. Roles and review

The policy owner maintains this policy, assigns responsibilities, and reviews it annually and after significant change. Exceptions are documented, time-limited, risk-assessed, and approved by the policy owner and IT Security.

## 4. Related criteria and documents

- SOC 2 criteria: CC9.1, CC7.5, A1.2, A1.3
- Related: ISO-PLAN-001 and ISO-POL-007 (ISO folder)

## 5. Approval

Approver: TBD · Approval date: TBD

---
**Disclaimer:** Illustrative draft; not approved or evidence of SOC 2 compliance. Numeric values are example values for a fictional organization.
