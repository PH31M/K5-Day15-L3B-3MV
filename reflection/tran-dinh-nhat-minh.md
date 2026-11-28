# Reflection — Trần Đình Nhật Minh

## 1. Vai trò và phần tôi làm

Tôi phụ trách đo lường của nhóm 3MV: bộ câu thử, cách chấm và báo cáo đánh giá.
Tôi hoàn thiện hồ sơ CP2, mở rộng từ 14 lên 25 câu thử và ghi rõ nguồn, phần chuyển thể cùng chi tiết giao dịch giả lập trong [eval/README.md](../eval/README.md).
Tôi ghi nhận kết quả lượt 1 là 16/25 (64%), lưu căn cứ từng câu ở [review-run-1.md](../eval/review-run-1.md) và nhận kiểm chéo của Vinh đồng ý 25/25 điểm, có AI hỗ trợ, không chấm độc lập.
Ở CP4, tôi chạy và ghi bản chấm lượt 2 đạt 21/25 (84%), tăng 5 câu / 20 điểm phần trăm, rồi bàn giao kết quả để nhóm kiểm chéo, tính chi phí và cập nhật slide.

## 2. AI hỗ trợ tôi thế nào

Tôi dùng trợ lý AI để đối chiếu nguồn câu thử, output, trace và dữ liệu JSON, hỗ trợ chấm theo tiêu chí đã khóa và viết báo cáo.
Tôi giữ riêng dữ liệu giả lập với bằng chứng người dùng thật; không coi bối cảnh AI chuyển thể là lời phỏng vấn nguyên văn.
Khi chấm E03/E09 ở lượt 1, tôi giữ cách đọc chặt tiêu chí thay vì đổi expected để câu được tính đạt; nhận xét về E14/E21 được ghi riêng để nhóm phân định.
Tôi khai báo việc có AI hỗ trợ; kết quả kiểm chéo cùng xem căn cứ không được mô tả thành hai người chấm độc lập.

## 3. Một câu thử trượt và điều tôi học được

E20 yêu cầu gặp nhân viên vì TX-912 treo 20 phút và khách không muốn kể lại từ đầu.
Ở lượt 1, output nói sẽ chuyển hồ sơ nhưng trace chỉ có request_verification, không có handoff hoặc ticket; tôi chấm 0.
Tôi học được rằng lời trả lời nghe đúng chưa đủ: phải kiểm hành động thực sự và mã hồ sơ trả về từ công cụ.
Cải tiến của Vinh đưa yêu cầu gặp người vào nhánh xử lý bằng code và bảo đảm hiển thị ticket; ở lượt 2 E20 đã có handoff/tóm tắt/ticket và được chấm 1. Tôi vẫn ghi rõ E22 còn suy diễn ghi nợ, E21 chờ nhóm phân định an toàn, không kết luận triển khai chỉ vì điểm tổng vượt 80%.
