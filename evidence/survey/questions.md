# Bộ câu hỏi khảo sát lớp — Nhóm 3MV · Track E (E3)

> **Ngưỡng R1:** ≥20 người ngoài nhóm (đúng người dùng ví điện tử / app ngân hàng), giữ log từng câu trả lời, **KHÔNG thu họ tên, email, số tài khoản, thu nhập hay số dư**.
> **Link Form công khai:** `https://docs.google.com/forms/d/e/1FAIpQLScgDeocfOpH46d04oBRExF-1D4Yey77_RzaRMS0dG2PEhP8xg/viewform`
> **Kênh gửi dự kiến:** Nhóm lớp AI20K L3A/L3B (mở 18:15 Thứ Sáu 27/11 → chốt 08:30 Thứ Bảy 28/11).

## 8 câu hỏi hành vi & kiểm chứng giả thuyết (bản hợp nhất chuẩn Mom Test — đã chốt giữa Làn 1 & Đội trưởng)

| # | Câu hỏi | Kiểu trả lời | Mục đích trong Spec / Eval / Cost |
| :---: | :--- | :--- | :--- |
| 1 | Bạn hiện dùng ứng dụng nào thường xuyên nhất để chuyển tiền / thanh toán? | Chọn nhiều: MoMo · ZaloPay · App ngân hàng (VCB/MB/TCB/BIDV…) · Khác | Xác nhận đúng người dùng & đối chiếu Nguồn 1 (review MoMo/MB Bank) |
| 2 | Trong 6 tháng qua, bạn (hoặc người thân gần) đã từng rơi vào tình huống nào sau đây chưa? | Chọn nhiều: Bị cuộc gọi/tin nhắn giục chuyển tiền gấp (giả công an, thuế, shipper, việc làm online…) · Đang cần chuyển tiền gấp (viện phí, thanh toán tại quầy, chuyển muộn…) thì app chặn/treo xác thực · Thấy trừ tiền lạ hoặc nghi tài khoản bị truy cập trái phép · Chưa từng gặp tình huống nào ở trên | Đo tỉ lệ từng nhóm tình huống E3 (`lua_dao` / `gap_that` / `chiem_tai_khoan`) |
| 3 | Lần gần nhất bạn (hoặc người thân) gặp một trong các tình huống trên hoặc cần hỏi hỗ trợ giao dịch, tổng cộng mất bao lâu để biết rõ phải làm gì tiếp theo? | Chọn một: Dưới 5 phút · 5–15 phút · 15–30 phút · Trên 30 phút / chờ tới hôm sau · Chưa từng gặp | Đo số phút thực tế cho Impact (`spec.md §2`) |
| 4 | Trải nghiệm thực tế của bạn khi nhắn Chat hỗ trợ / gọi tổng đài ví điện tử hoặc ngân hàng là gì? | Chọn nhiều: Xử lý nhanh, đúng vấn đề · Bot trả lời theo menu cứng/vòng vo, không đúng tình huống · Phải gửi ticket chờ phản hồi lâu trong khi đang cần gấp · Gọi tổng đài bận hoặc ngoài giờ hành chính (sau 20h) khó gặp người · Chưa từng liên hệ hỗ trợ | Kiểm chứng lỗi bot cứng & khoảng trống sau 20h (trung lập, tránh leading) |
| 5 | Theo bạn, nếu chính chủ tài khoản đã tự quét khuôn mặt (Face ID / sinh trắc học) thành công cho một giao dịch, giao dịch đó có chắc chắn an toàn không? | Chọn một: Chắc chắn an toàn (vì chính chủ đã xác nhận) · Chưa chắc an toàn (vẫn có thể đang bị thao túng/ép chuyển tiền) · Chưa từng nghĩ tới / Không rõ | Kiểm chứng "nghịch lý sinh trắc học" (`face_verified=true` vẫn giữ khi nghi bị thao túng) |
| 6 | Trong 3 tháng qua, bạn (hoặc người thân) gặp tình huống cần kiểm tra giao dịch bất thường hoặc nhận cuộc gọi/tin nhắn có dấu hiệu lừa đảo tài chính bao nhiêu lần? | Chọn một: 0 lần · 1 lần trong 3 tháng · 1–2 lần/tháng · Từ 3 lần/tháng trở lên | Cơ sở tần suất (`uses_per_month`) cho `cost/personas.yaml` |
| 7 | *(Tuỳ chọn)* Chia sẻ nhanh 1–2 câu về **lần gần nhất** bạn hoặc người thân bị chặn/treo tiền, gặp tin nhắn giục chuyển tiền, hoặc khó chịu khi nhắn CSKH: | Đoạn văn ngắn | Thu trích dẫn thật cho `evidence/summary.md` & câu thử `nguoi_dung:` cho CP3 |
| 8 | *(Tuỳ chọn)* Nếu bạn sẵn lòng cho nhóm hỏi nhanh 5–10 phút tối nay về trải nghiệm trên, để lại tên Zalo/Discord (không bắt buộc; sẽ xoá trước khi nộp bài): | Văn bản ngắn | Tuyển ≥3 người phỏng vấn sâu (`evidence/interviews/P1..P3.md`) |

## Lưu ý đạo đức & ẩn danh
- Không bật thu thập email trên Google Form.
- Trước khi commit `evidence/survey/results.csv`, **xoá hoàn toàn cột câu 8** và rút gọn Timestamp (chỉ giữ ngày) nếu có thể nhận diện người trả lời.
- Mọi trích dẫn chép sang `evidence/summary.md` ghi dạng `Khảo sát #12`, tối đa 2 câu.
