"""Nối model — chỗ DUY NHẤT gọi model AI (Nhóm 3MV · Track E · E3).

Hỗ trợ 0 thư viện ngoài (chỉ Python stdlib urllib):
- MODEL_PROVIDER=fake       (mặc định ở CP2 — chạy hết luồng, token=0)
- MODEL_PROVIDER=gemini     (Google Gemini API, vd gemini-2.5-flash)
- MODEL_PROVIDER=openrouter (OpenRouter OpenAI-compatible API)
- MODEL_PROVIDER=openai     (OpenAI API, vd gpt-4o-mini / gpt-5.4-nano)

Tuyệt đối KHÔNG ghi API key vào file này — điền trong .env cục bộ (đã .gitignore).
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
API_BASE_URL = (os.environ.get("API_BASE_URL") or "").strip()


def _post_json(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json", **headers},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", "replace")[:300]
        raise RuntimeError(f"HTTP {e.code}: {err_body}")


def _call_openai_compatible(url: str, system: str, user: str, model: str, extra_headers: dict | None = None) -> dict:
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    headers = {"Authorization": f"Bearer {API_KEY}", **(extra_headers or {})}
    data = _post_json(url, headers, {"model": model, "messages": messages, "temperature": 0.1})
    usage = data.get("usage") or {}
    text = data["choices"][0]["message"]["content"]
    return {
        "text": text,
        "model": data.get("model") or model,
        "tokens_in": int(usage.get("prompt_tokens", 0)),
        "tokens_out": int(usage.get("completion_tokens", 0)),
    }


def _call_gemini(system: str, user: str, model: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.1},
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = _post_json(url, {}, body)
    candidates = data.get("candidates") or []
    parts = (candidates[0].get("content") or {}).get("parts") or [] if candidates else []
    text = "".join(p.get("text", "") for p in parts)
    meta = data.get("usageMetadata") or {}
    tokens_in = int(meta.get("promptTokenCount", 0))
    tokens_out = int(meta.get("candidatesTokenCount", 0)) + int(meta.get("thoughtsTokenCount", 0))
    return {
        "text": text,
        "model": model,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
    }


@model_call
def call_model(system: str, user: str, model_override: str | None = None) -> dict:
    provider = (os.environ.get("MODEL_PROVIDER") or MODEL_PROVIDER or "fake").strip().lower()
    model = (model_override or os.environ.get("MODEL_NAME") or MODEL_NAME).strip()

    if provider == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {
            "text": f"[fake-mode] {last[:80]}",
            "model": "fake",
            "tokens_in": 0,
            "tokens_out": 0,
        }

    if not API_KEY:
        raise RuntimeError(f"Thiếu API_KEY trong .env cho MODEL_PROVIDER={provider}")

    if provider == "gemini":
        return _call_gemini(system, user, model or "gemini-2.5-flash")
    if provider == "openai":
        url = API_BASE_URL or "https://api.openai.com/v1/chat/completions"
        return _call_openai_compatible(url, system, user, model or "gpt-4o-mini")
    if provider == "openrouter":
        url = API_BASE_URL or "https://openrouter.ai/api/v1/chat/completions"
        return _call_openai_compatible(
            url,
            system,
            user,
            model or "google/gemini-2.5-flash",
            extra_headers={"HTTP-Referer": "https://github.com/PH31M/K5-Day15-L3B-3MV", "X-Title": "K5-3MV-E3"},
        )

    raise NotImplementedError(f"Chưa hỗ trợ MODEL_PROVIDER={provider}. Dùng fake | gemini | openrouter | openai.")
