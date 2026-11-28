# Nội dung 8 Slide Thuyết trình — Nhóm 3MV · Track E (E3)

> Bản CP4 chốt số thực đo (28/11/2026), đồng bộ 100% với `evidence/summary.md`, `spec.md`, `eval/report.md`, `cost/cost-estimate.md` và `demo-slides.pdf`.

---

## Slide 1: Người dùng & Vấn đề thực tế (Pain)
- **Tiêu đề:** Khi giao dịch bị tạm chặn — Người dùng đang chịu rủi ro gì?
- **Người dùng chính:** Người dùng ví điện tử & app ngân hàng (sinh viên, người đi làm) vừa bị hệ thống tạm giữ giao dịch chuyển tiền.
- **Pain 1 câu (không có chữ AI):** Khi giao dịch chuyển tiền bị tạm chặn đột ngột hoặc gặp cuộc gọi giục chuyển tiền, người dùng kẹt giữa chatbot menu cứng và tổng đài quá tải sau 20h — dẫn tới **mất sạch tiền trong vài giây** nếu bị thao túng chuyển tiếp, hoặc **trễ việc khẩn cấp** (viện phí, thanh toán tại quầy).
- **Bằng chứng kiểm chứng từ 3 nguồn sơ cấp đạt ngưỡng R1 (+ đối chứng thứ cấp VOZ/báo chí):**
  - **App Store VN (`N=100` MoMo & MB Bank):** `5/100 (5,0%)` toàn mẫu = `5/33 (15,2%)` phàn nàn 1–3★ về chặn giao dịch/CSKH chậm (`[MB_Bank_007]`: *"App lỗi không chuyển được tiền... cskh thì không có phản hồi??"*).
  - **Khảo sát lớp (`n=40`):** `22/40 (55,0%)` từng gặp tình huống E3 (`35%` bị giục chuyển tiền giả công an/thuế); `23/29 (79,3%)` người từng nhắn CSKH gặp bot vòng vo/chờ lâu; `17/40 (42,5%)` dễ chủ quan với Face ID.
  - **Phỏng vấn sâu Mom Test (`P1–P4`):** `P4` chưa từng cài app lạ nhưng sợ bị bắt giam nên tự chuyển 300k cho "Đại úy" và **nói dối mẹ là "trao đổi du học"** (hàng xóm mất 70 triệu); `P1` quét Face ID trong **`<1 giây`** theo phản xạ cơ bắp, không đọc popup chữ nhỏ và mất 45 phút vì rớt hàng chờ chat sau 20h.

---

## Slide 2: Vì sao chọn bài toán E3? (Impact)
- **So sánh 3 hướng Track E:**
  - *E1 (Giải thích sao kê):* Tác động thấp, sai số ít gây thiệt hại tiền trực tiếp.
  - *E2 (Cảnh báo vượt ngân sách):* Hữu ích nhưng phụ thuộc dữ liệu lịch sử giả định.
  - *E3 (Giao dịch bị tạm chặn nghi lừa đảo):* **CHỌN** — Sai 1 bước mất tiền không đảo được; chậm 1 bước lỡ việc gấp (viện phí/tại quầy).
- **Ước tính tác động (`spec.md §2` · quy mô 10.000 người dùng/tháng, *tự ước tính*):**
  - `500 – 2.000` ca phát sinh/tháng (5% App Store → 20% khảo sát).
  - Giảm `167 – 660` giờ chờ/tháng cho ca khẩn (`46,4%` nhóm từng xử lý mất ≥5 phút tới hôm sau; `P1–P4` mất 20–60 phút).
  - Bảo vệ **≥ 75 triệu ₫/tháng** (**≥ 7.500 ₫/người/tháng**) nếu chặn kịp chỉ 5 ca lừa đảo × 15 triệu ₫/ca.

---

## Slide 3: Giải pháp & Ranh giới AI (Workflow 3 bước)
- **Lát cắt 1 câu:** Người dùng nhắn khi giao dịch bị chặn → AI phân loại tình huống vào **9 nhóm** → Code thực thi **chỉ các công cụ đảo được** (`hold_transaction`, `request_verification`, `handoff_to_agent`) và **tuyệt đối không tự nhả tiền**.
- **Luồng cố định 3 bước (`codebase/agent.py`):**
  1. **Bước 1 · Input Guard (Code thuần):** Che OTP (kể cả có khoảng trắng `482 910`), mật khẩu, số thẻ trước khi gửi model; chặn dò ngưỡng & ngoài phạm vi.
  2. **Bước 2 · Context Lookup + LLM Classifier:** Tra `lookup_transaction` / `lookup_policy` (0 trường ngưỡng gian lận) + gọi model phân loại **9 nhóm** + hậu kiểm không hạ mức 5 nhóm rủi ro cao.
  3. **Bước 3 · Deterministic Policy Router (Code):** Gọi công cụ đảo được, gắn mã ticket `ADV-TX-...` & tóm tắt cấu trúc; quét bí mật lần cuối trước khi trả lời.
- **3 ranh giới cứng:** `release_transaction` bị chặn cứng (`BLOCKED_HUMAN_ONLY`); `lock_wallet` chỉ tạo bản nháp chờ tư vấn viên duyệt (`DRAFT_PENDING_ADVISOR`); G10 hỏi lại 1 câu ngắn khi thiếu mã TX.

---

## Slide 4: Demo Live — Bàn Điều Phối X-Ray (`python run.py`)
- **Giao diện 3 cột Python stdlib (`codebase/app.py` · 0 thư viện ngoài · server đa luồng):**
  - **Ca 1 — Lừa đảo đã quét Face ID (`TX-901`):** Giữ giao dịch (`hold_transaction`), trích `POL-SCAM-01`, cảnh báo dừng ngay & kênh chính thức dù `face_verified=true`.
  - **Ca 2 — Viện phí cấp cứu sau 20h (`TX-902`):** Gọi `handoff_to_agent(URGENT)` kèm tóm tắt ca, hiện phiếu duyệt tư vấn viên với mã `ADV-TX-902-U` & hotline 24/7.
  - **Ca 3 — Thử lửa tấn công (kẹp OTP `482 910` + `release_transaction`):** Che bí mật ngay tại Bước 1, chặn cứng bằng code (0 token), `0` lần gọi `release_transaction`.
- **Video dự phòng AI thật:** Đã quay trên `openai/gpt-4.1-mini` (link Drive trong `eval/report.md`, thấy rõ `1.402 token vào / 88 ra`, `3,5s`, `~$0.0007`).

---

## Slide 5: Đánh giá Lượt 1 → 1 Cải tiến → Lượt 2 (`eval/report.md`)
- **Bộ câu thử (`eval/benchmark.csv`):** **25 câu** (`7 thường · 14 khó · 4 từ chối`), **`14/25 (56%)`** nguồn thật (`nguoi_dung: 9` từ `S01..S40, P1..P4` + `data_that: 5`). Chuẩn đạt & `metric_spec.yaml` khóa cứng trước CP2 (`eval/.cp2_lock.json`, 40/40 unit test qua).
- **Kết quả đo thật (`openai/gpt-4.1-mini` · cùng 25 câu, cùng cách chấm):**
  - **Lượt 1 (`run-1@20261128-000708`):** **16/25 (64%)** — phát hiện 1 cụm lỗi lớn nhất: hứa chuyển người nhưng chưa gọi `handoff_to_agent` (`E18, E20, E21`) và gọi rồi nhưng thiếu mã ticket (`E02, E19, E22`).
  - **1 lần cải tiến (`8d89c64`):** Bổ sung nhận diện ca gấp tại quầy/tiền đã trừ chưa tới + hậu kiểm gắn mã ticket & hotline vào output.
  - **Lượt 2 (`run-2@20261128-121029`):** **21/25 (84%, +20 điểm phần trăm)** — 5 câu cải thiện (`E02, E18–E21`), **0 câu tụt `1 → 0`**, **6/6** ca lừa đảo chặn chuẩn, **0** lần gọi `release_transaction`.
- **Còn trượt 4 câu:** `E03` (thiếu số tiền), `E09` (thiếu nhắc OTP/mã TX), `E14` (thiếu lời nhắc không chia sẻ OTP), `E22` (diễn giải nhầm `reversible` thành *"có thể hoàn tác"*); nhóm gấp/nhạy cảm mới **6/8 (75%) < 7/8**.

---

## Slide 6: Chi phí khi dùng thật (`cost/cost-estimate.md`)
- **Mô phỏng 50 phiên thật (`simulate-1@20261128-121324`, 60 lượt hỏi, `seed=42`, 0 lỗi)** với 3 persona từ Khảo sát Q6 (`75%` dùng ít · `15%` dùng vừa · `10%` dùng nhiều) & tỉ lệ đạt **84%** từ `eval/run-2.csv`:
  - **`openai/gpt-4.1-mini` (thực đo):** **`$0.00059` (≈15 ₫)/phiên** · **`$0.00071` (≈18 ₫)/task thành công** · quy mô 10k / 50k / 200k người = **`252 nghìn ₫` / `1,26 triệu ₫` / `5,05 triệu ₫`/tháng**.
  - **`gemini-3.1-flash-lite` (tầng nhỏ):** **`$0.00050` (≈13 ₫)/task** · `890 nghìn ₫/tháng` (50k người · giảm ~30% nếu giữ 84%).
  - **`gemini-4-hydrogen` (tầng lớn):** **`$0.0028` (≈72 ₫)/task** · `5,03 triệu ₫/tháng` (50k người).
- **So với Impact:** Chi phí model **`≈ 25 ₫/người/tháng`** = **~1/300** mức impact bảo vệ giả định (`≥ 7.500 ₫/người/tháng`).
- **Giới hạn trung thực:** Chưa tính **giờ công tư vấn viên** (`21/60 = 35%` lượt hỏi tạo phiếu chuyển người).

---

## Slide 7: Kết luận — `ITERATE` (Chưa triển khai đại trà ngay)
- **Quyết định trung thực: `ITERATE` (hoàn thiện 1 vòng ngắn trước khi thí điểm có kiểm soát)**
- **Vì sao chưa tuyên bố GO chỉ vì điểm tổng 84% > 80%?**
  1. **An toàn lõi & kinh tế đã rất khả thi:** `0` lần tự nhả tiền, `6/6` ca lừa đảo giữ đúng, chi phí chỉ `18 ₫/task` (`25 ₫/người/tháng`).
  2. **Nhưng chưa đạt đủ chuẩn phụ đã khóa ở CP2:** nhóm ca gấp/nhạy cảm mới đạt **`6/8 (75%) < 7/8`**, còn 4 câu lỗi câu chữ (`E22` nói *"có thể hoàn tác"*, `E14` thiếu nhắc không gửi OTP).
  3. **Bài toán ROI tổng thể còn thiếu giờ công tư vấn viên** (`35%` lượt chuyển người trên bộ thử nhiều ca khó).

---

## Slide 8: Nếu có thêm 1 tuần (gắn trực tiếp với lỗi Lượt 2 & `evidence/`)
1. **Đóng sạch 4 câu trượt Lượt 2 (`E03, E09, E14, E22`):** Loại bỏ trường nội bộ `reversible` khỏi payload đưa vào LLM Responder để dứt điểm lỗi *"có thể hoàn tác"*, bắt buộc câu nhắc bảo mật khi `had_secret=True` và nêu đủ số tiền/mã TX; kiểm lại độ ổn định qua nhiều lượt chạy trên `gpt-4.1-mini` và `gemini-3.1-flash-lite`.
2. **Chạy kiểm thử người dùng thật (`validation/log.md`) với 3 người đã cam kết (`P1, P3, P4`):** Quan sát thao tác thực tế trên Web UI, đo lại tỉ lệ chuyển tư vấn viên và tinh chỉnh câu cảnh báo để phá vỡ *alert fatigue* `<1s`.
3. **Hoàn thiện bài toán ROI toàn phần:** Cộng chi phí giờ công tư vấn viên (từ tỉ lệ chuyển ca thực tế) + thời gian xử lý trung bình vào bảng `cost/cost-estimate.md` trước khi triển khai thí điểm có kiểm soát.
