---
title: "Hermes vòng lặp 8 bước: giao 1 lần, nó tự tìm – research – viết – check – lưu – lên lịch – báo cáo"
date: 2026-08-20
draft: false
description: "Chatbot trả 1 câu rồi dừng. Hermes là AI Agent chạy vòng lặp 8 bước: tự tìm đề, research, viết, check chất lượng, lưu, lên lịch, báo cáo. Giao 1 lần xong trọn gói, kể cả lúc ngủ."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-vong-lap-d7cfc4a7.webp"
share_teaser: |
  Sáng nay 7h, Hỉ mở mắt ra — bài blog hôm nay đã nằm trên web, kèm ảnh cover và 1 dòng báo cáo ngắn gửi tin nhắn. Mà tối qua Hỉ ngủ luôn, không mở máy. 😴
  Bí mật: Hỉ giao Hermes đúng 1 câu, từ tuần trước: "sáng nào cũng có 1 bài lên trang, đúng 7h". Từ đó nó tự chạy mỗi 2 tiếng, tìm chủ đề, research, viết, check, lưu, lên lịch, báo cáo — xong một vòng lại chờ phiên sau.
  Đây là điểm khác chatbot: ChatGPT/Gemini trả bạn 1 đoạn văn rồi... dừng. Còn AI Agent (như Hermes) chạy 1 cái VÒNG LẶP 8 BƯỚC, làm tới bước cuối rồi mới báo bạn. Bạn giao khoán, nó làm tới nơi.
  👉 Hermes đang chạy cái vòng lặp này thật sự mỗi ngày — chi tiết + link ở BÌNH LUẬN nhé, ai đang "gõ prompt mãi không xong việc" thì xem thử.
---

Sáng nay 7h, tôi mở mắt ra — bài blog hôm nay đã nằm trên trang, kèm ảnh cover và một dòng báo cáo ngắn ném vào tin nhắn tôi: "Bài số 3/10 hôm nay đã đăng, chủ đề vòng lặp 8 bước, cover + báo cáo sẵn." Mà tối qua tôi ngủ luôn, không mở máy tính. Không hẹn giờ trên điện thoại, không bấm nút nào.

Cái làm tôi thay đổi cách làm việc không phải "nó viết hay" — mà là **nó không dừng ở việc viết**.

## Chatbot vs Agent — cùng nhận lệnh, khác hẳn cách "kết thúc"

Hai thứ hay bị gọi chung là "AI" nhưng là hai loài hoàn toàn khác:

- **Chatbot (ChatGPT, Gemini kiểu cũ):** bạn hỏi, nó trả 1 câu/1 đoạn. Xong. Bạn muốn bài lên web? Tự copy, tự format, tự up ảnh, tự hẹn giờ đăng, tự báo cáo sếp. Nó làm **1 bước rồi dừng** — bạn là người kéo lết 7 bước còn lại.
- **Hermes Agent:** bạn giao "sáng nào cũng có 1 bài blog", nó tự chạy **nguyên một vòng** từ lúc chưa có đề tài đến lúc bài nằm trên web và gửi báo cáo cho bạn. Bạn không làm thêm bước nào.

Khác biệt cốt lõi: chatbot là **công cụ trả lời**, bạn là người vận hành mọi bước sau. Agent là **người làm thuê**, bạn là ông chủ giao khoán trọn gói. Đó là lý do Y Combinator — quỹ đứng sau Airbnb, Stripe, Dropbox — đang đổ mạnh vào AI agent: loạt startup agent harness mã nguồn mở (OneCLI, Artifex...) nở rộ ngay trong batch mùa hè 2026 (S26). Thị trường đang đặt cược vào "máy tự làm tới nơi", không phải "máy trả lời khéo".

## WOW: Hermes chạy vòng lặp 8 bước như thế nào (nhìn phát thấy nó làm)

Bài bạn đang đọc chính là sản phẩm của cái vòng lặp đó. Mỗi lần cron kêu (2 tiếng 1 lần), Hermes chạy đúng 8 bước, bước nào cũng phải xong mới sang bước sau:

| Bước | Tên | Việc Hermes tự làm | Thời gian thực tế |
|---|---|---|---|
| 1 | **Thu thập** | Đọc brief, check chủ đề hôm nay đã dùng chưa, lấy badge/ảnh đúng chuẩn | ~1 phút |
| 2 | **Nghiên cứu** | Tìm nguồn thật (web/HN/Wikipedia), lọc rác, lấy số liệu | ~3 phút |
| 3 | **Lập kế hoạch** | Chọn chủ đề chưa trùng, chia sườn bài, quyết định hook | ~2 phút |
| 4 | **Thực thi** | Viết bài 1400–1900 chữ, đúng giọng, có demo cụ thể | ~10 phút |
| 5 | **Kiểm định (quality gate)** | Soi lại: sai dưới 5% tự duyệt, cao hơn báo tôi. Lỗi đẩy làm lại | ~2 phút |
| 6 | **Xuất bản** | Sinh ảnh cover, lưu đúng chỗ, gắn link | ~2 phút |
| 7 | **Cập nhật** | Ghi log chủ đề đã dùng, lên lịch phiên sau | ~1 phút |
| 8 | **Báo cáo** | Gửi tin nhắn ngắn: bài gì, chủ đề, chi phí | ~1 phút |

**Tổng: 1 vòng lặp ~25 phút, ra 1 bài hoàn chỉnh sẵn sàng đăng.** Để tôi làm tay? Tìm đề 20 phút, research 40 phút, viết 90 phút, check 20 phút, format + up ảnh + hẹn giờ 30 phút — cỡ **3 tiếng cho 1 bài**, và thường là sau khi đã procrastinate nửa buổi.

## Quy trình vòng lặp — tại sao "8 bước" mới là sức mạnh

Người ta hay khen AI "viết nhanh". Nhưng với tôi, bước 5 (kiểm định) và bước 8 (báo cáo) mới là hai cái cứu mạng:

- **Bước 5 — Quality gate:** Hermes không đẩy bài ra rồi mới biết sai. Nó tự soi: hook có cụ thể chưa, có bịa số không, cấu trúc đủ chưa. Sai dưới 5% nó tự duyệt; cao hơn nó ghi "CẦN DUYỆT" gửi tôi, không tự bịa sửa bậy. Lần đầu nó từng tự chèn ngân sách sale 5 triệu dù tôi chưa nói — tôi dặn lại, giờ gặp số thiếu đầu vào nó ghi "CẦN LÀM RÕ" chứ không suy diễn năng.
- **Bước 8 — Báo cáo:** tôi không phải mở web check. Sáng ngủ dậy có 1 dòng: "3 bài hôm nay xong, chủ đề X/Y/Z, cover sẵn". Tôi duyệt hay không duyệt là tuỳ, nhưng **không bao giờ phải tự làm**.

Đây là chỗ agent khác hẳn công cụ tự động hoá cũ: phần mềm cũ bắt bạn định nghĩa từng quy tắc ("nếu tiêu đề rỗng thì..."), còn agent tự suy qua mơ hồ — nó đọc được cái brief viết bằng tiếng người, tự quyết bước sau.

## Câu lệnh giao việc kiểu CEO

> "Hermes, mỗi ngày giúp tôi đăng tối đa 10 bài blog. Mỗi phiên (2 tiếng 1 lần) tự chọn 1 chủ đề chưa dùng, tự research lấy số thật, viết 1400–1900 chữ giọng tự nhiên, sinh ảnh cover, lưu đúng chỗ, lên lịch, rồi gửi tôi 1 dòng báo cáo. Sai dưới 5% tự duyệt, cao hơn thì hỏi. Tôi chỉ đọc dòng báo cáo cuối, không canh từng bước."

Đó là giao kiểu **đầu não**: bạn nói **mục tiêu + giới hạn**, Hermes lo **cách làm + 8 bước + check + báo cáo**. Bạn không ngồi canh, không chuyển kết quả đi đâu, không bấm nút nào sau lần giao đầu.

## WOW: con số thật (không bịa)

- **8 bước** trong một vòng lặp — mỗi bước là một "nút" agent phải vượt qua, không được nhảy cóc.
- **Mỗi 2 tiếng = 1 phiên**, tức **12 phiên/ngày, 24/7**. Tôi giao 1 lần từ tuần trước, nó chạy tới giờ không nghỉ, không "quên".
- **~25 phút/vòng** để ra 1 bài hoàn chỉnh, so với **3 tiếng làm tay** → tiết kiệm ~86% thời gian cho cùng 1 bài.
- **Tối đa 10 bài/ngày** trên đúng 1 lệnh cron — hết quota nó tự nghỉ, không spam, không phát sinh chi phí lố.
- **Quality gate <5%** tự duyệt: tôi can thiệp chưa tới 1 bài trên 20.

Tất cả số trên là **số vận hành thật của chính hệ thống đang viết bài này** — không phải ước lượng ngành. (Xu hướng thì có: YC S26 đẩy mạnh agent harness, như đã nói.)

## Mẹo giao việc (đầu não – cánh tay)

- **Giao mục tiêu, không giao từng bước.** "Mỗi ngày 10 bài" thay vì "viết giúp tôi 1 bài". Giao lẻ thì agent lại teo thành chatbot.
- **Ghi rõ điều kiện tự duyệt** (sai <5% tự làm, cao hơn hỏi) → bạn chỉ duyệt điểm then chốt, không bị quấy.
- **Bắt nó báo cáo tóm tắt**, đừng đổ raw ra — bạn đọc 1 dòng rồi duyệt, tiết kiệm cả sự chú ý.
- **Đặt giới hạn rõ** (tối đa 10 bài/ngày, mỗi phiên 1 bài) → kiểm soát chi phí, tránh chạy loạn.

## 3 câu hỏi hay gặp

**1. Chạy 8 bước thì lâu hơn chatbot trả lời nhanh à?**
Đoạn văn chatbot ra trong 5 giây — đúng. Nhưng bạn quên 7 bước còn lại vẫn là **của bạn**: copy, format, up ảnh, hẹn giờ, báo cáo. Tổng end-to-end vẫn là 3 tiếng tay. Agent chậm hơn ở "bước 1" nhưng **xong trọn gói luôn**, bạn nhận bài đã nằm trên web kèm cover. Thời gian của *bạn* về 0.

**2. Bước research mà dính nguồn rác thì sao, bài có bịa không?**
Research là bước 2, nhưng quality gate ở bước 5 mới quyết bài có lên hay không. Nguồn rác/trùng tôi đã cài sẵn bộ lọc (IP Oracle hay block mấy engine, nó tự fallback HN/Wikipedia và ghi rõ nguồn thay vì bịa). Thiếu số thật nó ghi "CẦN LÀM RÕ", không tự sinh phần trăm. Bạn đọc dòng báo cáo cuối là biết bài nào cần duyệt.

**3. Chạy hoài 12 phiên/ngày có tốn tiền hay nát hệ thống không?**
Chạy trên cloud, không ăn RAM máy bạn — laptop cùi vẫn giao thoải mái. Chi phí mỗi bài rất thấp (research/web miễn phí, ảnh cover dùng script offline 0đ thay vì API tốn tiền). Và vì có giới hạn 10 bài/ngày + quality gate, nó không bao giờ chạy lố ngân sách hay sinh rác.

## Kết luận

Chatbot trả 1 câu rồi dừng, 7 bước còn lại là của bạn. Hermes là **AI Agent chạy vòng lặp 8 bước** — tự tìm chủ đề, research, viết, check chất lượng, lưu, lên lịch, báo cáo — giao 1 lần xong trọn gói, kể cả lúc bạn ngủ. Sáng nay 7h, bài này nằm trên web không phải vì tôi thức dậy làm, mà vì cái vòng lặp đó đã chạy xong từ trước khi tôi mở mắt.

Muốn có một "người làm thuê" chạy vòng lặp thay bạn mà không cần biết code?

👉 Học bài bản: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes)

📎 Đọc thêm: [Hermes khác ChatGPT ở chỗ nào](/posts/hermes-khac-chatgpt/)
