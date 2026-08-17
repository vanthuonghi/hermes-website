---
title: "Hermes kết nối API: giao 1 lệnh, nó gọi 20 công cụ — bạn không cần copy-paste lần nào"
date: 2026-08-17
draft: false
description: "Chatbot chỉ trả lời trong khung chat. Hermes là AI Agent — bạn giao 1 lệnh, nó tự gọi hàng chục API (email, Sheets, web, Telegram, thanh toán) để lấy data, xử lý, ghi lại, báo cáo. Thực tế: 1 câu lệnh kéo feedback khách từ Gmail, chép vào Google Sheets, đăng bài, nhắn bạn qua Telegram — không một lần dán tay."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-api-094c2b2c.webp"
share_teaser: |
  Hỉ thử một trò: sáng đưa Hermes (AI Agent) đúng 1 câu — "tổng hợp feedback khách tuần này, chép vào bảng, báo tôi qua Telegram" — rồi đi uống cà phê. ☕
  Về thấy: nó đã lục Gmail lấy 47 email, gom vào Google Sheets, đánh nhãn mức độ, xong nhắn "xong rồi anh" vào điện thoại. Hỉ không mở một tab, không dán một dòng.
  Đây là điểm chatbot làm không nổi: chatbot chỉ nằm trong khung chat, hỏi gì đáp đó. Còn Agent (nhân sự ảo) là "bản sao bạn" — nó có tay, gọi được đủ thứ công cụ bên ngoài rồi tự báo cáo.
  👉 Hermes đang làm cái này mượt thật — chi tiết + link ở BÌNH LUẬN nhé, ai ngán việc dán đi dán lại xem thử.
---

Sáng thứ Hai, trước mặt tôi là một đống việc "nối ống": lục 47 email khách tuần trước lấy feedback, gom vào một bảng Google Sheets, đánh nhãn mức độ hài lòng, rồi viết 1 bài tổng hợp đăng lên web, cuối cùng nhắn cho tôi qua Telegram. Làm tay thì sao? Mở Gmail, copy từng thư, dán sang Sheets, gõ nhãn, mở trình soạn bài, dán lại, rồi lại mở Telegram gửi mình. Tầm **2–3 tiếng** ngồi chuyển xe giữa các app, toàn thao tác copy-paste vô nghĩa.

Có một con số làm tôi giật mình: theo báo cáo *Businesses at Work* của Okta, một doanh nghiệp cỡ vừa trung bình xài **khoảng 89 ứng dụng SaaS** — từ email, Sheets, CRM, đến thanh toán, lưu trữ, tin nhắn. Nghĩa là mỗi ngày bạn "nhảy" giữa gần 90 công cụ, và phần lớn thời gian không phải để *nghĩ*, mà để *chuyển dữ liệu* giữa chúng. McKinsey thì ước tính nhân viên văn phòng đốt **1/3 đến 1/2** quỹ thời gian cho việc lặp đi lặp lại — và copy-paste giữa các app chính là vua của mấy việc đó.

Tôi chọn cách khác: để Hermes **kết nối API** — gom mọi Key, mọi công cụ vào một cái đầu. Giao một lần, nó tự gọi đủ thứ bên ngoài, xong báo tôi.

## Chatbot vs Agent — cùng "biết" công cụ, khác hẳn cách "đụng" vào nó

Nhiều người tưởng ChatGPT hay Claude là AI Agent. Không phải. Khác nhau ở chỗ: **ai là người bấm, ai là người chuyển data.**

- **Chatbot (ChatGPT kiểu cũ):** nó trả lời *trong khung chat*. Bạn hỏi "viết giúp tôi 1 đoạn tổng hợp", nó viết. Nhưng để đưa đoạn đó vào Sheets, đăng lên web, hay gửi tin nhắn — **bạn tự làm**. Chatbot không có "tay" với thế giới ngoài, nó không gọi được API. Mọi kết nối là bạn cầm chuột dán đi dán lại.
- **Hermes Agent:** tôi cấp cho nó quyền gọi API của các công cụ tôi dùng. Giao một lệnh, nó tự **gọi Gmail lấy mail → gọi Sheets ghi bảng → gọi web đăng bài → gọi Telegram nhắn tôi**. Nó là bản sao có tay, tự vận hành cả chuỗi rồi báo cáo. Bạn không đụng vào giữa chừng.

Khác biệt cốt lõi: chatbot là **cái loa** — bạn bấm mới kêu, rồi tự đi gắn dây. Agent là **cái máy có tay** — bạn vặn nút một lần, nó tự cắm ổ cắm, tự chạy, tự rút phích khi xong. Như TAKI Academy từng ví von: tư duy đúng không phải "cầm tay chỉ việc" cho AI, mà là **"giao khoán trọn gói"** — để nó tự hành, "cày cuốc ngày đêm không biết mỏi mệt".

## WOW: Hermes kết nối API như thế nào (nhìn phát thấy nó làm)

Thực ra, cái blog bạn đang đọc là minh chứng sống. Mỗi bài được Hermes tự đẩy lên web qua API — tôi không bấm nút đăng thủ công. Dưới đây là kịch bản sáng thứ Hai tôi kể ở đầu, được Hermes chạy thực tế:

| Bước | API được gọi | Việc Hermes tự làm |
|---|---|---|
| 1 | Gmail API | Lọc 47 email tuần trước, tách feedback khách |
| 2 | Sheets API | Tạo bảng mới, ghi 47 dòng, cột nhãn tự đánh (khen / góp ý / bức xúc) |
| 3 | Web API (GitHub) | Tự viết 1 bài tổng hợp, commit, deploy lên web |
| 4 | Telegram API | Nhắn tôi: "Đã gom 47 feedback, 5 khách bức xúc ưu tiên xử lý, bài live ở link này" |

**4 API, 1 câu lệnh, 0 lần dán tay.** Tôi nhận kết quả nằm sẵn, không mở một tab. Đây là lúc bạn thấy rõ: chatbot nằm im trong khung chat, Agent **bước ra ngoài**, cầm công cụ của bạn mà làm.

Chi tiết khiến tôi tin nhất: bước 2 Hermes tự đánh nhãn "bức xúc" cho 5 email khách giận, rồi ở bước 4 nó **đẩy 5 cái đó lên đầu** báo cáo. Nó không chỉ "gọi API" mù quáng — nó hiểu ưu tiên, xếp việc quan trọng trước. Chatbot thì bạn phải copy từng thư dán sang rồi tự quyết cái nào gấp.

## Quy trình vòng lặp — mỗi lần gọi API là 8 bước khép kín

Điều làm nên một Agent thật không phải mấy câu "kết nối mọi thứ" hoa mỹ, mà là **vòng lặp có kỷ luật** mỗi khi nó chạm vào một công cụ. Với việc gom feedback sáng nay, Hermes chạy đúng 8 bước:

1. **Thu thập** — gọi Gmail API, kéo đúng 47 email trong khoảng thời gian cần.
2. **Nghiên cứu** — đọc nội dung, phân loại ý định (khen / góp ý / bức xúc).
3. **Lập kế hoạch** — quyết định cấu trúc bảng, cột nào cần có.
4. **Thực thi** — gọi Sheets API ghi 47 dòng + nhãn; gọi web API viết bài.
5. **Kiểm định (quality gate)** — soi lại: thiếu email nào không, nhãn có lệch không, bài có lủng câu không. Sai dưới 5% tự duyệt, cao hơn báo tôi.
6. **Xuất bản** — Sheets đã lưu, bài đã live trên web.
7. **Cập nhật** — ghi log, tạo task nhắc xử lý 5 khách bức xúc.
8. **Báo cáo** — gọi Telegram API gửi tôi tóm tắt ngắn.

8 bước, 4 API, chạy liên hoàn không cần tôi đụng tay. Chatbot chỉ làm được bước 4 (viết đoạn văn), còn 7 bước kia bạn tự cõng. Đó là sức mạnh của **kết nối API**, không phải của "gõ prompt giỏi".

## Câu lệnh giao việc kiểu CEO

> "Hermes, cuối tuần này tổng hợp help feedback khách từ Gmail tuần qua, gom vào một bảng Google Sheets có cột nhãn (khen/góp ý/bức xúc), viết 1 bài tổng hợp ngắn đăng lên web, rồi nhắn tôi qua Telegram danh sách khách bức xúc xếp trước. Gọi API tự làm, sai sót dưới 5% tự duyệt, cao hơn hỏi tôi. Tôi chỉ đọc tin nhắn cuối."

Đó là giao kiểu đầu não: bạn nói **mục tiêu + giới hạn + công cụ được dùng**, Hermes lo **thứ tự gọi API + xử lý + check + báo cáo**. Bạn không ngồi dán, không chuyển kết quả đi đâu.

## WOW: con số thật (không bịa)

- **1 lệnh → 4 API → 0 lần dán tay.** Tay làm mất 2–3 tiếng chuyển xe; Hermes xong trong **vài phút** xử lý (thời gian chạy API). Tiết kiệm ~90% thời gian cho khối lượng đó.
- **~89 ứng dụng SaaS** một doanh nghiệp cỡ vừa xài (Okta). Mỗi app là một "ống" cần nối — Agent là người thợ nối ống, bạn không tự cầm ống nữa.
- **1/3–1/2** quỹ thời gian nhân viên đốt cho việc lặp (McKinsey) — phần lớn là chuyển data giữa app. Kết nối API triệt tiêu đúng khoản đó.
- **82% tổ chức** dự kiến tích hợp AI agent vào vận hành (Capgemini). "Giao khoán trọn gói" đang thành chuẩn, không phải trò chơi.
- **7,6 tỷ USD (2025) → 50 tỷ USD (2030)** — thị trường agent tự chủ tăng ~6,5 lần (Deloitte). Tiền đang chảy mạnh vào hướng "Agent có tay" này.

## Mẹo giao việc (đầu não – cánh tay)

- **Ghi rõ công cụ được dùng** trong lệnh ("gọi Gmail, Sheets, Telegram") → Agent biết mở khoá API nào, không đoán.
- **Ghi rõ điều kiện tự duyệt** (sai <5% tự làm) → ít bị quấy, bạn chỉ duyệt điểm then chốt.
- **Bắt nó báo cáo tóm tắt**, đừng đổ hết raw ra — bạn chỉ đọc "5 khách bức xúc, xong rồi anh".
- **Cấp quyền từng bước** — mới đầu chỉ cho gọi API đọc (Gmail, Sheets), quen rồi mới cho gọi API ghi/đăng. An toàn mà vẫn mạnh.

## 3 câu hỏi hay gặp

**1. Cấp quyền gọi API cho AI thì có an toàn không, nó có tự ý xoá dữ liệu không?**
Có rủi ro nên tôi cấp quyền *có giới hạn*. Gmail API chỉ được quyền *đọc* (lấy mail, không xoá), Sheets được quyền *ghi vào bảng cụ thể*, Telegram chỉ được *gửi tin nhắn cho tôi*. Tôi không cho quyền xoá, không cho quyền rút tiền. Và mỗi lần gọi đều có quality gate + log — sáng dậy đọc log là biết đêm qua nó chạm vào app nào, làm gì. Có khoá, có khiên, không phải "ném chìa khoá cho người lạ".

**2. Có cần biết code để kết nối API không, tốn bao nhiêu?**
Không cần một dòng code. Tôi cấp Key (một chuỗi ký tự app nào cũng cho sẵn) cho Hermes, nó tự lo cách gọi. Chi phí gần như bằng 0 so với thuê một bạn ops ngồi dán data — tôi chỉ trả phí vận hành vài chục nghìn mỗi lần sinh ảnh cover. Còn muốn tự dựng được "nhân sự ảo có tay" kiểu này, học 1 khóa là đủ (chi tiết cuối bài).

**3. Nó gọi sai API, lấy nhầm data thì sao?**
Chính là quality gate. Trước khi ghi Sheets hay đăng bài, Hermes tự soi: thiếu email nào không, nhãn có lệch không, link có hỏng không. Lần đầu nó từng gom nhầm cả email spam vào bảng — tôi dặn lại "chỉ lấy email trong thread khách hàng", giờ nó lọc sạch. Bạn đọc bản tóm tắt cuối 1 lần là an tâm, không cần canh từng cú gọi API.

## Kết luận

Chatbot là cái loa — bạn bấm mới kêu, rồi tự đi nối dây giữa 89 ứng dụng. Hermes là **bản sao có tay** — giao một lệnh, nó tự gọi hàng chục API, lấy data, xử lý, ghi lại, đăng bài, báo cáo — không một lần bạn dán tay. Bạn không cần thuê thêm người ngồi chuyển xe; bạn chỉ cần gom mọi Key vào một cái đầu, rồi giao khoán.

Muốn có "nhân sự ảo có tay" kết nối mọi công cụ mà không cần biết code?

👉 Học bài bản: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes)

📎 Đọc thêm: [Hermes tự động hoá: giao 1 lần chạy hoài](/posts/hermes-tu-dong-hoa/)
