"""Công cụ của bài toán Track E (E3) — Nhóm 3MV.

Khớp 1-1 với bảng công cụ ở spec.md §4.
- Dữ liệu giao dịch đọc từ data/held_transactions.json (synthetic, KHÔNG chứa ngưỡng gian lận).
- Chính sách đọc từ data/support_policies.json.
- Công cụ không đảo được (release_transaction) bị CHẶN CỨNG ở tầng code.
- Công cụ khó đảo (lock_wallet) CHỈ tạo bản nháp chờ tư vấn viên xác nhận.
"""
import functools
import json
import os
from datetime import datetime, timezone

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TX_PATH = os.path.join(ROOT, "data", "held_transactions.json")
POLICY_PATH = os.path.join(ROOT, "data", "support_policies.json")


@functools.lru_cache(maxsize=8)
def _load_json_cached(path: str, mtime_ns: int) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_json(path: str) -> dict:
    return _load_json_cached(path, os.stat(path).st_mtime_ns)


@tool
def lookup_transaction(tx_id: str) -> dict:
    """Tra hồ sơ công khai của một giao dịch theo mã TX trong data/held_transactions.json.
    Input: tx_id (str, vd 'TX-901'). Output: dict hồ sơ giao dịch hoặc {'found': False}. Không tác động ra ngoài."""
    code = (tx_id or "").strip().upper()
    if not code:
        return {"found": False, "tx_id": ""}
    data = _load_json(TX_PATH)
    for tx in data.get("transactions", []):
        if tx.get("tx_id", "").upper() == code:
            return {"found": True, **tx}
    return {"found": False, "tx_id": code}


@tool
def lookup_policy(topic: str) -> dict:
    """Tra quy tắc xử lý và kênh chính thức theo chủ đề trong data/support_policies.json.
    Input: topic (str: lua_dao | gap_that | chiem_tai_khoan | nguoi_than | bao_mat | ngoai_pham_vi).
    Output: dict chính sách hoặc {'found': False}. Không tác động ra ngoài."""
    key = (topic or "").strip().lower()
    data = _load_json(POLICY_PATH)
    for pol in data.get("policies", []):
        if pol.get("topic", "").lower() == key:
            return {"found": True, **pol}
    return {"found": False, "topic": key}


@tool
def hold_transaction(tx_id: str, reason: str) -> dict:
    """Giữ nguyên trạng thái tạm chặn của một giao dịch đang HELD để bảo vệ tiền của người dùng.
    Input: tx_id (str), reason (str). Output: dict xác nhận trạng thái HELD_CONFIRMED.
    Tác động ra ngoài: Có — đảo lại được (chỉ kéo dài thời gian chờ xử lý)."""
    tx = (tx_id or "UNKNOWN").strip().upper()
    return {
        "action": "hold_transaction",
        "tx_id": tx,
        "status": "HELD_CONFIRMED",
        "reversible": True,
        "reason": reason[:200],
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


@tool
def request_verification(tx_id: str, user_alias: str) -> dict:
    """Gửi yêu cầu màn hình xác thực bổ sung cho giao dịch đang HELD ở mức rủi ro thường.
    Input: tx_id (str), user_alias (str). Output: dict mã phiên xác thực.
    Tác động ra ngoài: Có — đảo lại được."""
    tx = (tx_id or "UNKNOWN").strip().upper()
    return {
        "action": "request_verification",
        "tx_id": tx,
        "user_alias": user_alias or "UNKNOWN",
        "verification_ticket": f"VER-{tx}",
        "status": "VERIFICATION_SENT",
        "reversible": True,
    }


@tool
def handoff_to_agent(tx_id: str, category: str, priority: str, summary: str) -> dict:
    """Chuyển cuộc hội thoại sang tư vấn viên trực kèm tóm tắt có cấu trúc.
    Input: tx_id (str), category (str), priority (NORMAL|HIGH|URGENT), summary (str).
    Output: dict mã ticket chuyển tư vấn viên. Tác động ra ngoài: Có — đảo lại được."""
    tx = (tx_id or "NO-TX").strip().upper()
    prio = priority.upper() if priority else "HIGH"
    return {
        "action": "handoff_to_agent",
        "ticket_id": f"ADV-{tx}-{prio[:1]}",
        "tx_id": tx,
        "category": category,
        "priority": prio,
        "summary": summary[:300],
        "status": "ESCALATED_TO_HUMAN",
        "reversible": True,
        "advisor_hours_vn": "08:00-20:00 (ngoài giờ: hotline khẩn 24/7 1900-0000-MAU)",
    }


@tool
def release_transaction(tx_id: str) -> dict:
    """CỔNG CHẶN CỨNG — AI tuyệt đối KHÔNG được phép tự nhả giao dịch đang bị giữ.
    Input: tx_id (str). Output: luôn trả BLOCKED_HUMAN_ONLY.
    Tác động ra ngoài: Không đảo được (tiền đi trong vài giây) -> chỉ tư vấn viên duyệt."""
    return {
        "action": "release_transaction",
        "tx_id": (tx_id or "UNKNOWN").strip().upper(),
        "status": "BLOCKED_HUMAN_ONLY",
        "allowed": False,
        "reason": "Hành động không đảo được: chỉ tư vấn viên có thẩm quyền mới được phép mở chặn giao dịch.",
    }


@tool
def lock_wallet(user_alias: str, reason: str) -> dict:
    """Tạo BẢN NHÁP yêu cầu khóa ví gửi tư vấn viên xác nhận (AI không tự khóa vĩnh viễn).
    Input: user_alias (str), reason (str). Output: dict bản nháp DRAFT_PENDING_ADVISOR.
    Tác động ra ngoài: Khó đảo (mở lại qua tổng đài mất nhiều giờ) -> bắt buộc người duyệt."""
    return {
        "action": "lock_wallet",
        "user_alias": user_alias or "UNKNOWN",
        "draft_id": f"LOCK-DRAFT-{user_alias or 'USER'}",
        "status": "DRAFT_PENDING_ADVISOR",
        "requires_human_approval": True,
        "reason": reason[:200],
    }
