"""Fail the pipeline when Bandit reports a High-severity finding."""
import json
import sys
from pathlib import Path


def main() -> int:
    report_path = Path(sys.argv[1] if len(sys.argv) > 1 else "bandit-report.json")
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Quality Gate gagal: laporan Bandit tidak dapat dibaca: {error}")
        return 2

    findings = report.get("results", [])
    high_findings = [
        finding for finding in findings
        if str(finding.get("issue_severity", "")).upper() == "HIGH"
    ]

    print(f"Total temuan Bandit: {len(findings)}")
    print(f"Temuan severity HIGH: {len(high_findings)}")
    if high_findings:
        for finding in high_findings:
            print(
                f"- {finding.get('filename')}:{finding.get('line_number')} "
                f"{finding.get('test_id')} — {finding.get('issue_text')}"
            )
        print("QUALITY GATE: FAIL")
        return 1

    print("QUALITY GATE: PASS (tidak ada temuan severity HIGH)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
