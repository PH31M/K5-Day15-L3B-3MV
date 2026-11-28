# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Antigravity CLI | Gợi ý cấu trúc Web UI stdlib trong `codebase/app.py` và khung router | Kiểm tra 100% không dùng thư viện ngoài, rà soát toàn bộ unit tests (40+ test) | Phạm Hoàng Đức Minh · Tào Quang Vinh |
| Prompt / thiết kế lời gọi mô hình | Claude 3.5 Sonnet / Antigravity | Soạn thảo prompt phân loại tình huống 9 category cho `codebase/agent.py` | Rà soát loại bỏ mọi rò rỉ ngưỡng gian lận, ép luật G10 | Phạm Hoàng Đức Minh · Tào Quang Vinh |
| Đào data (viết script đếm, gợi ý nhãn) | Antigravity CLI | Viết script cào review Apple App Store VN (`mine_reviews.py`) | Kiểm tay 30 review đầu, loại trừ từ lóng lừa đảo sai ngữ cảnh, khớp 100% | Nguyễn Văn Minh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude 3.5 Sonnet | Gợi ý bộ câu hỏi khảo sát và kịch bản Mom Test | Loại bỏ câu hỏi dẫn dắt/giả định, giữ câu đo thời gian thực tế, ẩn danh 100% PII | Nguyễn Văn Minh |
| Viết câu thử (benchmark) | Antigravity CLI | Chuyển thể tình huống từ khảo sát/review thành định dạng benchmark | Kiểm tra từng câu khớp mã TX trong data card, tự tay viết pass_criterion | Trần Đình Nhật Minh |
| Sinh data `synthetic` (nếu có) | Antigravity CLI | Tạo 15 bản ghi giao dịch JSON mẫu (`TX-901..TX-915`) theo schema | Kiểm tay 15/15 bản ghi, cố định seed=20261127, không chứa ngưỡng tiền | Phạm Hoàng Đức Minh |
| Chấm cột `pass` bằng LLM (nếu có) | Trợ lý AI (lượt 1 và kiểm chéo); Claude Code (lượt 2) | Không chấm tự động bằng code; AI đối chiếu output/trace và soạn điểm, căn cứ kiểm chéo | Lượt 1: Nhật Minh duyệt, Vinh đồng ý 25/25 điểm (có AI hỗ trợ, không chấm độc lập). Lượt 2: Vinh chọn 21/25; Nhật Minh đối chiếu có AI hỗ trợ và giữ 25/25 điểm, nhất là E05/E19/E21=1 và E22=0. Vinh đã xác nhận bản ghi, Đức Minh đã duyệt theo [cost/cost-estimate.md](../cost/cost-estimate.md); giữ CSV và rate 84%, kết luận điều kiện (2) cùng giới hạn trong [eval/report.md](../eval/report.md). Duyệt bản chấm không có nghĩa đạt đầy đủ các metric | Trần Đình Nhật Minh · Tào Quang Vinh |
| Sửa lõi AI và viết test | Claude Code | Viết phần gọi `handoff_to_agent` và nêu mã ticket trong `codebase/agent.py` (commit `8d89c64`) cùng test | Vinh commit; test và lượt 2 do Claude Code chạy theo yêu cầu. Đã đọc kiểm riêng phần code | Tào Quang Vinh |
| Giao diện Web UI | Claude Code | Viết lại HTML/CSS/JS và phần máy chủ trong `codebase/app.py`, thêm `tests/test_app_ui.py` | Vinh xem bản làm lại đầu tiên, yêu cầu nâng cấp và chỉnh nền tối, rồi commit; tự test web để đưa hướng cải thiện | Tào Quang Vinh |
| Mô phỏng chi phí | Claude Code | Soạn `cost/personas.yaml`, tra giá model và tỷ giá, chạy lệnh `simulate`, soạn `cost/cost-estimate.md` | Vinh commit `personas.yaml`; số người dùng 10.000–200.000 là (tự ước tính) | Tào Quang Vinh |
| Slide, văn bản | Antigravity CLI | Dàn trang Markdown, tóm tắt bảng biểu và căn chỉnh cấu trúc 8 slide | Tự biên soạn toàn bộ nội dung, số liệu, bài học kinh nghiệm và phân vai | Phạm Hoàng Đức Minh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
