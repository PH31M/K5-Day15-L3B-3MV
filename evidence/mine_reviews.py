#!/usr/bin/env python3
"""Reproducible public App Store (VN) review miner for Track E (E3) pain evidence.

Data Contract (locked BEFORE final counting):
- Source: Apple App Store Vietnam public RSS review feeds (no login, Python stdlib only)
  - MoMo (id=918751511)
  - ZaloPay (id=1112407590)
  - VCB Digibank (id=561433133)
  - MB Bank (id=1205807363)
  - Techcombank Mobile (id=1548623362)
- Sampling: Most recent RSS page(s) per app, ALL star ratings included.
- Denominator (N): Total unique readable reviews collected across all 5 apps.
- Codebook refined after reading first 30 rows (guide §1.2) to avoid false positives on 5★ feature requests:
  only tag complaints (rating <= 3) matching concrete operational keywords.
- Privacy: Reviewer names & URLs are NEVER saved; quotes truncated to <= 2 sentences.

Usage:
    python3 evidence/mine_reviews.py          # fetch live + save anonymized CSV & print report
    python3 evidence/mine_reviews.py --recount  # recount offline from saved anonymized CSV
"""

import argparse
import csv
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

APPS = [
    ("MoMo", "918751511"),
    ("ZaloPay", "1112407590"),
    ("VCB_Digibank", "561433133"),
    ("MB_Bank", "1205807363"),
    ("BIDV_SmartBanking", "1061867449"),
]

THEMES = [
    (
        "blocked_or_failed_tx",
        "Giao dịch bị chặn/khóa/treo, không chuyển được tiền hoặc trừ tiền nhưng không tới",
        re.compile(
            r"(bị khóa|bị khoá|khóa tài khoản|khoá tài khoản|tạm chặn|bị chặn|tạm giữ|treo tiền|"
            r"treo giao dịch|không chuyển được|ko chuyển được|k chuyển tiền|bị giữ tiền|đóng băng|"
            r"lỗi chuyển tiền|trừ tiền.*không nhận|báo lỗi.*vẫn trừ|vẫn bị trừ tiền|hạn chế giao dịch|"
            r"lỗi.*sinh trắc|sinh trắc.*lỗi|quét khuôn mặt.*lỗi|xác thực.*không được)",
            re.I,
        ),
    ),
    (
        "support_slow_or_loop",
        "Hỗ trợ / tổng đài / CSKH chậm, không gặp được người thật hoặc ticket không phản hồi",
        re.compile(
            r"(cskh|tổng đài|tổng tài|chăm sóc khách|nhân viên tư vấn|nhân viên hỗ trợ|"
            r"ticket hỗ trợ|không hỗ trợ|ko hỗ trợ|không ai hỗ trợ|ko ai hỗ trợ|không giải quyết|"
            r"gọi.*không nghe|gọi.*ko đc|gọi.*không được|bận suốt|trả lời.*chậm|phản hồi.*chậm|"
            r"khiếu nại|bot.*trả lời|trợ lý ảo|tra soát)",
            re.I,
        ),
    ),
    (
        "unauth_or_security_risk",
        "Trừ tiền lạ / bị chiếm tài khoản / lo ngại bảo mật giao dịch (loại trừ phàn nàn phí dịch vụ)",
        re.compile(
            r"(bị hack|chiếm tài khoản|trừ tiền lạ|tự động trừ|bị trừ tiền|mất tiền oan|"
            r"mất sạch|gian lận|mạo danh|không bảo mật|xoá.*vẫn trừ|xóa.*vẫn trừ)",
            re.I,
        ),
    ),
]

OUT_CSV = Path(__file__).resolve().parent / "reviews_sample_anonymized.csv"


def trim_two_sentences(text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", clean)
    clipped = " ".join(parts[:2]).strip()
    if len(clipped) > 260:
        clipped = clipped[:257].rstrip() + "..."
    return clipped


def fetch_app_reviews(app_name: str, app_id: str, pages: int = 3) -> list[dict]:
    rows = []
    seen = set()
    for page in range(1, pages + 1):
        url = f"https://itunes.apple.com/vn/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"
        req = urllib.request.Request(url, headers={"User-Agent": "K5-3MV-EvidenceMiner/1.1"})
        data = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                break
            except Exception as e:
                if attempt == 2:
                    print(f"[WARN] {app_name} page {page}: {e}", file=sys.stderr)
                else:
                    time.sleep(2.0 * (attempt + 1))
        if data is None:
            break
        entries = data.get("feed", {}).get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        added = 0
        for entry in entries:
            if "im:rating" not in entry:
                continue
            rid = entry.get("id", {}).get("label", "")
            if rid in seen:
                continue
            seen.add(rid)
            title = (entry.get("title", {}).get("label") or "").strip()
            body = (entry.get("content", {}).get("label") or "").strip()
            full = f"{title}. {body}".strip(". ").strip()
            if not full:
                continue
            rating = int(entry["im:rating"]["label"])
            updated = (entry.get("updated", {}).get("label") or "")[:10]
            rows.append(
                {
                    "review_uid": f"{app_name}_{len(rows)+1:03d}",
                    "app": app_name,
                    "date": updated,
                    "rating": rating,
                    "quote_2s": trim_two_sentences(full),
                }
            )
            added += 1
        if added == 0:
            break
    return rows


def tag_row(row: dict) -> dict:
    rating = int(row["rating"])
    txt = row["quote_2s"]
    # Codebook rule: only complaints (rating <= 3) qualify as pain evidence
    tags = [code for code, _, pat in THEMES if rating <= 3 and pat.search(txt)]
    row["themes"] = "|".join(tags) if tags else "other"
    row["is_e3_pain"] = "1" if tags else "0"
    return row


def summarize(rows: list[dict]):
    n = len(rows)
    if n == 0:
        print("No reviews loaded.")
        return
    dates = sorted(r["date"] for r in rows if r["date"])
    low_star = sum(1 for r in rows if int(r["rating"]) <= 3)
    any_pain = sum(1 for r in rows if r["is_e3_pain"] == "1")
    overlap = sum(
        1
        for r in rows
        if "blocked_or_failed_tx" in r["themes"] and "support_slow_or_loop" in r["themes"]
    )
    print(f"=== K5 3MV Review Mining Report (UTC {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')}) ===")
    print(f"Total N (all ratings): {n} | Date range: {dates[0]} -> {dates[-1]}")
    print("Per app: " + ", ".join(f"{a}={sum(1 for r in rows if r['app']==a)}" for a, _ in APPS))
    print(f"1-3 star complaints: {low_star}/{n} ({low_star*100/n:.1f}%)")
    print(f"Any E3-related pain (1-3★ matching codebook): {any_pain}/{n} ({any_pain*100/n:.1f}%) [{any_pain}/{low_star} = {any_pain*100/max(low_star,1):.1f}% of 1-3★]")
    for code, label, _ in THEMES:
        c = sum(1 for r in rows if code in r["themes"].split("|"))
        print(f"  - {code:24s}: {c:3d}/{n} ({c*100/n:5.1f}%) | {label}")
    print(f"  - overlap(blocked+support): {overlap:3d}/{n} ({overlap*100/n:5.1f}%)")

    print("\n--- Top Anonymized Examples (<=2 sentences, no reviewer names) ---")
    priority = sorted(
        [r for r in rows if r["is_e3_pain"] == "1"],
        key=lambda r: (-len(r["themes"].split("|")), int(r["rating"]), -len(r["quote_2s"])),
    )
    for i, r in enumerate(priority[:15], 1):
        print(f"{i:2d}. [{r['review_uid']} | {r['app']} | {r['date']} | {r['rating']}★ | {r['themes']}] \"{r['quote_2s']}\"")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--recount", action="store_true", help="Recount offline from saved anonymized CSV")
    ap.add_argument("--pages", type=int, default=1, help="RSS pages per app (50 reviews/page)")
    args = ap.parse_args()

    if args.recount and OUT_CSV.exists():
        with OUT_CSV.open(encoding="utf-8", newline="") as f:
            rows = [tag_row(r) for r in csv.DictReader(f)]
    else:
        rows = []
        for idx, (app_name, app_id) in enumerate(APPS):
            if idx > 0:
                time.sleep(1.5)
            rows.extend(fetch_app_reviews(app_name, app_id, pages=args.pages))
        rows = [tag_row(r) for r in rows]
        with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["review_uid", "app", "date", "rating", "themes", "is_e3_pain", "quote_2s"])
            w.writeheader()
            w.writerows(rows)
        print(f"Saved {len(rows)} anonymized rows to {OUT_CSV}")

    summarize(rows)


if __name__ == "__main__":
    main()
