# Reflection — Nguyễn Văn Minh

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
- Thành viên nhóm 3MV (Lớp L3B, Track E · mã học viên `2A202604117`), phụ trách chính **Làn 1 (Bằng chứng pain `evidence/*`)**, bàn giao đầu vào khảo sát/phỏng vấn cho đánh giá & chi phí (`evidence/handoff-cp3-cp4.md`), và nâng cấp hạ tầng kiểm thử repo.
- Xây dựng trọn bộ **3/3 nguồn bằng chứng sơ cấp vượt ngưỡng R1** có script tái lập 100% ngoại tuyến + phụ lục đối chứng thứ cấp tách bạch: đào review Apple App Store VN (`N=100` MoMo & MB Bank — `evidence/mine_reviews.py`, `evidence/data-mining.md`, commit `03f33a9`), khảo sát lớp (`n=40` phiếu hợp lệ đã ẩn danh sạch 0 SĐT/email — `evidence/survey/results.csv`, `analyze_survey.py`, commit `cb6c3c3`), 4 phỏng vấn Mom Test (`evidence/interviews/P1.md`–`P4.md`, `evidence/summary.md`, commits `ce45fd5`, `2caeeb2`) và `evidence/desk-research.md`.
- Tái cấu trúc sâu lõi `codebase/` + bộ mini-fuzz & `make verify` (`bb8629e`), dựng bản nháp Web UI X-Ray 3 cột trên nhánh `feat/xray-stage-ui` (`fb61bfa`, đã được nhóm nâng cấp và merge vào `main` ở `227754f`), và bổ sung GitHub Actions CI + cổng kiểm cơ học toàn repo (`tests/test_repo_guards.py`, `.github/workflows/verify.yml`, commit `5c614e8`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
- Dùng trợ lý coding AI (Antigravity CLI) để viết script Python stdlib cào/đếm review (`mine_reviews.py`), script ẩn danh hóa & thống kê khảo sát (`analyze_survey.py`), khung kịch bản Mom Test, bản đầu Web UI X-Ray (`app.py`), và bộ test cơ học `test_repo_guards.py`.
- **Những chỗ bắt buộc phải tự kiểm và sửa lại output AI:**
  - Bộ đếm review App Store bản đầu gán nhầm một số đánh giá 5★ góp ý tính năng và review phàn nàn phí dịch vụ dùng từ lóng *"lừa đảo"* vào nhóm pain E3; mình đọc tay 30 dòng đầu và chỉnh luật chỉ lấy 1–3★ kèm từ loại trừ để đưa dương tính giả về `0`.
  - Khi hợp nhất góp ý nâng cấp form khảo sát, mình loại câu hỏi giả định/dẫn dắt (*"nếu đang bị lừa bạn muốn hệ thống làm gì"*) và giữ câu đo thời gian xử lý thực tế chuẩn Mom Test; chủ động tải file thô ngoài repo, xoá hoàn toàn cột câu 8 chứa 2 SĐT cá nhân trước khi xuất `results.csv` để đảm bảo `0` PII.
  - Trực tiếp thực hiện phỏng vấn `P1–P4`, giữ nguyên bằng chứng phản biện (`P2` không dùng chatbot và từ chối thử demo) và tách riêng dữ liệu thứ cấp VOZ/báo chí sang `evidence/desk-research.md`, tuyệt đối không trộn vào mẫu số phỏng vấn trực tiếp.

3. **Một câu thử / lỗi trượt của nhóm và mình học được gì từ nó:**
- Ở giai đoạn trước CP2 (`bb8629e`), bộ mini-fuzz phát hiện **3 ca dò ngưỡng trượt** và đặc biệt là **lỗ hổng không che OTP có khoảng trắng (`"Mã xác thực: 482 910"`)** vốn bị chế độ `fake` che khuất vì template không lặp lại input. Sau đó trên model thật (`openai/gpt-4.1-mini`), dù cải tiến `8d89c64` nâng điểm từ **16/25 (64%) → 21/25 (84%, +20 điểm phần trăm)** với `0` câu tụt `1 → 0`, lượt 2 (`run-2@20261128-121029`) vẫn còn trượt **4 câu** — đáng nhớ nhất là **`E22`** khi LLM tự diễn giải cờ `reversible=True` của tool `hold_transaction` thành câu *"có thể hoàn tác"* khiến khách dễ hiểu nhầm là lấy lại được tiền.
- Bài học lớn nhất rút ra: không bao giờ đánh giá an toàn chỉ qua mock hay điểm tổng; cần test qua *leaky stub adapter* từ đầu, đối chiếu từng câu trên model thật, và giữ kỷ luật kết luận **`ITERATE`** khi nhóm ca gấp/nhạy cảm (`6/8`) và câu chữ pháp lý (`E22`, `E14`) chưa thật sự khít 100%.
