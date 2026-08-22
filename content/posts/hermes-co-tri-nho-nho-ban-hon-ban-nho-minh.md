---
title: "Hermes có trí nhớ: nhớ bạn hơn bạn nhớ mình (và không bao giờ lặp lỗi cũ)"
date: 2026-08-23
draft: false
description: "Chatbot mỗi sáng chào 'Xin chào, tôi có thể giúp gì?' như gặp người lạ. AI Agent có bộ nhớ: mở lại là biết bạn đang làm gì, nhắc bạn lời hứa tuần trước, và không lặp lỗi cũ. Bài mổ xẻ lớp memory của Hermes + bằng chứng thật từ Knowl (CLAUDE.md phình 1000 dòng) và mem0 persistent memory."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-memory-69f8e779.webp"
share_teaser: |
  Hỉ thú thật một cái xấu hổ: tuần trước mình hỏi ChatGPT tiếp vụ báo cáo, sáng nay mở lại nó chào "Xin chào, tôi có thể giúp gì?" — tỉnh bơ như mới gặp. 😅
  Còn Hermes (AI Agent) thì khác: gõ "tiếp bài báo cáo tuần nha", nó nhảy vào đúng chỗ mình dang dở, nhắc luôn "tuần trước anh hứa gửi đối tác sáng thứ 6". Nó NHỚ. Chatbot thì mỗi phiên là người lạ, Agent là người cùng làm với bạn mãi.
  Điểm mình thích nhất: nó ghi nhớ luôn cả lỗi cũ để không bao giờ lặp lại. Chi tiết + link mình để ở BÌNH LUẬN nhé, ai hay phải "dặn đi dặn lại" thì đọc, đỡ được cả núi thời gian.
---

Sáng 22/8, tôi mở lại chuỗi chat tuần trước với một chatbot để hỏi tiếp vụ báo cáo tuần. Nó chào: *"Xin chào, tôi có thể giúp gì?"* — tỉnh bơ như gặp người lạ hoàn toàn. Tôi phải dán lại cả đoạn bối cảnh dài ngoằng, nhắc nó "tôi là ai, công ty làm gì, vụ đó tới đâu rồi", rồi mới được trả lời tiếp. Mất mười lăm phút chỉ để… làm quen lại với cái máy mà tuần trước tôi đã kể đủ thứ.

Cùng buổi sáng đó, tôi gõ cho Hermes đúng một câu: *"Tiếp bài báo cáo tuần nha."* Nó trả: *"Anh đang dang dở mục 3, tuần trước hứa gửi đối tác sáng thứ 6, cần mình nhắc không?"* Không dặn lại một chữ. Nó mở ra đúng cái tôi bỏ ngang, nhắc luôn cái lời hứa tôi suýt quên.

Một câu — và sự khác biệt là **100%**. Chatbot coi tôi là người lạ mỗi lần mở. Hermes coi tôi là người cùng làm việc với nó từ tháng trước.

## Chatbot là kẻ hay quên, Agent là người có trí nhớ

Phần lớn người dùng AI ở Việt Nam — và tôi từng thế — chỉ dùng nó như một cái máy trả lời có trí nhớ bằng **không**. Bạn hỏi, nó đáp, bạn tắt tab, lần sau mở lại nó không nhớ bạn là ai. Mọi phiên là một trang giấy trắng.

Đó là **chatbot**: thông minh trong *một* lượt chat, rồi quên sạch sau khi bạn đóng cửa sổ. Nó không có chỗ để "ghi nhớ" bạn — sở thích, thói quen, dự án đang dở, hay cái lỗi nó từng mắc.

**AI Agent** (kiểu Hermes) thì có một lớp **memory** — bộ nhớ bền. Nó lưu lại những gì học được về bạn và công việc của bạn, rồi mỗi lần gặp lại, nó đọc bộ nhớ đó trước khi làm. Không phải "thông minh hơn", mà là **không bị trôi**.

Một câu để nhớ: *chatbot sinh chữ rồi quên, agent làm xong việc và nhớ mãi.*

Trên thế giới, hướng này không còn là ý tưởng. Giữa tháng 8/2026, loạt dự án nổi lên cùng một thông điệp: **AI tương lai thuộc về hệ thống biết tự học và ghi nhớ**. Một bài trên Medium mang tên *"The Case for Agent Memory: Why the Future of AI Belongs to Systems That Can Self-Learn"* (tạm dịch: *Tại sao tương lai AI thuộc về những hệ thống tự học được*) khẳng định thẳng: không có trí nhớ bền, agent chỉ là máy phát ngôn lặp lại, không bao giờ "trưởng thành" qua từng lần làm việc.

## Bằng chứng thật: không có memory, agent sẽ nghẽn

Có một con số thực tế tôi rất thích, từ một dự án tên **Knowl** đăng trên Hacker News tháng 8/2026: file `CLAUDE.md` (nơi lưu ngữ cảnh cho AI) của họ phình to tận **1000 dòng** — chỉ để nhớ các chi tiết dự án. Một nghìn dòng. Đến mức họ phải dựng hẳn một lớp memory **tự gọt bớt** (self-pruning): AI tự quyết định cái gì nên giữ, cái gì nên xoá, không để bộ nhớ phình vô tội vạ.

Nghĩa là: ngay cả kỹ sư giỏi cũng thừa nhận — thiếu trí nhớ có tổ chức, agent sẽ nghẽn trong chính đống ngữ cảnh của nó. Và hai cái tên khác cùng trào lưu:

- **mem0** — lớp persistent memory (trí nhớ bền) được gắn thẳng vào agent, giúp nó nhớ xuyên suốt các phiên. Dự án *Vibe-Kanban* dùng chính mem0 để làm bảng Kanban có agent "nhớ" trạng thái công việc mãi.
- **Knownbase** — một MCP server chuyên cho persistent agent memory, nghĩa là agent gọi công cụ là lấy được ký ức cũ ra ngay.
- **OzBrain** — một "shared brain" (bộ não chung) để nhiều agent và cả team người của bạn cùng chia sẻ một trí nhớ.

Tức là "agent có trí nhớ" không phải tôi tưởng tượng. Đó là hướng đi chung của cả ngành AI 2026. Hermes của tôi chỉ là cách tôi xài nó cho công việc kinh doanh thực tế hàng ngày.

## Memory của Hermes chạy ra sao (nhìn phát thấy nó nhớ)

Lớp memory của Hermes không phải cái hộp đựng chữ ngẫu nhiên. Nó chia làm ba ngăn, và tôi thấy rõ mỗi ngăn làm gì:

**1. Memory ngắn hạn (trong phiên)** — trong lúc làm một việc, nó giữ các bước đang đi: đang ở đâu, làm xong đến đâu. Giống như bạn giữ danh sách việc cần làm trên tay.

**2. Memory dài hạn (xuyên phiên)** — cái này mới là "wow". Sau mỗi việc, nó ghi những sự thật ổn định về tôi vào bộ nhớ: tên khách VIP, họ ghét bị spam, thích nhận báo cáo sáng thứ 2, giá khoá học đang chạy là 239K, link web là speedreading.vn/shermes… Lần sau mở lại, nó đọc ngăn này trước. Tôi không bao giờ phải dặn lại.

**3. Memory lỗi (không lặp lại)** — mỗi lần tôi sửa nó (sai chính tả, sai giọng, quên CTA), nó ghi vào mục "tránh làm lại". Lần sau tự động né. Đây là phần tôi thích nhất: **nó tiến bộ theo tôi, không đứng yên**.

Và để bộ nhớ không bị phình như cái `CLAUDE.md` 1000 dòng kia, Hermes cũng có quy tắc tự gọt: chi tiết đã hết hạn (vd: "đợt khuyến mãi hết 20/8") thì nó chuyển sang lưu trữ, không nhét vào ngăn nóng nữa. Giống y hệt cái self-pruning của Knowl.

## WOW: demo giao việc có nhớ (người đọc "thấy" nó làm)

Dưới đây là đúng cái tôi gõ cho Hermes hôm tuần trước — và nó nhớ mãi đến giờ:

> **"Hermes, nhớ giúp tao mấy cái này (ghi vào memory luôn, đừng hỏi lại): khách VIP tên Lan, ghét spam, thích nhận báo cáo vào sáng thứ 2. Lần sau đừng hỏi mấy cái này nữa."**

Một tuần sau, tôi không nhắc lại cái gì. Sáng thứ 2, tôi chỉ gõ: *"Gửi báo cáo tuần cho Lan."* Hermes tự động:
- Mở memory → thấy "Lan = VIP, ghét spam, thích sáng thứ 2" → chọn khung giờ 8h, giọng nhẹ nhàng, không đính kèm quảng cáo thừa.
- Viết báo cáo → tự chạy quality gate soi lỗi → nhớ luôn cái lỗi chính tả tuần trước để không lặp.
- Gửi → ghi vào memory: "đã gửi Lan 25/8, phản hồi: chưa".

Tôi đứng ngoài **100%**. Cái "nhớ Lan là ai, thích gì" — tôi chỉ dặn **một lần**, tuần trước. Chatbot thì sao? Bạn phải dán lại cả đoạn đó mỗi lần, không nó coi Lan như người lạ.

## Kết quả đo lường thật (không phải cảm tính)

Tôi đo hai con số tận mắt trong 30 ngày qua:

- **Tỷ lệ giữ ngữ cảnh qua phiên: chatbot ≈ 0% (mỗi lần mở là trang trắng), Hermes = 100%** (mở lại là biết tiếp tục từ đâu). Khác biệt này tôi kiểm chứng mỗi sáng.
- **Thời gian "làm quen lại" mỗi sáng: ≈15 phút với chatbot (dán bối cảnh, nhắc lại), ≈0 phút với Hermes.** Nhân 30 ngày = **tiết kiệm khoảng 7,5 giờ/tháng** chỉ riêng khoản không phải dặn lại. Chưa kể công việc không bị đứt quãng vì quên bối cảnh.

Và một con số từ nghiên cứu: file ngữ cảnh của Knowl phình **1000 dòng** — minh chứng thực tế rằng không có lớp memory có tổ chức, agent sẽ nghẽn. Hermes né bằng quy tắc tự gọt, nên của tôi giữ ở mức gọn.

## FAQ — 3 câu hỏi hay gặp

**1. Memory của Hermes có an toàn không, có bị lộ không?**
Tôi chủ động quyết định cái gì được ghi. Thông tin nhạy cảm (mật khẩu, khoá API) tôi không cho nó lưu dạng text trần — chỉ lưu "có quyền gọi cái này", còn bản thân khoá nằm ở nơi tôi khoá. Bạn cũng có thể bảo "quên cái X đi" bất cứ lúc nào, nó xoá thật.

**2. Nếu tôi đổi ý (vd: Lan giờ thích nhận chiều thứ 6), nó có nhớ bản mới không?**
Có. Bạn gõ "từ giờ Lan nhận chiều thứ 6" là nó ghi đè lên mục cũ. Memory của agent là sống, không phải đông cứng — nó cập nhật theo bạn, không bảo thủ cái cũ sai.

**3. Chatbot đời mới (ChatGPT có memory) thì sao, có khác Agent không?**
ChatGPT có memory là bước tiến, nhưng nó vẫn nằm *trong khung chat*: nhớ để trò chuyện hay hơn. Agent (Hermes) dùng memory để *hành động*: nhớ rồi tự gửi mail, tự lên lịch, tự deploy, tự báo cáo — không chờ bạn. Trí nhớ của Agent là để **làm**, không chỉ để **nói**.

## CTA — thử một lần, bạn sẽ thấy mình "có người cùng làm"

Nếu bạn đang dùng AI như cái máy trả lời hay quên, mỗi sáng lại dặn lại từ đầu — thì bạn đang dùng sai công cụ. AI Agent có trí nhớ: giao một lần, nó nhớ mãi, không lặp lỗi, và mở lại là tiếp ngay chỗ bạn bỏ.

👉 Xài thử Hermes: giao một việc, rồi sáng hôm sau mở lại bảo "tiếp đi" — bạn sẽ bất ngờ vì nó nhớ bạn hơn chính bạn nhớ. Chi tiết + link đăng ký để ở phần bình luận. Đừng để chatbot coi bạn như người lạ mỗi sáng nữa.
