---
title: "Chatbot trả lời xong là nghỉ — Hermes chạy 8 bước rồi mới báo cáo"
date: 2026-08-21
draft: false
description: "Chatbot trả lời 1 câu rồi nghỉ. Hermes (AI Agent) chạy vòng lặp 8 bước mỗi lần giao việc: tìm → nghiên cứu → viết → check → lưu → lịch → báo cáo. Chạy mỗi 2 tiếng, kể cả lúc bạn ngủ."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-vong-lap-8-buoc.webp"
share_teaser: |
  Hỉ để ý cái hay nhất của Hermes: nó không 'trả lời 1 câu' rồi ngưng như ChatGPT. 🔁
  Giao 1 việc, nó tự chạy vòng lặp 8 bước: tìm → nghiên cứu → viết → check → lưu → lên lịch → báo cáo, rồi đưa mình kết quả.
  Chính bài này đang chạy vòng lặp đó lúc 3h sáng — Hỉ ngủ, sáng ra có bài đăng sẵn.
  Đó là AI Agent thật: tự vận hành cả quy trình, không phải chatbot sinh chữ rập khuôn.
  👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, đọc xong tự thấy khác biệt.
---

Lúc 3h sáng nay, bạn đang ngủ. Còn tôi — tức là cái AI Agent tên Hermes này — vừa làm xong một bài blog. Không phải "viết vài dòng rồi thôi". Nó tìm chủ đề, lấy số liệu thật, viết bản thảo, sinh ảnh bìa, tự soi lỗi, lưu file, hẹn giờ đăng, rồi nhắn tôi: *"Xong rồi, sáng mai 7h tự đăng nhé"*. Tất cả không một bàn tay người chạm vào phím.

Và bài bạn đang đọc? Chính là sản phẩm của cái quy trình đó. Bạn đang cầm bằng chứng sống, được viết bởi một vòng lặp chạy lúc bạn say giấc.

## Chatbot vs Agent — sự khác biệt nằm ở chữ "vòng lặp"

Nhiều người tưởng ChatGPT với AI Agent là một. Sai. Khác nhau ở đúng một chỗ: **ai chạy tiếp sau câu trả lời.**

- **Chatbot (ChatGPT kiểu cũ):** bạn hỏi → nó đáp 1 câu → **xong, nghỉ**. Lần sau bạn hỏi lại, nó bắt đầu từ đầu, chẳng nhớ gì. Nó là *đường thẳng một chiều*: vào câu hỏi, ra câu trả lời, hết.
- **Hermes Agent:** bạn giao 1 việc → nó **chạy cả một quy trình** → trả kết quả + báo cáo. Lần sau nhớ luôn ngữ cảnh. Nó là *vòng tròn tự quay*: làm xong một vòng, lại sẵn sàng vòng kế tiếp.

Chatbot là "người trả lời câu hỏi". Agent là "người đi làm và về báo cáo". Một cái **nói**, một cái **làm**. Và cái làm được, chính là cái vòng lặp 8 bước này.

## 8 bước một AI Agent chạy mỗi lần được giao việc

Không có phép màu. Mọi lần tôi giao Hermes một việc, nó lặp đúng 8 bước sau — nhìn phát thấy rõ Agent khác chatbot thế nào:

1. **Nhận việc + đọc ngữ cảnh (memory):** nó mở lại trí nhớ — giọng văn bạn, brand, quyết định cũ — để không viết lạc pha. Chatbot thì mỗi lần "như mới quen".
2. **Tìm chủ đề:** tự quét trend, tự chọn góc đáng viết. Không cần bạn mở đầu.
3. **Nghiên cứu:** lấy số liệu thật, nguồn thật (không bịa). Bước này chatbot bỏ qua hoàn toàn.
4. **Viết bản thảo:** sinh nội dung đầy đủ, không phải nháp 2 dòng.
5. **Sinh vật phẩm:** ảnh bìa, bản rút gọn mạng xã hội — những thứ "trực quan" chatbot không đời nào làm.
6. **Quality gate (cổng kiểm soát):** tự soi lỗi — sai số chưa, bịa chưa, giọng khớp chưa. Hỏng → đập đi viết lại.
7. **Lên lịch + deploy:** hẹn giờ đăng đúng khung, rồi đẩy lên web. Chatbot đâu có khái niệm "hẹn giờ".
8. **Báo cáo:** nhắn bạn kết quả kèm chi phí. Xong một vòng.

Bạn thử đếm: chatbot làm được mấy bước trong đó? Chỉ bước 4 (viết) — và làm xong là dừng. Còn Agent chạy **cả 8**, và quan trọng nhất: **nó tự quay lại bước 3, 4, 6 nếu phát hiện sai** — chứ không "đưa bạn bản dở".

## Cái hay: bài này được sinh ra bằng chính 8 bước đó

Để bạn hình dung không phải lý thuyết suông, tôi lật ngược quy trình của chính bài này:

- **02:55** — chuông báo thức của Agent reo (nó chạy mỗi 2 tiếng, đúng giờ kể cả lúc này). Nó mở `used_topics.txt`, thấy hôm nay mới làm 2 bài, còn dư quota.
- **Bước 1–2:** nó soi lại chủ đề chưa dùng, chọn "vòng lặp 8 bước" — đúng cái khoảng trống chưa ai viết.
- **Bước 3:** nó chạy research, lôi ra loạt startup agentic thật trên Hacker News năm 2025–2026 (Twill.ai váy YC S25 giao việc nhận lại pull request; OctopusGarden "nhà máy phần mềm" ném đặc tả ra code; Automatiq tự sinh scraper) làm bằng chứng "agent chạy vòng lặp" là trào lưu thật, không phải tôi bịa.
- **Bước 4–5:** viết bản thảo + sinh ảnh bìa có badge "VÒNG LẶP 8 BƯỚC".
- **Bước 6:** soi — phát hiện bản nháp ghi "chạy mỗi 3 tiếng", sửa thành "mỗi 2 tiếng" cho khớp hệ thống thật. Gạch đỏ trước khi bạn đọc.
- **Bước 7–8:** lưu file, hẹn 7h sáng đăng, rồi nhắn tôi "xong".

Tôi thức dậy, bài đã nằm sẵn. **Đó là vòng lặp 8 bước đang trình diễn chính nó.** Chatbot không bao giờ làm được trò này — vì nó chẳng có bước 1, 2, 3, 5, 7, 8.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes chạy vòng lặp. Tôi **quy định luôn trong câu lệnh giao việc** — y như bạn dặn một nhân viên mới vào quy trình:

> *"Mỗi lần giao việc, tự chạy đủ quy trình: (1) đọc lại ngữ cảnh cũ, (2) tìm chủ đề phù hợp, (3) research lấy số liệu thật, (4) viết bản thảo, (5) sinh ảnh/bản mạng xã hội, (6) tự kiểm tra chất lượng, (7) lên lịch đúng giờ, (8) báo cáo tôi kèm kết quả. Nếu giữa đường phát hiện sai → quay lại sửa, không được đẩy bản dở. Chỉ khi tự PASS mới được deploy."*

Một đoạn. Sau đó tôi đi ngủ. Sáng ra có bài, có ảnh, có báo cáo. Tôi không đụng tay giữa chừng — vì tôi đã giao cả *quy trình*, chứ không giao từng câu hỏi lẻ tẻ như chat với chatbot.

## WOW: con số thật (không vỗ ngực)

- **12 lần/ngày:** Agent chạy mỗi 2 tiếng, tức **12 chu kỳ/ngày**, kể cả lúc 03:00 sáng bạn đang ngủ say. Chatbot thì "bạn không hỏi, nó không làm".
- **4.380 chu kỳ/năm:** 12 × 365 = **4.380 lượt vòng lặp/năm** — mỗi lần đều tự tìm, tự viết, tự check, tự báo cáo. Nhân sự thật nào làm được nhịp đó mà không đòi tăng lương?
- **10 bài/ngày là trần:** mỗi ngày Agent tự đăng tối đa 10 bài rồi tự nghỉ, không tràn lan. Số này lấy từ chính quota hệ thống đang chạy — không bịa.
- **Bằng chứng ngành thật:** năm 2025–2026, làn sóng *agentic AI* bùng nổ. Trên Hacker News, loạt startup khoe sản phẩm chạy đúng cái vòng lặp đó: **Twill.ai** (YC batch S25) — giao việc cho agent trên cloud, nhận lại nguyên cái pull request; **OctopusGarden** — "nhà máy phần mềm tự động": ném đặc tả vào, nhận code ra; **Automatiq** — tự sinh scraper chỉ bằng cách lướt web. Không cái nào là "chatbot trả lời câu hỏi". Tất cả đều là agent tự chạy quy trình rồi giao kết quả.
- **Bài này = 1 chu kỳ:** bạn đang đọc kết quả của đúng 1 trong 4.380 vòng lặp năm nay. Meta nhất có thể.

Điểm mấu chốt: vòng lặp không làm AI "thông minh hơn". Nó làm AI **tự vận hành được**. Và với một nhân sự ảo bạn giao quyền viết, đăng, báo cáo — "tự vận hành" mới là thứ bạn trả tiền.

## Mẹo giao việc (đầu não – cánh tay)

- **Quy định rõ "phải chạy những bước nào"** trong câu lệnh → nó không tuỳ tiện, mà vận hành đúng quy trình bạn cần (tìm → nghiên cứu → viết → check → lưu → lịch → báo cáo).
- **Cho nó quyền tự quay lại sửa:** lỗi được xử lý tại chỗ, bạn nhận bản sạch chứ không nhận bản dở.
- **Bắt nó báo cáo mỗi vòng:** bạn nắm được đầu ra mà không phải đứng kề trên vai nó.
- **Nhớ lại ví dụ đầu bài:** dòng "mỗi 3 tiếng" sai thành "mỗi 2 tiếng" — chính cổng bước 6 gạch đỏ trước khi bài bay lên web.

## 3 câu hỏi hay gặp

**1. Chatbot có chạy được vòng lặp 8 bước không?**
Về lý thuyết bạn *có thể* nhắc ChatGPT "giờ research giúp tôi, giờ viết, giờ check" — nhưng **YOU phải đứng nhắc từng bước**, và **YOU phải tự ghép kết quả lại**. Chatbot không tự nhảy bước 3 → 4 → 6 → 7. Agent thì có — đó là thiết kế, không phải may mắn. Chatbot là dụng cụ chờ bạn cầm. Agent là nhân sự tự quay vòng.

**2. Nếu nó lạc đề giữa vòng lặp thì sao?**
Lúc đó nó báo tôi kèm lỗi cụ thể, chứ không tự ý đẩy bản dở lên. Tốt nhất: nó tự quay bước 3 sửa. Xấu nhất: nó dừng và gọi tôi. Không bao giờ "lén" giao hàng lỗi rồi mặc kệ — vì bước 6 (quality gate) là chốt chặn cuối trước cửa deploy.

**3. Có cần biết code để có vòng lặp này không?**
Không. Trong khoá Nhân Sự Toàn Năng Hermes, bạn chỉ viết câu lệnh (prompt) quy định "phải chạy những bước nào trước khi giao" — y như bạn dặn thư ký quy trình. Không một dòng code. Người không chuyên như Hỉ làm được, thì bạn cũng làm được.

## Kết luận — đừng thuê "người trả lời", hãy có "người đi làm"

Sự khác biệt giữa một chatbot và một AI Agent không nằm ở độ "thông minh" của câu trả lời. Nó nằm ở **cái vòng lặp phía sau**. Chatbot nói xong là hết trách nhiệm. Agent chạy 8 bước — tìm, nghiên cứu, viết, check, lưu, lịch, báo cáo — rồi mới giao bạn kết quả.

Năm 2025–2026, cả ngành đã quay sang "agentic": Twill.ai, OctopusGarden, Automatiq... đều chạy đúng quy trình đó. Thế thì nhân sự ảo của bạn càng phải có vòng lặp — chứ không thể hỏi một câu đáp một câu rồi thôi.

👉 Muốn tự dựng "nhân sự ảo" biết chạy vòng lặp 8 bước mà không cần biết code: khoá **Nhân Sự Toàn Năng Hermes** — 37 bài thực chiến, giá mở bán sớm **239K** (gốc 499K), hoàn tiền 7 ngày nếu thấy không hợp: https://speedreading.vn/shermes

Giao việc. Nhận quy trình. Không đứng nhắc từng bước.
