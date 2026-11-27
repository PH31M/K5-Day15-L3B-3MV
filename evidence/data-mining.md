# Đào data — cách đếm và kết quả (Nhóm 3MV · Track E · E3)

> Script tái lập: [`evidence/mine_reviews.py`](mine_reviews.py) · Chạy lại ngoại tuyến ra cùng kết quả: `python3 evidence/mine_reviews.py --recount`
> Nguồn gốc: Apple App Store Việt Nam RSS công khai (không cần đăng nhập, đã xoá toàn bộ tên người viết và cắt ≤2 câu trong `evidence/reviews_sample_anonymized.csv`).

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** Review công khai mới nhất trên Apple App Store Việt Nam của 2 ứng dụng tài chính phổ biến có dữ liệu RSS trả về đầy đủ ngày lấy mẫu (27/11/2026): **MoMo** (`id=918751511`, 50 review) và **MB Bank** (`id=1205807363`, 50 review), khoảng thời gian đăng từ **21/11/2026 → 25/11/2026**. *(Lưu ý: feed RSS của ZaloPay/VCB/BIDV tạm giới hạn trả về 0 dòng tại thời điểm chạy; ghi nhận trung thực trong giới hạn data).*
- **Đếm gì:** Số review phàn nàn (mức **1–3★**) khớp bộ quy tắc chủ đề E3 (đã tinh chỉnh sau khi đọc 30 dòng đầu để loại trừ dương tính giả như góp ý tính năng 5★ hoặc phàn nàn phí thường niên dùng từ lóng "lừa đảo"):
  1. `blocked_or_failed_tx`: Giao dịch bị khóa/chặn/treo, không chuyển được tiền hoặc lỗi sinh trắc học/chuyển tiền.
  2. `support_slow_or_loop`: CSKH / tổng đài / ticket hỗ trợ không phản hồi, trả lời chậm hoặc vòng vo.
  3. `unauth_or_security_risk`: Bị trừ tiền lạ / không rõ nguồn / lo ngại bảo mật (đã loại trừ phàn nàn phí thường niên & hợp đồng vay).
- **Mẫu số là gì:**
  - Mẫu số chính **`N = 100`** (toàn bộ 100 review thu được ở **mọi mức sao 1–5★**, kể cả review khen và review không liên quan).
  - Mẫu số phụ **`N_1to3 = 33`** (nhóm review phàn nàn 1–3★) để thấy tỉ trọng trong tập người dùng đang gặp vấn đề.
- **Script:** `python3 evidence/mine_reviews.py --recount` (thư viện chuẩn Python, 0 thư viện ngoài).

## 2. Đọc trước, đếm sau

Đã đọc 30 dòng đầu của mẫu (kèm kiểm tay toàn bộ các dòng gắn nhãn). Các kiểu hành vi nổi bật trước khi khoá bộ đếm:
- Nhóm review 5★ phần lớn khen ngắn hoặc góp ý thêm tính năng (vd đề xuất mở app tự quét khuôn mặt — cần loại khỏi tập pain bằng điều kiện `rating <= 3`).
- Trong nhóm 1–3★, nổi lên 3 nhóm phàn nàn trực tiếp liên quan E3: (a) bị khóa/chặn không chuyển khoản được mà không rõ lý do cụ thể, (b) gọi CSKH / gửi ticket không được phản hồi kịp, và (c) bị trừ tiền bất thường gây hoảng loạn.

## 3. Kết quả

| Đếm gì | x / N (toàn mẫu 1–5★) | % toàn mẫu | Trên tập 1–3★ (`x / 33`) | Ghi chú |
|---|---:|---:|---:|---|
| Tổng review phàn nàn 1–3★ | **33 / 100** | **33,0%** | 33 / 33 (100%) | MoMo 50 + MB Bank 50 |
| **Ít nhất 1 pain thuộc E3 (1–3★)** | **5 / 100** | **5,0%** | **5 / 33 (15,2%)** | Đã kiểm tay 0 dương tính giả |
| — `blocked_or_failed_tx` (chặn/khóa/lỗi chuyển) | 2 / 100 | 2,0% | 2 / 33 (6,1%) | Không rõ lý do bị khóa chuyển khoản |
| — `support_slow_or_loop` (CSKH không phản hồi) | 2 / 100 | 2,0% | 2 / 33 (6,1%) | Ticket/CSKH không hồi âm |
| — `unauth_or_security_risk` (trừ tiền lạ) | 2 / 100 | 2,0% | 2 / 33 (6,1%) | Đã trừ tiền lạ / đã xóa app vẫn trừ |
| — Giao nhau (`blocked` + `support`) | 1 / 100 | 1,0% | 1 / 33 (3,0%) | Vừa không chuyển được vừa không có CSKH |

## 4. ≥5 ví dụ cụ thể (nguyên văn ≤2 câu, đã ẩn danh)

1. `[MB_Bank_007 · MB Bank · 25/11/2026 · 1★ · blocked + support]`: *"App lỗi không chuyển được tiền. báo lỗi không cho chuyển, cskh thì không có phản hồi??"*
2. `[MB_Bank_024 · MB Bank · 23/11/2026 · 1★ · blocked]`: *"Tệ. Tối ngày bị khoá ko chuyển khoản được vì lý do vi phạm lỗi ngân hàng nhưng không biết vi phạm qq gì nữa riết tệ thật"*
3. `[MoMo_021 · MoMo · 25/11/2026 · 1★ · support]`: *"ticket hỗ trợ không bao giờ được trả lời. ticket hỗ trợ không bao giờ được trả lời"*
4. `[MoMo_003 · MoMo · 25/11/2026 · 1★ · unauth]`: *"App. App lol xoá r vẫn trừ tiền lừa đảo v tr"*
5. `[MB_Bank_038 · MB Bank · 22/11/2026 · 1★ · unauth]`: *"bị trừ tiền tk. bị trừ tiền"*

## 5. Giới hạn của data

- **Thiên lệch nguồn:** Người để lại review 1★ thường đang bức xúc; ngược lại, nạn nhân bị lừa đảo chuyển tiền thường ít viết lên App Store (họ báo công an hoặc nhắn tổng đài kín) nên tỉ lệ `5/100` là **cận dưới** của ca rủi ro thực tế và chỉ phản ánh **họ gặp chuyện gì**, chưa giải thích **vì sao bị lừa hay lúc đang gấp họ cần gì**.
- **Giới hạn độ phủ mẫu CP2:** Mới lấy ổn định 2 app (MoMo, MB Bank, `N=100`, 5 ngày gần nhất).
- **→ Kiểm chéo bằng nguồn 2 (xong trước CP3 10:00 Thứ Bảy):** Khảo sát ≥20 bạn cùng lớp ([`evidence/survey/questions.md`](survey/questions.md)) + phỏng vấn Mom Test ≥3 người ngoài nhóm (`evidence/interviews/P1..P3.md`) về trải nghiệm bị giữ giao dịch / gặp tin nhắn giục chuyển tiền trong 1–6 tháng qua.
