#!/usr/bin/env python3
"""Phân tích & ẩn danh hóa kết quả khảo sát lớp (Nhóm 3MV · Track E · E3).

Chạy tái lập ngoại tuyến (0 thư viện ngoài):
    python3 evidence/survey/analyze_survey.py

Nhập file thô từ Google Forms (tự xoá cột 8 liên hệ, bỏ dòng trống, chỉ giữ ngày, kiểm 0 SĐT/email):
    python3 evidence/survey/analyze_survey.py --ingest /path/to/raw.csv
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

SURVEY_DIR = Path(__file__).resolve().parent
RESULTS_CSV = SURVEY_DIR / "results.csv"

PHONE_RE = re.compile(r"(?<!\d)(?:\+?84|0)(?:3|5|7|8|9)\d{8}(?!\d)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

CLEAN_HEADERS = [
    "respondent_id",
    "date",
    "q1_apps",
    "q2_scenarios",
    "q3_wait_time",
    "q4_support_exp",
    "q5_faceid_safe",
    "q6_freq_3m",
    "q7_story",
]

Q2_ITEMS = [
    ("scam_coercion", "Bị gọi/nhắn giục chuyển tiền gấp (công an, thuế...)"),
    ("urgent_blocked", "Đang cần gấp (viện phí, tại quầy) thì app chặn/treo"),
    ("unauth_ato", "Thấy trừ tiền lạ hoặc nghi tài khoản bị truy cập"),
    ("never", "Chưa từng gặp tình huống nào ở trên"),
]

Q4_ITEMS = [
    ("fast_ok", "Xử lý nhanh, đúng vấn đề"),
    ("rigid_bot", "Bot menu cứng / vòng vo, không đúng tình huống"),
    ("slow_ticket", "Phải gửi ticket chờ lâu trong khi đang cần gấp"),
    ("busy_after_20h", "Tổng đài bận / sau 20h khó gặp người thật"),
    ("never_contacted", "Chưa từng liên hệ hỗ trợ"),
]


def _sanitize_text(text: str) -> str:
    cleaned = PHONE_RE.sub("[ĐÃ_ẨN_SĐT]", text or "")
    cleaned = EMAIL_RE.sub("[ĐÃ_ẨN_EMAIL]", cleaned)
    return " ".join(cleaned.split())


def ingest_raw(raw_path: Path) -> tuple[int, int]:
    rows = []
    skipped_blank = 0
    with raw_path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header or len(header) < 8:
            raise ValueError("File CSV thô không đủ cột khảo sát (cần ≥8 cột).")
        for raw in reader:
            padded = list(raw) + [""] * (9 - len(raw))
            answers = [c.strip() for c in padded[1:7]]
            if not any(answers):
                skipped_blank += 1
                continue
            date_only = (padded[0].strip().split(" ")[0] if padded[0].strip() else "")
            rows.append(
                {
                    "respondent_id": f"S{len(rows) + 1:02d}",
                    "date": date_only,
                    "q1_apps": _sanitize_text(padded[1]),
                    "q2_scenarios": _sanitize_text(padded[2]),
                    "q3_wait_time": _sanitize_text(padded[3]),
                    "q4_support_exp": _sanitize_text(padded[4]),
                    "q5_faceid_safe": _sanitize_text(padded[5]),
                    "q6_freq_3m": _sanitize_text(padded[6]),
                    "q7_story": _sanitize_text(padded[7]),
                }
            )

    with RESULTS_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CLEAN_HEADERS)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows), skipped_blank


def load_clean_rows() -> list[dict]:
    with RESULTS_CSV.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def pct(x: int, n: int) -> str:
    return f"{(100.0 * x / n):.1f}%" if n else "0.0%"


def report(rows: list[dict]) -> None:
    n = len(rows)
    print(f"=== K5 3MV Class Survey Report (n = {n} valid responses) ===")

    # Privacy check
    full_blob = "\n".join(" ".join(r.values()) for r in rows)
    phones = PHONE_RE.findall(full_blob)
    emails = EMAIL_RE.findall(full_blob)
    print(f"Privacy check: phones={len(phones)}, emails={len(emails)}")

    # Q1: Apps
    print("\n[Q1] Ứng dụng dùng thường xuyên (chọn nhiều):")
    for label in ("App ngân hàng (VCB/MB/TCB/BIDV...)", "MoMo", "ZaloPay", "Khác"):
        c = sum(1 for r in rows if label in r["q1_apps"])
        print(f"  - {label:36s}: {c:2d}/{n} ({pct(c, n)})")

    # Q2: E3 scenarios (note: 1 respondent selected both scam + never; count actual E3 pain explicitly)
    print("\n[Q2] Tình huống E3 gặp trong 6 tháng qua (chọn nhiều):")
    any_e3 = 0
    for _, label in Q2_ITEMS:
        c = sum(1 for r in rows if label in r["q2_scenarios"])
        print(f"  - {label:55s}: {c:2d}/{n} ({pct(c, n)})")
    for r in rows:
        if any(lbl in r["q2_scenarios"] for key, lbl in Q2_ITEMS if key != "never"):
            any_e3 += 1
    print(f"  => Ít nhất 1 tình huống E3 (lừa đảo / chặn gấp / trừ tiền lạ): {any_e3}/{n} ({pct(any_e3, n)})")

    # Q3: Wait time
    print("\n[Q3] Thời gian xử lý / biết cần làm gì:")
    q3_counts = Counter(r["q3_wait_time"] for r in rows)
    for k, v in q3_counts.most_common():
        print(f"  - {k:36s}: {v:2d}/{n} ({pct(v, n)})")
    over_5m = sum(v for k, v in q3_counts.items() if k in {"5-15 phút", "15-30 phút", "Trên 30 phút / chờ tới hôm sau"})
    experienced = sum(v for k, v in q3_counts.items() if k != "Chưa từng gặp")
    print(f"  => Mất >= 5 phút: {over_5m}/{n} ({pct(over_5m, n)}) tổng mẫu | {over_5m}/{experienced} ({pct(over_5m, experienced)}) nhóm từng xử lý")

    # Q4: Support experience
    print("\n[Q4] Trải nghiệm Chat hỗ trợ / tổng đài (chọn nhiều):")
    any_friction = 0
    contacted = 0
    for _, label in Q4_ITEMS:
        c = sum(1 for r in rows if label in r["q4_support_exp"])
        print(f"  - {label:55s}: {c:2d}/{n} ({pct(c, n)})")
    for r in rows:
        s = r["q4_support_exp"]
        has_fric = any(lbl in s for key, lbl in Q4_ITEMS if key in {"rigid_bot", "slow_ticket", "busy_after_20h"})
        if has_fric:
            any_friction += 1
        if s and s != "Chưa từng liên hệ hỗ trợ":
            contacted += 1
    print(f"  => Gặp ít nhất 1 vướng mắc CSKH/bot: {any_friction}/{n} ({pct(any_friction, n)}) tổng | {any_friction}/{contacted} ({pct(any_friction, contacted)}) nhóm từng liên hệ")

    # Q5: Face ID paradox
    print("\n[Q5] Nghịch lý sinh trắc học (Face ID thành công có chắc chắn an toàn?):")
    q5_counts = Counter(r["q5_faceid_safe"] for r in rows)
    for k, v in q5_counts.most_common():
        print(f"  - {k:58s}: {v:2d}/{n} ({pct(v, n)})")

    # Q6: Frequency in 3 months (for cost/personas.yaml)
    print("\n[Q6] Tần suất 3 tháng qua (cơ sở cost/personas.yaml):")
    q6_counts = Counter(r["q6_freq_3m"] for r in rows)
    for k, v in q6_counts.most_common():
        print(f"  - {k:30s}: {v:2d}/{n} ({pct(v, n)})")

    # Q7: Real stories
    print("\n[Q7] Trích dẫn thực tế (không trống / không phải 'không'):")
    skip_words = {"", "không", "ko có", "chưa có", "chưa từng bị", "không nhớ"}
    for r in rows:
        story = r["q7_story"].strip()
        if story.lower() not in skip_words:
            print(f"  - [{r['respondent_id']}]: \"{story}\"")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ingest", type=Path, help="Đường dẫn file CSV thô từ Google Forms")
    args = parser.parse_args()
    if args.ingest:
        kept, skipped = ingest_raw(args.ingest)
        print(f"Đã ẩn danh hóa {kept} phiếu hợp lệ (bỏ {skipped} dòng trống, xoá hoàn toàn cột 8) -> {RESULTS_CSV.name}\n")
    rows = load_clean_rows()
    report(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
