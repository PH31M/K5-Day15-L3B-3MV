# Data Card — Nhóm 3MV · Track E (E3)

> Bản CP2 (27/11/2026) — mô tả toàn bộ dữ liệu dùng để chạy thử bản mẫu và đào bằng chứng.
> **Cam kết an toàn:** Không chứa sao kê thật, giao dịch thật, số tài khoản, OTP hay thông tin cá nhân thật của bất kỳ ai.

## Dataset 1 · `data/held_transactions.json` (`synthetic`)

| Hạng mục | Chi tiết |
|---|---|
| Dùng để làm gì | Nguồn tra cứu cho công cụ `lookup_transaction` / `hold_transaction` trong `codebase/tools.py` và bộ câu thử `eval/benchmark.csv`. |
| Từ đâu | Nhóm tự sinh có chủ đích theo đúng kịch bản `track-e-finance.md` (E3), gắn nhãn `synthetic`, `seed = 20261127`. |
| Xử lý & Thiết kế an toàn | Gồm 15 giao dịch dựng (`TX-901` → `TX-915`) với 9 trường công khai (`tx_id`, `user_alias`, `status`, `amount_vnd`, `recipient_label`, `created_at_vn`, `face_verified`, `hold_reason_public`, `completed_flag`). **Cố ý KHÔNG lưu ngưỡng tiền/điểm rủi ro nội bộ** để model không thể bị khai thác lộ ngưỡng gian lận. |
| Số dòng | 15 giao dịch (12 đang `HELD`, 3 đã `COMPLETED`). |
| Phiên bản / ngày tạo | `v1.0` · 27/11/2026 · kiểm tay đủ 15/15 dòng bởi Đức Minh & Nhật Minh. |
| Nhãn | `synthetic` (**không dùng làm bằng chứng pain**). |
| Giới hạn | Số lượng tình huống còn gọn (15 mã), chưa mô phỏng lịch sử nhiều giao dịch liên tiếp của cùng 1 người dùng. |

## Dataset 2 · `data/support_policies.json` (`public-summary` / `synthetic`)

| Hạng mục | Chi tiết |
|---|---|
| Dùng để làm gì | Nguồn căn cứ chính sách cho công cụ `lookup_policy` trong `codebase/tools.py`. |
| Từ đâu | Tổng hợp nguyên tắc công khai của ví điện tử Việt Nam (mô tả bối cảnh trong `track-e-finance.md`: trợ lý 24/7, tư vấn viên trực 8h–20h, khuyến cáo chống lừa đảo công an/cơ quan nhà nước); hotline dùng số dựng (`1900-0000-MAU`). |
| Số dòng | 6 chính sách (`POL-SCAM-01`, `POL-HOLD-02`, `POL-ATO-03`, `POL-PRIVACY-04`, `POL-SECRET-05`, `POL-SCOPE-06`). |
| Phiên bản / ngày tạo | `v1.0` · 27/11/2026. |
| Nhãn | `synthetic` (dựa trên nguyên tắc công khai, không liên kết bất kỳ hãng ví nào). |
| Giới hạn | Chỉ phủ phạm vi E3 (giao dịch bị chặn / nghi lừa đảo / chiếm TK / người thân / bảo mật). |

## Dataset 3 · `evidence/reviews_sample_anonymized.csv` (dữ liệu công khai đã ẩn danh — dùng cho bằng chứng R1)

| Hạng mục | Chi tiết |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain Nguồn 1 (`evidence/data-mining.md`) và tạo câu thử nguồn thật (`data_that:`) cho `eval/benchmark.csv`. |
| Từ đâu | Apple App Store Việt Nam RSS công khai: MoMo (`id=918751511`, 50 dòng) và MB Bank (`id=1205807363`, 50 dòng), tải bằng `evidence/mine_reviews.py` ngày 27/11/2026. |
| Xử lý những bước gì | Bỏ hoàn toàn tên tác giả & URL hồ sơ; cắt tối đa 2 câu (`<= 260` ký tự); gắn nhãn 3 chủ đề E3 chỉ trên review phàn nàn `rating <= 3` để loại dương tính giả 5★. |
| Số dòng | 100 dòng (21/11/2026 → 25/11/2026), trong đó 33 review 1–3★ và 5 review khớp trực tiếp pain E3. |
| Nhãn | Thật (review công khai đã ẩn danh). |
| Giới hạn | Nghiêng về người dùng bức xúc trên App Store; ít phản ánh các nạn nhân bị lừa đảo chuyển tiền kín → kiểm chéo bằng khảo sát lớp ≥20 người và phỏng vấn ≥3 người trước CP3. |
