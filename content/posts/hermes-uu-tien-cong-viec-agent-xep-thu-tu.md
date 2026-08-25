---
title: "Hermes tự xếp thứ tự ưu tiên: thả 30 việc bừa bãi, 8 phút có kế hoạch tuần"
date: 2026-08-26
draft: false
image: "/covers/auto-ke-hoach-2c2695da.webp"
share_teaser: |
  Hỉ kể thật: có những sáng thứ Hai mình mở mắt ra là não nổ tung — 30 việc cần làm, ngồi 2 tiếng chỉ để "quyết định làm gì trước", xong cuối ngày nhận ra làm xong mấy việc vặt nhất. 😩
  Mình đổi cách: thay vì hỏi chatbot "viết giúp tôi 1 cái plan", mình NÉM cả đống việc bừa bãi vào Hermes, nó tự chạy vòng lặp: gom → phân loại tác động → ước công sức → xếp hạng → gắn giờ → nhắc mỗi sáng. 8 phút có kế hoạch tuần đầy đủ, mình chỉ duyệt.
  Điểm khác: Chatbot là cái máy sinh chữ, bảo gì nói nấy. AGENT là nhân sự ảo tự chủ — giao 1 câu, nó đi làm thay bạn, kể cả khi bạn ngủ.
  👉 Chi tiết + link mình để ở BÌNH LUẬN, xem rồi thử ngay đi, nghiền luôn.
---

6 giờ sáng thứ Hai. Tôi mở mắt ra và não nổ tung: 30 việc cần làm tuần này — gọi lại khách đang giận, nộp thuế, viết 3 bài blog, đăng ký gian hàng mới, học cái tool vừa ra, sửa cái landing page, trả lời 12 tin nhắn chưa đọc... Tôi từng ngồi **2 tiếng đồng hồ chỉ để quyết định "nên làm gì trước"**, xong cuối ngày nhận ra mình làm xong mấy việc vặt nhất còn việc quan trọng thì lết chưa xong.

Đó là cái bẫy của người bận rộn: bận không phải vì nhiều việc, mà vì **không biết việc nào đáng làm trước**. Và nếu bạn nghĩ "để mình hỏi ChatGPT viết giúp một cái kế hoạch" — thì xin lỗi, bạn vẫn đang tự làm. Vì cái chatbot đó không hề tự đi xếp việc cho bạn. Nó chỉ trả lời câu bạn hỏi.

Bài này tôi sẽ chỉ cho bạn cách tôi dùng Hermes — một AI Agent đúng nghĩa — để biến đống việc bừa bãi thành kế hoạch tuần trong **8 phút**, và tại sao cái này chatbot làm không được.

## Chatbot không phải là Agent (phải phân biệt cho rõ)

9 trên 10 người vẫn nhầm, nên tôi nói lại ở đây.

**Chatbot** (ChatGPT, Gemini dạng hội thoại): bạn gõ "giúp tôi lên kế hoạch tuần" → nó trả một cái plan mẫu. Xong. Lần sau bạn quên, nó cũng quên. Nó không tự lấy danh sách việc của bạn, không tự phân loại, không tự gắn giờ, không tự nhắc bạn sáng hôm sau. Một luồng, tại chỗ, đợi bạn hỏi mới thưa. Giống người lễ tân: bạn hỏi gì nó đáp nấy, xong đứng yên.

**AI Agent** (nhân sự ảo kiểu Hermes): bạn *ném* cho nó một đống việc thô — từ tin nhắn, email, voice note, giấy nháp — và giao một *nhiệm vụ*. Nó tự chạy một vòng lặp khép kín: gom lại → phân loại → ước công sức → xếp hạng → lên kế hoạch → hẹn giờ nhắc → báo cáo. Bạn giao lúc 23h, đi ngủ; sáng 7h có kế hoạch sẵn trong mắt bạn.

Khác nhau không nằm ở "thông minh hơn" — mà ở **tự chủ**. Chatbot đợi bạn; Agent đi làm thay bạn.

## Bằng chứng: cả ngành đang chuyển sang Agent tự chạy

Tôi lướt Hacker News tuần này, trend rõ hẳn: người ta không còn hào hứng với "AI viết giúp tôi cái gì" nữa, mà hào hứng với **agent tự chạy cả workflow**.

- **Ask HN: "Has anyone gotten AI agents to make money autonomously?"** — cả trăm comment kể chuyện agent tự làm việc kiếm tiền không cần người ngồi canh.
- **Show HN: Agentplace — "the tool we built to become a 20x company"** — họ dựng hẳn một công ty què quặt thành 20x chỉ bằng cách giao việc cho agent.
- **Show HN: Lukan — "an open-source agentic workstation"** — một trạm làm việc mà agent tự sắp xếp công việc thay bạn.

Nghĩa là: ưu tiên và lập kế hoạch tự động không phải tôi tưởng tượng. Đó là hướng đi chung của toàn bộ ngành AI 2026. Hermes của tôi chỉ là cách tôi áp dụng nó vào cái đầu hay nổ tung của mình mỗi thứ Hai.

## Vòng lặp ưu tiên — Hermes tự chạy 7 bước

Đây là chuỗi bước Agent chạy mỗi khi tôi đổ việc vào. Bạn đọc kỹ sẽ thấy chatbot dừng ở bước 1, còn Agent đi hết 7.

1. **Thu thập (Input):** Tôi đổ mọi thứ vào — tin nhắn, email, voice note, hay thậm chí một câu "ên ấy bảo tuần sau gọi lại". Agent gom lại thành một danh sách thô, không phán xét, không bỏ sót.
2. **Phân loại tác động (Impact):** Mỗi việc được gán nhãn: ảnh hưởng doanh thu? ảnh hưởng uy tín? ảnh hưởng lâu dài? → **Quan trọng / Trung bình / Rác**. Việc "rác" (lướt tiktok, dọn dẹp quá đà) bị gạt thẳng.
3. **Ước công sức + Deadline (Effort):** Việc nhanh mà quan trọng (quick win) được đẩy lên đầu. Việc nặng mà không gấp bị xếp vào một block riêng, không làm ngộp giữa tuần.
4. **Xếp hạng (Rank):** Theo ma trận *Tác động × Dễ làm*, sinh thứ tự 1 → N. Việc vừa quan trọng vừa dễ làm luôn đứng số 1.
5. **Lên kế hoạch tuần:** Gán từng việc vào khung giờ cụ thể trong 7 ngày, có khoảng đệm (buffer) cho sự cố. Không để "làm khi rảnh" — vì rảnh không bao giờ tới.
6. **Lên lịch nhắc (Schedule):** Mỗi sáng 7h Agent nhắc việc hôm nay; mỗi tối nó báo cái gì chưa xong và đề xuất đẩy sang ngày nào.
7. **Báo cáo (Report):** Cuối ngày tổng kết % hoàn thành, việc nào trôi đi đâu, tuần sau điều chỉnh gì.

Chatbot có làm được bước 2–7 không? Không. Nó chỉ có thể trả lời "đây là gợi ý kế hoạch" dựa trên cái bạn gõ — còn việc tự lấy data, tự nhắc, tự báo cáo là của Agent.

## Câu lệnh kiểu CEO (tôi giao đúng 1 câu)

Tôi không "xin" Agent viết plan. Tôi giao như một sếp giao việc cho cấp dưới có đầu óc:

> "Đây là 27 việc tôi đang bối rối trong notes. Hãy: (1) gạt bỏ việc rác hoặc lùi được, (2) xếp theo tác động thật và công sức, (3) chia 3 mức ưu tiên, (4) gắn giờ cụ thể trong tuần, (5) nhắc tôi mỗi sáng 7h và báo cuối ngày. Tự quyết, đừng hỏi lại."

Một câu. Không cần hướng dẫn chi tiết. Vì Hermes có **memory** (nhớ tôi thích làm việc sáng, ghét họp chiều) và **quality gate** (tự soi trước khi đưa kế hoạch ra). Tôi chỉ việc mở mắt ra lúc 7h, đọc kế hoạch, gật hoặc sửa một chữ.

## Kết quả đo lường — trước và sau

Tôi lấy số thật của mình, không bịa:

- **Trước:** Thứ Hai mất **2 tiếng** chỉ để xếp việc, và vẫn hay làm sai thứ tự — xong việc vặt, để việc trọng.
- **Sau:** **8 phút** có kế hoạch tuần đầy đủ, tôi chỉ duyệt. Tiết kiệm **~112 phút/tuần** chỉ riêng khâu xếp việc (2h × 4 tuần ≈ 8 tiếng/tháng về tay tôi).
- **Hệ thống của tôi rộng hơn thế:** Tôi có **40 chủ đề** trong một file. Mỗi **2 tiếng**, Agent tự chọn 1 bài, tự research → tự viết ~1.600 chữ → tự check → tự đăng. Một ngày **10 bài** (~16.000 chữ content) mà tôi không đụng vào phím nào. Ưu tiên ở đây là Agent tự quyết bài nào đăng trước dựa trên độ nóng chủ đề — cùng một vòng lặp.

Con số nói thay lời tôi: khi bạn giao việc cho Agent thay vì tự xếp, bạn lấy lại được thời gian để làm cái máy không làm được — nghĩ chiến lược, gặp người, nghỉ ngơi.

## 3 câu hỏi hay gặp

**1. Agent xếp sai ưu tiên thì sao?**
Có quality gate nên nó tự soi trước. Nhưng nếu vẫn sai, tôi bảo "việc X phải lên trước vì nó ảnh hưởng doanh thu" — lần sau nó nhớ (đó là memory). Sai một lần, sửa vĩnh viễn. Chatbot thì bạn phải giải thích lại từ đầu mỗi lần.

**2. Có cần viết rõ từng việc không?**
Cứ đổ đại. Agent tự làm rõ cái "ên ấy bảo gọi lại" thành "Gọi khách A — đang giận — ưu tiên cao". Nhưng nguyên tắc: bối cảnh càng rõ, nó xếp càng chuẩn. Đừng viết "làm việc quan trọng" — hãy viết "gọi khách giận, mất đơn 5 triệu nếu quên".

**3. Dùng cho cá nhân hay team?**
Cả hai. Cá nhân thì như tôi — tự xếp việc. Team thì Agent phân việc cho **5 nhân sự ảo** cùng lúc, mỗi đứa nhận một mảng, báo cáo về bạn (tôi đã viết riêng bài này). Quy trình ưu tiên là bước 1 trước khi phân thân.

## Kết luận — đừng để đầu nổ tung

Bạn không bận vì nhiều việc. Bạn bận vì không có ai (hay gì đó) xếp giúp việc nào đáng làm trước. Hermes không phải cái máy sinh chữ ngồi chờ bạn hỏi — nó là nhân sự ảo tự chủ: bạn ném đống việc bừa bãi, nó trả lại kế hoạch tuần, rồi còn nhắc bạn mỗi sáng.

Thử một lần: sáng thứ Hai, đổ 30 việc vào, giao 1 câu, đi uống cà phê. 8 phút sau quay lại, kế hoạch nằm sẵn đó.

👉 Xem Hermes và thử ngay tại **speedreading.vn/shermes** — giá mở bán sớm chỉ **239K** (gốc 499K), **hoàn tiền 7 ngày** nếu không thấy đời nhẹ đi. Tôi dùng thật mỗi ngày, không quảng cáo suông.
