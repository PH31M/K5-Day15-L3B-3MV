# Tóm tắt mô phỏng simulate-1@20261128-121324

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 41 | 1 | 976 | 77 | 1.6 | 2.8 |
| dung_vua | 8 | 2 | 1556 | 131 | 2.8 | 4.5 |
| dung_nhieu | 1 | 3 | 3797 | 333 | 6.0 | 8.0 |

Tỉ lệ đạt dùng để tính: 21/25 (84%) — lượt run-2@20261128-121029

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (50.000 người) | Chi phí / tháng — cao (200.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| openai/gpt-4.1-mini (vào 0.4 · ra 1.6 $/1M) | $0.00059 (≈ 15 ₫) | $0.00071 (≈ 18 ₫) | $0.00059 (≈ 15 ₫) | $9.82 (≈ 252.327 ₫) | $49.12 (≈ 1.261.634 ₫) | $196.46 (≈ 5.046.537 ₫) | $0.00098 (≈ 25 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00042 (≈ 11 ₫) | $0.00050 (≈ 13 ₫) | $0.00041 (≈ 11 ₫) | $6.93 (≈ 177.945 ₫) | $34.64 (≈ 889.725 ₫) | $138.55 (≈ 3.558.899 ₫) | $0.00069 (≈ 18 ₫) |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0024 (≈ 61 ₫) | $0.0028 (≈ 72 ₫) | $0.0023 (≈ 60 ₫) | $39.20 (≈ 1.006.948 ₫) | $196.00 (≈ 5.034.739 ₫) | $784.01 (≈ 20.138.954 ₫) | $0.0039 (≈ 101 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: openai/gpt-4.1-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.687 ₫ (Tỷ giá trung tâm NHNN ngày 27/11/2026 theo báo https://thitruongtaichinhtiente.vn/ngay-27-11-ty-gia-trung-tam-tang-11-dong-87350.html · xem 28/11/2026).
