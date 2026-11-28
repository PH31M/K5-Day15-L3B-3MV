# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Antigravity CLI | Gợi ý cấu trúc Web UI stdlib trong `codebase/app.py` và khung router | Kiểm tra 100% không dùng thư viện ngoài, rà soát 29/29 unit tests | Phạm Hoàng Đức Minh · Tào Quang Vinh |
| Prompt / thiết kế lời gọi mô hình | Claude 3.5 Sonnet / Antigravity | Soạn thảo prompt phân loại tình huống 6 category cho `codebase/agent.py` | Rà soát loại bỏ mọi rò rỉ ngưỡng gian lận, ép luật G10 | Phạm Hoàng Đức Minh · Tào Quang Vinh |
| Đào data (viết script đếm, gợi ý nhãn) | Antigravity CLI | Viết script cào review Apple App Store VN (`mine_reviews.py`) | Kiểm tay 30 review đầu, loại trừ từ lóng lừa đảo sai ngữ cảnh, khớp 100% | Nguyễn Văn Minh |
| Rà câu hỏi phỏng vấn / khảo sát | Claude 3.5 Sonnet | Gợi ý bộ câu hỏi khảo sát và kịch bản Mom Test | Loại bỏ câu hỏi dẫn dắt/giả định, giữ câu đo thời gian thực tế, ẩn danh 100% PII | Nguyễn Văn Minh |
| Viết câu thử (benchmark) | Antigravity CLI | Chuyển thể tình huống từ khảo sát/review thành định dạng benchmark | Kiểm tra từng câu khớp mã TX trong data card, tự tay viết pass_criterion | Trần Đình Nhật Minh |
| Sinh data `synthetic` (nếu có) | Antigravity CLI | Tạo 8 bản ghi giao dịch JSON mẫu theo schema | Kiểm tay 8/8 bản ghi, cố định seed=20261127, không chứa ngưỡng tiền | Phạm Hoàng Đức Minh |
| Chấm cột `pass` bằng LLM (nếu có) | Trợ lý AI | Hỗ trợ đối chiếu 25 output/trace/JSON mỗi lượt, giải thích từng điểm và điền hai cột pass/ghi_chu | Nhật Minh đã duyệt lượt 1 (16/25), Vinh đồng ý 25/25 điểm có AI hỗ trợ, không chấm độc lập; lượt 2 ghi 21/25 (84%), chờ kiểm chéo và duyệt, không sửa output/trace/expected | Trần Đình Nhật Minh · Tào Quang Vinh |
| Slide, văn bản | Antigravity CLI | Dàn trang Markdown, tóm tắt bảng biểu và căn chỉnh cấu trúc 8 slide | Tự biên soạn toàn bộ nội dung, số liệu, bài học kinh nghiệm và phân vai | Phạm Hoàng Đức Minh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
