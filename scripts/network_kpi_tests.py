import csv
import sys
from pathlib import Path

CSV_PATH = Path("data/sample_kpis.csv")
REPORT_PATH = Path("report.md")

THRESHOLDS = {
    "4G": {"lat_max": 90.0, "thr_min": 50.0, "loss_max": 1.0},
    "5G": {"lat_max": 50.0, "thr_min": 150.0, "loss_max": 0.6},
}

def main():
    if not CSV_PATH.exists():
        print("Missing data file:", CSV_PATH)
        return 2

    failures = []
    summary = {"4G": {"n": 0, "fail": 0}, "5G": {"n": 0, "fail": 0}}

    with CSV_PATH.open() as f:
        reader = csv.DictReader(f)
        for r in reader:
            tech = r["tech"]
            users = int(r["users"])
            lat = float(r["latency_ms"])
            thr = float(r["throughput_mbps"])
            loss = float(r["packet_loss_pct"])

            summary[tech]["n"] += 1
            t = THRESHOLDS[tech]
            reasons = []

            if lat > t["lat_max"]:
                reasons.append("latency {}ms > {}ms".format(lat, t["lat_max"]))
            if thr < t["thr_min"]:
                reasons.append("throughput {}Mbps < {}Mbps".format(thr, t["thr_min"]))
            if loss > t["loss_max"]:
                reasons.append("packet_loss {}% > {}%".format(loss, t["loss_max"]))

            if reasons:
                summary[tech]["fail"] += 1
                failures.append((tech, users, "; ".join(reasons)))

    lines = []
    lines.append("# Network KPI Test Report (Simulated)\n\n")
    lines.append("Data source: `{}`\n\n".format(CSV_PATH))
    lines.append("## Summary\n")
    lines.append("- 4G: {} samples, {} failing\n".format(summary["4G"]["n"], summary["4G"]["fail"]))
    lines.append("- 5G: {} samples, {} failing\n\n".format(summary["5G"]["n"], summary["5G"]["fail"]))

    lines.append("## Thresholds\n")
    lines.append("- 4G: latency<= {}ms, throughput>= {}Mbps, loss<= {}%\n".format(
        THRESHOLDS["4G"]["lat_max"], THRESHOLDS["4G"]["thr_min"], THRESHOLDS["4G"]["loss_max"]
    ))
    lines.append("- 5G: latency<= {}ms, throughput>= {}Mbps, loss<= {}%\n\n".format(
        THRESHOLDS["5G"]["lat_max"], THRESHOLDS["5G"]["thr_min"], THRESHOLDS["5G"]["loss_max"]
    ))

    lines.append("## Failures\n")
    if failures:
        for tech, users, reason in failures:
            lines.append("- {} @ {} users: {}\n".format(tech, users, reason))
    else:
        lines.append("- None\n")

    REPORT_PATH.write_text("".join(lines))
    print("Report written to", REPORT_PATH)
    return 0

if __name__ == "__main__":
    sys.exit(main())
