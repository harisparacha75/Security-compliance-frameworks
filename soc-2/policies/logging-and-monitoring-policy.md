# Logging and Monitoring Policy

**Document ID:** SOC2-POL-008  
**Version:** 0.1  
**Status:** Draft — Portfolio Example  
**Policy Owner:** SOC  
**Review Frequency:** Annually and after significant changes

## 1. Purpose and scope

Sets requirements for logging security-relevant events and monitoring them so anomalies and incidents are detected and evaluated.

## 2. Requirements

1. Log authentication events, privileged activity, access changes, security tool alerts, and changes to critical systems from all in-scope log sources.
2. Send logs to a central platform, synchronize clocks to approved time sources, and protect logs from alteration and unauthorized access.
3. Retain security logs for at least 12 months, with at least 90 days immediately searchable.
4. Define alert use cases mapped to threats and review them at least quarterly.
5. Triage high-severity alerts within 30 minutes and other alerts within one business day; document the outcome.
6. Monitor the log pipeline for failures and missing sources and review log source coverage at least quarterly.
7. Evaluate events against incident criteria and open an incident under the Incident Response Policy when criteria are met.

## 3. Roles and review

The policy owner maintains this policy, assigns responsibilities, and reviews it annually and after significant change. Exceptions are documented, time-limited, risk-assessed, and approved by the policy owner and IT Security.

## 4. Related criteria and documents

- SOC 2 criteria: CC7.2, CC7.3
- Related: SOC2-POL-003 Incident Response Policy; ISO-POL-006 Logging and Monitoring Policy (ISO folder)

## 5. Approval

Approver: TBD · Approval date: TBD

---
**Disclaimer:** Illustrative draft; not approved or evidence of SOC 2 compliance. Numeric values are example values for a fictional organization.
