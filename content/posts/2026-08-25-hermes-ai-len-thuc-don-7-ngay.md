---
title: "Chatbot chờ bạn nghĩ món — Hermes tự lên thực đơn 7 ngày, giảm 2kg/tháng, 0 phút lo"
date: 2026-08-25
draft: false
description: "Chatbot là thợ: bạn phải nghĩ ra thực đơn rồi mới bảo nó gõ. Hermes là AI Agent — bạn nói mục tiêu (giảm 2kg/tháng, thích cá, ngân sách 120k/ngày), nó tự tra CSDL dinh dưỡng, tính calo, ghép 7 ngày món ăn, tự check chất lượng rồi báo số. Thực tế của tôi: mỗi Chủ Nhật mất 3 tiếng lên thực đơn mà vẫn tăng 2kg, giờ chỉ 15 phút, giảm 2,3kg sau 1 tháng. Căn cứ khoa học: DRI (Viện Hàn lâm Y khoa Mỹ) khuyến nghị 0,8g protein/kg/ngày; thâm hụt 500 kcal/ngày giảm ~0,5kg/tuần. Năm 2026, loạt startup AI agent (Screenpipe, Coasty, Speko — YC batch S26) đổ bộ Hacker News chứng minh trào lưu 'máy tự lập kế hoạch thay bạn' là thật."
image: "https://vanthuonghi.github.io/hermes-website/covers/ai-thuc-don-20260825.webp"
share_teaser: |
  Mỗi Chủ Nhật Hỉ ngồi 3 tiếng trước tủ lạnh lên thực đơn, mà tháng nào cũng tăng 2kg, tuần nào cũng order đồ ăn 3 lần vì "chả biết ăn gì". 🍜
  Tuần này Hỉ giao Hermes đúng một câu: "lên thực đơn 7 ngày, giảm 2kg/tháng, thích cá ghét cải, 120k/ngày" — không cần Hỉ nghĩ món. Sáng thứ 2 mở máy: bảng 21 bữa sẵn, kèm danh sách đi chợ. Hết 1 tháng: nhẹ 2,3kg.
  Chatbot làm được không? Không. Chatbot là thợ: bạn phải bảo "thứ 2 ăn gì, thứ 3 ăn gì" — nó mới gõ. Còn Hermes (AI Agent) là người "lên kế hoạch hộ" — bạn nói MỤC TIÊU, nó tự tính calo, tự ghép món, tự soi chất lượng.
  👉 Hermes đang làm cái này mượt — chi tiết + link ở BÌNH LUẬN nhé, ai đang giảm cân mà lười nghĩ món thử xem.
---

Tôi từng coi "lên thực đơn" là chuyện nhỏ. Đến khi đếm được: mỗi Chủ Nhật tôi ngồi **3 tiếng đồng hồ** trước tủ lạnh, lật điện thoại xem món, ghi chép rồi xoá, rồi ghi lại — chỉ để chốt 7 ngày ăn gì. Ba tiếng mỗi tuần, cộng lại gần **13 tiếng một tháng**, chỉ để làm cái việc mà cuối cùng tôi vẫn không theo được. Tệ hơn: hai tháng liền tôi **tăng 2kg**, và tuần nào cũng bấm Grab 3 lần vì về nhà "chả biết ăn gì" nên thà order. Nghĩa là tôi vừa tốn thời gian lên kế hoạch, vừa vứt kế hoạch đi, vừa tốn tiền order, vừa béo lên. Một vòng lặp vô dụng.

Cái ngày tôi giao Hermes lo chuyện này, vòng lặp đó chết hẳn.

## Chatbot vs Agent — một chữ "lên kế hoạch" làm nên khác biệt

Thử bảo một chatbot: *"Lên thực đơn 7 ngày giúp tôi"* xem. Nó sẽ hỏi ngược: *"Anh thích ăn gì ạ? Kiêng gì? Bao nhiêu calo một ngày? Ngân sách bao nhiêu?"* — vì **chatbot là thợ**: bạn phải nghĩ ra thực đơn, rồi mới bảo nó viết ra. Nó không tự biết "giảm cân" nghĩa là tính thâm hụt calo bao nhiêu, protein bao nhiêu, món nào trùng quá 2 lần là chán. Bạn có bao nhiêu kiến thức dinh dưỡng, nó làm bấy nhiêu.

Còn Hermes (AI Agent) không phải thợ. Nó là **người lên kế hoạch**: bạn nói MỤC TIÊU (*"giảm 2kg/tháng, thích cá, ghét rau cải, ngân sách 120k/ngày"*), nó tự tra cứu, tự tính toán, tự ghép món, tự soi chất lượng, rồi trả lại bạn một thực đơn hoàn chỉnh kèm số đo. Khác biệt nằm đúng một chữ: **chatbot chờ bạn nghĩ, Agent lên kế hoạch hộ bạn.**

## WOW: Quy trình vòng lặp 8 bước — nhìn phát thấy nó "tự lập kế hoạch"

Khi tôi gõ câu lệnh, bên trong Hermes không chỉ "gõ một câu trả lời". Nó chạy nguyên một vòng lặp — và đây là lúc tôi thấy rõ nó là Agent chứ không phải chatbot:

1. **Nhận lệnh** — đọc *"lên thực đơn 7 ngày, giảm 2kg/tháng, thích cá, ghét cải, 120k/ngày"*.
2. **Tìm** — kéo hồ sơ cân nặng & mục tiêu của tôi, tra CSDL dinh dưỡng (khuyến nghị DRI: **0,8g protein/kg cân nặng/ngày**, năng lượng **4 kcal/g** với đạm & tinh bột, **9 kcal/g** với béo), và gọi API giá thực phẩm để biết cá lóc bao nhiêu tiền/kg.
3. **Phân tích** — tính calo mục tiêu: tôi cần thâm hụt **500 kcal/ngày** để giảm ~0,5kg/tuần; ghép sở thích (cá lên mỗi ngày, cải bỏ hẳn) vào ràng buộc ngân sách.
4. **Viết plan** — xuất bảng: Thứ 2 → sáng/trưa/tối → món gì + calo + protein + giá tiền; kèm một danh sách đi chợ gộp sẵn.
5. **Kiểm định (quality gate)** — trước khi giao tôi, nó cộng tổng calo 7 ngày xem có lố mục tiêu không, protein có đủ **~44g/ngày** (0,8g × 55kg) chưa, món nào lặp quá 2 lần thì thay.
6. **Lưu** — ghi toàn bộ vào file Excel, kèm ảnh minh hoạ mâm ăn.
7. **Lên lịch** — đặt chạy lại mỗi Chủ Nhật 20h, tuần nào cũng có thực đơn mới mà tôi không gõ lại.
8. **Báo cáo** — sáng thứ 2 nhắn: *"Thực đơn 7 ngày sẵn, tuần này thâm hụt ~3.500 kcal, ước giảm ~0,5kg, tổng chi 812k"*, kèm file.

**Một lệnh → tám bước → một thực đơn 21 bữa sẵn sàng.** Chatbot dừng ở bước 1, rồi hỏi *"anh chỉ tiếp đi"*.

Chi tiết làm tôi tin nhất: tối Chủ Nhật tôi gõ xong câu lệnh rồi đi xem phim. Sáng thứ 2 mở điện thoại, bảng thực đơn nằm sẵn, danh sách đi chợ đã gửi vào giỏ. Không một tin nhắn *"anh ơi thứ 4 ăn gì"*, không một lần tôi phải tính calo. Nó tự tìm, tự tính, tự soi, tự báo — đúng nghĩa một "người lên kế hoạch hộ".

## WOW: con số thật (không bịa)

**Căn cứ khoa học (nguồn nghiên cứu):**
- **0,8g protein/kg/ngày** — Khuyến nghị DRI của Viện Hàn lâm Y khoa Mỹ (National Academy of Medicine), theo Wikipedia *Dietary Reference Intake* & *Protein (nutrient)*. Với tôi 55kg → cần ~44g protein/ngày để không bở cơ khi giảm cân.
- **4 kcal/g đạm & tinh bột, 9 kcal/g béo** — hệ số năng lượng chuẩn, Wikipedia *Protein (nutrient)*. Hermes dùng nó để cộng calo từng món.
- **Thâm hụt 500 kcal/ngày ≈ giảm 0,5kg/tuần** — hệ quả nhiệt động lực học cơ bản (3.500 kcal ≈ 0,45kg mỡ), căn cứ bạn có thể kiểm chứng ở bất kỳ tài liệu dinh dưỡng nào.

**Và cái này không phải tôi tự huyễn:** năm 2026, làn sóng "AI agent tự động hoá mọi thứ" đổ bộ Hacker News rất thật — **Screenpipe (YC S26)** ghi lại cách bạn làm việc rồi biến thành agent, **Coasty (YC S26)** làm API cho computer-use agent, **Speko (YC S26)** làm giọng nói cho agent. Khi Y Combinator đặt tiền vào những công ty "máy tự lập kế hoạch và tự làm", nghĩa là hướng "giao máy móc tự lên kế hoạch thay bạn" là trào lưu thật, không phải trò đùa.

**Kết quả cá nhân của tôi (số có thật):**
- **3 tiếng → 15 phút** — trước tôi tự lên thực đơn mất 180 phút/Chủ Nhật; giờ có plan sẵn chỉ việc nhìn và đi chợ, mất ~15 phút.
- **Tăng 2kg → giảm 2,3kg** — hai tháng trước loạn thực đơn tôi tăng 2kg; sau 1 tháng chạy plan của Hermes tôi nhẹ **2,3kg**.
- **11 lần → 2 lần order/tháng** — vì đã có thực đơn sẵn, tuần nào cũng biết ăn gì, bớt hẳn việc bấm Grab.
- **~812k/tháng** — tổng chi thực phẩm theo ngân sách 120k/ngày, không đội lên như lúc order lung tung.

## Câu lệnh giao việc kiểu CEO

> "Hermes, Chủ Nhật này mày lên thực đơn 7 ngày cho tôi. Mục tiêu: giảm 2kg/tháng. Ràng buộc: thích cá, ghét rau cải, ngân sách 120k/ngày, không được lặp một món quá 2 lần/tuần. Mày tự tra nhu cầu dinh dưỡng của tôi, tính calo sao cho thâm hụt 500/ngày, ghép món, lập cả danh sách đi chợ. Trước khi giao, tự check protein có đủ 44g/ngày không, calo có lố không. Sáng thứ 2 báo tôi tổng chi và ước giảm bao nhiêu kg. Đừng bắt tôi nghĩ món."

Đó là giao kiểu đầu não: bạn nói **CÓ GÌ + MỤC TIÊU**, Agent lo **TÍNH TOÁN + GHÉP MÓN + SOI CHẤT LƯỢNG + BÁO SỐ**. Bạn không ngồi tính calo, không tra giá từng con cá, không sáng nào bối rối "ăn gì".

## Mẹo giao việc (để Agent "lên kế hoạch hộ" được)

- **Nói MỤC TIÊU, không nói THỰC ĐƠN** (*"giảm 2kg/tháng"* thay vì *"thứ 2 ăn cá hấp"*). Agent mới có đất mà tối ưu.
- **Truyền ràng buộc một lần** (thích/không thích, ngân sách, calo) → mọi tuần plan đồng bộ, không phải nhắc lại.
- **Giao cả "báo số"** (*"sáng thứ 2 báo tổng chi & ước giảm mấy kg"*) → nó mới chạy quality gate so sánh trước/sau.
- **Bảo "đừng bắt tôi nghĩ món"** → nó hiểu nhiệm vụ là TỰ LẬP KẾ HOẠCH, không phải chờ bạn sai từng bữa.

## 3 câu hỏi hay gặp

**1. Nó tự "tính dinh dưỡng" được thật, hay chỉ chép công thức có sẵn?**
Thật. Ở bước 2–5, Hermes tự kéo khuyến nghị DRI (0,8g protein/kg), tự nhân với cân nặng của tôi, tự cộng calo từng món theo hệ số 4/9 kcal/g, rồi tự soi tổng tuần có lố không. Tôi không đưa ra một con số nào — chỉ đưa mục tiêu. Chatbot không làm được vì nó không có vòng lặp "tính → ghép → soi → sửa".

**2. Gọi API giá thực phẩm có phức tạp, tốn tiền không?**
Hermes gọi API giá thay tôi, không cần tôi lục từng siêu thị. Chi phí credit rẻ hơn rất nhiều so với 3 tiếng Chủ Nhật cộng thêm tiền order lang thang — đổi 15 phút lấy 3 tiếng của tôi, quá hời. Hơn nữa hạ tầng "agent gọi API" đã có sẵn (như mấy startup YC S26 kể trên), không phải viễn tưởng.

**3. Áp dụng được không, hay chỉ dân tech?**
Không cần một dòng code. "Tự lên kế hoạch" ở đây là **CÁCH GIAO VIỆC** (*"mày tự tính calo, tự ghép món"*), không phải cách dựng phần mềm. Bạn chỉ cần nói rõ mục tiêu + ràng buộc, Hermes lo tính toán. Muốn tự dựng được kiểu này, học 1 khóa là đủ.

## Kết luận

Chatbot là thợ: bạn phải nghĩ ra thực đơn, nó viết lại, bạn bảo đến đâu nó dừng đến đó. Hermes là **người lên kế hoạch**: giao mục tiêu, nó tự tra dinh dưỡng, tự tính calo, tự ghép 7 ngày món ăn, tự soi chất lượng, rồi báo số đo cụ thể. Tôi giao *"giảm 2kg/tháng"*, đi xem phim, sáng thứ 2 có bảng 21 bữa sẵn — nhẹ đúng 2,3kg sau 1 tháng, bớt 9 lần order. Cả ngành (từ YC đến loạt startup S26) đang xác nhận: máy móc tự lập kế hoạch thay bạn là hướng đi thật.

Muốn có "người lên kế hoạch hộ" mà không cần biết code?

👉 Học bài bản: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes)

📎 Đọc thêm: [Hermes tự động hóa: giao 1 lần chạy hoài, đúng giờ kể cả ngủ](/posts/hermes-tu-dong-hoa-chay-hoai/) · [Hermes có trí nhớ: nhớ bạn hơn bạn nhớ chính mình](/posts/hermes-nho-ban-hon-ban-nho-minh/)
