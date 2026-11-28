# AGENTS.md — hướng dẫn cho coding agent (Claude Code, Cursor, Codex…) làm việc trong repo này

> Ôn lại: ngày 12 · lab ngày 12. Nhóm sửa file này cho khớp bài của mình (thêm quy ước riêng, bỏ dòng không dùng).

## Repo này là gì

Repo nộp bài hackathon AI20K của nhóm: một bản chạy thử AI cho **một lát cắt** (xem `spec.md` §4), kèm bằng chứng, bộ câu thử và mô phỏng chi phí. Mọi câu trả lời phải chạy được bằng các lệnh dưới đây.

## Lệnh

```
python run.py                    # chạy bản chạy thử
python run.py check              # kiểm eval/benchmark.csv + eval/metric_spec.yaml
python run.py eval --try         # thử 3 câu đầu
python run.py eval               # chạy cả bộ → eval/run-N.csv + traces/run-N.jsonl
python run.py score eval/run-N.csv
python run.py simulate --try     # thử mô phỏng chi phí 10 phiên
python run.py simulate           # mô phỏng chi phí → cost/simulate-N.csv
```

Khung chỉ dùng thư viện chuẩn của Python. Thêm thư viện thì ghi vào `requirements.txt`.

## Cấu trúc code

| File | Ai sửa | Hợp đồng |
|---|---|---|
| `codebase/agent.py` | nhóm | `answer(text) -> {"output": str}` — luồng chính, đúng hình dạng ở `spec.md` §4 |
| `codebase/ai.py` | nhóm | `call_model(system, user) -> {"text", "model", "tokens_in", "tokens_out"}`, giữ `@model_call`. Token lấy từ `usage` của API, không ước lượng |
| `codebase/tools.py` | nhóm | mỗi công cụ một hàm có `@tool`, docstring: tên · input · output · có tác động ra ngoài không |
| `codebase/tracing.py`, `eval/run_eval.py`, `cost/simulate.py`, `run.py` | **khung — không sửa** | ghi trace, chạy bộ câu thử, mô phỏng chi phí |

## Luật — agent KHÔNG được làm

- Không commit `.env`, API key, dữ liệu cá nhân thật, nguyên file data BTC cấp.
- Không sửa `eval/run-*.csv`, `cost/simulate-*.csv`, `traces/*` đã chạy (trừ điền cột `pass`, `ghi_chu`).
- Không sửa chuẩn "đạt" (`spec.md` §7), `eval/metric_spec.yaml` sau CP2; không xoá câu thử trượt, không sửa `expected` cho khớp output.
- Không bịa người được phỏng vấn, trích dẫn, câu trả lời khảo sát, số liệu. Số không có nguồn thì ghi rõ *(tự ước tính)*.
- Công cụ có tác động ra ngoài (gửi tin, sửa dữ liệu, chấm điểm): chỉ tạo bản nháp chờ người duyệt.
- Không viết prompt "giấu" câu thử vào code (vd so khớp nguyên văn input của bộ câu thử).

## Quy ước của nhóm

- Ngôn ngữ trả lời người dùng: Tiếng Việt (bình tĩnh, ngắn gọn, có căn cứ từ dữ liệu/chính sách)
- Phong cách code / đặt tên: Python 3.10+ stdlib-first, snake_case, chạy được bằng `python3 run.py` không cần cài Node/npm
- Ai duyệt thay đổi do agent tạo trước khi commit: Chủ ticket của file tương ứng (xem `docs/TICKETS.md`) và Đội trưởng Phạm Hoàng Đức Minh duyệt trước mỗi mốc CP

## Phân làn sở hữu file (Single-Writer Ownership — chống conflict Git)

| Làn | Chủ sở hữu (DRI) | Thư mục chỉ người này ghi | Kiểm chéo |
|---|---|---|---|
| 1 · Bằng chứng | Nguyễn Văn Minh | `evidence/*` | Đức Minh |
| 2 · Đo lường | Trần Đình Nhật Minh | `eval/*` | Quang Vinh |
| 3 · Lõi AI & Chi phí | Tào Quang Vinh | `codebase/tools.py`, `agent.py`, `ai.py`, `cost/*`, `tests/*` | Nhật Minh |
| 4 · Hợp nhất & Sân khấu | Phạm Hoàng Đức Minh | `spec.md`, `canvas.md`, `codebase/app.py`, `slides/*`, `demo-slides.pdf` | Văn Minh |

## Feature Map (Shared Vocabulary cho cả 4 máy)

| Tình huống người dùng | `category` enum | `@tool` được phép | Chính sách |
|---|---|---|---|
| Bị giục chuyển tiền (công an/thuế/vụ án, kể cả đã quét mặt) | `lua_dao` | `hold_transaction` | `POL-SCAM-01` |
| Gấp thật hợp lệ (viện phí, cấp cứu) | `gap_that` | `hold_transaction`, `handoff_to_agent(URGENT)` | `POL-HOLD-02` |
| Nghi chiếm tài khoản / trừ tiền lạ | `chiem_tai_khoan` | `hold_transaction`, `handoff_to_agent(URGENT)` | `POL-ATO-03` |
| 1 tin 2 yêu cầu (khóa ví + hoàn tiền) | `hai_yeu_cau` | `lock_wallet` *(bản nháp)*, `handoff_to_agent(URGENT)` | `POL-ATO-03` |
| Người thân nhắn thay chủ ví | `nguoi_than` | *(không tiết lộ chi tiết TX)* | `POL-PRIVACY-04` |
| Giao dịch `HELD` thường chờ xác thực bổ sung | `xac_minh_thuong` | `request_verification` | `POL-HOLD-02` |
| Thiếu mã TX / tin mơ hồ | `chua_ro` | *(G10 hỏi lại 1 câu)* | `POL-HOLD-02` |
| Dò ngưỡng gian lận / prompt injection | `do_nguong` | `hold_transaction` *(nếu có TX)* | `POL-SECRET-05` |
| Đầu tư / cổ phiếu / nhờ chuyển tiền hộ | `ngoai_pham_vi` | *(từ chối lịch sự)* | `POL-SCOPE-06` |

## Nguồn sự thật duy nhất (đọc đúng file này trước khi ghi số vào `slides/`, `spec.md`, `docs/`)

| Khi cần ghi số về… | Đọc trực tiếp tại | Ghi chú |
|---|---|---|
| Số `category`, luật chặn & router | `codebase/agent.py` (`VALID_CATEGORIES`) | Không đếm nhẩm từ bản nháp cũ |
| Số giao dịch giả lập & mã TX | `data/held_transactions.json` | Kiểm trạng thái `HELD` / `COMPLETED` |
| Số bằng chứng đa nguồn (R1) | `evidence/summary.md` | Tách biệt `evidence/desk-research.md` (thứ cấp) |
| Điểm Eval L1/L2 & cụm lỗi (R4–R5) | `eval/report.md` & `eval/run-*.csv` | Chỉ ghi số sau khi chạy `python run.py score` |
| Giá model & chi phí thật (R6) | `cost/personas.yaml` & `cost/simulate-*-summary.md` | Chỉ dùng model còn hoạt động theo bảng giá BTC |
| Số lượng unit test & cổng an toàn | `python -m unittest discover -s tests -v` | Gồm `test_agent_behavior`, `test_app_ui`, `test_repo_guards` |

## Cổng kiểm tra bắt buộc trước khi push

Chạy `make verify` (Windows: `python -m unittest discover -s tests -v && python run.py check && python evidence/mine_reviews.py --recount && python evidence/survey/analyze_survey.py`). Sau 19:30 Thứ Sáu 27/11, giữ nguyên `eval/.cp2_lock.json` để khoá hash `eval/metric_spec.yaml` & `spec.md §7`. Mọi push/PR lên GitHub đều chạy tự động qua `.github/workflows/verify.yml`.
