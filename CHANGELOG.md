# Changelog

## Accuracy and consistency corrections

- Corrected SOC 2 criteria references: CC5.2 (general control activities over technology) and CC5.3 (policies and procedures) were transposed in the control matrix and evidence register.
- Fixed duplicate section numbering in the risk assessment methodology and duplicated header fields in the ISO access control policy.
- Aligned SoA counts across READMEs: 93 controls listed; 32 with illustrative decisions (22 applicable, 10 excluded); 61 pending assessment.
- Made scope and exclusions consistent: product engineering is out of scope, so A.8.25–A.8.31 carry sample exclusions; building-level physical controls stay pending as a supplier dependency. Removed the A.8.34 exclusion and reworded A.7.11.
- Added A.5.1, A.5.10, A.8.2, A.5.23, A.8.20, and A.8.22 as applicable (Planned) with control-register and evidence entries (ISO-EV-017 to ISO-EV-022); updated risk mappings for RISK-001, 003, 006, and 007 and the treatment plan to match.

## Portfolio consistency and traceability update

- Added Annex A mappings, risk owners, inherent risk levels, residual-risk fields, and illustrative risk acceptance criteria.
- Aligned the risk treatment plan with the risk register and differentiated the cloud-access and information-classification risks.
- Expanded the SoA register to list all 93 Annex A controls; unreviewed entries are explicitly marked `Pending assessment`, not presumed applicable or excluded. Added sample exclusion rationales.
- Added evidence references for selected ISO controls and namespaced ISO evidence IDs as `ISO-EV-###`.
- Added authentication and logging policies, defined a fictional ISMS scope, and completed incident-response policy metadata/disclaimer.
- Expanded the SOC 2 sample matrix to include CC4, CC5, and Availability criteria A1.1–A1.3, including backup and recovery testing examples. Namespaced evidence IDs as `SOC2-EV-###`.
- Added an illustrative ISO/SOC 2 crosswalk, usable register templates, `LICENSE`, `.gitignore`, and `SECURITY.md`; removed placeholder `.gitkeep` files.
- Corrected README wording and code-fence formatting.

**Important:** This is still an educational sample. `Planned` and `Pending assessment` do not indicate implemented controls or compliance. The fictional scope, risk ratings, exclusions, evidence descriptions, policy content, and mappings require validation before operational use.
