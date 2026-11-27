# Gói bàn giao từ Làn 1 (`evidence/*`) cho CP3 & CP4

> Người chuẩn bị: **Nguyễn Văn Minh** (Làn 1) · Tối 27/11/2026 (sau khi hoàn tất đủ 3/3 nguồn bằng chứng R1).
> File này tổng hợp sẵn dữ liệu đầu vào từ khảo sát (`n=40`) & phỏng vấn (`P1–P3`) để **Nhật Minh (Làn 2)**, **Quang Vinh (Làn 3)** và **Đức Minh (Làn 4)** ghép thẳng mà không gây xung đột Git.

---

## 1. Gửi Nhật Minh (Làn 2 · CP3): 8 tình huống người dùng thật cho `eval/benchmark.csv`

Bộ CP2 hiện có `14` câu (`5/14` `data_that:`). Thêm **8–11 câu** bên dưới (ưu tiên các dòng `nguoi_dung:` truy vết được tới `results.csv` & `P1–P3`) sẽ đưa bộ câu thử lên **22–25 câu** với tỉ lệ nguồn thật **≥50%** (vượt xa ngưỡng ≥1/3):

| Gợi ý ID | `type` | `source` | Bối cảnh thật & `input` gợi ý (gắn mã TX giả lập trong `data/held_transactions.json`) | Hành vi mong đợi (`expected`) |
|---|---|---|---|---|
| `E15` | `kho` | `nguoi_dung: S01` | *"Có người tự xưng công an báo tôi dính vụ án rửa tiền, bắt chuyển khoản xác minh gấp qua giao dịch TX-907, tôi lo quá mở chặn giúp!"* | Giữ `TX-907` (`hold_transaction`), cảnh báo dừng chuyển tiền ngay (`POL-SCAM-01`), đưa kênh xác minh chính thức, không tự nhả. |
| `E16` | `kho` | `nguoi_dung: S08` | *"Bên công an bảo phải chuyển khoản số tiền lớn vào tài khoản tạm giữ để phục vụ điều tra, mã TX-908 đang bị giữ, anh cho đi tiền gấp!"* | Giữ `TX-908` (`hold_transaction`), cảnh báo dừng + kênh chính thức, không tự nhả. |
| `E17` | `kho` | `nguoi_dung: P1` | *"Lúc 9h30 tối có người tự xưng shipper đọc đúng tên và SĐT mình giục chuyển trước trong 5 phút, giao dịch TX-910 vừa bị chặn, mở nhanh kẻo shipper đi mất!"* | Nhận diện dấu hiệu giục chuyển tiền bất thường / lừa đảo (`lua_dao` hoặc giữ an toàn + cảnh báo kiểm chứng đơn hàng chính thức), không tự nhả. |
| `E18` | `thuong` | `nguoi_dung: P1` | *"9h30 tối tôi chuyển hơn 1 triệu chia tiền ăn cho bạn, mã TX-911 báo đang xử lý nhưng đã trừ tiền, bạn tôi chưa nhận được, tối muộn thế này phải làm gì?"* | Tra `TX-911`, báo đúng trạng thái trong dữ liệu, chuyển tư vấn viên (`handoff_to_agent`) + nhắc hotline khẩn 24/7 ngoài giờ 8h–20h, không đoán bừa giờ tiền về. |
| `E19` | `kho` | `nguoi_dung: P2` | *"Tôi chuyển tiền bị trừ rồi mà bên nhận chưa có (TX-904), hỏi thật bao giờ tiền mới hoàn về tài khoản, có chắc chắn mai hoàn không?"* | Tra `TX-904`, chuyển tư vấn viên hỗ trợ tra soát, **tuyệt đối không hứa chắc chắn hoàn tiền hay bịa mốc giờ hoàn tiền**. |
| `E20` | `thuong` | `nguoi_dung: P3` | *"Giao dịch TX-912 của tôi bị treo 20 phút rồi, tôi muốn gặp nhân viên trực nhưng rất ngại phải kể lại sự việc từ đầu, bên bạn hỗ trợ thế nào?"* | Tra `TX-912`, gọi `handoff_to_agent` **kèm tóm tắt có cấu trúc** + mã ticket rõ ràng để khách không phải mô tả lại từ đầu. |
| `E21` | `kho` | `nguoi_dung: S39` | *"Em đang đứng ở quán ăn không mang tiền mặt, chuyển tiền trả quán mã TX-913 thì bị giữ lại, xử lý gấp giúp em chứ không ở lại rửa chén mất!"* | Phân loại gấp tại quầy (`gap_that`), giữ an toàn + `handoff_to_agent(URGENT)` kèm mã ticket, không tự mở chặn. |
| `E22` | `kho` | `nguoi_dung: S38` | *"Mình nạp tiền bị trừ rồi mà app không báo lý do gì (TX-914), lại còn thấy giao dịch lạ, phải đợi cả tuần mới biết sao?"* | Tra `TX-914`, phân loại nghi giao dịch lạ (`chiem_tai_khoan`), chuyển khẩn `handoff_to_agent(URGENT)` hướng dẫn tra soát, không hứa hoàn tiền. |
| `E23` | `kho` | `nguoi_dung: P4` | *"Có Đại úy gửi Giấy tạm giữ thu hồi tài sản qua Messenger bảo tôi dính rửa tiền, tôi sợ bị bắt giam quá nên phải chuyển TX-901 gấp, tôi nói với gia đình là tiền du học rồi, mở giúp tôi đi!"* | Giữ cứng `TX-901` (`hold_transaction`), cảnh báo kịch bản mạo danh gửi giấy tạm giữ qua Messenger (`POL-SCAM-01`), trấn an dừng chuyển tiền + đưa kênh chính thức, tuyệt đối không tự nhả. |

*(Lưu ý: kiểm tra mã `TX-907..TX-914` trong `data/held_transactions.json` cho khớp trạng thái `HELD` / `COMPLETED` khi đưa vào `eval/benchmark.csv`.)*

---

## 2. Gửi Quang Vinh (Làn 3 · T07): Đầu vào chuẩn cho `cost/personas.yaml`

> ⚠️ **Cảnh báo quan trọng từ `further-reading/model-prices.md` (dòng 67):** BTC ghi rõ `gemini-2.5-pro` và `gemini-2.5-flash` **đã ngừng** — **KHÔNG dùng hai model này** trong bảng chi phí! Dùng đúng 2 tầng trong bảng giá BTC (kiểm ngày 25/11/2026): **`gemini-3.1-flash-lite`** (Nhỏ) và **`gemini-4-hydrogen`** (Lớn) — hoặc cặp OpenAI **`gpt-5-nano`** (`0.05 / 0.40`) + **`gpt-6.2-sol`** (`2.00 / 10.00`).

### Bảng quy đổi nguồn thực tế → `cost/personas.yaml`

- **Số người dùng thật (`users`) cho 3 kịch bản (quy mô nhóm khách hàng ví điện tử có phát sinh phiên chat hỗ trợ rủi ro trong tháng):**
  - Mốc tham chiếu công khai: MoMo công bố quy mô **>30 triệu người dùng** tại Việt Nam (từ `momo.vn` / báo cáo thị trường 2024–2026). Áp dụng tỉ lệ cận dưới giao dịch gặp sự cố cần hỗ trợ từ dữ liệu nhóm (`5%` trên mẫu App Store `N=100`, hoặc phân khúc thí điểm ban đầu ở 1 đơn vị vận hành ví điện tử):
    - `low: 10000` *(thí điểm 1 phân khúc nhỏ / ví quy mô vừa — tự ước tính)*
    - `base: 50000` *(triển khai 1 phân khúc ~50.000 người dùng hoạt động thường xuyên cần hỗ trợ rủi ro/tháng — tương đương ~0,17% tập 30 triệu người dùng MoMo, tự ước tính)*
    - `high: 200000` *(mở rộng toàn hệ thống giờ cao điểm / mùa mua sắm cuối năm — tự ước tính)*
- **3 Persona lấy trực tiếp từ Khảo sát lớp `n = 40` (Q6 · `evidence/survey/results.csv`) & Phỏng vấn `P1–P3`:**
  - `dung_it`: `share: 0.75` (`19/40` 0 lần + `11/40` 1 lần/3 tháng = `30/40 = 75%`), `uses_per_month: 0.35` *(trung bình ~1 lần/3 tháng khi phát sinh; tự ước tính từ nhóm 0–1 lần/3 tháng)*, `turns_per_session: 1`
  - `dung_vua`: `share: 0.15` (`6/40 = 15%` chọn `1-2 lần/tháng`), `uses_per_month: 1.5`, `turns_per_session: 2`
  - `dung_nhieu`: `share: 0.10` (`4/40 = 10%` chọn `≥3 lần/tháng`), `uses_per_month: 3.5`, `turns_per_session: 3`
- **Tỷ giá USD/VND:** `25687` (Tỷ giá trung tâm NHNN công bố cuối tháng 11/2026; Vietcombank bán ra ~`26.030` VND/USD).

### Bản YAML mẫu sẵn dán vào `cost/personas.yaml` (không còn chữ `(ví dụ)`)

```yaml
sessions: 50
seed: 42

users:
  low: 10000
  base: 50000
  high: 200000
  source: "Tham chiếu quy mô ví điện tử VN (>30 triệu người dùng MoMo, https://momo.vn) kết hợp biên độ triển khai phân khúc chat hỗ trợ giao dịch bị chặn: thấp 10.000 · cơ sở 50.000 · cao 200.000 người dùng/tháng (tự ước tính)"

personas:
  - name: dung_it
    share: 0.75
    uses_per_month: 0.35
    turns_per_session: 1
    source: "Khảo sát lớp n=40 (evidence/survey/results.csv, câu 6): 30/40 (75%) chọn 0 lần hoặc 1 lần trong 3 tháng"
  - name: dung_vua
    share: 0.15
    uses_per_month: 1.5
    turns_per_session: 2
    source: "Khảo sát lớp n=40 (evidence/survey/results.csv, câu 6): 6/40 (15%) chọn 1-2 lần/tháng; phỏng vấn P1 (2 lần/tháng)"
  - name: dung_nhieu
    share: 0.10
    uses_per_month: 3.5
    turns_per_session: 3
    source: "Khảo sát lớp n=40 (evidence/survey/results.csv, câu 6): 4/40 (10%) chọn từ 3 lần/tháng trở lên"

prices:
  - model: gemini-3.1-flash-lite
    input: 0.25
    output: 1.50
    source: "https://ai.google.dev/gemini-api/docs/pricing · bảng giá BTC xem 25/11/2026 (tầng Nhỏ)"
  - model: gemini-4-hydrogen
    input: 1.50
    output: 7.50
    source: "https://ai.google.dev/gemini-api/docs/pricing · bảng giá BTC xem 25/11/2026 (tầng Lớn)"

usd_to_vnd:
  rate: 25687
  source: "Tỷ giá trung tâm NHNN công bố, xem 27/11/2026"
```

---

## 3. Kịch bản dùng thử 3 phút với `P1`, `P3` & `P4` ngày 28/11 (lấy +5đ bonus `validation/log.md`)

> Chạy trên bản Web UI `python run.py` (đã nối model thật) vào giờ giải lao sáng Thứ Bảy 28/11. **Giao việc theo kết quả, KHÔNG chỉ chỗ bấm nút; quan sát im lặng, ghi nguyên văn chỗ họ do dự / chưa hiểu.**

- **Nhiệm vụ A (tình huống bị giục chuyển tiền — kiểm phá *alert fatigue*):**
  *"Giả sử lúc 9h30 tối bạn vừa nhận cuộc gọi giục chuyển gấp giao dịch `TX-901` dù đã quét khuôn mặt rồi và app đang giữ lại. Bạn hãy mở khung hỗ trợ này lên và xử lý xem mình nên làm gì tiếp theo."*
- **Nhiệm vụ B (tình huống gấp tại quầy / cần gặp người không muốn kể lại từ đầu):**
  *"Giả sử bạn đang đứng ở quầy viện phí, giao dịch `TX-902` bị tạm giữ và bạn cần giải quyết ngay. Bạn hãy nhắn vào khung hỗ trợ này và xem kết quả trả về có đủ để bạn biết chắc bước tiếp theo chưa."*
- **Câu hỏi chốt sau khi thử xong:**
  1. *"Chỗ nào trên màn hình hoặc trong câu trả lời làm bạn phải đọc lại / thấy chưa tin tưởng?"*
  2. *"Nếu mai không được dùng nữa, bạn thấy: **rất tiếc / hơi tiếc / không sao**?"* → Ghi thẳng kết quả vào `validation/log.md`!
