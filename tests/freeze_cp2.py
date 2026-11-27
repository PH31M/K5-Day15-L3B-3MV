"""Khóa chuẩn "đạt" CP2: băm eval/metric_spec.yaml và spec.md §7 → eval/.cp2_lock.json.

Chạy sau 19:30 Thứ Sáu 27/11: `python tests/freeze_cp2.py` (hoặc `make freeze-cp2`).
Dòng "- **Kết quả:** ..." trong §7 được điền ở CP3/CP4 nên KHÔNG nằm trong phần bị khóa.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK_FILE = ROOT / "eval" / ".cp2_lock.json"


def locked_section_7(spec_text: str) -> str:
    m = re.search(r"(## §7\..*?)(?=\n## §8\.)", spec_text, re.S)
    if not m:
        raise ValueError("Không tìm thấy §7 (đứng trước §8) trong spec.md")
    return re.sub(r"(?m)^- \*\*Kết quả:\*\*.*(?:\n|$)", "", m.group(1)).strip()


def current_hashes() -> dict:
    def sha256(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    metric = (ROOT / "eval" / "metric_spec.yaml").read_text(encoding="utf-8")
    spec = (ROOT / "spec.md").read_text(encoding="utf-8")
    return {"metric_spec_sha256": sha256(metric), "spec_sec7_sha256": sha256(locked_section_7(spec))}


if __name__ == "__main__":
    if LOCK_FILE.exists():
        raise SystemExit(f"{LOCK_FILE.name} đã tồn tại, không ghi đè.")
    LOCK_FILE.write_text(json.dumps(current_hashes(), indent=2), encoding="utf-8")
    print("Frozen CP2 hashes -> eval/.cp2_lock.json")
