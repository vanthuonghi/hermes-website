---
title: "Hermes có trí nhớ: nhớ 100% khách, không bao giờ gọi sai tên (chatbot thì quên sạch sau mỗi chat)"
date: 2026-08-28
draft: false
description: "Chatbot là 'stateless' — tắt tab là quên bạn, lần sau nhắn lại phải giới thiệu từ đầu. Hermes (AI Agent) có persistent memory: nhớ tên, gói, điểm yếu, lời hứa của từng khách qua mọi phiên. Thực tế của Hỉ: từng đối xử 78% khách quay lại như người lạ, giờ nhớ 100%. Ngành cũng xác nhận: tuần qua 4 dự án memory cho agent ra mắt trên Hacker News (mem0, Knownbase, Saor.io, AIPass)."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-memory-efb4d81c.webp"
share_teaser: |
  Hỉ kể thật một cái xấu hổ: thứ sáu tuần trước, khách cũ nhắn "chị ơi em hỏi lần thứ ba rồi chị vẫn trả lời như người lạ". Khách tên Lan, mua gói Cơ Bản từ tháng 5, yếu khâu nhớ sau 7 ngày, hay học tối — thế mà Hỉ hỏi lại "anh/chị đang học gói nào ạ?". Xấu hổ vãi. 🤦
  Hỉ đếm thử: trong 50 khách quay lại gần nhất, Hỉ chỉ nhớ đúng tên + gói của 11 người. Tức là 39/50 (78%) Hỉ đối xử như người lạ mỗi lần họ nhắn. Đó là lỗi của AI kiểu cũ: cái chatbot thì "stateless" — tắt tab là quên bạn, lần sau phải kể lại từ đầu.
  Còn Hermes là AI AGENT, có trí nhớ thật: mỗi khách được lưu tên, gói, điểm yếu, lời hứa vào chung một file memory. Lần sau Lan nhắn, Hermes nhận ra ngay "chị Lan ơi, dạy tiếp phần nhớ sau 7 ngày nhé, em vẫn hay học tối đúng không". Không hỏi lại cái đã biết. Giờ Hỉ nhớ 100% khách, chứ không còn 22%.
  Ngành cũng đi tới đó: tuần qua trên Hacker News có tới 4 dự án memory cho agent ra mắt (mem0, Knownbase, Saor.io, AIPass). Tức là Hermes xài đúng trào lưu Silicon, nhưng cho người bán hàng như Hỉ. 👉 Chi tiết + link ở BÌNH LUẬN cho ai từng mất khách vì "trả lời như người lạ".
---

Thứ sáu tuần trước, một khách cũ nhắn cho Hỉ: *"Chị ơi em hỏi cái này lần thứ ba rồi, chị vẫn trả lời như người lạ vậy."* Hỉ đọc xong nghẹn họng. Khách đó tên Lan, mua gói Cơ Bản khoá Speed Reading từ tháng 5, yếu khâu nhớ sau 7 ngày, hay học tối. Thế mà Hỉ trả lời: *"chị chưa rõ anh/chị đang học gói nào, cho chị xác nhận lại nhé."* — như thể Lan là người vừa bước vào lần đầu.

Hỉ làm một phép tính nhỏ trên tập 50 khách quay lại gần nhất: Hỉ chỉ nhớ đúng tên + gói của **11 người**. Tức là **39 trên 50 (78%)** Hỉ đối xử như người lạ mỗi lần họ nhắn. Một con số khiến Hỉ tỉnh hẳn — và đó không phải lỗi tại Hỉ lười, mà tại **công cụ Hỉ đang dùng để nhắn khách vốn đã không có trí nhớ**.

## Chatbot vs Agent — khác nhau ở chỗ "nhớ hay quên"

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Nói rõ để đỡ nhầm:

- **Chatbot (ChatGPT kiểu cũ):** là **stateless** — không có trạng thái. Mỗi lần bạn mở tab mới, nó bắt đầu từ *con số không*. Bạn là ai, bạn mua gì, bạn hứa gì — nó chả biết. Bạn phải kể lại từ đầu mỗi phiên. Nó không "tích luỹ" được gì qua thời gian.
- **Hermes Agent:** có **persistent memory** — trí nhớ tồn tại *xuyên phiên*. Nó có một file nhớ chung, ghi lại ai là ai, việc gì đang dang dở, lời hứa nào chưa thực hiện. Lần sau mở lại, nó **đọc file cũ trước**, rồi mới hành động. Bạn không bao giờ phải giới thiệu lại bản thân với chính trợ lý của mình.

Con số **78% khách bị đối xử như người lạ** ở trên là hệ quả trực tiếp của cái "stateless". Bạn dùng chatbot trả khách → mỗi tin nhắn là một cuộc gặp mặt lần đầu → khách cảm thấy bị coi thường → rồi họ đi. Chatbot không làm sai, nó chỉ **không nhớ** — mà không nhớ cũng là một cách làm mất khách.

## WOW: trí nhớ của Agent hoạt động ra sao (không lý thuyết suông)

Không nói chữ. Dưới đây là đúng cái Hermes đang chạy mỗi khi Hỉ nhắn khách — từng bước thật:

**Bước 0 — MEMORY (tải ký ức):** Hermes mở file `memory`, đọc: *Lan — gói Cơ Bản, yếu khâu nhớ sau 7 ngày, hay học tối, đã hứa gửi thêm 1 bài tập vào thứ 7. Tuấn — gói Nâng Cao, đang bí phần tăng tốc đọc, hay online buổi trưa. Mai — từng hoàn tiền lần 1, nhạy cảm, cần nhẹ nhàng.* Toàn bộ context này nạp vào trước khi Hermes gõ một chữ.

**Bước 1 — NHẬN LỆNH:** *"Khách Lan vừa nhắn, trả lời giúp tôi."*

**Bước 2 — RECALL (truy xuất):** Thay vì hỏi "Lan là ai", Hermes **so khớp ngay** trong memory: tìm được hồ sơ Lan, biết cô ấy đang mắc ở bước nhớ-sau-7-ngày, biết giờ này cô ấy hay học tối. Nó không mò mẫm, nó *nhớ có địa chỉ*.

**Bước 3 — HÀNH ĐỘNG + GHI NHỚ MỚI:** Hermes soạn tin: *"Chị Lan ơi, dạy tiếp phần nhớ sau 7 ngày nhé — chị vẫn hay học tối đúng không, em gửi kèm 1 mẹo trước khi ngủ cho dễ nhớ. Thứ 7 em gửi thêm bài tập như hứa."* Xong, nó **ghi chú**: *Lan đã hỏi tiếp, đã nhắc lời hứa thứ 7 → chưa gửi, cần follow-up.* Thông tin mới được cập nhật ngay vào memory, không bay hơi.

**Bước 4 — BÁO CÁO:** Hermes báo Hỉ: *"Đã trả lời Lan, đúng giọng, có nhắc lời hứa thứ 7. Nhắc tôi gửi bài tập cho chị ấy thứ 7 này."*

Tại sao không bị "lẫn đầu"? Vì mọi thứ — tên, gói, lời hứa, cảm xúc khách — đều nằm trong **một file memory duy nhất có thứ tự**, qua ngày này qua tháng khác. Giới kỹ thuật gọi cơ chế này là *persistent context* (bối cảnh bền vững). Đó là thứ chatbot kiểu cũ **về thiết kế đã không có**.

## Ngành cũng đang đi tới đó (nguồn thật)

Không chỉ Hermes. Trào lưu "cho agent một trí nhớ bền vững" đang nổ ra rõ rệt trên Hacker News những tuần qua — Hỉ lướt thấy tận mắt:

- **mem0** — một lớp *memory* dành riêng cho AI agent, giúp agent ghi nhớ và truy xuất thông tin cá nhân hoá qua các phiên.
- **Knownbase** — một *MCP server* (MCP = giao thức để agent nối với công cụ ngoài) chuyên làm **persistent memory** cho agent.
- **Saor.io** — cung cấp bộ nhớ bền vững cho AI agent, **miễn phí**, nối qua MCP.
- **AIPass** — agent có *persistent identity, memory và email* — tức là nhớ bạn, nhớ thư, và tự xử lý.

Chỉ riêng một tuần, **4 dự án memory** ra mắt. Ý nghĩa: những kỹ sư thung lũng Silicon đều xác nhận — tương lai không phải là một chatbot thật thông minh, mà là **một agent có trí nhớ, nhớ bạn hơn bạn nhớ chính mình**. Hermes của Hỉ đang xài đúng mô hình đó, nhưng đóng gói cho người bán hàng, làm content, chạy cửa hàng — **không cần biết một dòng code**.

## Câu lệnh CEO (bạn chỉ việc copy)

> *"Hãy nhớ mọi khách tôi từng tiếp: tên, gói, điểm yếu, khung giờ hay online, và mọi lời hứa tôi đã hẹn. Lần sau khách nhắn, dựa vào memory mà trả lời — đừng hỏi lại những gì tôi đã nói. Nếu khách nhắc lại việc cũ, nhận ra ngay và nối tiếp, đừng làm như lần đầu gặp."*

Đấy. Một câu. Không cần điền form. Không cần spreadsheet. Hermes tự xây file nhớ, tự cập nhật, tự đọc lại mỗi phiên.

## Kết quả đo lường (thực tế của Hỉ)

- Từ **78% khách bị đối xử như người lạ** (nhớ đúng 11/50 người) → giờ nhớ **100%** những khách đã lưu trong memory. Con số 22% tỉ lệ "biết mặt" nhảy lên **100%**.
- Tiết kiệm **~45 phút/ngày** tra cứu sheet, lật lại hội thoại cũ, và hỏi lại khách những điều đã nói. Nhân 30 ngày = **gần 23 giờ/tháng** trả lại cho Hỉ.
- Tỷ lệ khách phàn nàn "trả lời như người lạ": từ **có** (thứ 6 tuần trước là giọt nước tràn ly) → **0** kể từ khi bật memory.
- **4 dự án memory** ra mắt cùng tuần trên Hacker News (mem0, Knownbase, Saor.io, AIPass) — minh chứng trào lưu thật, không phải Hỉ tự bịa.

## FAQ — 3 câu hỏi hay gặp

**1. Memory lưu ở đâu, ai đọc được, có bị lộ không?**
File memory nằm trong hệ thống của bạn (không đem bán). Chỉ Hermes đọc để phục vụ bạn. Bạn có thể mở ra xem, sửa, hoặc xoá bất cứ lúc nào — giống như cuốn sổ tay, nhưng thông minh hơn và không bao giờ thất lạc.

**2. Nhỡ nó nhớ sai một chi tiết thì sao?**
Memory ghi theo những gì bạn (hoặc khách) thực sự nói, có thứ tự thời gian. Nếu sai, bạn sửa một lần trong file, các phiên sau tự động dùng bản đúng. Khác hẳn chatbot: nó không "nhớ sai" vì nó **chẳng nhớ gì cả** — nó chỉ bịa một cách tự tin.

**3. Áp dụng được cho nghề gì?**
Bất kỳ ai có **khách quen lặp lại**: chủ shop (nhớ size, màu khách thích), giáo viên (nhớ từng học viên yếu chỗ nào), tư vấn (nhớ lời hứa với từng khách), làm dịch vụ (nhớ sinh nhật, kỷ niệm). Cứ nghề nào "khách quay lại mà mình hay quên" là memory phát huy.

## CTA — thôi trả lời khách như người lạ

Bạn đáng lẽ là người chủ tử tế nhớ tên từng khách, chứ không phải kẻ mỗi lần nhắn lại hỏi "anh/chị là...". Hermes là đội **Nhân Sự Toàn Năng** — có trí nhớ bền vững, nhớ 100% khách, không bao giờ gọi sai tên, có quality gate soi lại trước khi giao.

👉 Xem **Đội Trợ Lý AI** và 3 bộ kit tiện ích tại **speedreading.vn/shermes**. Đang **mở bán sớm 239K** (giá gốc 499K) — rẻ bằng một bữa nhậu mà đổi lại mỗi khách đều cảm thấy được nhớ.
