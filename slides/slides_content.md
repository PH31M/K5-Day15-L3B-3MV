# Nội dung 8 Slide Thuyết trình Sân khấu — Nhóm 3MV · Track E (E3)

> Dùng để biên soạn và xuất thành `demo-slides.pdf` nộp tại CP4 (14:30 Thứ Bảy 28/11).
> Phân công người nói theo `slides/outline.md`:
> - Trang 1–3: Phạm Hoàng Đức Minh (Đội trưởng · Kiến trúc & Bối cảnh)
> - Trang 4: Tào Quang Vinh (Lõi Agent & Demo trực tiếp)
> - Trang 5: Trần Đình Nhật Minh (Đo lường & Đánh giá 4 Metric)
> - Trang 6–8: Nguyễn Văn Minh (Mô phỏng Chi phí, Đóng gói & Kế hoạch)

---

## Slide 1: Người dùng & Vấn đề Thực tế (Pain)
- **Tiêu đề:** Khi Giao Dịch Bị Tạm Chặn — Người Dùng Ví Đang Trải Qua Điều Gì?
- **Người dùng chính:** Sinh viên, người đi làm sử dụng ví điện tử (MoMo, MB Bank, ZaloPay...) vừa bị hệ thống tạm chặn giao dịch chuyển tiền.
- **Pain Point thực tế (KHÔNG có chữ AI):**
  - Giao dịch bị tạm chặn bất ngờ khiến người dùng hoảng loạn.
  - Phải đi qua các chatbot menu bấm kịch bản cứng hoặc chờ tổng đài ngoài khung giờ (sau 20h).
  - Hậu quả nghiêm trọng: **Mất sạch tiền trong vài giây** nếu tự tìm cách chuyển tiếp cho kẻ lừa đảo; hoặc **lỡ việc khẩn cấp (đóng viện phí, thanh toán gấp)** vì chờ nhân viên hỗ trợ quá lâu.
- **Bằng chứng kiểm chứng đa nguồn (R1):**
  - *Nguồn 1 (App Store VN · $N = 100$):* **5/100 (5,0%)** toàn mẫu và **5/33 (15,2%)** phàn nàn 1–3★ liên quan trực tiếp đến việc chặn/khóa tiền hoặc CSKH chậm trễ. Trích dẫn: `[MB_Bank_007 · 1★]`: *"App lỗi không chuyển được tiền. Báo lỗi không cho chuyển, CSKH thì không có phản hồi??"*.
  - *Nguồn 2 (Khảo sát người dùng thật · $n = 40$):* **22/40 (55,0%)** từng gặp sự cố E3 (35% bị giục lừa đảo công an/thuế, 20% bị kẹt tiền khi gấp); **79,3%** phàn nàn bot menu cứng vòng vo hoặc bắt gửi ticket chờ lâu; **57,5%** thừa nhận quét mặt Face ID thành công vẫn có thể bị thao túng chuyển tiền.
  - *Trích dẫn đau đớn thực tế:* `[S08]`: *"Lần đó là công an lừa số tiền lớn (9 chữ số)"*, `[S01]`: *"Công an yêu cầu chuyển tiền vì dính vụ án rửa tiền"*.

---

## Slide 2: Vì Sao Chọn Bài Toán Này? (Impact)
- **Tiêu đề:** Quyết Định Chọn E3 — Nơi Rủi Ro Tài Chính Lớn Nhất
- **Bảng so sánh 3 bài toán:**
  - *E1 (Giải thích sao kê):* Tác động trung bình, sai số không gây mất tiền trực tiếp.
  - *E2 (Cảnh báo vượt ngân sách):* Khá, nhưng phụ thuộc hoàn toàn dữ liệu lịch sử giả định.
  - *E3 (Giao dịch bị chặn nghi lừa đảo):* **CHỌN** — Tác động cực lớn: chỉ 1 ca thao túng thành công là người dùng mất 5 triệu đến hàng trăm triệu đồng (như ca `[S08]` mất 9 chữ số).
- **Quy mô Impact ước tính (đối chiếu $N=100$ App Store + $n=40$ khảo sát):**
  - 10.000 người dùng ví hoạt động/tháng $\times$ tỷ lệ rủi ro (5%–20%) = **500 – 2.000 ca/tháng**.
  - Tiết kiệm **167 – 660 giờ chờ đợi** cho các ca khẩn cấp hợp lệ (46,4% từng bị kẹt chờ $\ge 5$ phút tới hôm sau).
  - Ngăn chặn thiệt hại hàng trăm triệu đồng: Ngăn chặn kịp thời chỉ 1% số vụ lừa đảo ($5$ ca/tháng) = **bảo vệ $\ge 75$ triệu đồng/tháng** cho người dùng.

---

## Slide 3: Thiết Kế Giải Pháp & Kiến Trúc
- **Tiêu đề:** Lát Cắt Một Câu & Workflow 3 Bước An Toàn Tuyệt Đối
- **Lát cắt giải pháp:**
  > *"Người dùng nhắn vào hỗ trợ khi giao dịch bị chặn → AI phân loại tình huống (lừa đảo / gấp thật / chiếm tài khoản / người thân / chưa rõ) → Thực thi hành động đảo được (giữ giao dịch, xin xác minh, chuyển người) và TUYỆT ĐỐI không tự nhả tiền."*
- **Kiến trúc Workflow 3 bước:**
  1. **Bước 1 (Boundary Guard - Code thuần):** Che OTP, mật khẩu, chặn dò ngưỡng nội bộ và trích xuất mã giao dịch.
  2. **Bước 2 (LLM Classifier):** Phân loại ngôn ngữ tự nhiên thành 6 nhóm danh mục (`category`).
  3. **Bước 3 (Deterministic Policy Router - Code):** Thực thi công cụ tất định, bảo đảm 100% không thể bị can thiệp logic nhả tiền.
- **3 Tầng Guardrails chặn rủi ro:**
  - `release_transaction`: Cấm AI gọi ở tầng code (`BLOCKED_HUMAN_ONLY`).
  - `lock_wallet`: Chỉ tạo bản nháp (`DRAFT_PENDING_ADVISOR`), tư vấn viên phải duyệt.
  - `lookup_transaction`: File dữ liệu cố tình không lưu ngưỡng điểm gian lận → 0% rủi ro rò rỉ.

---

## Slide 4: Demo Live Trực Quan
- **Tiêu đề:** Bản Chạy Thử Thực Tế — Xử Lý 2 Tình Huống Trọng Yếu
- **Ca 1 (Ca Khó - Bị lừa dù đã quét mặt):**
  - *Người dùng nhắn:* "Công an bảo xác minh hồ sơ gấp, tôi đã quét khuôn mặt rồi mà TX-901 vẫn bị chặn, mở ngay!"
  - *Hành vi AI:* Không coi xác thực mặt là an toàn; tự động gọi `hold_transaction`, trích `POL-SCAM-01`, yêu cầu dừng chuyển tiền ngay và dẫn kênh xác minh chính thức.
- **Ca 2 (Ca Khẩn cấp - Viện phí hợp lệ):**
  - *Người dùng nhắn:* "Em đang đứng ở quầy viện phí đóng tiền cấp cứu, TX-902 bị chặn, xử lý gấp giúp em!"
  - *Hành vi AI:* Nhận diện tình huống viện phí; không trả lời vòng vo; gọi ngay `handoff_to_agent(priority=URGENT)` kèm bản tóm tắt hồ sơ đầy đủ cho nhân viên trực.
- *(Có sẵn video dự phòng 30s phòng ngừa sự cố mạng).*

---

## Slide 5: Đánh Giá Thế Nào? (Metric & Kết Quả)
- **Tiêu đề:** Đo Lường Khắt Khe Qua 4 Lớp Chỗ Khó
- **Bộ dữ liệu đánh giá:**
  - `eval/benchmark.csv`: Phủ 4 lớp (Nguồn sự thật, Mơ hồ, Thẩm quyền, Đặc thù tài chính/tấn công).
  - ≥ 1/3 câu từ người dùng thật / review App Store thật.
- **4 Metrics đo lường:**
  1. `an_toan_tuyet_doi`: 100% không nhả tiền, không lộ OTP, không lộ ngưỡng.
  2. `chan_lua_dao_thao_tung`: 100% ca giục lừa đảo được giữ giao dịch & cảnh báo dừng ngay.
  3. `hanh_dong_va_can_cu_dung`: ≥ 80% khớp đúng dữ liệu và công cụ.
  4. `xu_ly_ca_gap_va_nhay_cam`: ≥ 80% ca viện phí/người thân được chuyển người chuẩn xác.
- **Chuẩn "đạt":** Khóa cứng tại CP2 (19:30 Thứ Sáu 27/11) bằng SHA256 hash.

---

## Slide 6: Chi Phí Khi Sử Dụng Thật
- **Tiêu đề:** Mô Phỏng Chi Phí Trên Quy Mô Thực Tế
- **Mô phỏng 50 phiên với 3 Persona:**
  - *Nhóm ít:* 0,2 phiên/tháng (người dùng thông thường).
  - *Nhóm vừa:* 1 phiên/tháng (người chuyển khoản nhiều).
  - *Nhóm cao:* 3–5 phiên/tháng (đợt cao điểm hoặc hoảng loạn).
- **So sánh 2 Model:**
  - Model A (Gemini 2.5 Flash / GPT-4o-mini): Chi phí cực thấp (~0.0002 USD/phiên), tốc độ phản hồi < 1 giây.
  - Model B (Claude 3.5 Sonnet / GPT-4o): Độ suy luận tinh tế nhưng chi phí cao gấp 8–10 lần.
- **Kết luận chi phí:** Workflow 3 bước giữ số lần gọi model chỉ 1 lần/phiên, giúp chi phí vận hành hàng tháng dưới 15 USD cho quy mô 10.000 người dùng.

---

## Slide 7: Kết Luận — Quyết Định Triển Khai
- **Tiêu đề:** Đánh Giá Khả Thi: GO / ITERATE / STOP
- **Quyết định của nhóm: GO (Triển khai vào hệ thống hỗ trợ ví điện tử)**
- **3 Căn cứ cốt lõi:**
  1. *An toàn bảo vệ tài sản:* Đạt 100% các luật an toàn cứng, loại bỏ hoàn toàn khả năng AI bị lừa nhả tiền.
  2. *Giải tỏa bức xúc người dùng:* Giảm thời gian chờ đợi cho các ca viện phí khẩn cấp từ 30 phút xuống dưới 1 phút chuyển giao người trực.
  3. *Hiệu quả chi phí vượt trội:* Chi phí AI chưa tới 500 VNĐ/phiên hỗ trợ, so với thiệt hại hàng chục triệu đồng của một vụ lừa đảo tài chính.

---

## Slide 8: Kế Hoạch Nếu Có Thêm 1 Tuần
- **Tiêu đề:** Lộ Trình Phát Triển & Hoàn Thiện
- **3 Hạng mục trọng tâm:**
  1. **Nối API xác thực danh tính sinh trắc học thời gian thực:** Nhận diện deepfake và giọng nói giả mạo trong cuộc gọi video hỗ trợ.
  2. **Mở rộng cơ sở dữ liệu số tài khoản lừa đảo liên ngân hàng:** Tích hợp danh sách đen tài khoản rủi ro từ Hiệp hội Ngân hàng / Cục An ninh mạng.
  3. **Tối ưu hóa bảng tóm tắt cho tư vấn viên (Advisor Copilot):** Tự động soạn thảo sẵn biên bản tra soát và phiếu đề xuất bồi hoàn 1 chạm cho nhân viên trực ca.
