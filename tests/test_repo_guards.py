"""Cổng kiểm tra cơ học toàn repo: 0 API key, 0 SĐT cá nhân, 0 data BTC gốc, 0 model ngừng hỗ trợ."""
import os
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEXT_EXTS = {".py", ".md", ".yaml", ".yml", ".json", ".csv", ".html", ".txt"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}

KEY_PATTERNS = [
    re.compile(r"\bsk-(?:proj-|or-v1-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{30,}\b"),
]
VN_PHONE_RE = re.compile(r"(?<!\d)(?:\+?84|0)(?:3|5|7|8|9)\d{8}(?!\d)")
DEPRECATED_MODEL_RE = re.compile(r"(?i)\bgemini-2\.5-(?:flash|pro)\b")


def _iter_repo_text_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            if fname == ".env":
                continue
            p = Path(dirpath) / fname
            if p.suffix.lower() in TEXT_EXTS:
                yield p


class TestRepoGuards(unittest.TestCase):
    def test_no_hardcoded_api_keys_or_tokens(self):
        hits = []
        for path in _iter_repo_text_files():
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pat in KEY_PATTERNS:
                if pat.search(text):
                    hits.append(str(path.relative_to(ROOT)))
                    break
        self.assertEqual(hits, [], f"Phát hiện chuỗi giống API key/token trong: {hits}")

    def test_no_vietnamese_phone_numbers_outside_teams(self):
        hits = []
        for path in _iter_repo_text_files():
            rel = path.relative_to(ROOT).as_posix()
            if rel in {"TEAMS.md", "tests/test_repo_guards.py"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if VN_PHONE_RE.search(text):
                hits.append(rel)
        self.assertEqual(hits, [], f"Phát hiện số điện thoại VN ngoài TEAMS.md trong: {hits}")

    def test_no_raw_btc_dataset_directories(self):
        self.assertFalse((ROOT / "data" / "preclass").exists(), "Không đưa data/preclass của BTC vào repo nhóm")
        self.assertFalse((ROOT / "data" / "training-ops").exists(), "Không đưa data/training-ops của BTC vào repo nhóm")

    def test_personas_yaml_has_no_example_placeholders(self):
        personas = (ROOT / "cost" / "personas.yaml").read_text(encoding="utf-8")
        self.assertNotIn("(ví dụ", personas, "cost/personas.yaml vẫn còn chữ '(ví dụ)'")

    def test_no_deprecated_gemini_25_in_cost_or_slides(self):
        targets = [
            ROOT / "cost" / "personas.yaml",
            ROOT / "cost" / "cost-estimate.md",
            ROOT / "slides" / "slides_content.md",
            ROOT / "slides" / "slides.html",
        ]
        hits = []
        for path in targets:
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if DEPRECATED_MODEL_RE.search(text):
                hits.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(hits, [], f"Phát hiện model ngừng hỗ trợ (gemini-2.5-*) trong: {hits}")


if __name__ == "__main__":
    unittest.main()
