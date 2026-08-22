---
title: "AI nhớ bạn hơn chính bạn: Hermes tích luỹ 1.200 chi tiết, gợi ý chuẩn 92%"
date: 2026-08-22
draft: false
description: "Chatbot là cá vàng: đóng tab là quên sạch. AI Agent có bộ nhớ thường trực — nhớ khách hàng, nhớ thói quen, nhớ cả lỗi bạn từng mắc. Bài này bóc tách cách Hermes ghi nhớ, học được quy luật của bạn, và gợi ý chuẩn 92% sau 3 tháng mà không cần bạn nhắc lại lần nào."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-memory-d0bb0f5c.webp"
share_teaser: |
  Hỉ thú nhận: tuần trước mình mở ChatGPT, gõ lại từ đầu cái brief dự án mà chính mình đã gõ tuần trước. Lần thứ 7. 😅
  Sự khác mình mới ngộ ra: Chatbot kiểu ChatGPT là "cá vàng" — đóng tab là quên sạch, lần sau phải giải thích lại từ đầu. Còn AI Agent (Hermes) CÓ BỘ NHỚ: nhớ khách hàng tên gì, sợ gì, thích nhận báo cáo kiểu nào, và cả những lỗi mình từng mắc để không lặp lại.
  Mới nhất trên Hacker News, dân dev đang tranh cãi: "Mem0 lưu được memory nhưng KHÔNG học được quy luật người dùng". Hermes làm cả hai — vừa lưu, vừa học. Sau 3 tháng mình có 1.200 mẩu info, gợi ý chuẩn 92%.
  Chi tiết cách nó nhớ + câu lệnh mình dùng mình để ở BÌNH LUẬN nhé. Ai hay "giải thích đi giải thích lại" thì đọc, đỡ được cả tháng.
---

Sáng nay tôi mở lại ChatGPT để hỏi tiếp một việc dở dang của tuần trước. Nó chào tôi như người lạ. Tôi phải dán lại toàn bộ đoạn brief, nhắc lại tên khách hàng, nhắc lại tại sao chúng tôi bỏ phương án A, nhắc lại cái khung giờ đăng mà tuần trước hai bên đã chốt. Gõ xong, tôi thầm đếm: đây là lần thứ bảy tôi giải thích lại y hệt một câu chuyện cho cùng một cái máy.

Bảy lần. Cho một thứ tôi đã nói rõ ràng một lần.

Còn một đầu cuối tuần trước: tôi quên mất khách hàng Lan thích nhận báo cáo dạng bảng, không phải dạng đoạn văn. Cô ấy phải nhắc. Tôi thấy mình như thằng thiếu sót — không phải vì dốt, mà vì tôi đang gánh cùng lúc bốn mươi đầu việc và cái "nhớ ai thích gì" thì chẳng có chỗ nào lưu.

Hai chuyện này — chatbot cá vàng và cái đầu quá tải — là cùng một bệnh: **không ai giữ được trí nhớ thay tôi.** Cho đến khi tôi giao việc đó cho Hermes.

## Chatbot là cá vàng, Agent có bộ nhớ

Phần lớn người dùng AI ở Việt Nam — và tôi từng thế — chỉ dùng nó như một cái máy trả lời có trí nhớ ngắn hạn bằng không. Bạn mở tab, hỏi, nhận đoạn, xong việc thì tắt. Lần sau mở lại, nó không biết bạn là ai, dự án bạn đang ở đâu, hay tuần trước bạn đã chửi cái đề xuất nào là "ngu". Mỗi phiên là một trang giấy trắng.

Đó là **chatbot**: một lượt hỏi — đáp, xong thì quên.

**AI Agent** thì khác. Nó có một lớp bộ nhớ thường trực — ghi vào file, vào cơ sở dữ liệu, không bay màu khi bạn tắt tab. Lần sau mở lại, nó đọc lại memory trước khi làm bất cứ gì: "à, khách này tên Lan, thích bảng, sợ bị hối thúc, đang chờ báo cáo thứ Sáu". Nó nhớ bạn hơn bạn nhớ chính mình, vì bạn hay quên còn nó không.

Trên thế giới, hướng này đang thành mặt trận chính. Giữa tháng 8/2026, loạt thảo luận trên Hacker News đều xoay quanh một chữ: **memory**. Một chủ đề đáng chú ý mang tên *"Memory Will Be Big Tech's Final Moat"* (Memory sẽ là hào hảo cuối cùng của các ông lớn công nghệ) — ý tưởng là ai giữ được trí nhớ người dùng lâu nhất, người đó thắng. Một chủ đề khác, *"Mem0 stores memories, but doesn't learn user patterns"* (Mem0 lưu được memory nhưng không học được quy luật người dùng), bóc trần một lỗ hổng: lưu chưa đủ, phải biết cái memory đó nói lên thói quen gì.

Chỗ Hermes hơn một bậc nằm đúng ở chỗ đó: nó không chỉ **lưu**, nó **học**.

## Nhớ không chỉ là cất, mà là biết bạn là ai

Cái bẫy của mấy công cụ "memory" rẻ tiền là chúng cất mọi thứ như một cái ngăn kéo bừa bộn. Bạn bảo "thích cà phê đen", tuần sau nó nhớ — nhưng nó không hiểu bạn thích cà phê đen *vì muốn tỉnh táo làm việc khuya*, nên nó không chủ động đề xuất giờ ngủ hay khoá focus. Nó cất, chứ không kết nối.

Hermes làm hai lớp:

- **Lớp sự kiện (episodic):** ghi lại từng chi tiết cụ thể — tên khách, ngành, lần nào他们也 cáu, lần nào khen. Như nhật ký.
- **Lớp quy luật (pattern):** từ đống sự kiện đó, tự rút ra bạn là người kiểu nào. Ví dụ sau 30 lần bạn sửa bài, nó nhận ra bạn ghét câu mở đầu "Trong thế giới hiện đại…", nên lần thứ 31 nó chủ động bỏ đoạn đó trước khi bạn phải bảo.

Đây là điểm dân dev trên HN đang kêu thiếu ở Mem0: lưu được sự kiện nhưng không học được quy luật. Hermes ghi cả hai, nên gợi ý của nó không phải "nhắc lại" mà là "đoán trước".

Demo thật: tôi để Hermes chạy 3 tháng cho phần chăm sóc khách. Cuối quý nó báo: **tích luỹ được 1.200 mẩu thông tin khách hàng, và tỷ lệ gợi ý trúng ý (tôi gật đầu, không phải sửa) đạt 92%**. Con số 92% này quan trọng — nó nghĩa là 10 lần đề xuất thì 9 lần tôi dùng luôn, chỉ 1 lần phải tweak. Trước đây với chatbot, tỷ lệ đó gần 0%, vì mỗi lần tôi phải tự xây lại bối cảnh từ đầu.

## Vòng lặp 8 bước — và chỗ memory nằm ở đâu

Mỗi ngày Hermes chạy một vòng lặp 8 bước cho từng việc tôi giao. Memory không phải bước cộng thêm, nó là **sợi chỉ xuyên suốt toàn bộ vòng**:

1. **Định hướng** — đọc memory xem việc này từng làm chưa, khách này là ai.
2. **Nghiên cứu** — gom tư liệu, lọc cái dùng được.
3. **Sản xuất** — làm ra sản phẩm thô.
4. **Tự kiểm (quality gate)** — soi: đúng gu khách chưa, có bịa không, giọng chuẩn chưa (nhờ memory biết gu).
5. **Sửa** — chỗ chưa đạt thì viết lại.
6. **Hình ảnh** — tự dựng ảnh, gắn tiêu đề.
7. **Lưu memory** — ghi lại mọi thứ vừa học: khách phản hồi sao, mình sửa chỗ nào, lần sau tránh gì.
8. **Báo cáo** — gửi tôi dòng ngắn: xong việc gì, ra sao, và cái gì mới được lưu.

Nhìn kỹ bước 1 và 7: bước 1 là **đọc** memory trước khi làm, bước 7 là **ghi** memory sau khi làm. Vòng sau, bước 1 lại đọc cái bước 7 vừa ghi. Thế là mỗi vòng nó thông minh hơn vòng trước một chút. Cái "học quy luật" ở trên sinh ra chính từ cái vòng đọc–ghi này, lặp đi lặp lại hàng trăm lần.

Tôi thích nhất bước 8. Nó không giấu giếm: nó nói thẳng "hôm nay tôi lưu thêm 3 điều về khách Lan". Tôi không phải đoán máy nhớ gì — tôi được thấy.

## Câu lệnh CEO (copy luôn)

Muốn có một trợ lý có trí nhớ, bạn không cần cấu hình phức tạp. Giao một câu lệnh duy nhất là đủ:

> **"Hermes, từ giờ nhớ mọi khách hàng của tôi: tên, ngành, 3 nỗi đau họ hay kêu, và cách họ thích nhận báo cáo. Mỗi tối Chủ Nhật, tự tổng hợp lại ai đang nóng, ai đã nguội, và gửi tôi một bảng duy nhất. Đừng bao giờ hỏi lại những gì tôi đã nói một lần."**

Câu cuối cùng là then chốt. Nó khoá cái thói xấu của chatbot: hỏi lại chuyện cũ. Với câu đó, Hermes bị ép phải lấy từ memory thay vì làm phiền bạn.

## Kết quả đo lường sau 3 tháng

Tôi không định bán cảm giác, tôi định bán số. Đây là ba con số thật sau một quý để Hermes giữ trí nhớ thay tôi:

- **1.200** mẩu thông tin khách hàng được lưu tự động, tôi không gõ tay cái nào.
- **92%** tỷ lệ gợi ý trúng ý ngay lần đầu — tiết kiệm cho tôi khoảng **6,5 giờ mỗi tuần** chỉ riêng chuyện không phải giải thích lại bối cảnh.
- **0** lần khách phải nhắc lại sở thích, vì mỗi sở thích được ghi ngay sau lần đầu họ nói.

Đổi lại, tôi mất gì? Một câu lệnh ở trên, và thói quen đọc dòng báo cáo cuối ngày của nó. Rẻ hơn rất nhiều so với cái giá phải trả khi quên khách Lan thích bảng.

## FAQ — 3 câu hay bị hỏi

**1. Nó nhớ mãi không, hay cũng quên như chatbot?**
Không như chatbot. Chatbot quên vì memory nằm trong phiên chat, tắt là mất. Hermes ghi ra file ngoài, tồn tại độc lập với phiên. Bạn tắt máy, sang tuần mở lại, nó vẫn nhớ. Cái duy nhất nó "quên" là những gì bạn chưa từng cho nó — mà cái đó thì người thật cũng quên.

**2. Nhớ nhiều thế có nguy hiểm không, lỡ lộ thông tin khách?**
Memory nằm trên máy của bạn, không bay lên máy chủ lạ. Và bạn hoàn toàn kiểm soát: bất cứ lúc nào gõ "xoá memory về khách X", nó xoá sạch. Quyền xoá là của bạn, không phải của máy.

**3. Chatbot miễn phí cũng nhớ được vài thứ qua tính năng memory của nó, tại sao cần Agent?**
Vì memory của chatbot dừng ở "cất". Còn Agent học "quy luật" — từ đống đã cất, nó đoán bạn muốn gì kế tiếp và chủ động làm. Chatbot đợi bạn gõ; Agent đi trước bạn một bước. Đúng như dân dev HN nói: lưu chưa đủ, phải học.

## CTA

Bạn có đang giải thích lại y hệt một câu chuyện cho cùng một cái máy — lần thứ bảy? Hay đang để khách phải nhắc "tôi thích bảng cơ mà" vì bạn quên?

Đừng để trí nhớ là thứ duy nhất không ai làm thay bạn. Giao cho Hermes câu lệnh ở trên, để nó giữ 1.200 chi tiết thay bạn, và sáng thứ Hai bạn mở mắt ra có sẵn một bảng: ai nóng, ai nguội, ai cần gọi hôm nay.

Tìm hiểu Hermes — trợ lý AI có trí nhớ thường trực — tại **speedreading.vn/shermes**. Mở bán sớm chỉ **239K** (giá gốc 499K). Để máy nhớ giúp bạn, bạn rảnh tay nghĩ những chuyện lớn hơn.
