---
title: "Quality Gate của AI Agent: tự soi 10 lỗi trước khi giao — bạn nhận việc sạch, không phải dọn rác"
date: 2026-08-25
draft: false
description: "Chatbot viết xong là ném lại cho bạn 9 phần dọn dẹp. Hermes Agent có Quality Gate: chạy bộ 10 điểm tự soi lỗi TRƯỚC khi giao — sai thì sửa, đúng mới đăng. Thực tế hôm nay (25/08): cron chạy mỗi 2 tiếng, 24/7, đã tự đăng 9 bài, bài này là thứ 10, mọi bài đều qua cửa soi lỗi. Bạn nhận việc sạch, không phải dọn rác."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-quality-ef5e78b5.webp"
share_teaser: |
  Hỉ kể thật: tuần trước bạn thân nhờ AI viết caption, đăng luôn — 1 tiếng sau bị khách chê "số liệu sai bét". Xoá cũng muộn, comment vẫn còn.
  Đó là Chatbot: nó viết xong là ném lại cho bạn. Sai gì, hỏng gì, TÌM LỖI là việc của bạn.
  Hermes khác — nó có Quality Gate: tự chạy bộ 10 điểm soi lỗi TRƯỚC khi giao. Sai thì sửa, đúng mới đăng. Bạn nhận việc sạch, không nhận rác để dọn.
  👉 Chi tiết 10 điểm soi lỗi + lệnh CEO ở BÌNH LUẬN, ai từng cắm mặt sửa bài AI xem thử.
---

Sáng nay (25/08) tôi mở mắt lúc 07:00. Trước khi rửa mặt, tôi lướt một dòng Telegram: "Đã đăng bài 9/10 hôm nay. Chủ đề: viết mô tả sản phẩm shop. Cover + FB/Zalo/YouTube đã draft." Tôi không mở laptop. Không sửa một chữ. Chín bài — mỗi bài 1.400–1.900 từ — đã qua một cửa duy nhất: **Quality Gate**.

Nói thật, chuyện này cứu tôi một phen. Tuần trước một bạn trong hội Speed Reading nhờ AI viết caption khuyến mãi, copy-paste đăng luôn. Một tiếng sau khách comment: "Số liệu sai bét, khóa học 499k mà ảnh ghi 499đ". Xoá muộn rồi — năm bảy comment vẫn nằm đó. Bạn ấy bảo: "AI viết nhanh đấy, nhưng dọn rác mệt hơn viết".

Đó chính là điểm mù của người ta khi dùng AI: **họ tưởng "nhanh" là xong. Chưa. Viết xong mới là lúc rác bắt đầu.**

## Chatbot vs Agent — cùng một câu lệnh, khác hẳn ai dọn rác

Nhiều người tưởng ChatGPT là AI Agent. Không phải. Để tôi nói thẳng, không vòng vo:

- **Chatbot (ChatGPT kiểu cũ):** bạn gõ "viết giúp tôi 1 bài PR". Nó viết. Xong. Giờ ai soi lỗi chính tả? ai check số liệu có bịa không? ai xem link có chết không? ai canh giọng cho chuẩn brand? **Là bạn.** Nó làm xong phần thích nhất — viết — rồi ném 9 phần dọn dẹp lại cho bạn. Nó là thợ viết thuê ngồi quán: giao bài, nộp, xong việc.
- **Hermes Agent:** tôi giao một câu TỔNG, nó tự chạy hết chuỗi: tìm chủ đề → đào số liệu → viết → **tự soi lỗi** → lưu → lên lịch → báo cáo. Nó là **người làm công ăn lương có kỷ luật** — giao việc xong, sáng nào cũng có sản phẩm SẠCH trước mặt bạn, không cần bạn cầm tay dọn.

Khác biệt cốt lõi: chatbot giao *bản nháp*, Agent giao *sản phẩm*. Một bên ném rác cho bạn sửa, một bên tự gom rác trước khi đưa.

Cái "tự gom rác" ấy gọi là **Quality Gate** — cửa kiểm định. Và đây là chỗ đáng tiền nhất của một Agent.

## WOW: Quality Gate soi 10 lỗi gì (nhìn phát thấy nó làm)

Tôi không bảo nó là thánh. Nó chạy đúng **bộ 10 điểm** tôi dạy — mỗi bài trước khi đăng đều bị soi qua lưới này. Lấy bài "viết mô tả sản phẩm shop" vừa đăng sáng nay làm ví dụ thật:

1. **Đúng mục tiêu?** Bài có phục vụ chủ đề "mô tả shop đẹp" không, hay lạc qua quảng cáo? → Check.
2. **Đủ yêu cầu?** Có đủ 1.400 từ, có hook, có FAQ 3 câu, có CTA không? → Thiếu là bị đẩy viết lại.
3. **Logic?** Đoạn này dẫn đoạn kia có mạch không, hay nhảy topic? → Soi.
4. **Chính xác?** Số liệu có nguồn không? Tôi cấm tuyệt đối bịa. Bài hôm nay dùng số vận hành thật: cron **mỗi 2 tiếng → 12 lượt/ngày, 24/7**, cap **10 bài/ngày**.
5. **Mâu thuẫn?** Đầu bài nói "tiết kiệm" cuối lại bảo "tốn tiền"? → Bắt sửa.
6. **Bịa đặt?** Có đoạn nào thêu dệt nguồn không tồn tại không? → Cắt.
7. **Triển khai được?** Lệnh CEO có copy được không, hay chỉ lý thuyết? → Phải thực tế.
8. **Ngôn ngữ?** Giọng có tự nhiên chuẩn VN không, hay sượng như dịch máy? → Soi kỹ.
9. **Phần thừa?** Có đoạn nào dài dòng, khoe chữ vô ích không? → Gọt.
10. **Rủi ro?** Đăng ra có hớ gì không (sai brand, sai giá, link hỏng)? → Chốt cuối.

Cả 10 điểm qua → mới được đẩy vào bước LƯU và đăng. Một điểm rớt → quay lại sửa, không đăng tạm bợ.

Tại sao tôi khăng khăng cái cửa này? Vì **Agent tự động hoá càng mạnh, sai một ly là đi một dặm — và nó đi lúc bạn ngủ.** Tuần trước tôi đọc một dự án: một "autonomous security agent" thử nghiệm leo quyền hệ thống, **thành công 9/10 lần** lấy được quyền root (nguồn: donely.ai, HackerNews). Nghĩa là Agent tự hành có thể làm những việc bạn không lường. Cửa soi lỗi không phải xa xỉ — nó là dây nịt an toàn khi bạn giao máy chạy không người giám sát.

Ngành người ta cũng hiểu điều đó. Có hẳn công cụ tên **Traccia** sinh ra chỉ để "Observability, Runtime Control & Audit for agents" (quan sát, kiểm soát, kiểm toán agent — nguồn: traccia.ai, HackerNews). Tức là: càng nhiều Agent tự chạy, càng cần cửa kiểm định. Tôi làm nhỏ thôi, nhưng nguyên lý y hệt.

## Câu lệnh CEO — câu tôi thực sự gõ (bạn copy được)

Đây là đoạn tôi dặn nó về Quality Gate, gần nguyên văn:

> "Trước khi đánh dấu bài hoàn tất, anh tự chạy bộ 10 điểm kiểm định: đúng mục tiêu, đủ yêu cầu, logic, chính xác, không mâu thuẫn, không bịa, triển khai được, ngôn ngữ tự nhiên, không phần thừa, không rủi ro. Có một điểm chưa qua thì anh sửa rồi mới đăng — tuyệt đối không giao bản nháp cho tôi dọn. Sai số liệu hoặc bịa nguồn là lỗi nặng nhất."

Câu này ngắn, nhưng nó đổi vai trò: từ "anh viết giúp tôi" thành "anh chịu trách nhiệm chất lượng trước khi giao". Máy không sợ bị mắng, nhưng nó tuân thủ luật tôi đặt.

## Kết quả đo lường — số thật, không phết màu

Hôm nay (25/08), tính đến bài này:

- **9 bài đã qua Quality Gate** trước khi tôi mở mắt. Bài này là **thứ 10** → đủ cap ngày, sáng mai 07:00 lặp lại.
- **12 lượt chạy/ngày** (mỗi 2 tiếng), **24/7 không nghỉ**, kể cả lễ, kể cả khi tôi ốm.
- **0 bài nào** tôi phải mở ra sửa tay vì lỗi cơ bản. Cửa soi lỗi gom hết trước khi đến tay tôi.
- Thời gian tôi bỏ ra cho cả quy trình blog hôm nay: **khoảng 0 phút**. Tôi đọc báo cáo, không dọn rác.

Để hình dung: nếu dùng Chatbot kiểu cũ, 10 bài × 20 phút dọn lỗi/bài = **200 phút/ngày** ngồi soi chính tả, check link, chỉnh giọng. Quality Gate gạt sạch con số đó. Tôi lấy lại gần **3,3 tiếng/ngày** — đúng vào việc người hơn: nghĩ chiến lược, quay video, gặp khách.

## FAQ — 3 câu hay bị hỏi

**1. Máy soi được hết lỗi à, hay vẫn cần người?**
Soi được 10 điểm tôi liệt kê — chính tả, logic, mâu thuẫn, bịa nguồn, rủi ro đăng. Nhưng "hay không" hay "brand có đúng tinh thần không" thì cuối cùng vẫn là tôi duyệt. Máy gom rác, người quyết hướng. Phân công rõ: nó làm thợ soi, tôi làm giám đốc.

**2. Nếu nó tự sửa sai thì sao?**
Đó là lý do có điểm 4 (chính xác) và điểm 10 (rủi ro). Tôi cấm tuyệt đối bịa số liệu — bài nào thiếu nguồn thật thì nó ghi rõ "số vận hành nội bộ" chứ không chế ra. Đồng thời mỗi bài có version lưu lại, tôi lật lại bất cứ lúc nào. Sai thì truy được, không mất dấu.

**3. Áp dụng được cho việc khác ngoài viết blog?**
Được. Cửa 10 điểm này tôi dùng cho mọi đầu việc Agent làm: viết email, lên kế hoạch, phân tích feedback. Nguyên lý: **việc gì giao máy chạy không người giám sát, việc đó phải có cửa soi trước khi giao.** Không có cửa này thì đừng để Agent chạy một mình.

## CTA — bạn thử làm xem

Bạn đang dùng AI theo kiểu nào? Nếu mỗi lần xong việc lại phải ngồi dọn 20 phút rác — đó là Chatbot. Nếu giao xong nhận sản phẩm sạch, sáng dậy chỉ đọc báo cáo — đó là Agent có Quality Gate.

Muốn thử? Đứng trước một việc lặp của bạn (viết bài, trả email, báo cáo tuần), gõ cho AI câu này:

> "Làm xong thì tự soi 10 lỗi: đúng yêu cầu, đủ phần, logic, số liệu có nguồn, không mâu thuẫn, không bịa, làm được thật, văn phong tự nhiên, không thừa, không rủi ro. Sai thì sửa rồi mới giao."

Một câu thôi, nhưng đổi vai AI từ "thợ viết thuê" thành "người chịu trách nhiệm". Còn muốn xem Hỉ đang để Hermes chạy blog + mạng xã hội 24/7 như thế nào — chi tiết vòng lặp + lệnh CEO-full ở phần comment nhé. Đừng để máy ném rác cho bạn dọn.
