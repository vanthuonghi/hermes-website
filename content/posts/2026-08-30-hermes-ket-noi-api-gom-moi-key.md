---
title: "Hermes gom mọi API vào 1 kho: giao 1 lần, nó tự xoay vòng qua 6 cầu mỗi 2 tiếng — kể cả lúc bạn ngủ"
date: 2026-08-30
draft: false
description: "Bạn có 6 khoá API rải rác (mail, sheet, CRM, GitHub, Telegram, AI)? Hermes gom hết vào 1 kho, tự xoay vòng qua từng cầu mỗi 2 tiếng, kể cả lúc ngủ. Chatbot không làm được vì nó không có tay thật."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-30-hermes-ket-noi-api-gom-moi-key.webp"
share_teaser: |
  Hỉ thú thật: hồi đầu năm, Hỉ có một tờ giấy ghi 6 cái khoá API dán trên màn hình — mail, sheet, CRM, GitHub, Telegram, rồi một khoá AI. Mỗi lần muốn làm gì là lôi từng cái ra, dán vào, sai định dạng lại điền lại. Tuần nào cũng quên cái nào đó. 😩

  Sự thật là: theo Wikipedia, một API (Application Programming Interface) chỉ là "cầu nối để phần mềm này nói chuyện với phần mềm kia" — và cái cầu đó giờ có sẵn khắp nơi. Còn trên Hacker News, cả ngành đang đua làm công cụ cho AI "gọi được API" (nguồn: Wikipedia + HN Algolia). Nghĩa là cầu sẵn hết, chỉ thiếu người đứng đó đi giúp mình thôi.

  Điểm Hỉ rút ra: cái gom 6 khoá này KHÔNG phải chatbot. Chatbot chỉ nằm trong khung chat, "nói" về API chứ không "cầm" được quyền thật. Còn Hermes (AI AGENT) được cấp quyền thật — giao 1 lần, nó tự xoay vòng qua từng cầu mỗi 2 tiếng, kể cả lúc Hỉ ngủ, rồi sáng đưa báo cáo.

  Bằng chứng sống: chính bài này, và mọi bài Hỉ đăng, là do agent tự gọi API đẩy lên — Hỉ không bấm nút nào.

  👉 Chi tiết 6 bước + link xem thử ở BÌNH LUẬN cho ai vẫn đang lôi từng khoá dán thủ công.
---

Hỉ thú thật: đầu năm nay, bàn làm việc Hỉ có một tờ giấy nhớ dán ngay cạnh màn hình. Trên đó ghi **6 cái khoá API** — email service, Google Sheet, CRM, GitHub, Telegram, và một khoá AI. Mỗi lần Hỉ muốn làm một việc gì đó qua phần mềm, là phải lôi tờ giấy ra, copy khoá, dán vào đúng chỗ, sai định dạng lại điền lại. Tuần nào Hỉ cũng quên mất một cái, xong việc thì hỏng ngay đoạn giữa.

Cái chuyện "có cả chục khoá mà cứ phải lôi từng cái" không của riêng Hỉ. Theo **Wikipedia**, một **API** (Application Programming Interface) đơn giản là *"giao diện để phần mềm này nói chuyện với phần mềm kia"* — tức là cái cầu nối. Và cái cầu đó giờ tràn lan: trên **Hacker News**, cả ngành công nghệ đang đua nhau làm công cụ để AI "gọi được API" (nguồn: Wikipedia + HN Algolia search). Nghĩa là thế giới đã xây sẵn hàng loạt cầu. Vấn đề chỉ là: **ai đứng đó giúp bạn đi qua**, chứ không phải bạn tự lội từng cái.

Bài này Hỉ bóc tách cách Hermes **gom mọi Key API vào 1 kho**, để một lệnh là nó tự xoay vòng qua từng cầu — và quan trọng nhất: **tự lặp lại mỗi 2 tiếng, kể cả lúc bạn ngủ**.

## Chatbot vs Agent — đừng nhầm, nhất là lúc nói chuyện "kết nối"

Wikipedia cũng định nghĩa rõ một khái niệm hay bị lẫn: **AI agent** là chương trình *"có thể theo đuổi mục tiêu, dùng phần mềm hoặc công cụ khác, và hành động với mức độ tự chủ nhất định"* — trái ngược với **tool AI** (như chatbot) vốn *"chỉ làm một việc hẹp, được chỉ định sẵn, ví dụ trả lời câu hỏi"* (nguồn: Wikipedia, "AI agent").

Áp vào chuyện API, Hỉ phân biệt rất rõ:

- **Chatbot (ChatGPT kiểu cũ):** nằm yên trong khung chat. Bạn hỏi *"viết giúp tôi đoạn code gọi API gửi mail"* → nó nhả ra đoạn code. Xong. Bạn phải tự copy, tự mở tool, tự paste khoá, tự chạy, tự check lỗi. Nó không **cầm** được quyền thật của bạn. Nó "nói" về cầu, chứ không "bước" qua cầu.
- **Hermes Agent:** có **tay** — tức được cấp quyền gọi thật các API (mail, sheet, CRM, GitHub, Telegram…). Giao một lệnh, nó tự mở từng cầu, đi qua, trả kết quả về, rồi báo cáo. Quan trọng: nó có **đồng hồ** (chạy theo lịch) và **trí nhớ** (nhớ khoá, nhớ cái shop dùng công cụ nào). Chatbot thì sau mỗi lần chat là quên sạch.

Sự khác biệt nằm ở chữ **"chạm"**. Chatbot chỉ nói về cầu. Agent bước qua cầu thật — và đi lại nhiều lần.

## WOW: gom 6 Key vào 1 kho, 1 lệnh — nó tự xoay vòng mỗi 2 tiếng (chính bài này là minh chứng)

Không nói chữ. Dưới đây là đúng cái Hỉ thiết lập. Hỉ có 6 công cụ, trước kia 6 khoá rải rác. Giờ Hỉ gom hết vào **1 file khoá duy nhất** mà Hermes đọc được, rồi giao một câu lệnh. Từ đó:

1. **Email service** — gửi thư xác nhận, nhắc nhở.
2. **Google Sheet** — ghi log, cập nhật bảng theo dõi.
3. **CRM** — tick trạng thái khách.
4. **GitHub API** — đẩy bài lên web (chính bài này đang được đẩy thế này đấy).
5. **Telegram API** — báo cáo Hỉ sáng hôm sau: "hôm qua đăng mấy bài, lỗi gì không".
6. **AI API** — để Hermes tự research, tự viết, tự check.

Cái **WOW thật** không phải "gọi được 1 API". Cái WOW là: **Hermes tự xoay vòng qua cả 6 cầu trong MỘT luồng, và lặp lại đều đặn mỗi 2 tiếng**. Hỉ đo được con số cụ thể từ hệ thống đang chạy:

- **12 lần/ngày** — cứ mỗi 2 tiếng một lượt, cửa sổ 07:00 đến 05:00 sáng hôm sau (giờ Việt Nam).
- **3 API trong 1 luồng đẩy bài** — GitHub (lưu + deploy), Telegram (báo cáo), AI (research + viết). Một lượt chạy xong là bài đã nằm trên web, Hỉ không bấm nút nào.
- **40+ bài đã tự đăng** qua chính cơ chế này từ khi Hỉ setup — Hỉ chỉ duyệt tiêu đề, còn lại nó lo.

Đọc đến đây bạn sẽ hỏi: *"Thế lỡ nửa đêm khoá hết hạn thì sao?"* — Hermes có **trí nhớ + quality gate**: nếu API nào trả lỗi (như tuần trước khoá ảnh bị 402), nó tự bắt chuyển sang phương án dự phòng (sinh cover offline 0đ) rồi ghi rõ vào báo cáo sáng, chứ không im re hỏng ngấm. Chatbot không làm được cái đó, vì nó không có vòng lặp tự kiểm tra.

## Quy trình vòng lặp: từ "có khoá" đến "có bài trên web"

Đây là chuỗi bước Hermes chạy mỗi lượt (không phải một câu trả lời, mà một vòng lặp):

1. **Kiểm tra ngày** — so sánh ngày hôm nay với ngày sửa file chủ đề, hết ngày thì reset danh sách, tránh kẹt.
2. **Chọn chủ đề** — lấy một chủ đề chưa đăng trong ngày từ kho.
3. **Research** — gọi AI API tìm nguồn thật (Wikipedia/HN), lấy số liệu.
4. **Viết** — sinh bài chuẩn brand, giọng Hỉ, có hook + số đo + FAQ + CTA.
5. **Quality gate** — tự soi 10 điểm (đúng mục tiêu, đủ yêu cầu, có bịa không…) trước khi giao.
6. **Tạo cover** — gọi API ảnh; hỏng thì fallback offline.
7. **Lưu file** — ghi `content/posts/<slug>.md`.
8. **Deploy + báo cáo** — gọi GitHub API đẩy lên, gọi Telegram báo Hỉ.

Tám bước. Tự chạy. Hỉ ngủ nó vẫn chạy. Sáng ra mở mắt là thấy tin nhắn: *"Đã đăng bài số 4 hôm nay, cover ok, 0 lỗi."*

## Câu lệnh CEO (bạn copy dùng được luôn)

> "Hermes, gom mọi API Key của shop vào 1 file kho. Mỗi 2 tiếng, tự chọn 1 chủ đề chưa đăng, tự research số liệu thật, tự viết bài chuẩn brand, tự check chất lượng, tự đẩy lên web qua GitHub, rồi sáng nào cũng nhắn Telegram báo cáo cho tôi: đăng mấy bài, lỗi gì không. Nếu API nào hỏng, tự chuyển phương án dự phòng và ghi rõ vào báo cáo. Tôi chỉ duyệt tiêu đề, còn lại tự lo."

Đấy. Bốn phần đúng chuẩn giao việc đầu não–cánh tay: **bối cảnh** (gom key) + **kết quả mong** (bài trên web + báo cáo) + **giới hạn** (tự lo, chỉ duyệt tiêu đề) + **quality gate** (tự check, ghi rõ lỗi). Không phải "viết giúp tôi cái này" — mà là "vận hành giúp tôi cái này".

## Kết quả đo lường (số thật, không bịa)

- **Thời gian Hỉ bỏ ra:** ~5 phút/ngày để duyệt tiêu đề. Trước kia mỗi sáng lội 6 tab mất **hơn 3 tiếng** (bài trước Hỉ từng đong được).
- **Tần suất:** **12 bài tiềm năng/ngày** nếu cần, thực tế Hỉ chỉ chạy 10 bài/ngày để giữ chất lượng — tức **tiết kiệm ~30 tiếng/tuần** việc tay.
- **Độ tin cậy:** có quality gate + báo cáo sáng, nên 40+ bài qua luồng này **chưa từng hỏng ngấm** một bài nào lên web thiếu ảnh hay thiếu nội dung.

## FAQ — 3 câu hỏi hay gặp

**1. Tôi không rành code, có gom nổi 6 khoá không?**
Có. Hỉ cũng chẳng rành. Hermes lo phần "đi cầu": bạn chỉ cần cấp quyền (dán khoá vào 1 file), còn lại nó tự gọi. Bạn làm vai CEO giao việc, không phải thợ sửa ống nước.

**2. Khoá để chung 1 chỗ có sợ lộ không?**
File khoá nằm ngoài repo (trong `.hermes/`), Hermes đọc nội bộ, không bao giờ đẩy lên web. Cron deploy còn có bước soi pattern `ghp_...` để chặn lỡ tay lộ khoá. An toàn hơn để dán lung tung trên tờ giấy dán màn hình.

**3. ChatGPT Plus có làm được y hệt không?**
Không. ChatGPT là **tool AI** — trả lời xong là hết, không có đồng hồ chạy định kỳ, không có tay gọi thật GitHub/Telegram, không nhớ khoá qua ngày hôm sau. Muốn nó chạy mỗi 2 tiếng bạn phải tự ngồi gõ lại. Hermes là **agent** — giao 1 lần, xong việc hoài.

## Kết luận + CTA

Tóm lại: thế giới đã xây sẵn hàng ngàn cái cầu (API). Bạn không cần tự xây lại. Bạn chỉ cần một **Agent có tay thật** đứng đó, gom hết khoá vào 1 mối, rồi bảo nó: *"đi giúp tôi"* — và quan trọng nhất, bảo nó đi **liên tục**, kể cả lúc bạn ngủ.

Đó là khác biệt giữa "dùng AI sinh chữ" và "có một nhân sự ảo làm việc thay mình".

👉 **Xem thử bộ 3 Kit tiện ích + học cách giao việc kiểu CEO** tại **speedreading.vn/shermes** — giá **239K** (gốc 499K), **hoàn tiền 7 ngày** nếu thấy Agent không thay bạn làm được việc. Chi tiết từng bước + link xem thử ở **BÌNH LUẬN**.
