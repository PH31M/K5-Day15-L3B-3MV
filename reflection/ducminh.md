# Reflection — Phạm Hoàng Đức Minh

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
- Đội trưởng nhóm 3MV (Lớp L3B, Track E): Điều phối tổng thể 4 thành viên theo 4 làn file riêng biệt, phụ trách nộp các mốc Checkpoint CP1–CP4 bằng mã học viên `2A202604114`.
- Trực tiếp sở hữu Làn 4 (Hợp nhất & Sân khấu): Soạn thảo toàn bộ kiến trúc và ranh giới an toàn tại `spec.md` (§0–§10), xây dựng `canvas.md`, thiết kế bộ dữ liệu giả lập có seed tại `data/held_transactions.json` và `data/DATA_CARD.md`.
- Lập trình giao diện Web UI demo tương tác tại `codebase/app.py` và chuẩn bị nội dung 8 slide thuyết trình sân khấu `slides/slides_content.md`.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
- AI hỗ trợ viết khung script cào review App Store, tạo cấu trúc dữ liệu JSON giả lập chuẩn schema và gợi ý các kịch bản kiểm thử biên (boundary testing).
- Chỗ phải sửa: Ban đầu khi thiết kế công cụ, AI đề xuất để bot có thể gọi lệnh "hủy giao dịch hoàn tiền", tôi đã kiên quyết loại bỏ và thiết lập luật cấm tuyệt đối `release_transaction` trong `spec.md §4` và khóa cứng ở tầng code. AI cũng có xu hướng trả lời chung chung hoặc đoán bừa số tiền khi người dùng không cung cấp mã TX, tôi đã áp dụng nguyên tắc G10 để ép bot chỉ hỏi lại đúng 1 câu ngắn xin mã.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
- Câu thử `E01` / `E14` khi người dùng cố tình đóng giả là công an kèm thông báo "đã xác thực khuôn mặt thành công" hoặc đưa mã OTP giả mạo để lừa bot mở khóa giao dịch.
- Ban đầu mô hình ngôn ngữ thấy có cụm từ "đã quét mặt" thì dễ nhầm tưởng là giao dịch an toàn và có xu hướng trấn an người dùng. Nhóm đã học được rằng trong lĩnh vực tài chính, không bao giờ được tin tưởng hoàn toàn vào một tầng suy luận LLM; giải pháp là phải dùng Workflow 3 bước có Boundary Guard và Deterministic Router bằng code chặn cứng mọi lệnh nhả tiền, đồng thời kích hoạt cảnh báo `POL-SCAM-01` bất kể trạng thái xác thực sinh trắc học.
