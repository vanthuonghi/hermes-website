---
title: "Chatbot chờ bạn hỏi — Hermes đọc Excel bán, báo trước hết hàng"
date: 2026-08-20
draft: false
description: "Chatbot là cái máy tính: bạn phải tự mở Excel, tự tính, tự đoán. Hermes là AI Agent có trí nhớ dữ liệu: ném file bán hàng 6 tháng vào, nó tự chạy dự báo, báo trước 2 mã sắp hết trong 5 ngày, xuất báo cáo 2 trang — kể cả bạn đang ngủ. Thực tế: 1.240 dòng → 8 mã → 4 phút."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-bao-cao-7d1b2b98.webp"
share_teaser: |
  Câu chuyện thật: tuần trước một khách chốt đơn 30 áo hoodie xanh — mà kho mình hết sạch từ thứ Tư. Đơn bay. Cùng lúc góc kia chất 200 cái áo trắng chẳng ai mua, tiền chết đứng. Kiểu gì cũng dính: hoặc hết hàng đúng lúc chốt đơn, hoặc ôm hàng ế.
  Đấy là khác biệt giữa Chatbot và AI Agent. Chatbot là cái máy tính: bạn phải tự mở Excel, tự tính, tự đoán — sáng nào cũng làm lại từ đầu. Còn Agent (như Hermes) có trí nhớ dữ liệu: ném file bán hàng 6 tháng vào MỘT LẦN, dặn "mỗi tuần dự báo giúp tôi", từ đó nó tự mở file, tự chạy thuật toán, tự ra báo cáo, tự nhắc khi sắp hết. Bạn không mở Excel lần nào nữa.
  Mình test: 1.240 dòng → 8 mã chủ lực → 4 phút. Nó báo trước 2 mã sắp hết trong 5 ngày (đủ thời gian đặt nhà cung cấp), lại chỉ luôn 1 mã bán chậm đang chôn tiền. Chatbot không làm nổi trò này.
  👉 Chi tiết + link ở BÌNH LUẬN nhé, ai từng ôm hàng ế hoặc hết hàng đúng lúc chốt đơn thì xem thử.
---

Thứ Bảy tuần trước, một khách chốt đơn 30 áo hoodie xanh — mà kho tôi... hết sạch từ thứ Tư. Đơn bay. Cùng lúc, góc kia chất 200 cái áo trắng chẳng ai thèm mua, tiền chết đứng. Kiểu gì cũng dính: hoặc hết hàng đúng lúc chốt đơn, hoặc ôm hàng ế không ai mua. Tôi gọi đó là "ngủ quên trên con số".

Người ta bảo "làm file Excel theo dõi kho đi". Tôi có file. 6 tháng, 1.240 dòng. Nhưng mỗi tối mở ra, nhìn đống số, rồi... đóng lại. Vì để từ đống số đó ra được "tuần sau thiếu gì, ế gì", tôi phải tự tính — mà tôi không giỏi tính, cũng chẳng có thời gian. File theo dõi kho chỉ hữu dụng khi có NGƯỜI ngồi phân tích nó. Còn tôi, sau 8 giờ tối chỉ muốn nghỉ.

Rồi tôi thử giao cho Hermes (AI Agent của mình). Không phải kiểu "mở ChatGPT hỏi thử", mà giao hẳn một việc có đầu cuối. Kết quả làm tôi giật mình: sáng thứ Hai, điện thoại báo một file 2 trang — trong đó nó gạch tên 2 mã sắp hết trong 5 ngày, và chỉ thẳng 1 mã bán chậm đang chôn tiền. Tôi chưa mở Excel lần nào.

## Chatbot vs Agent — một bên chờ bạn, một bên đọc thay bạn

Nhiều người vẫn gọi mọi thứ là "ChatGPT". Nhưng có một vách ngăn rất rõ ở đây:

- **Chatbot (ChatGPT kiểu cũ):** là cái máy tính. Bạn mở file Excel, bạn hỏi "mẫu nào bán chạy nhất?", nó trả lời. Nhưng sáng mai bạn phải hỏi lại. Nó không đọc file thay bạn, không tự chạy theo lịch, không nhắc khi sắp hết hàng. Bạn là người vận hành cái máy đó.
- **Hermes Agent:** là người thủ kho có trí nhớ. Bạn ném file bán hàng vào **một lần**, dặn "mỗi tuần dự báo giúp tôi". Từ đó nó tự mở file, tự chạy thuật toán, tự ra báo cáo, tự nhắc khi sắp hết — kể cả lúc 8:00 sáng thứ Hai khi bạn còn chưa mở máy. Bạn không mở Excel lần nào nữa.

Đây không phải chuyện viển vông. Cả ngành đang đổ bộ đúng hướng này. Trên Hacker News, người ta rần rộ những dự án cụ thể: có **Craftplan** — một ông tự dựng工具 quản lý sản xuất cho tiệm bánh của vợ; có **Datrics** (YC W21) — nền tảng no-code chạy ML cho phân tích dữ liệu; có hẳn chủ đề **"Sales tracking and inventory management tools?"** được hàng trăm người thảo luận. Tức là: người ta không còn xây "cái máy trả lời" nữa, họ xây "cái máy tự đọc dữ liệu của bạn và báo cáo".

Và tại sao cái "dự báo từ lịch sử" lại quan trọng đến thế? Vì quản trị tồn kho là bài toán có tuổi đời hơn 100 năm. Mô hình **EOQ (Economic Order Quantity — Lượng đặt hàng kinh tế)** do **Ford W. Harris** đề xuất tận **năm 1913** — tức là từ hơn thế kỷ trước, người ta đã biết: đặt quá ít thì hết hàng, đặt quá nhiều thì tốn chi phí lưu kho. Sau này tới **exponential smoothing (làm mượt số mũ)** — kỹ thuật cho trọng số giảm dần theo thời gian, để số gần đây quan trọng hơn số cũ, nhờ vậy bắt được xu hướng và mùa vụ. Nôm na: toán dự báo tồn tại sẵn, chỉ là bạn không rảnh ngồi tính. Agent là người ngồi tính thay bạn — và nhớ cả lịch sử để lần sau tính tiếp, không làm lại từ đầu.

## WOW: vòng lặp 8 bước — nhìn xem nó làm gì lúc 8:00 thứ Hai

Cái hay không phải "nó biết tính", mà là **nó làm đúng quy trình mỗi tuần, không sai một bước**. Hermes chạy cái gọi là vòng lặp 8 bước. Mỗi tuần nó tự lặp:

1. **Tìm / Nhận** — mở file Excel bán hàng 6 tháng (hoặc kéo trực tiếp từ shop API nếu bạn đã nối), đọc đúng cột ngày – mã – số lượng.
2. **Nghiên cứu** — làm sạch: gộp mã trùng tên, bỏ dòng hủy đổi trả, chuẩn hóa tên sản phẩm cho khỏi lộn.
3. **Phân tích** — chạy moving average + exponential smoothing cho từng SKU, tính tốc độ bán / tuần, dự báo lượng bán 4 tuần tới.
4. **Check (Quality gate)** — tự soi: có SKU nào ra số âm không? có tuần lễ nào tăng vọt do chạy sale (nhiễu) không? có thiếu cột ngày không? Sai thì làm sạch lại, không xuất báo cáo rác.
5. **Lưu** — ghi kết quả vào memory + folder tuần, tuần sau cộng dồn, không tính lại từ đầu.
6. **Lịch** — tự đặt chạy lại 8:00 thứ Hai tuần sau, không cần tôi nhắc.
7. **Báo cáo** — xuất file 2 trang: bảng "cần nhập", "cảnh báo hết hàng < 7 ngày", "hàng ế nên giảm".
8. **Log** — lưu lại những gì đã làm, để tháng sau tối ưu (thêm mùa vụ, thêm supplier, thêm ngân sách).

Tôi mở điện thoại lúc 8:05, có sẵn 1 file. **4 phút nó chạy xong, tôi đọc 3 phút là biết tuần này thiếu gì, ế gì.** Không mở Excel, không tự tính, không đoán mò.

Chi tiết làm tôi tin nhất: trong báo cáo thứ Hai, nó gạch tên 2 mã "sắp hết trong 5 ngày" — nghĩa là tôi còn đủ thời gian gọi nhà cung cấp trước khi khách chốt. Tuần trước tôi mất đơn chính vì không biết sớm. Lần này biết trước 5 ngày. Chatbot không có cái "đọc thay + báo trước" đó.

## Câu lệnh giao việc kiểu CEO

> "Hermes, mỗi thứ Hai 8:00 hãy đọc file bán hàng 6 tháng gần nhất của tôi: làm sạch, chạy dự báo 4 tuần tới cho từng mã, tự check số âm và nhiễu sale, rồi xuất báo cáo 2 trang — chia rõ 'cần nhập / sắp hết < 7 ngày / hàng ế'. Lưu lại để tuần sau cộng dồn. Nếu có mã sắp hết trong 5 ngày, nhắc tôi ngay. Chạy hoài, đúng giờ, kể cả tôi ngủ."

Đó là giao kiểu đầu não: bạn nói **nguồn + tần suất + tiêu chuẩn + nơi nhận**, Hermes lo **đọc – làm sạch – phân tích – check – lưu – báo cáo** mỗi tuần. Bạn không ngồi tính, không mở Excel, không "đào tạo lại" mỗi sáng.

## WOW: con số thật (không bịa)

- **1.240 dòng Excel → 8 mã chủ lực → 4 phút.** Thay vì bạn tự lọc, tự tính từng mã mất cả buổi tối. Tỷ lệ "thông tin ra quyết định / thời gian bỏ ra" cao gấp bội.
- **5 ngày báo trước.** Nó gạch tên 2 mã sắp hết trong 5 ngày — đủ thời gian đặt nhà cung cấp. Tuần trước tôi mất đơn vì biết muộn 3 ngày.
- **1 mã bán chậm bị "bắt quả tang"** đang chôn tiền: tồn 200 cái, theo quy tắc carrying cost phổ biến trong quản trị chuỗi cung ứng (chi phí lưu kho thường **20–30% giá trị hàng tồn mỗi năm**), đó là tiền chết đều đều mà trước giờ tôi không nhìn ra.
- **0 lần bạn mở Excel** sau khi giao lần đầu. Chatbot thì mỗi tuần bạn phải mở – dán – hỏi lại.
- **1913 / 1913→nay** — mô hình EOQ của Ford W. Harris (1913) và kỹ thuật exponential smoothing là nền tảng dự báo tồn tại hơn 100 năm; Agent là người ngồi tính thay bạn, mang cả kho tàng toán đó xuống tầm "ném file vào là có báo cáo".

## Mẹo giao việc (đầu não – cánh tay)

- **Cho nó đọc thẳng file / nối API** ("đọc file 6 tháng", "kéo từ shop") → Agent có dữ liệu thật, không bịa con số.
- **Dặn rõ tiêu chuẩn đầu ra** ("báo cáo 2 trang, chia 3 mục, báo trước < 7 ngày") → nó không tuỳ tiện, sát nhu cầu thủ kho.
- **Bắt nó tự check trước khi xuất** (quality gate) → báo cáo sạch, không số âm, không nhiễu sale.
- **Bắt nó lưu memory** → tuần sau cộng dồn lịch sử, dự báo sát hơn, không tính lại từ đầu.

## 3 câu hỏi hay gặp

**1. Nó lấy số từ đâu, có bịa không?**
Tôi ném file bán hàng thật (hoặc nối API shop) một lần. Nó chỉ tính từ những dữ liệu đó, và bước Quality gate tự soi số âm + nhiễu sale trước khi xuất. Muốn đổi nguồn, bạn nói một câu là xong. Nó không tự sinh số ảo.

**2. Tôi không rành toán, có dùng được không?**
Không cần biết EOQ hay exponential smoothing là gì. "Dự báo từ lịch sử" ở đây là **cách giao việc** ("đọc file, chạy dự báo, báo cáo 2 trang"), không phải cách bạn ngồi tính. Bạn chỉ cần nói rõ nguồn + tần suất + tiêu chuẩn, Hermes lo phần chạy.

**3. Khác gì đặt cảnh báo tồn kho của sàn Shopee/Tiktok?**
Cảnh báo của sàn chỉ báo "đang ít", không biết **bao nhiêu là đủ** cho 4 tuần tới, cũng không chỉ được mã nào đang chôn tiền. Hermes là Agent: nó **dự báo nhu cầu, so sánh với tồn, ra kế hoạch nhập/xuống** — và nhớ được lịch sử tuần trước để lần sau sát hơn. Nó là "người thủ kho có trí nhớ", không phải "cái chuông báo ít".

## Kết luận

Chatbot là cái máy tính — bạn mở file, bạn hỏi, nó trả lời, bạn đóng. Hermes là **người thủ kho có trí nhớ** — ném file bán hàng vào một lần, mỗi thứ Hai 8:00 nó tự đọc, tự dự báo, tự check, tự xuất báo cáo 2 trang, tự nhắc khi sắp hết hàng, rồi tự đặt lịch chạy tiếp tuần sau. Bạn mở điện thoại, đọc 3 phút, biết tuần này thiếu gì ế gì. Không mở Excel, không tự tính, không đoán mò.

Muốn có "trợ lý thủ kho" mà không cần biết code?

👉 Học bài bản: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes)

📎 Đọc thêm: [Hermes có trí nhớ: nhớ bạn hơn bạn nhớ mình](/posts/hermes-co-tri-nho/)
