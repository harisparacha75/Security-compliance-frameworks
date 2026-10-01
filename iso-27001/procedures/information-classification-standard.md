# Information Classification Standard

**Document ID:** ISO-STD-001  
**Version:** 0.2  
**Status:** Draft — Portfolio Example  
**Owner:** IT Security  
**Review Cycle:** Annually and after significant change

## 1. Purpose and scope

Define classification levels and handling rules so information receives protection proportionate to its sensitivity. Applies to all in-scope information, regardless of format.

## 2. Classification levels

| Level | Definition | Examples |
|---|---|---|
| Public | Approved for release; no harm if disclosed | Published marketing material |
| Internal | For personnel; limited harm if disclosed | Internal procedures, general IT documentation |
| Confidential | Sensitive; disclosure could harm customers, personnel, or the organization | Customer support records, financial records, HR records, security logs |
| Restricted | Highly sensitive; disclosure could cause severe harm | Authentication secrets, cryptographic keys, security assessment findings |

The information owner assigns the level. If unsure, treat information as Confidential until the owner decides.

## 3. Handling rules

| Control | Internal | Confidential | Restricted |
|---|---|---|---|
| Labelling | Label recommended | Label required | Label required |
| Storage | Approved company storage | Approved storage with access limited to need | Secrets vault or key store only |
| Encryption | In transit | In transit and at rest | In transit and at rest with managed keys |
| Sharing externally | Owner approval | Owner approval and agreement in place | Not shared except by approved secure process |
| Access review | Annual | Quarterly | Quarterly with named approvers |
| Disposal | Standard deletion | Verified deletion | Verified deletion; keys destroyed |

## 4. Labelling and inventory

Documents and repositories carry the classification in their name, header, or metadata. Assets in `asset-inventory.csv` carry the classification of the information they hold (A.5.9, A.5.13).

## 5. Review

Owners review classifications annually and when content or use changes. Reclassification is recorded.

## Related references

- Annex A: A.5.12, A.5.13, A.5.14, A.8.12
- SOC 2: CC6.7
- Risks: RISK-008, RISK-012
- Related documents: [Acceptable Use Policy](../policies/acceptable-use-policy.md)

## Approval

**Approver:** TBD  
**Approval date:** TBD  
**Next review:** TBD

---
**Disclaimer:** Draft illustrative portfolio document only. All numeric targets, tiers, and timeframes are example values for the fictional scenario; a real organization must set its own from its risk assessment, legal duties, and business needs. It is not approved, adopted, or evidence of ISO/IEC 27001 compliance.
