# Canvas — 3MV · Track E

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | **Track E (Tài chính — E3):** Trợ lý phân loại và xử lý ban đầu trong chat hỗ trợ khi giao dịch ví điện tử bị tạm chặn do nghi ngờ rủi ro/lừa đảo. |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Người dùng ví điện tử (sinh viên, người đi làm) vừa bị tạm chặn một giao dịch chuyển tiền và đang lo lắng nhắn vào kênh chat hỗ trợ của ví. |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Người dùng ví điện tử khi giao dịch chuyển tiền bị tạm chặn phải nhắn vào kênh hỗ trợ trả lời theo kịch bản cứng hoặc chờ tổng đài ngoài giờ (sau 20h), dẫn tới nguy cơ mất tiền trong vài giây nếu mở nhầm ca đang bị giục lừa đảo hoặc lỡ việc khẩn cấp (viện phí, thanh toán gấp) khi phải chờ quá lâu. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | **Giả thuyết:** Phần lớn phàn nàn về hỗ trợ chặn/giữ giao dịch trên ví điện tử xoay quanh việc bot vòng vo, không phân biệt được ca khẩn cấp thật với ca nghi lừa đảo/chiếm tài khoản, và phải chờ người hỗ trợ quá lâu. **Nguồn sẽ kiểm:** (1) Đào ≥100 review công khai trên Google Play/App Store của ví điện tử & app ngân hàng (MoMo, ZaloPay, VCB) lọc theo chủ đề chặn/khóa giao dịch & CSKH; (2) Khảo sát ≥20 học viên ngoài nhóm + phỏng vấn ≥3 người từng bị tạm giữ giao dịch hoặc gặp tình huống bị giục chuyển tiền. |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Một người dùng ví điện tử nhắn vào chat hỗ trợ vì giao dịch vừa bị tạm chặn · AI phân loại tình huống (bị giục chuyển tiền lừa đảo / gấp thật / nghi chiếm tài khoản / chưa rõ) và quyết định giữ giao dịch, gửi xác minh, hỏi thêm 1 câu làm rõ hay chuyển tư vấn viên (tuyệt đối không tự nhả tiền) · người đang bị lừa không mất tiền trong vài giây còn người gấp thật được ưu tiên chuyển người kèm tóm tắt ca ngay. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | **AI tự làm các bước đảo được** (giữ giao dịch `hold_transaction`, gửi màn hình xác minh `request_verification`, chuyển tư vấn viên kèm tóm tắt `handoff_to_agent`) và **tuyệt đối không tự nhả giao dịch (`release_transaction`) hay tự khoá ví vĩnh viễn (`lock_wallet`)** — vì nếu nhả nhầm cho người đang bị lừa, tiền đi trong vài giây và không đảo lại được; còn chuyển tư vấn viên thừa chỉ tốn vài phút chờ. |
| 7 | Phân công có tên | **Phạm Hoàng Đức Minh (ĐT):** Điều phối, kiến trúc agent & demo · **Nguyễn Văn Minh:** Đào review công khai, khảo sát/phỏng vấn & bảng impact · **Trần Đình Nhật Minh:** Bộ 20–30 câu thử an toàn, metric spec & đánh giá L1→L2 · **Tào Quang Vinh:** Lập trình công cụ agent, UI demo & mô phỏng chi phí. |
| — | *(CP2)* Đã đổi gì so với CP1 | *(Cập nhật trước 19:30 Thứ Sáu 27/11)* |
