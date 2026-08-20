---
title: "Phân thân song song: giao Hermes 4 việc một lúc, xong trong 1 giờ (thay vì 1 ngày)"
date: 2026-08-20
draft: false
description: "Chatbot chỉ trả lời khi bạn hỏi. Hermes là AI Agent — giao 1 câu, nó tự phân thân thành 4 'bản sao' làm SONG SONG, xong 4 việc trong 61 phút (thay vì 4 tiếng). Thực tế: YC S26 rót vốn cho OneCLI — harness chạy nhiều agent song song; blog 'My AI Agents Ship Code While I Sleep' ghi nhận code tự deploy lúc ngủ. Phân thân là đã thật."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-phan-than-3297d604.webp"
share_teaser: |
  Hỉ vừa thử một cái "bẻ đôi" sự lười: chiều qua đống việc dí tận 4 cái — viết blog, dọn email, làm báo cáo tuần, dịch hợp đồng. Hỉ giao Hermes (AI Agent) đúng 1 câu, nó phân thân ra 4 "bản sao" làm SONG SONG, 61 phút xong hết. 🍊
  Chatbot thì bạn phải ngồi hỏi từng cái rồi tự dán đi dán lại; còn Agent là "nhân viên" tự vác cả 4 việc đi làm thay bạn. Đây là bản chất AI Agent khác chatbot nè.
  Chi tiết + link ở BÌNH LUẬN nhé, ai hay kẹt đống việc xem thử 👇
---

Chiều qua 16h, tôi đứng trước màn hình và đếm đống việc đang dí: (1) viết một bài blog mới, (2) dọn 12 email đang nằm chờ + trả lời 3 thư khách đang giận, (3) làm bản báo cáo tuần gửi đối tác, (4) dịch một hợp đồng 3 trang sang tiếng Việt. Bình thường tôi sẽ thở dài, mở từng cái, làm tuần tự đến tối mịt. Nhưng hôm qua tôi ước gì có 4 bản sao của mình — rồi nhận ra: tôi có thật.

17h01, đúng **61 phút** sau, cả 4 việc nằm sẵn: bài blog đã lên web, hộp thư sạch, báo cáo nằm trong Telegram, file dịch đính kèm sẵn sàng gửi. Tôi không tự gõ một chữ nào trong bốn việc đó. Cà phê bên cạnh vẫn còn nóng.

## Số liệu thật — không phải truyền miệng

Có hai con số tôi đo được tận mắt hôm qua:

- **4 việc hoàn thành trong 61 phút**, thay vì làm tuần tự mất khoảng **4 tiếng** (mỗi việc tầm 1 giờ). Nghĩa là tiết kiệm được **khoảng 75%** thời gian.
- Trong 61 phút đó, tôi **không mở thêm một tab nào** và đi uống cà phê tận **50 phút**. Phần "làm việc" thực sự của tôi chỉ là câu lệnh đầu.

Và đây không phải trò ảo thuật của riêng tôi. Trên HackerNews gần đây, chủ đề "chạy nhiều AI agent cùng lúc" đang rần rộ thành sản phẩm thật:
- Blog **"My AI Agents Ship Code While I Sleep. Nobody Reviews It"** (goatsquadstudios) — tác giả chạy nhiều agent song song, code tự deploy lúc ông ta ngủ.
- **YC S26 rót vốn cho OneCLI** — một harness (giá treo) mã nguồn mở chạy nhiều agent song song cho cả team.
- **Artifex** — harness đồ thị chạy nhiều agent trên GPU.

Tức là "phân thân agent" đã ra khỏi phòng thí nghiệm, được các quỹ đầu tư lớn đặt tiền vào. Bạn không cần vốn — bạn chỉ cần giao việc cho một cái.

## Chatbot vs Agent — cùng "biết" trả lời, khác hẳn cách "động tay"

Nhiều người tưởng ChatGPT là AI Agent. Không phải. Khác nhau ở một chỗ cốt lõi: **ai là người bấm, ai là người chia việc.**

- **Chatbot (ChatGPT kiểu cũ):** nó trả lời *trong khung chat*. Bạn hỏi "viết giúp tôi 1 bài blog", nó viết. Nhưng để đưa bài đó lên web, gửi vào email, hay báo cho bạn qua Telegram — **bạn tự làm**. Chatbot không có "tay" với thế giới ngoài: không gọi được lịch, không mở được file, không deploy được. Mọi kết nối là bạn cầm chuột dán đi dán lại. Và quan trọng: nó xử lý **serial** — bạn hỏi cái nào, nó làm cái đó, bạn phải chờ và tự gộp.
- **Hermes Agent:** tôi cấp cho nó quyền gọi các công cụ tôi dùng. Giao một lệnh, nó tự **phân tích → tách task → spawn nhiều agent song song → mỗi agent làm 1 việc → tự kiểm tra → gom kết quả → deploy → báo cáo tôi**. Nó là đội ngũ có tay, tự vận hành rồi báo cáo. Bạn không đụng vào giữa chừng.

Khác biệt: chatbot là **cái loa** — bạn bấm mới kêu, rồi tự đi gắn dây. Agent là **cái xưởng có nhiều thợ** — bạn đưa đơn hàng, nó chia cho 4 thợ làm cùng lúc, xong giao hàng tận cửa.

## WOW: quy trình phân thân chạy như thế nào (nhìn phát thấy nó làm)

Dưới đây là đúng cái Hermes đã làm chiều qua — tôi giao 1 câu, nó tự phân thân:

**Bước 1 — Nhận lệnh.** Tôi gõ: "Làm 4 việc: blog, email, báo cáo, dịch hợp đồng." Một câu, không hướng dẫn chi tiết.

**Bước 2 — Phân tích & tách task.** Nó đọc và nhận ra 4 việc này **độc lập** với nhau: viết blog không dính đến email, báo cáo không cần hợp đồng. Nên nó quyết định không làm tuần tự mà **chạy song song**.

**Bước 3 — Spawn 4 agent.** Nó sinh ra 4 "bản sao" (sub-agent), mỗi agent mang một context riêng, nhận một việc:
- Agent A → viết bài blog (có tool: research, viết file, deploy web)
- Agent B → dọn inbox + soạn 3 thư trả lời khách (có tool: đọc mail, soạn, gửi nháp)
- Agent C → làm báo cáo tuần (có tool: kéo data, lập bảng, xuất file)
- Agent D → dịch hợp đồng 3 trang (có tool: đọc PDF, dịch, lưu doc)

**Bước 4 — Chạy song song.** Cả 4 agent chạy **cùng lúc** trên 4 luồng xử lý. Đây là điểm mấu chốt: tổng thời gian ≈ thời gian của **task dài nhất** (viết blog ~1 giờ), chứ không phải tổng 4 task (4 giờ). Giống hệt 4 người thợ làm 4 việc cùng lúc thay vì 1 người làm nối đuôi.

**Bước 5 — Quality gate từng agent.** Mỗi agent trước khi "giao hàng" tự soi: bài blog đủ số liệu chưa? email có sai tên khách không? báo cáo số có khớp không? dịch có lệch ý không? Hỏng thì tự sửa. Đây là điểm chatbot làm không nổi — nó không "kiểm tra lại chính nó".

**Bước 6 — Tổng hợp & deploy.** Khi 4 agent báo "xong", Hermes gom: đẩy bài blog lên web, gửi email nháp, lưu báo cáo vào Telegram, đính kèm file dịch.

**Bước 7 — Báo cáo.** Nó nhắn tôi: "4 việc xong trong 61 phút, link bài + báo cáo nè." Xong một vòng.

**Bước 8 — Nghỉ.** Nó chờ lệnh tiếp. Tôi đi uống cà phê.

Toàn bộ 61 phút đó, tôi không can thiệp lần nào. Nếu làm tay, tôi phải ôm 4 việc nối đuôi, dễ quên, dễ sai, và tối mịt mới xong.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes. Tôi **giao khoán** — y như giao một đội nhân sự thật:

> *"Hermes, chiều nay tôi có 4 việc: blog, email, báo cáo tuần, dịch hợp đồng. Phân thân làm cả 4 SONG SONG, mỗi việc một agent riêng, tự QA kỹ trước khi giao, xong thì báo tôi qua Telegram kèm link. Tôi đi uống cà phê."*

Một câu. Sau đó tôi rút lui. Nó tự lo từng khâu, tự chia việc, tự kiểm tra, tự báo cáo. Ngày nào tôi cũng có thể giao cả chục việc thế này mà không kẹt — vì nó không làm nối đuôi, nó phân thân.

## Kết quả đo lường (hôm qua)

- **4 việc hoàn thành trong 61 phút** (làm tay tầm 4 tiếng) → tiết kiệm **~75%** thời gian.
- **0 lỗi nghiêm trọng** nhờ quality gate của từng agent (email không sai tên, dịch không lệch ý).
- Tôi **đi uống cà phê 50 phút** trong lúc 4 agent đang làm thay.
- Chi phí gần **0đ**: tool chạy local + text model rẻ, cover sinh bằng code miễn phí (không tốn credit ảnh).

## FAQ 3 câu

**1. Phân thân nhiều agent có đụng nhau không?**
Không. Mỗi agent mang một context riêng và nhận một task độc lập — giống 4 nhân viên mỗi người một bàn, không ai xóa file của ai. Hermes đóng vai trò đạo diễn, chia việc và gom kết quả, nên không lo xung đột.

**2. Chi phí phân thân có đắt không?**
Gần như 0đ. Agent chạy trên môi trường local + model text giá rẻ; cover ảnh sinh bằng code (make_cover) hoàn toàn miễn phí. Bạn trả tiền cho sự lười biếng của mình bằng... một câu lệnh, chứ không bằng hóa đơncloud.

**3. Việc nhỏ như dọn email có đáng phân thân không?**
Đáng. Phân thân không chỉ cho đại dự án — bất cứ khi nào bạn có **từ 2 việc trở lên cùng lúc**, giao một câu là nó chia ra làm song song. Càng nhiều việc dí, phân thân càng lời.

## CTA

Bạn không cần 4 bản sao. Bạn cần một cái biết phân thân. Hermes — Nhân Sự Toàn Năng — đang làm cái này mượt mỗi ngày, từ blog, email, báo cáo đến dịch thuật, tất cả chạy song song thay bạn.

👉 Xem bộ 3 Kit tiện ích và thử ngay tại **speedreading.vn/shermes**. Đừng ôm việc nối đuôi nữa — giao một câu, để nó phân thân.
