# Tổng hợp bằng chứng pain — Nhóm 3MV · Track E (E3)

> Hoàn thiện **đủ cả 3/3 nguồn độc lập đều vượt ngưỡng R1** trước CP3 (**10:00 Thứ Bảy 28/11**). Chấm ở rubric R1.
> Cả Nguồn 1 và Nguồn 2 đều có script tái lập ngoại tuyến 100%; Nguồn 3 có đủ log nguyên văn `P1.md..P4.md` (`4` người ngoài nhóm) + **3 người cam kết dùng thử bản demo ngày 28/11** (`P1`, `P3`, `P4` — chuẩn bị trọn bộ cho `validation/log.md`).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | Quy mô & tái lập | File |
|---|:---:|---|---|
| **Nguồn 1 · Đào data công khai** (App Store VN: MoMo + MB Bank, 21–25/11/2026) | ☑ Đạt | `N = 100` review (1–5★), `33` review 1–3★ · `python3 evidence/mine_reviews.py --recount` | [`evidence/data-mining.md`](data-mining.md) · [`reviews_sample_anonymized.csv`](reviews_sample_anonymized.csv) |
| **Nguồn 2 · Khảo sát lớp** (AI20K L3A/L3B, mở 18:15 · chốt đợt 1 lúc 18:55 ngày 27/11/2026) | ☑ Đạt | `n = 40` phiếu hợp lệ (từ `41` dòng thô, loại `1` dòng trống lúc cập nhật form; đã xoá hoàn toàn cột câu 8 & giờ chi tiết, kiểm `0` SĐT/email) · `python3 evidence/survey/analyze_survey.py` | [`evidence/survey/questions.md`](survey/questions.md) · [`evidence/survey/results.csv`](survey/results.csv) |
| **Nguồn 3 · Phỏng vấn sâu Mom Test** (4 người dùng ngoài nhóm, 27/11/2026) | ☑ Đạt | `4/4` người ngoài nhóm (`P1`–`P4`), hỏi theo [`GUIDE.md`](interviews/GUIDE.md) · **3/4 người cam kết test demo ngày 28/11** | [`P1.md`](interviews/P1.md) · [`P2.md`](interviews/P2.md) · [`P3.md`](interviews/P3.md) · [`P4.md`](interviews/P4.md) |

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

### Nguồn 3 · Phỏng vấn sâu Mom Test (`4/4` người gặp sự cố giao dịch / lừa đảo E3 · *n nhỏ không ghi %*)

- Số người gặp sự cố giao dịch treo/trừ tiền: **3/4 người** (`P1`, `P2`, `P3`) · gặp lừa đảo giục chuyển tiền trực tiếp: **2/4 người** (`P1` giả shipper, `P4` giả Đại úy vụ án rửa tiền đã mất thật 300k & hàng xóm mất 70 triệu) · gặp chatbot chung chung/vòng vo: **2/4 người** (`P1`, `P3`; `P2` gọi thẳng tổng đài) · bỏ qua cảnh báo chữ nhỏ: **2/4 người** (`P1`, `P2`).
- Thời gian xử lý sự cố ban đầu: **20–60 phút** (`P3`: 20–30 phút, `P1`: 45 phút, `P4`: ~60 phút); thời gian hoàn tiền thực tế: **từ sáng hôm sau (`P1`) đến 3 ngày (`P2`)**.
- Cam kết dùng thử bản demo ngày 28/11: **3/4 người** (`P1`, `P3`, `P4`).

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Học viên AI20K (ngoài nhóm, dùng app ngân hàng & ví) | Có (treo giao dịch sau 21h + gọi giả shipper) | 2 lần | **45 phút** kiểm tra/chờ chat (sáng hôm sau mới hoàn) | Bỏ ngang chatbot vì rớt hàng chờ sau 20h, chuyển bù từ ví khác rồi gọi hotline hôm sau |
| P2 | Sinh viên dùng app ngân hàng BIDV (ngoài nhóm) | Một phần (bị trừ tiền không tới, bỏ sót cảnh báo chữ nhỏ) | 1 lần | **3 ngày** mới hoàn tiền *(giờ gọi tổng đài: không nhớ)* | Gọi thẳng tổng đài điện thoại (chưa từng dùng chatbot) |
| P3 | Người dùng app ngân hàng thường xuyên (ngoài nhóm) | Có (bị trừ tiền không rõ trạng thái + bot chung chung) | 0–1 lần *(gần nhất 1–2 tháng trước)* | **20–30 phút** kiểm tra & tìm cách tra soát | Chụp màn hình, nhắn chatbot rồi chuyển tổng đài (phải kể lại tình huống nhiều lần) |
| P4 | Sinh viên / người dùng chuyển khoản (ngoài nhóm) | **Có (bị giả Đại úy dọa rửa tiền, mất thật 300k; hàng xóm mất 70 triệu)** | 0 lần *(sự cố năm 2024)* | **~60 phút** giải quyết (và mất 300k thật) | Bị cô lập vì sợ bắt giam, gọi mẹ nói dối "trao đổi du học", không biết kiểm chứng qua kênh chính thức |

## 3. ≥5 trích dẫn / ví dụ nguyên văn (đã ẩn danh, đủ cả 3 nguồn)

1. *"App lỗi không chuyển được tiền. báo lỗi không cho chuyển, cskh thì không có phản hồi??"* — App Store VN `[MB_Bank_007 · 1★ · 25/11/2026]`
2. *"Tệ. Tối ngày bị khoá ko chuyển khoản được vì lý do vi phạm lỗi ngân hàng nhưng không biết vi phạm qq gì nữa riết tệ thật"* — App Store VN `[MB_Bank_024 · 1★ · 23/11/2026]`
3. *"Mình bị Công an yêu cầu chuyển tiền vì mình dính 'vụ án rửa tiền'"* — Khảo sát `S01` *(27/11/2026)*
4. *"Lần đó là công an lừa số tiền lớn(9 chữ số)"* — Khảo sát `S08` *(27/11/2026)*
5. *"Nạp tiền vào VISA a bị trừ tiền nhưng ngân hàng lại không thông báo lý do gì. Phải đến 1 tuần sau thì ngân hàng mới gửi thông tin"* — Khảo sát `S38` *(27/11/2026)*
6. *"Đợi được tầm 15 phút, mình lỡ thoát app ra trả lời tin nhắn nhóm trên Messenger, quay lại thì mất phiên chat và bị đẩy xuống xếp hàng lại từ đầu. Bực quá mình bỏ ngang luôn..."* — Phỏng vấn `P1` *(27/11/2026)*
7. *"Còn cái màn hình cảnh báo trước khi quét Face ID trên app hiện tại rất dễ bị lướt qua... thành phản xạ cơ bắp rồi, cứ hiện popup xác nhận là mình đưa mặt vào quét trong chưa tới 1 giây chứ không bao giờ đọc nội dung bên trong."* — Phỏng vấn `P1` *(27/11/2026)*
8. *"Mặc dù trc khi ck ngân hàng cũng có thông báo về việc có vấn đề nhưng chữ hơi nhỏ nên t ko để ý lắm."* — Phỏng vấn `P2` *(27/11/2026)*
9. *"Nếu vấn đề phức tạp hơn thì phải chuyển sang tổng đài hoặc nhân viên hỗ trợ. Việc phải mô tả lại tình huống nhiều lần khá mất thời gian."* — Phỏng vấn `P3` *(27/11/2026)*
10. *"Phản xạ là mình nhận được Giấy tạm giữ thu hồi tài sản gửi qua Mess, gọi cho mẹ nói dối là trao đổi du học... Mình chưa từng cài ứng dụng lạ nào, nhưng điều khiến bị cuống là do sợ bị bắt giam."* — Phỏng vấn `P4` *(27/11/2026)*

## 4. Các nguồn có khớp nhau không (Triangulation 3 nguồn)

- **Chỗ khớp mạnh across cả 3 nguồn:** Review App Store (`MB_Bank_007`, `MB_Bank_024`, `MoMo_021`), khảo sát (`23/29 = 79,3%` gặp vướng mắc CSKH/bot; `13/28 = 46,4%` mất ≥5 phút), và phỏng vấn (`P1` mất 45 phút + rớt hàng chờ sau 20h, `P3` mất 20–30 phút + phải kể lại nhiều lần) đều hội tụ vào cùng điểm nghẽn: **khi giao dịch bị chặn/treo hoặc trừ tiền bất thường, người dùng không có thông tin rõ ràng để biết bước tiếp theo và bị kẹt ở bot FAQ chung chung / chờ lâu sau 20h**.
- **Chỗ lệch giữa dữ liệu công khai và người dùng thật:** App Store công khai chỉ ghi nhận `5/100 (5,0%)` ca E3 và gần như vắng bóng ca bị giả công an lừa đảo; trong khi khảo sát kín (`14/40 = 35,0%`, gồm `S01`, `S08`) và phỏng vấn (`P1` giả shipper, `P4` bị giả Đại úy gửi "Giấy tạm giữ" qua Messenger mất thật 300k & hàng xóm mất 70 triệu) cho thấy **tỉ lệ gặp lừa đảo giục chuyển tiền ngoài đời cao hơn rất nhiều so với review công khai**.
- **4 phát hiện MỚI / NGƯỢC với giả thuyết ban đầu từ phỏng vấn sâu `P1–P4`:**
  1. **Thao túng tâm lý không cần mã độc — nạn nhân còn tự nói dối gia đình (`P4`):** `P4` chưa từng cài app lạ nhưng vì sợ bị bắt giam nên tự chuyển tiền và gọi mẹ nói dối là *"trao đổi du học"* → khẳng định sống còn vì sao E3 bắt buộc giữ giao dịch ngay cả khi chính chủ tự xác thực (`face_verified=true`) và cảnh báo rõ *công an không gửi giấy tạm giữ qua Messenger / không yêu cầu chuyển tiền*.
  2. **Alert fatigue & phản xạ cơ bắp Face ID (`P1`, `P2`):** Ngay cả người trẻ rành công nghệ cũng lướt qua cảnh báo chữ nhỏ trong `<1 giây` khi đang vội/đa nhiệm → cảnh báo của E3 phải ngắn, nổi bật, **nêu đúng dữ kiện cụ thể của giao dịch** thay vì thông báo chung chung.
  3. **Nỗi đau "kể lại từ đầu" khi chuyển tư vấn viên (`P3`) & rớt hàng chờ sau 20h (`P1`):** Người dùng vẫn muốn dùng kênh chính thức trong app vì độ tin cậy (`P3`), nên công cụ `handoff_to_agent` kèm **bản tóm tắt có cấu trúc + mã ticket + hotline 24/7 ngoài giờ** giải quyết đúng điểm đau thật.
  4. **Một bộ phận người dùng bỏ qua chatbot gọi thẳng hotline (`P2`):** Nhắc nhóm không phóng đại rằng 100% người dùng sẽ chat bot; giá trị cốt lõi là những ai vào kênh hỗ trợ được phân loại đúng, cấp mã tra soát / chuyển khẩn ngay trong vài giây.

## 5. Kết luận

- Giả thuyết ở [`evidence/hypothesis.md`](hypothesis.md): **ĐÚNG** và được tinh chỉnh sâu hơn ở 3 điểm thiết kế sản phẩm từ phỏng vấn `P1–P4`: (1) phá vỡ cô lập tâm lý & *alert fatigue* `<1 giây` bằng cảnh báo nêu rõ dữ kiện giao dịch và kịch bản giả công an qua Messenger (`P1`, `P2`, `P4`), (2) tóm tắt cấu trúc khi `handoff_to_agent` để khách không phải kể lại từ đầu (`P3`), và (3) giữ cứng luật **không tự nhả tiền** + **không hứa hoàn tiền/mốc giờ hoàn tiền** nếu chưa có kết quả tra soát.
- **Bước tiếp theo (cho +5đ bonus `validation/log.md`):** Chạy phiên dùng thử 3 phút với **`P1`**, **`P3`** và **`P4`** vào ngày 28/11 trên bản chạy thử Web UI (`python run.py`) với model thật.

## Nhật ký hoàn thành phỏng vấn sâu (không ghi tên thật)

| Mã | Vai | Thời điểm | Trạng thái | Cam kết test demo 28/11 |
|---|---|---|:---:|:---:|
| P1 | Học viên AI20K (ngoài nhóm, dùng app ngân hàng & ví) | 27/11/2026 | ☑ Đã xong ([`P1.md`](interviews/P1.md)) | **Có** |
| P2 | Sinh viên dùng app ngân hàng BIDV (ngoài nhóm) | 27/11/2026 | ☑ Đã xong ([`P2.md`](interviews/P2.md)) | Không |
| P3 | Người dùng app ngân hàng thường xuyên (ngoài nhóm) | 27/11/2026 | ☑ Đã xong ([`P3.md`](interviews/P3.md)) | **Có** |
| P4 | Sinh viên / người dùng chuyển khoản (từng bị giả Đại úy dọa rửa tiền) | 27/11/2026 | ☑ Đã xong ([`P4.md`](interviews/P4.md)) | **Có** |

## Phụ lục · Đối chứng thứ cấp (Desk Research — KHÔNG tính vào 3 nguồn sơ cấp)

- Nhóm bổ sung báo cáo đối chứng thứ cấp từ thảo luận công khai (VOZ, VnExpress, Báo Đồng Nai, Lao Động, MoMo Hỏi Đáp) tại [`evidence/desk-research.md`](desk-research.md) — **tách biệt hoàn toàn khỏi 4 cuộc phỏng vấn trực tiếp `P1–P4`** và không cộng gộp vào mẫu số `N=100` / `n=40`.
- Kết quả đối chứng khớp hoàn toàn với 3 nguồn sơ cấp: cửa sổ chặn tiền chỉ tính bằng phút, tổng đài quá tải/nghỉ ngoài giờ, kịch bản lừa đảo nhắm thẳng vào tâm lý sợ hãi & share màn hình OTP, và cách duy nhất giúp người dùng thoát là dừng giao dịch + đảo kênh gọi số chính thức.
