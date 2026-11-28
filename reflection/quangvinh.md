# Reflection — Tào Quang Vinh

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
- Thành viên nhóm 3MV (L3B, Track E · mã học viên `2A202604081`), phụ trách lõi AI và chi phí: `codebase/agent.py`, `tools.py`, `ai.py`, `cost/*`, `tests/*`; kiểm chéo phần đo lường.
- Sửa lỗi an toàn của agent, thêm test và công cụ khóa chuẩn đạt CP2 (`d42f675`); kiểm chéo hiệu chuẩn E01–E05 (`2c5bd96`).
- Điền `cost/personas.yaml` (`4ab4402`); sửa để ca cần người thật gọi `handoff_to_agent` và câu trả lời nêu mã ticket (`8d89c64`); làm lại giao diện Web UI (`3957d1e`, `7e93a97`); chạy lượt 2 và mô phỏng chi phí.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
- Tôi dùng Claude Code cho phần của tôi ở CP3 và CP4: sửa agent, viết test, làm lại giao diện, mô phỏng chi phí và soạn nháp điểm lượt 2. Báo cáo lượt 2 và bản reflection này AI cũng soạn nháp.
- Giao diện AI làm lần đầu trông còn cơ bản quá, tôi bắt nâng cấp lên và chỉnh lại nền tối.
- Tôi mở localhost thì thấy nó nhảy sang web build phase, hỏi AI mới biết hai chương trình trùng cổng 8000. Bản giao diện sau tự đổi sang cổng trống.
- File khai báo dùng AI ghi chưa đúng ai làm gì, tôi nhắc AI không được nhận bừa, AI phải sửa lại.
- Điểm lượt 2 AI chỉ soạn nháp, tôi là người chọn cách chấm (câu E22 cho trượt).

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
- Câu E20 ở lượt 1: khách muốn gặp nhân viên, bot trả lời "Tôi sẽ chuyển ngay hồ sơ" nhưng thật ra không gọi công cụ chuyển người nào cả. Khách mà tin thì ngồi chờ mãi.
- Tôi rút ra là bot nói đã làm chưa chắc đã làm, phải mở trace xem công cụ có chạy không.
- Cách sửa là để code quyết định việc chuyển người, mã ticket lấy từ công cụ. Lượt 2 câu này đạt, cả bộ từ 16 lên 21/25.
- Nhưng sửa khi đã biết câu sai nên điểm có thể hơi đẹp hơn thực tế. Thử câu ngoài bộ "gọi mãi không gặp được tư vấn viên" thì hệ thống vẫn chưa chuyển người.
