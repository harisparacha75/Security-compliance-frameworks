# Risk Assessment Methodology

## 1. Purpose

This document defines the methodology for identifying, analyzing, evaluating, and treating information security risks in accordance with ISO/IEC 27001:2022.

## 2. Scope

This methodology applies to organizational information assets, systems, networks, applications, personnel, and business processes.

## 3. Risk Assessment Process

The risk assessment process consists of the following steps:

1. Identify information assets and record them in `../asset-inventory.csv` (each risk references asset IDs, and each asset lists its linked risks).
2. Identify threats and vulnerabilities.
3. Evaluate the likelihood of each risk.
4. Assess the potential business impact.
5. Calculate the risk score.
6. Determine risk treatment priorities.
7. Record the results in the risk register.

## 4. Risk Scoring

Risk is calculated using the following formula:

**Risk Score = Likelihood × Impact**

### 4.1 Likelihood Scale

| Score | Rating | Description |
|---|---|---|
| 1 | Rare | Unlikely to occur |
| 2 | Unlikely | Could occur occasionally |
| 3 | Possible | May occur under certain conditions |
| 4 | Likely | Expected to occur |
| 5 | Almost Certain | Expected to occur frequently |

### 4.2 Impact Scale

| Score | Rating | Description |
|---|---|---|
| 1 | Insignificant | Minimal business impact |
| 2 | Minor | Limited operational impact |
| 3 | Moderate | Noticeable business disruption |
| 4 | Major | Significant financial or operational impact |
| 5 | Severe | Critical business disruption or major data loss |

## 5. Risk Classification

| Risk Score | Level |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

## 6. Risk Treatment Options

Risks may be treated using the following approaches:

- **Mitigate:** Implement controls to reduce risk.
- **Avoid:** Eliminate the activity causing the risk.
- **Transfer:** Share or transfer risk through contractual or insurance arrangements.
- **Accept:** Formally accept the risk with appropriate authorization.

## 7. Risk Acceptance Criteria

For this fictional portfolio, the following **illustrative** acceptance thresholds are used and must be approved or replaced by a real organization before operational use:

| Residual risk score | Level | Illustrative decision rule |
|---|---|---|
| 1–4 | Low | May be accepted by the designated risk owner, subject to documentation. |
| 5–9 | Medium | Requires documented risk-owner rationale and Information Security review. |
| 10–16 | High | Requires documented treatment plan and explicit management approval; acceptance is not presumed. |
| 17–25 | Critical | Not acceptable by default; escalate to management for additional treatment and formal decision. |

Residual score = residual likelihood × residual impact, using the same 1–5 scales. The risk owner records the decision, rationale, approver, and review date. `Pending` means no acceptance has been granted. These thresholds are examples, not universal ISO 27001 requirements.

## 8. Residual Risk and Review

After treatment is implemented, reassess likelihood and impact, calculate the residual score and level, and document acceptance or further treatment. In this portfolio the residual likelihood, impact, score, and level in `risk-register.csv` are illustrative **target** values that assume the planned controls are implemented; they are not measured results. Acceptance remains `Pending` until a real organization reassesses residual risk with implementation evidence and records an approved decision.

## 9. Review and Approval

- **Document Owner:** IT Security
- **Approved By:** To be assigned
- **Review Frequency:** Annually and after significant changes
- **Version:** 1.0
- **Status:** Draft
