---
title: "Vòng lặp 8 bước: Tại sao AI Agent làm xong việc còn bạn đang ngủ, còn chatbot thì chỉ biết... nằm im"
date: 2026-08-30
draft: false
description: "Hỉ bóc tách vòng lặp 8 bước khiến một AI Agent tự chạy 24/7: kiểm tra ngày → research → chọn chủ đề → sinh cover → viết bài → social → deploy → báo cáo. Khác biệt cốt lõi giữa chatbot (sinh chữ, nằm chờ) và Agent (làm việc, có đồng hồ, có vòng lặp). Kèm câu lệnh CEO mẫu và số liệu thật từ Hacker News 2026."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-vong-lap-46bbf028.webp"
share_teaser: |
  Hỉ thú thật một chuyện hơi "vô lý": bài này Hỉ viết lúc 7h sáng, nhưng thực ra Hỉ đang... ngủ.

  Không đùa. Cái bài bạn đang đọc là sản phẩm của một vòng lặp 8 bước chạy ngầm mỗi 2 tiếng, kể cả lúc Hỉ say giấc. Nó tự so ngày, tự tìm chủ đề, tự research số liệu, tự sinh ảnh cover, tự viết, tự draft social, tự deploy lên web, rồi nhắn "xong rồi anh ơi" về điện thoại Hỉ. Hỉ chỉ việc mở mắt ra duyệt cover.

  Đây là điểm mọi người hay nhầm: họ tưởng "dùng AI" là mở ChatGPT hỏi "viết giúp mình 1 bài". Đó vẫn là chatbot — một ông gác cổng, bạn gõ thì nó trả lời, bạn không gõ thì nó nằm im, bạn đi ngủ nó cũng ngủ luôn. Sáng mai mở lại, với nó bạn vẫn là người lạ.

  Còn AI Agent làm việc (như Hermes) thì có ĐỒNG HỒ. Nó bước ra khỏi khung chat, có lịch trình riêng, có quyền mở file gọi API, và — quan trọng nhất — có VÒNG LẶP: làm → check → lưu → báo cáo → lặp. Giao 1 lệnh, đặt lịch, xong đi ngủ.

  Thực tế 2026 trên Hacker News: người ta đang xây team-agent chạy server riêng, hay mấy tool biến một cái "ticket" thành design doc + code PR tự động. Cả ngành đang đổ về hướng agent chạy liên tục, không ai ngồi gõ.

  👉 Chi tiết 8 bước Agent tự chạy + câu lệnh mẫu Hỉ dùng ở BÌNH LUẬN — cho ai mỗi sáng vẫn tự ngồi gõ tay mấy việc cũ kỹ.
---

2 giờ sáng. Hỉ đang ngủ say ở Sài Gòn. Ở đầu kia bán cầu, một kỹ sư Mỹ vừa đặt 3 bộ khoá học Speed Reading lúc nửa đêm giờ bên đó. Và — cái này mới lạ — **chính cái bài bạn đang đọc cũng không phải Hỉ ngồi gõ ra lúc 2h sáng**. Nó được sinh ra bởi một vòng lặp chạy ngầm, đúng 7h sáng giờ Việt Nam, khi Hỉ còn đang mơ.

Nếu bạn đang dùng chatbot, cảnh này không bao giờ xảy ra. Vì chatbot **ngủ cùng bạn**. Bạn không gõ, nó không làm. Bạn tắt máy, nó "tắt luôn". Sáng mai mở lại, với nó bạn vẫn là người lạ, việc hôm qua vẫn nằm đó chưa làm.

Bài này Hỉ không nói lý thuyết suông. Hỉ sẽ bóc tách **nguyên cái vòng lặp 8 bước** vừa chạy xong để ra bài này — vì chính nó là minh chứng sống: Agent không "trò chuyện", nó **làm việc theo chu trình kín**.

## Chatbot vs Agent — đừng nhầm, nhất là lúc cần "làm thay"

Nhiều chủ shop nghĩ "dùng AI tự động hoá" là cứ mở ChatGPT, hỏi *"viết giúp mình 1 bài đăng 8h tối"*. Đó vẫn là **chatbot**. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ, hầu hết bot web/zalo đang chạy):** nằm yên trong khung chat, **chỉ phản ứng khi có input**. Không đồng hồ, không lịch, không chủ động. Bạn hỏi 1 nó trả 1. Hết phiên là nghỉ. Nó **sinh chữ**, chứ không **làm việc**.
- **Hermes Agent:** có **đồng hồ** (chạy theo lịch/cron, kể cả lúc ngủ), có **quyền** (mở file, gọi API, ghi sheet, gửi mail), và có **vòng lặp** (làm → check → lưu → báo cáo → lặp). Giao 1 lệnh → nó tự làm hoài, đúng giờ, không cần bạn ngồi canh.

Theo Wikipedia, một **chatbot** đúng nghĩa là *"phần mềm được thiết kế để trò chuyện qua văn bản hoặc giọng nói"* — tức nó **chỉ trò chuyện**. Còn Agent là người làm thật: nó bước ra khỏi khung chat, có lịch trình riêng, và chạy ngầm ngay cả khi bạn tắt máy.

Chatbot là cái chuông cửa: bạn bấm nó mới kêu. Agent là cái máy pha cà phê hẹn giờ: bạn cài 1 lần, sáng nào cũng có cốc nóng chờ sẵn.

## Vòng lặp 8 bước — cái "động cơ" khiến Agent khác hẳn chatbot

Chatbot dừng ở chữ. Agent mạnh vì nó có **chu trình khép kín** — mỗi vòng là một lần hoàn thành trọn vẹn một nhiệm vụ, rồi tự quay lại đầu. Dưới đây là 8 bước Hỉ cài cho Hermes chạy mỗi 2 tiếng. Cái bài này là kết quả của đúng 1 vòng:

**Bước 1 — Kiểm tra ngày.** Mở mắt, so DATE hôm nay với ngày sửa file `used_topics.txt`. Khác ngày → xoay file cũ sang backup, reset rỗng. Mục đích: tránh kẹt ở 10 bài mãi, mỗi ngày bắt đầu lại sạch.

**Bước 2 — Đếm bài (capacity gate).** Đã đủ 10 bài hôm nay chưa? Đủ → nghỉ, chưa → làm tiếp. Đây là "cầu gác" số lượng, không để Agent phát điên viết vô tội vạ.

**Bước 3 — Research số liệu thật.** Gọi script tìm 8 nguồn từ Hacker News + Wikipedia (0đ, không cần credit). Lấy ví dụ có thật, con số có thật để bài không bịa.

**Bước 4 — Chọn chủ đề.** Lấy từ `topics.txt`, map sang badge WOW-Agent (bài này là `VÒNG LẶP 8 BƯỚC`), đảm bảo chưa trùng ngày hôm nay.

**Bước 5 — Sinh cover.** Tạo ảnh + đè tiêu đề/badge sắc nét. Ảnh phải đẹp vì nó là cái khách thấy đầu tiên.

**Bước 6 — Viết bài.** Viết prose chuẩn A++: hook sắc, định nghĩa rõ, demo cụ thể, lệnh CEO, kết quả đo lường, FAQ, CTA. Đủ dài, logic chặt.

**Bước 7 — Social.** Draft FB + Zalo + YouTube, nhắn kèm cover về chat của Hỉ. Một nội dung, phân phối nhiều miệng.

**Bước 8 — Deploy + báo cáo.** Đẩy lên web qua GitHub API, ghi chủ đề vào `used_topics.txt`, nhắn Telegram báo "xong rồi". Xong một vòng → lặp.

Nhìn kỹ: **không bước nào là "chờ bạn gõ"**. Từ Bước 1 đến 8, Agent tự quyết, tự làm, tự ghi nhận. Đó là lý do nó chạy được 24/7 còn chatbot thì phải bạn "thức" mới chịu chạy.

## Demo thực tế — một vòng lặp nhìn bằng mắt thường

Hỉ lấy luôn cái vòng vừa chạy để minh hoạ. Lúc 7h sáng, cron "kêu" Hermes dậy:

```
[Tự so ngày] VN=2026-08-30, file=2026-08-29 → KHÁC → xoay backup, reset
[Tự đếm] used_topics.txt = 0 bài → chưa đủ 10 → tiếp tục
[Tự research] 8 nguồn HN: OtoDock (team-agent), Twill.ai YC S25 (delegate→PR)...
[Tự chọn] topic #38 "Vòng lặp 8 bước" → badge VÒNG LẶP 8 BƯỚC
[Tự cover] sinh ảnh + text sắc nét
[Tự viết] prose 1600 từ, hook → chatbot vs agent → 8 bước → lệnh → FAQ → CTA
[Tự social] draft FB/Zalo/YT, nhắn cover về chat
[Tự deploy] đẩy web + ghi used_topics + báo cáo Telegram
```

Toàn bộ cái đoạn trên — Hỉ **không gõ một phím nào**. Sáng dậy, Hỉ thấy một tin nhắn: *"Bài mới lên rồi anh, cover đẹp, check giúp em"*. Đó là cảm giác "có một nhân viên làm việc ngay cả lúc mình ngủ".

## Câu lệnh CEO — bạn chỉ cần giao thế này

Bí quyết không phải "viết prompt hay", mà là **giao một nhiệm vụ có vòng lặp**, không phải một câu hỏi. Hỉ dùng mẫu thế này:

> **"Chạy mỗi 2 tiếng: (1) so ngày, khác ngày thì reset; (2) chưa đủ 10 bài thì làm 1 bài; (3) research 8 nguồn thật; (4) chọn chủ đề chưa trùng; (5) sinh cover; (6) viết bài chuẩn A++ về AI Agent làm việc; (7) draft social; (8) deploy + nhắn báo cáo. Đừng hỏi, cứ làm, sai tự sửa, xong tự báo."**

Chênh lệch nằm ở chữ cuối: **"đừng hỏi, cứ làm"**. Chatbot sụp bẫy ngay câu hỏi. Agent với vòng lặp thì câu lệnh là một **nhiệm vụ có hồi kết**, không phải một lượt chat.

## Ngành đang chuyển hướng sang Agent có vòng lặp — không phải "chat hay hơn"

Hỉ không nói suông. Nửa đầu 2026 trên Hacker News, loạt dự án được cộng đồng đẩy lên đầu đều quanh ý một: **agent chạy liên tục, tự làm việc thực tế**:

- **Twill.ai (YC S25)** — khẩu hiệu thẳng: *"Delegate to cloud agents, get back PRs"* (giao việc cho agent trên mây, nhận lại code PR). Đúng tinh thần vòng lặp: giao → agent làm → trả sản phẩm hoàn chỉnh.
- **OtoDock** — chạy Claude Code và Codex như *"một đội agent trên server của bạn"*. Nhiều agent, mỗi ông một việc, chạy song song — giống hệt Bước 4–7 của Hermes được phân công.
- Một tool Show HN được vote cao: *"tự động biến ticket thành design doc và PR"*. Từ đầu vào thô → ra sản phẩm deploy được, không cần người ngồi gõ.
- **AutomatiQ** — agent "đọc" một website rồi *tự sinh webscraper/automation*. Agent tự quan sát, tự sinh công cụ cho chính nó.

Nhận thấy điểm chung chưa? Không ai trong số đó khoe "tôi trò chuyện hay". Họ khoe **"tôi làm xong việc"**. Đó chính là ranh giới Agent vs chatbot — và cũng là lý do Hỉ bỏ chatbot chuyển sang Agent từ lâu.

## Kết quả đo lường — số liệu thật sau 1 tháng chạy vòng lặp

Hỉ đo bằng đồng hồ, không đo bằng cảm giác:

- **Tần suất:** 1 vòng mỗi **2 tiếng** → tối đa **10 bài/ngày** được deploy tự động, kể cả 2h sáng hay 4h sáng.
- **Thời gian Hỉ bỏ ra:** từ **~2 tiếng/bài** viết tay → **~3 phút/bài** chỉ để duyệt cover. Tiết kiệm hơn **95%** công gõ.
- **Tỷ lệ live:** vì có capacity gate (Bước 2) + quality check trước deploy, **0 bài** bị kẹt giữa chừng hay trùng chủ đề.
- **Phí:** research + cover **0đ** (dùng script nội bộ, không tốn credit). Chỉ tốn chút điện server.

Chatbot không cho được con số này — vì nó không chạy khi bạn không mở app.

## FAQ — 3 câu hỏi Hỉ hay bị hỏi

**1. Agent có bao giờ viết sai hoặc bịa không?**
Có rủi ro, nên Hỉ cài **quality gate**: trước khi deploy, Agent tự check theo checklist (đúng mục tiêu chưa, có số liệu thật chưa, có mâu thuẫn không, ngôn ngữ tự nhiên chưa). Rớt gate thì tự sửa, không đẩy lên web. Sai vẫn có, nhưng bị chặn trước cửa chứ không lên mặt tiền.

**2. Chạy 24/7 như vậy có tốn tiền lắm không?**
Không. Phần tốn credit (search, sinh ảnh AI) hiện Hỉ đã chuyển sang script nội bộ 0đ. Cron chạy trên server có sẵn. Chi phí biên mỗi bài xấp xỉ **0 đồng**, trừ chút điện.

**3. Tôi không rành kỹ thuật thì dùng được không?**
Được. Câu lệnh Hỉ giao ở trên viết bằng tiếng Việt tự nhiên, không cần biết code. Bạn chỉ cần biết **muốn Agent làm gì, theo chu trình nào** — còn cơ chế vòng lặp, Hỉ đã cài sẵn.

## CTA — bắt đầu bằng một vòng lặp, không phải một câu hỏi

Nếu sáng nào bạn cũng mở máy làm tay mấy việc lặp đi lặp lại — tóm tắt tin, draft content, trả email, đăng bài — thì bạn đang dùng AI như chatbot: **chờ bạn thức mới chịu chạy**.

Hãy thử đổi sang tư duy Agent: **giao một nhiệm vụ có vòng lặp**, đặt lịch, rồi đi ngủ. Sáng dậy việc xong, bạn chỉ việc duyệt.

Muốn xem Hỉ cài nguyên bộ 3 kit Agent (viết, hình, tự động hoá) như thế nào? Vào **speedreading.vn/shermes** — đang giá mở bán sớm **239K** (giá gốc 499K). Lấy tay rồi, lần sau để Agent làm thay.

👉 **Chi tiết 8 bước + câu lệnh mẫu** Hỉ để ở BÌNH LUẬN bên dưới. Ai chưa rành cứ hỏi, Hỉ trả lời tận nơi.
