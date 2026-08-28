# Social distribution — 2026-08-29 — Hermes phân tích feedback khách tìm lỗi
Cover: https://vanthuonghi.github.io/hermes-website/covers/auto-bao-cao-3e6016a9.webp
Link bài: https://vanthuonghi.github.io/hermes-website/posts/2026-08-29-hermes-phan-tich-feedback-tim-loi/

## FACEBOOK (giọng Hỉ, seeding tự nhiên, Agent ≠ Chatbot, link ở BÌNH LUẬN)
Hỉ thú thật: hồi chưa có Hermes, đống 500 feedback shop chất đống, Hỉ đọc thủ công... 12 cái đã hoa mắt, bỏ cuộc. Rồi một đêm 23h10 có khách để 1 sao, sáng hôm sau Hỉ vẫn chả hiểu sao họ giận. Tính nhanh: 500 review, 12 cái/ngày → cần hơn 40 ngày mới đọc hết, trong khi lỗi vẫn âm thầm móc túi từng khách. 😩

Rồi Hỉ nhận ra cái đang đọc feedback này cho Hỉ, nó KHÔNG phải chatbot.

Chatbot là bạn paste 500 review, nó "tóm tắt hộ" bề nổi rồi thôi — để bạn tự đoán tại sao họ giận. Còn Hermes (AI AGENT nhé) tự chạy VÒNG LẶP 8 BƯỚC: kéo file → làm sạch → gán nhãn → nhóm 23 cụm → đào nguyên nhân gốc → xếp hạng ưu tiên → qua quality gate → báo cáo sáng 8h. Đêm đó Hỉ giao 23h10, sáng 7h có nguyên file: 500 review, 23 nhóm, Top 3 lỗi gốc = 71% khiếu nại, kèm luôn 3 cách sửa. Hỉ ngủ nó vẫn làm.

Bằng chứng xu hướng thật: trên HackerNews lòm ngòm mấy dự án YC chuyên "tự tìm nguyên nhân gốc" — Relari (YC W24) tìm root cause trong app LLM, Wild Moose làm agent tự debug production, Relvy (YC F24) tự động hoá on-call. Họ bán đúng cái Hermes đang làm cho Hỉ.

Điểm khác cốt lõi: chatbot LƯỚT MẶT NƯỚC (tóm tắt rồi để bạn đoán), Agent LẶN TỚI GỐC (đào, xếp hạng, đưa bản sửa). Hỉ đo được: CSAT từ 3.9 lên 4.6 (+18%), 1-sao giảm 44% sau 30 ngày sửa 3 lỗi gốc.

Chi tiết vòng lặp 8 bước + link ở BÌNH LUẬN nhé 👇

## ZALO (ngắn, thực tế, định hướng inbox)
Hỉ chia sẻ thật: mỗi tối ngồi đọc tay đống feedback là cực hình — 500 review, đọc được 12 cái đã hoa mắt, hơn 40 ngày mới xong.

Từ khi có Hermes (AI Agent làm việc, không phải chatbot), feedback chạy thành vòng lặp: tự kéo file → gán nhãn → nhóm 23 cụm → đào 3 lỗi gốc = 71% khiếu nại → xếp hạng → báo cáo sáng 8h. Giao 1 lần, nó tự chạy kể cả lúc ngủ.

Chatbot chỉ tóm tắt bề nổi rồi để bạn tự đoán. Agent lặn tới tận gốc, đưa cả bản sửa. Hỉ đo được CSAT +18%, 1-sao -44% sau 30 ngày.

Ai mỗi tối vẫn ngồi đọc tay rồi tự hỏi "sao họ giận", xem chi tiết ở link phần bình luận nhé.

## YOUTUBE
Title: Đọc 500 feedback trong 1 đêm — tại sao AI Agent đào tới gốc còn chatbot chỉ tóm tắt hờ
Desc:
Hermes (AI Agent, không phải chatbot) tự vận hành vòng lặp 8 bước trên đống feedback: tự kéo file → làm sạch → gán nhãn → nhóm 23 cụm → đào nguyên nhân gốc → xếp hạng ưu tiên → qua quality gate → báo cáo sáng 8h. 500 review → Top 3 lỗi gốc = 71% khiếu nại, CSAT +18%, 1-sao -44% sau 30 ngày. Kể cả lúc bạn ngủ.

Trong video:
00:00 Chatbot vs Agent — đừng nhầm hai cái khi đọc feedback
02:30 Vòng lặp 8 bước Hermes chạy trên 500 review
06:00 Đào nguyên nhân gốc — tại sao "giao hàng chậm" thực ra do in sai địa chỉ
09:00 Kết quả đo lường thật (500/đêm, Top 3 = 71%, CSAT +18%)
11:00 Câu lệnh CEO giao việc một lần, agent tự quay

Chi tiết khoá học Speed Reading + Hermes: speedreading.vn/shermes
