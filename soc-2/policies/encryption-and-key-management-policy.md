# Encryption and Key Management Policy

**Document ID:** SOC2-POL-009  
**Version:** 0.1  
**Status:** Draft — Portfolio Example  
**Policy Owner:** IT Security  
**Review Frequency:** Annually and after significant changes

## 1. Purpose and scope

Sets requirements for protecting information at rest and in transit and for managing cryptographic keys for the in-scope system.

## 2. Requirements

1. Encrypt Confidential and Restricted data at rest, and all in-scope data in transit over untrusted networks, using current industry-accepted algorithms and protocol versions.
2. Encrypt endpoints and removable media that may hold in-scope data.
3. Generate, store, and manage keys in an approved key store or service with restricted access and separation from the data they protect.
4. Rotate keys at least annually and immediately on suspected compromise; revoke keys when no longer needed.
5. Do not store secrets or keys in source code, tickets, or chat; keep them in a secrets vault.
6. Review approved algorithms and configurations annually and after publication of significant weaknesses.
7. Retain key management records (inventory, rotation, access reviews).

## 3. Roles and review

The policy owner maintains this policy, assigns responsibilities, and reviews it annually and after significant change. Exceptions are documented, time-limited, risk-assessed, and approved by the policy owner and IT Security.

## 4. Related criteria and documents

- SOC 2 criteria: CC6.1, CC6.7
- Related: ISO 27001 control register and Statement of Applicability (A.8.24)

## 5. Approval

Approver: TBD · Approval date: TBD

---
**Disclaimer:** Illustrative draft; not approved or evidence of SOC 2 compliance. Numeric values are example values for a fictional organization.
