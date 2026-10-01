# Changelog

## Repository consistency cleanup

- **README:** Updated the project-status summary and repository tree to match the current repository contents; removed the outdated reference to seven ISO procedures and standards.
- **SOC 2:** Clarified that the current matrix contains 36 criteria: 33 Security criteria and 3 Availability criteria.
- **References:** Removed stale ISO procedure references from the root README and aligned the current project-status counts with the repository contents.

## Completeness, consistency, and validation update

- **Statement of Applicability:** decided all 93 Annex A controls (76 applicable, 17 excluded with rationale); none remain pending. Reconciled the control register (76 rows) and evidence register (ISO-EV-001 to ISO-EV-076) with the SoA.
- **Risk register:** expanded from 12 to 19 risks, adding continuity, insider misuse, legal and privacy compliance, equipment loss, supplier-managed facility, cryptography, and incident handling. Filled illustrative target residual values, added asset links, and regenerated the treatment plan from the register so text cannot drift.
- **Asset inventory:** grew from 7 to 15 assets, adding information assets, and linked each asset to risks.
- **Procedures and standards:** replaced seven boilerplate stubs with real draft content (recovery tiers, remediation targets, classification handling, identity lifecycle timings, supplier tiers). Moved the backup policy to `policies/` as ISO-POL-007.
- **Document IDs:** resolved the ISO-POL-002 collision and adopted one scheme (`ISO-POL`, `ISO-STD`, `ISO-PROC`, `ISO-PLAN`, `ISO-GOV`).
- **Governance (clauses 4–10):** added a clause-to-document map and ISMS roles, completed the context register, set objective targets, and replaced the placeholder corrective-action row with clearly marked worked examples.
- **SOC 2:** rebuilt the matrix and evidence register for all 36 Security and Availability criteria in criterion order, corrected CC6.5, and removed out-of-scope C1.1, PI1.1, and P1.1 rows. Added eight policies (vendor, continuity and recovery, vulnerability, logging and monitoring, encryption, physical security, risk, code of conduct).
- **Crosswalk:** now covers all 36 criteria (78 relationships, 156 rows), using management-system clauses where no Annex A control applies.
- **Documentation:** corrected counts, scope wording, structure trees, and typos across READMEs; removed `.gitkeep` files.
- **Validation:** added `scripts/validate_repo.py` and a GitHub Actions workflow that checks IDs, counts, cross-references, and links.

## Earlier updates

- Corrected SOC 2 criteria references (CC5.2 and CC5.3 were transposed); fixed duplicate section numbering in the risk assessment methodology and duplicated header fields in the ISO access control policy.
- Made scope and exclusions consistent: product engineering is out of scope, so A.8.25–A.8.31 carry sample exclusions.
- Added Annex A mappings, risk owners, inherent risk levels, residual-risk fields, and illustrative risk acceptance criteria.
- Added evidence references and namespaced evidence IDs as `ISO-EV-###` and `SOC2-EV-###`.
- Added authentication and logging policies, a fictional ISMS scope, an illustrative ISO/SOC 2 crosswalk, usable register templates, `LICENSE`, `.gitignore`, and `SECURITY.md`.
- Corrected README wording and code-fence formatting.

**Important:** This is still an educational sample. `Planned` does not indicate implemented controls or compliance. The fictional scope, risk ratings, exclusions, evidence descriptions, policy content, and mappings require validation before operational use.
