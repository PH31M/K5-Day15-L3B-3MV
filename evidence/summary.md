# Tổng hợp bằng chứng pain — Nhóm 3MV · Track E (E3)

> Cập nhật cho **CP2 (27/11/2026)** và hoàn thiện tiếp phỏng vấn P1–P3 trước **CP3 (10:00 Thứ Bảy 28/11)**. Chấm ở rubric R1.
> Cả **2 nguồn độc lập** đều đã **đạt ngưỡng R1** ngay tại mốc CP2, có script tái lập ngoại tuyến 100% không cần mạng.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | Quy mô & tái lập | File |
|---|:---:|---|---|
| **Nguồn 1 · Đào data công khai** (App Store VN: MoMo + MB Bank, 21–25/11/2026) | ☑ Đạt | `N = 100` review (1–5★), `33` review 1–3★ · `python3 evidence/mine_reviews.py --recount` | [`evidence/data-mining.md`](data-mining.md) · [`reviews_sample_anonymized.csv`](reviews_sample_anonymized.csv) |
| **Nguồn 2 · Khảo sát lớp** (AI20K L3A/L3B, mở 18:15 · chốt đợt 1 lúc 18:55 ngày 27/11/2026) | ☑ Đạt | `n = 40` phiếu hợp lệ (từ `41` dòng thô, loại `1` dòng trống lúc cập nhật form; đã xoá hoàn toàn cột câu 8 & giờ chi tiết, kiểm `0` SĐT/email) · `python3 evidence/survey/analyze_survey.py` | [`evidence/survey/questions.md`](survey/questions.md) · [`evidence/survey/results.csv`](survey/results.csv) |
| **Nguồn 3 · Phỏng vấn sâu Mom Test** (bổ sung cho CP3) | ☐ Đang hẹn | Dự kiến ≥3 người ngoài nhóm tối 27/11 (`P1.md`..`P3.md`) | `evidence/interviews/` |

## 2. Số chính

### Nguồn 1 · Đào data App Store VN (`N = 100`, 21–25/11/2026)
- Tổng review phàn nàn 1–3★: **33/100 (33,0%)**.
- Review 1–3★ liên quan trực tiếp pain E3 (chặn/khóa chuyển tiền, trừ tiền lạ, CSKH không phản hồi): **5/100 (5,0%)** toàn mẫu = **5/33 (15,2%)** tập phàn nàn 1–3★ (đã kiểm tay 0 dương tính giả).

### Nguồn 2 · Khảo sát hành vi người dùng ví / app ngân hàng (`n = 40` phiếu hợp lệ)
- **Đúng đối tượng dùng app tài chính (Q1):** `31/40 (77,5%)` dùng App ngân hàng (VCB/MB/TCB/BIDV…), `21/40 (52,5%)` dùng MoMo, `6/40 (15,0%)` dùng ZaloPay — khớp trực tiếp phạm vi Nguồn 1.
- **Tỉ lệ gặp ít nhất 1 tình huống rủi ro E3 trong 6 tháng qua (Q2):** **22/40 (55,0%)** *(gồm: **14/40 = 35,0%** bị gọi/nhắn giục chuyển tiền giả công an/thuế; **8/40 = 20,0%** đang cần gấp tại quầy/viện phí thì app chặn/treo; **6/40 = 15,0%** thấy trừ tiền lạ / nghi truy cập trái phép)*.
- **Vướng mắc với Chat bot / CSKH hiện tại (Q4):** **23/40 (57,5%)** toàn mẫu = **23/29 (79,3%)** nhóm từng liên hệ hỗ trợ gặp ít nhất 1 vướng mắc:
  - Bot menu cứng / vòng vo, không đúng tình huống: **17/40 (42,5%)**
  - Phải gửi ticket chờ lâu trong khi đang cần gấp: **10/40 (25,0%)**
  - Tổng đài bận / sau 20h khó gặp người thật: **5/40 (12,5%)**
- **Thời gian xử lý thực tế (Q3 — dữ liệu Impact cho `spec.md §2`):** **13/40 (32,5%)** tổng mẫu = **13/28 (46,4%)** nhóm từng xử lý mất **≥5 phút** mới biết cần làm gì, trong đó **4/40 (10,0%)** mất **trên 30 phút hoặc chờ tới hôm sau**.
- **Nghịch lý sinh trắc học (Q5 — chứng minh luật giữ giao dịch kể cả khi `face_verified=true`):** **23/40 (57,5%)** nhận định Face ID thành công *chưa chắc an toàn* vì vẫn có thể bị thao túng ép chuyển, trong khi **8/40 (20,0%)** tin *chắc chắn an toàn* và **9/40 (22,5%)** *chưa từng nghĩ tới* → tổng **17/40 (42,5%)** có rủi ro chủ quan nếu không được cảnh báo chặn đúng lúc.
- **Tần suất 3 tháng qua (Q6 — cơ sở persona cho `cost/personas.yaml`):** `0 lần`: **19/40 (47,5%)** · `1 lần / 3 tháng`: **11/40 (27,5%)** · `1–2 lần / tháng`: **6/40 (15,0%)** · `≥3 lần / tháng`: **4/40 (10,0%)**.

### Nguồn 3 · Phỏng vấn sâu Mom Test *(cập nhật đầy đủ trước CP3 10:00 Thứ Bảy)*

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | *(đang hẹn tối 27/11)* | | | | |
| P2 | *(đang hẹn tối 27/11)* | | | | |
| P3 | *(đang hẹn tối 27/11)* | | | | |

## 3. ≥5 trích dẫn / ví dụ nguyên văn (đã ẩn danh, đa nguồn)

1. *"App lỗi không chuyển được tiền. báo lỗi không cho chuyển, cskh thì không có phản hồi??"* — App Store VN `[MB_Bank_007 · 1★ · 25/11/2026]`
2. *"Tệ. Tối ngày bị khoá ko chuyển khoản được vì lý do vi phạm lỗi ngân hàng nhưng không biết vi phạm qq gì nữa riết tệ thật"* — App Store VN `[MB_Bank_024 · 1★ · 23/11/2026]`
3. *"Mình bị Công an yêu cầu chuyển tiền vì mình dính 'vụ án rửa tiền'"* — Khảo sát `S01` *(27/11/2026)*
4. *"Lần đó là công an lừa số tiền lớn(9 chữ số)"* — Khảo sát `S08` *(27/11/2026)*
5. *"Nạp tiền vào VISA a bị trừ tiền nhưng ngân hàng lại không thông báo lý do gì. Phải đến 1 tuần sau thì ngân hàng mới gửi thông tin"* — Khảo sát `S38` *(27/11/2026)*
6. *"Dùng agribank, đi ăn không có tiền mặt nhưng không ck được với lí do bảo trì hệ thống. Đã xảy ra khá nhiều lần (5-7 lần). Ở lại quán rửa chén."* — Khảo sát `S39` *(27/11/2026)*
7. *"Trả tiền subscribe dịch vụ claude, thẻ từ chối giao dịch và khóa luôn. Tới giờ mình vẫn chưa mở lại (TPBank)."* — Khảo sát `S40` *(27/11/2026)*

## 4. Các nguồn có khớp nhau không (Triangulation)

- **Chỗ khớp hoàn toàn:** Cả review App Store (`MB_Bank_007`, `MB_Bank_024`, `MoMo_021`) lẫn khảo sát (`23/29 = 79,3%` người từng nhắn hỗ trợ gặp vướng mắc; `S38`, `S39`, `S40`) đều xác nhận cùng một nút thắt: **khi giao dịch/thẻ bị chặn hoặc trừ tiền bất thường, người dùng không biết lý do và gặp bot menu cứng / ticket chờ quá lâu**.
- **Chỗ lệch có ý nghĩa quan trọng:** Trên App Store công khai chỉ thấy `5/100 (5,0%)` ca E3 và **gần như không có** review kể chuyện bị giả công an lừa đảo; ngược lại, trong khảo sát kín `n = 40`, tới **14/40 (35,0%)** từng bị gọi/nhắn giục chuyển tiền giả công an/thuế (`S01`, `S08` mức thiệt hại tới 9 chữ số). Điều này **xác nhận giả định về thiên lệch nguồn**: nạn nhân lừa đảo ít viết review công khai lên App Store nên số đào data chỉ là **cận dưới** của quy mô rủi ro thực tế.

## 5. Kết luận

- Giả thuyết ở [`evidence/hypothesis.md`](hypothesis.md): **ĐÚNG** và được củng cố mạnh hơn ở 2 điểm thiết kế cốt lõi:
  1. **Nỗi đau bot cứng/chậm là rất lớn (`79,3%` người từng liên hệ CSKH gặp vướng mắc)** → chứng minh giá trị của luồng phân loại 3 bước + tóm tắt chuyển tư vấn viên khẩn ngay.
  2. **Rủi ro bị thao túng ép chuyển tiền cực phổ biến (`35,0%`) trong khi `42,5%` chưa nhận thức đầy đủ rủi ro sau khi quét Face ID** → củng cố tuyệt đối luật cứng: AI không bao giờ tự nhả giao dịch (`release_transaction` bị chặn ở tầng code) và tiếp tục giữ ca nghi lừa đảo kể cả khi `face_verified = true`.
- **Điều vẫn chưa biết (sẽ làm rõ qua phỏng vấn P1–P3 tối 27/11):** Diễn biến tâm lý cụ thể trong 5 phút đầu khi người dùng bị giục chuyển tiền hoặc kẹt tại quầy — câu cảnh báo ngắn gọn kiểu nào khiến họ dừng lại thay vì cáu gắt bỏ qua.

## Lịch hẹn phỏng vấn sâu (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| P1 · Học viên đại học dùng App ngân hàng/MoMo (từng gặp cuộc gọi giả công an) | Tối 27/11 · 20:00 | ☐ |
| P2 · Người đi làm dùng ví/thẻ thanh toán thường xuyên (từng bị chặn/khóa thẻ) | Tối 27/11 · 20:30 | ☐ |
| P3 · Người thân / người dùng phổ thông hay chuyển khoản | Tối 27/11 · 21:00 | ☐ |
