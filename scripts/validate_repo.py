#!/usr/bin/env python3
"""Consistency checks for the Security-compliance-frameworks portfolio.

Standard library only. Exit code 0 = all checks passed, 1 = at least one failure.
Run from anywhere:  python3 scripts/validate_repo.py
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISO = ROOT / "iso-27001"
SOC = ROOT / "soc-2"
errors = []


def err(msg):
    errors.append(msg)


def rel(p):
    return str(Path(p).relative_to(ROOT))


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        err(f"{rel(path)}: empty file")
        return [], []
    header, body = rows[0], rows[1:]
    for n, r in enumerate(body, 2):
        if len(r) != len(header):
            err(f"{rel(path)} line {n}: {len(r)} columns, expected {len(header)}")
    return header, [dict(zip(header, r)) for r in body if len(r) == len(header)]


def text(path):
    return Path(path).read_text(encoding="utf-8")


OWNERS = {"IT Security", "IT Operations", "SOC", "HR", "Legal/Compliance",
          "Vendor Management", "Management", "Service Owner"}


def check_owner(where, value):
    for o in re.split(r"\s*;\s*", value.strip()):
        if o not in OWNERS:
            err(f"{where}: unknown owner '{o}'")


# ---------------------------------------------------------------- expected IDs
EXPECTED_CONTROLS = ([f"A.5.{n}" for n in range(1, 38)] + [f"A.6.{n}" for n in range(1, 9)]
                     + [f"A.7.{n}" for n in range(1, 15)] + [f"A.8.{n}" for n in range(1, 35)])
EXPECTED_CRITERIA = ([f"CC1.{n}" for n in range(1, 6)] + [f"CC2.{n}" for n in range(1, 4)]
                     + [f"CC3.{n}" for n in range(1, 5)] + [f"CC4.{n}" for n in range(1, 3)]
                     + [f"CC5.{n}" for n in range(1, 4)] + [f"CC6.{n}" for n in range(1, 9)]
                     + [f"CC7.{n}" for n in range(1, 6)] + ["CC8.1"] + [f"CC9.{n}" for n in range(1, 3)]
                     + [f"A1.{n}" for n in range(1, 4)])


def level(score):
    return "Low" if score <= 4 else "Medium" if score <= 9 else "High" if score <= 16 else "Critical"


# ---------------------------------------------------------------- repo hygiene
def check_hygiene():
    for name in ("LICENSE", "SECURITY.md", ".gitignore", "CHANGELOG.md", "README.md"):
        if not (ROOT / name).exists():
            err(f"missing {name}")
    for p in ROOT.rglob(".gitkeep"):
        err(f"{rel(p)}: placeholder .gitkeep should not exist")
    for p in ROOT.rglob("*.csv"):
        if ".git" in p.parts:
            continue
        header, rows = read_csv(p)
        if p.parent.name == "templates":
            if rows:
                err(f"{rel(p)}: templates must contain headers only")
            continue
        for n, r in enumerate(rows, 2):
            for k, v in r.items():
                if v.strip() == "":
                    err(f"{rel(p)} line {n}: empty cell in '{k}'")
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        t = text(p)
        if sum(1 for line in t.splitlines() if line.strip().startswith("```")) % 2:
            err(f"{rel(p)}: unbalanced code fence")
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", t):
            target = m.group(1).split("#")[0]
            if not target or re.match(r"^(https?:|mailto:)", target):
                continue
            if not (p.parent / target).resolve().exists():
                err(f"{rel(p)}: broken link {target}")


# ---------------------------------------------------------------- document IDs
ID_PREFIX_BY_DIR = {
    ("iso-27001", "policies"): ["ISO-POL"],
    ("iso-27001", "procedures"): ["ISO-STD", "ISO-PROC", "ISO-PLAN"],
    ("iso-27001", "governance"): ["ISO-GOV"],
    ("soc-2", "policies"): ["SOC2-POL"],
}


def check_document_ids():
    seen = {}
    by_prefix = {}
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts or p.name == "README.md":
            continue
        head = "\n".join(text(p).splitlines()[:12])
        m = re.search(r"\*\*Document ID:\*\*\s*([A-Z0-9]+(?:-[A-Z0-9]+)*-(\d{3}))", head)
        parts = p.relative_to(ROOT).parts
        expected = ID_PREFIX_BY_DIR.get(parts[:2])
        if not m:
            if expected or p.name in ("isms-scope.md", "system-description.md"):
                err(f"{rel(p)}: missing Document ID")
            continue
        did = m.group(1)
        if did in seen:
            err(f"duplicate Document ID {did}: {rel(p)} and {seen[did]}")
        seen[did] = rel(p)
        prefix = did.rsplit("-", 1)[0]
        by_prefix.setdefault(prefix, []).append(int(m.group(2)))
        if expected and prefix not in expected:
            err(f"{rel(p)}: ID {did} does not match folder (expected {expected})")
        for field in ("Version", "Status"):
            if f"**{field}:**" not in head:
                err(f"{rel(p)}: missing {field} line")
        if not re.search(r"\*\*(Policy )?Owner:\*\*", head):
            err(f"{rel(p)}: missing Owner line")
        if not re.search(r"\*\*Review (Cycle|Frequency):\*\*", head):
            err(f"{rel(p)}: missing Review line")
        first = head.splitlines()
        for line in first:
            if line.startswith("**Document ID:**") and not line.endswith("  "):
                err(f"{rel(p)}: Document ID line lacks trailing double space")
    for prefix, nums in by_prefix.items():
        if sorted(nums) != list(range(1, len(nums) + 1)):
            err(f"Document IDs for {prefix} are not sequential from 001: {sorted(nums)}")
    # every policy-like file listed in the SOC 2 policy README
    pol_readme = text(SOC / "policies" / "README.md")
    for p in (SOC / "policies").glob("*.md"):
        if p.name != "README.md" and p.name not in pol_readme:
            err(f"soc-2/policies/README.md does not list {p.name}")


# ---------------------------------------------------------------- ISO registers
def check_iso():
    _, soa = read_csv(ISO / "statement-of-applicability" / "soa-register.csv")
    ids = [r["Control ID"] for r in soa]
    if ids != EXPECTED_CONTROLS:
        err(f"SoA control list differs from Annex A 2022 (93 controls expected, found {len(ids)})")
    yes = {r["Control ID"] for r in soa if r["Applicable"] == "Yes"}
    no = {r["Control ID"] for r in soa if r["Applicable"] == "No"}
    for r in soa:
        c = r["Control ID"]
        if r["Applicable"] not in ("Yes", "No"):
            err(f"SoA {c}: Applicable must be Yes or No, found '{r['Applicable']}'")
        elif r["Applicable"] == "Yes" and r["Implementation Status"] != "Planned":
            err(f"SoA {c}: applicable control must be Planned")
        elif r["Applicable"] == "No" and r["Implementation Status"] != "Not applicable (illustrative)":
            err(f"SoA {c}: excluded control has wrong status")
        if len(r["Justification"]) < 40:
            err(f"SoA {c}: justification too short")

    _, ctl = read_csv(ISO / "control-implementation" / "control-register.csv")
    ctl_ids = [r["Control ID"] for r in ctl]
    if set(ctl_ids) != yes:
        err("control register does not match SoA applicable controls: "
            f"missing {sorted(yes - set(ctl_ids))}, extra {sorted(set(ctl_ids) - yes)}")
    if len(ctl_ids) != len(set(ctl_ids)):
        err("control register has duplicate control IDs")
    for r in ctl:
        check_owner(f"control register {r['Control ID']}", r["Control Owner"])

    _, ev = read_csv(ISO / "evidence" / "evidence-register.csv")
    ev_ids = [r["Evidence ID"] for r in ev]
    if ev_ids != [f"ISO-EV-{n:03d}" for n in range(1, len(ev) + 1)]:
        err("ISO evidence IDs are not unique and sequential from ISO-EV-001")
    ev_by_id = {r["Evidence ID"]: r for r in ev}
    covered = set()
    for r in ev:
        if r["Control ID"] not in yes:
            err(f"evidence {r['Evidence ID']} points to control {r['Control ID']} that is not applicable in the SoA")
        covered.add(r["Control ID"])
        check_owner(f"evidence {r['Evidence ID']}", r["Owner"])
    for c in sorted(yes - covered):
        err(f"applicable control {c} has no evidence entry")
    soa_ref = {r["Control ID"]: r["Evidence Reference"] for r in soa if r["Applicable"] == "Yes"}
    for r in ctl:
        c = r["Control ID"]
        if soa_ref.get(c) != r["Evidence"]:
            err(f"{c}: SoA evidence reference '{soa_ref.get(c)}' differs from control register '{r['Evidence']}'")
        e = ev_by_id.get(r["Evidence"])
        if not e or e["Control ID"] != c:
            err(f"{c}: evidence {r['Evidence']} missing or linked to a different control")

    # risks
    _, risks = read_csv(ISO / "risk-assessment" / "risk-register.csv")
    _, assets = read_csv(ISO / "asset-inventory.csv")
    asset_ids = {a["Asset ID"] for a in assets}
    risk_ids = [r["Risk ID"] for r in risks]
    if risk_ids != [f"RISK-{n:03d}" for n in range(1, len(risks) + 1)]:
        err("risk IDs are not sequential from RISK-001")
    for r in risks:
        i = r["Risk ID"]
        try:
            L, I = int(r["Likelihood (1-5)"]), int(r["Impact (1-5)"])
            rL, rI = int(r["Residual Likelihood (1-5)"]), int(r["Residual Impact (1-5)"])
            for v in (L, I, rL, rI):
                if not 1 <= v <= 5:
                    err(f"{i}: scale value out of range")
            if int(r["Inherent Risk Score"]) != L * I or r["Inherent Risk Level"] != level(L * I):
                err(f"{i}: inherent score or level is wrong")
            if int(r["Residual Risk Score"]) != rL * rI or r["Residual Risk Level"] != level(rL * rI):
                err(f"{i}: residual score or level is wrong")
            if rL * rI > L * I:
                err(f"{i}: residual risk exceeds inherent risk")
        except ValueError:
            err(f"{i}: non-numeric score field")
        if r["Risk Treatment"] not in ("Mitigate", "Avoid", "Transfer", "Accept"):
            err(f"{i}: invalid treatment '{r['Risk Treatment']}'")
        if r["Risk Acceptance Decision"] != "Pending":
            err(f"{i}: acceptance decision must stay Pending until approved")
        check_owner(i, r["Risk Owner"])
        for c in re.split(r"\s*;\s*", r["Annex A Control Mapping"]):
            if c not in yes:
                err(f"{i}: mapped control {c} is not applicable in the SoA")
        for a in re.split(r"\s*;\s*", r["Asset IDs"]):
            if a not in asset_ids:
                err(f"{i}: unknown asset {a}")
    for a in assets:
        check_owner(a["Asset ID"], a["Owner"])
        linked = {x for x in re.split(r"\s*;\s*", a["Linked Risks"]) if x}
        expected = {r["Risk ID"] for r in risks if a["Asset ID"] in re.split(r"\s*;\s*", r["Asset IDs"])}
        if linked != expected:
            err(f"{a['Asset ID']}: Linked Risks {sorted(linked)} differ from risk register {sorted(expected)}")

    # every applicable control is cited by risk, mapping, or an explicit rationale elsewhere: report only coverage of risks
    # treatment plan
    tp = text(ISO / "risk-assessment" / "risk-treatment-plan.md")
    m = re.search(r"covers all (\d+) sample risks", tp)
    if not m or int(m.group(1)) != len(risks):
        err(f"treatment plan intro does not state {len(risks)} risks")
    plan = {}
    for line in tp.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| RISK-") and len(cells) == 8:
            plan[cells[0]] = cells
    if set(plan) != set(risk_ids):
        err(f"treatment plan lists {sorted(set(plan))} but register has {len(risk_ids)} risks")
    for r in risks:
        c = plan.get(r["Risk ID"])
        if c and (c[1], c[2], c[3], c[4], c[5]) != (r["Risk Title"], r["Risk Treatment"],
                                                  r["Annex A Control Mapping"], r["Planned Controls"], r["Risk Owner"]):
            err(f"{r['Risk ID']}: treatment plan row differs from risk register")

    # README counts
    n_yes, n_no = len(yes), len(no)
    for f in ("README.md", "iso-27001/README.md", "iso-27001/statement-of-applicability/README.md"):
        t = text(ROOT / f)
        for num, word in re.findall(r"\b(\d+)\s+(?:are\s+)?(applicable|excluded|pending)", t):
            want = {"applicable": n_yes, "excluded": n_no, "pending": 0}[word]
            if int(num) != want:
                err(f"{f}: states {num} {word}, SoA has {want}")
        if not re.search(rf"\b{n_yes}\s+(?:are\s+)?applicable", t):
            err(f"{f}: does not state {n_yes} applicable controls")
        if not re.search(rf"\b{n_no}\s+(?:are\s+)?excluded", t):
            err(f"{f}: does not state {n_no} excluded controls")
    for f in ("README.md", "iso-27001/README.md"):
        t = text(ROOT / f)
        for num in re.findall(r"\b(\d+) risks\b", t):
            if int(num) != len(risks):
                err(f"{f}: states {num} risks, register has {len(risks)}")
    if re.search(r"\bPending assessment\b", text(ISO / "isms-scope.md")):
        err("isms-scope.md still refers to Pending assessment")
    return yes


# ---------------------------------------------------------------- SOC 2
def check_soc2():
    _, matrix = read_csv(SOC / "control-matrix" / "control-matrix.csv")
    ids = [r["Control ID"] for r in matrix]
    if ids != EXPECTED_CRITERIA:
        err(f"SOC 2 matrix rows must be the 36 Security and Availability criteria in order; found {ids}")
    _, ev = read_csv(SOC / "evidence" / "evidence-register.csv")
    ev_ids = [r["Evidence ID"] for r in ev]
    if ev_ids != [f"SOC2-EV-{n:03d}" for n in range(1, len(ev) + 1)]:
        err("SOC 2 evidence IDs are not unique and sequential")
    by_ctl = {}
    for r in ev:
        by_ctl.setdefault(r["Control ID"], []).append(r)
        check_owner(r["Evidence ID"], r["Owner"])
    for r in matrix:
        c = r["Control ID"]
        check_owner(c, r["Owner"])
        want_cat = "Availability" if c.startswith("A1") else "Security"
        if r["Trust Services Category"] != want_cat:
            err(f"{c}: category should be {want_cat}")
        m = re.match(r"(SOC2-EV-\d{3}) — (.+)$", r["Evidence"])
        if not m:
            err(f"{c}: evidence column format")
            continue
        e = [x for x in by_ctl.get(c, []) if x["Evidence ID"] == m.group(1)]
        if not e or e[0]["Evidence Description"] != m.group(2):
            err(f"{c}: matrix evidence does not match evidence register")
    for c in by_ctl:
        if c not in ids:
            err(f"SOC 2 evidence references criterion {c} that is not in the matrix")
    # CC6.5 content guard (disposal / sanitization, not environmental protection)
    cc65 = next((r for r in matrix if r["Control ID"] == "CC6.5"), None)
    if cc65 and not re.search(r"dispos|sanitiz|discontinu", cc65["Control Objective"] + cc65["Sample Control Activity"], re.I):
        err("CC6.5 description must be about discontinuing protections and disposal")
    trust = text(SOC / "trust-services-criteria" / "README.md") + text(SOC / "control-matrix" / "README.md") + text(SOC / "README.md")
    if re.search(r"does not cover all|selected sample|selected criteria", trust, re.I):
        err("SOC 2 READMEs still describe the matrix as a partial sample")
    if re.search(r"\ban planning\b", trust):
        err("typo 'an planning' present")


# ---------------------------------------------------------------- crosswalk
def check_crosswalk(yes):
    _, rows = read_csv(ROOT / "control-mapping" / "iso27001-soc2-crosswalk.csv")
    fwd, back = set(), set()
    for r in rows:
        if r["Direction"] == "ISO-to-SOC2":
            iso_ref, crit = r["Source Control"], r["Target Criterion"]
            fwd.add((iso_ref, crit))
        elif r["Direction"] == "SOC2-to-ISO":
            iso_ref, crit = r["Target Criterion"], r["Source Control"]
            back.add((iso_ref, crit))
        else:
            err(f"crosswalk: bad direction {r['Direction']}")
            continue
        m = re.match(r"(A\.\d+\.\d+)\b", iso_ref)
        if m and m.group(1) not in yes:
            err(f"crosswalk: {m.group(1)} is not applicable in the SoA")
        elif not m and not iso_ref.startswith("Clause "):
            err(f"crosswalk: unrecognized ISO reference '{iso_ref}'")
        if crit not in EXPECTED_CRITERIA:
            err(f"crosswalk: unknown criterion {crit}")
    if fwd != back:
        err(f"crosswalk directions are not mirrored: {sorted(fwd ^ back)[:5]}")
    covered = {c for _, c in fwd}
    missing = [c for c in EXPECTED_CRITERIA if c not in covered]
    if missing:
        err(f"crosswalk does not cover criteria: {missing}")
    t = text(ROOT / "README.md")
    m = re.search(r"(\d+) illustrative ISO/IEC 27001 to SOC 2 relationships \((\d+) rows", t)
    if not m or int(m.group(1)) != len(fwd) or int(m.group(2)) != len(rows):
        err(f"README crosswalk counts do not match ({len(fwd)} relationships, {len(rows)} rows)")


def main():
    check_hygiene()
    check_document_ids()
    yes = check_iso()
    check_soc2()
    check_crosswalk(yes)
    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
