# Bảng Chia Việc (Tickets) — Nhóm 3MV · Track E (E3)

> **Quy tắc chống xung đột Git:** Mỗi người chỉ sửa các file thuộc ticket của mình; trước khi bắt đầu làm luôn chạy `git pull --rebase origin main`.
> **Mốc khóa cứng:** `spec.md §7` và `eval/metric_spec.yaml` **tuyệt đối không sửa sau 19:30 Thứ Sáu 27/11 (CP2)**.

## Phân công 8 Ticket cắt dọc (CP2 → CP3 → CP4)

| # | Ticket | Phụ trách | Chặn bởi | File sở hữu chính | Trạng thái |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **T01** | Đào review App Store VN + tung khảo sát lớp | **Nguyễn Văn Minh** | — | `evidence/mine_reviews.py`, `evidence/data-mining.md`, `evidence/survey/questions.md`, `canvas.md` | ✅ Xong phần CP2 (chờ kết quả Form) |
| **T02** | Dữ liệu giao dịch giả lập có seed + `DATA_CARD.md` + `spec.md §0–§7` | **Phạm Hoàng Đức Minh** | — | `data/held_transactions.json`, `data/support_policies.json`, `data/DATA_CARD.md`, `spec.md` | 🟡 Đã có bản nháp CP2 — **cả nhóm rà §7 trước 19:15** |
| **T03** | Khóa 4 Metric + Bộ câu thử (14 câu CP2 → 25 câu CP3) + hiệu chuẩn 2 người | **Trần Đình Nhật Minh** | T01, T02 | `eval/metric_spec.yaml`, `eval/benchmark.csv`, `eval/README.md` | 🟡 Đã có 14 câu CP2 — **chấm thử 5 output trước 19:15** |
| **T04** | Workflow 3 bước + 7 `@tool` + nối model thật (`gemini`/`openrouter`) | **Tào Quang Vinh** | T02 | `codebase/tools.py`, `codebase/agent.py`, `codebase/ai.py`, `tests/test_agent_behavior.py` | 🟡 Đã chạy mock 7/7 test — **nối API key `.env` test `eval --try`** |
| **T05** | Thu ≥20 phiếu khảo sát + ≥3 phỏng vấn → kiểm chéo `evidence/summary.md` & Impact `spec.md §2` | **Văn Minh + Đức Minh** | T01 | `evidence/survey/results.csv`, `evidence/interviews/P1..P3.md`, `evidence/summary.md`, `spec.md §2` | ⬜ Trước **CP3 (10:00 T7)** |
| **T06** | Chạy Eval Lượt 1 (`run-1.csv`) + Video 30s AI thật → gom ≥3 lỗi → 1 cải tiến → Lượt 2 (`run-2.csv`) | **Nhật Minh + Quang Vinh** | T03, T04 | `eval/run-1.csv`, `eval/run-2.csv`, `eval/report.md`, `eval/README.md` | ⬜ **CP3 (Lượt 1) → CP4 (Lượt 2)** |
| **T07** | Mô phỏng chi phí ≥50 phiên (`run.py simulate`) + 3 kịch bản × ≥2 model + 2 biểu đồ | **Quang Vinh + Văn Minh** | T05, T06 | `cost/personas.yaml`, `cost/simulate-1.csv`, `cost/cost-estimate.md` | ⬜ Trước **CP4 (14:30 T7)** |
| **T08** | Web UI 1 file HTML từ `python run.py` + 8 slide `demo-slides.pdf` + video dự phòng + 4 `reflection/` | **Đức Minh + Cả nhóm** | T04, T06, T07 | `codebase/app.py`, `demo-slides.pdf`, `reflection/*.md`, `docs/ai-usage.md` | ⬜ **CP4 (14:30 T7) → Khóa 23:59 T7** |

## Việc mỗi người làm NGAY (17:35 → 19:15 trước khi chốt CP2)

1. **Nguyễn Văn Minh (T01 → T05):** Chép 8 câu trong `evidence/survey/questions.md` lên Google Form và gửi ngay vào nhóm lớp L3A/L3B; rà lại 5 trích dẫn trong `evidence/data-mining.md`.
2. **Phạm Hoàng Đức Minh (T02):** Đọc duyệt `spec.md` (§0–§7) & `data/DATA_CARD.md`; chốt cùng cả nhóm xem ngưỡng `spec.md §7` (**≥80% tổng + 100% 4 luật cứng an toàn**) có cần chỉnh gì trước 19:15 không; chuẩn bị nộp Form 2 nhánh CP2 bằng mã `2A202604114`.
3. **Trần Đình Nhật Minh (T03):** Rà `eval/metric_spec.yaml` & 14 câu `eval/benchmark.csv`; cùng 1 thành viên khác chấm độc lập 5 output mẫu (`E01–E05`) để xác nhận khớp ≥4/5 rồi ghi vào `eval/README.md`. Lên kế hoạch bổ sung thêm 10–12 câu thật (từ khảo sát/phỏng vấn) để đủ 24–26 câu trước CP3.
4. **Tào Quang Vinh (T04):** Pull code về máy, tạo `.env` cục bộ (từ `.env.example`, **tuyệt đối không commit**), điền API key `gemini` hoặc `openrouter`, chạy thử `python3 run.py` và `python3 run.py eval --try` kiểm tra `tokens_in > 0` trước khi rời lớp.
