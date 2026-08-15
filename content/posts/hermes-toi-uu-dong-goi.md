---
title: "Hermes thay bạn nghĩ: tự tối ưu cách đóng gói, mỗi tối tự chạy lại"
date: 2026-08-15
draft: false
description: "Chatbot chờ bạn hỏi. Hermes tự đọc dữ liệu đơn hàng, tự nghĩ ra cách đóng gói tiết kiệm hơn, tự làm bảng hướng dẫn — mỗi tối tự chạy lại, sáng có báo cáo."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-toi-uu-dong-goi.webp"
share_teaser: |
  Hỉ vừa phát hiện một thứ hơi rùng mình: cái AI của Hỉ nó TỰ NGHĨ giúp mình. 😳📦
  Hỉ không hỏi gì cả. Nó tự mở dữ liệu đơn hàng, tự thấy "chỗ này đóng gói đang lỗ tiền ship", tự đề xuất bộ hộp gọn hơn, tự làm bảng hướng dẫn dán tường. Mỗi tối 21h nó tự chạy lại, sáng ra Hỉ có báo cáo sẵn.
  Đây là chỗ khác nhau căn bản: chatbot là ĐỨA CHỜ HỎI — bạn hỏi nó mới nói, hỏi xong là hết. AI Agent là ĐỨA ĐI LÀM — bạn giao một lần, nó tự tìm việc, tự làm, tự kiểm tra, tự báo cáo, và tự lặp lại ngày mai mà không cần bạn nhắc.
  👉 Hermes đang làm đúng cái này — chi tiết + link ở BÌNH LUẬN nhé.
---

Chín giờ tối, shop đóng xong đơn cuối. Bạn ngồi giữa một đống hộp carton, cầm cuộn băng keo mà đầu vẫn đang tính: hộp này to quá cho một cái áo, phí ship lên 8 nghìn vô lý; hai đơn cùng một khách ở cùng phường mà nhân viên đóng thành hai gói riêng; cái size hộp mua nhiều nhất thì lúc nào cũng hết trước.

Bạn *biết* là đang lỗ chỗ nào đó. Nhưng để biết chắc thì phải mở file đơn hàng, lọc, cộng, so sánh — một buổi tối nữa. Mà tối nào bạn cũng hết pin.

Đây đúng là loại việc bạn nên **giao cho một đứa tự nghĩ**, chứ không phải một đứa chờ bạn hỏi.

## Chatbot chờ hỏi — Agent tự đi tìm việc

**Cách 1 (chatbot):** bạn mở ChatGPT, gõ "cách đóng gói tiết kiệm phí ship". Nó trả về 7 gạch đầu dòng chung chung, đúng nhưng không dính gì tới shop bạn — vì nó chưa hề thấy đơn hàng của bạn. Bạn đóng tab. Mai lại như cũ.

**Cách 2 (Hermes — Agent):** bạn giao một lần, kèm quyền đọc file đơn hàng. Nó **tự mở dữ liệu thật của bạn**, tự thấy "60% đơn nặng dưới 400g nhưng đang bị nhét vào hộp size L", tự đề xuất còn 3 size hộp, tự viết bảng quy tắc gộp đơn cho nhân viên, tự kiểm tra lại số rồi mới đưa bạn. Và tối mai, nó **tự chạy lại với dữ liệu mới** — bạn không gõ thêm một chữ nào.

Khác nhau nằm ở chỗ này: chatbot cho bạn **kiến thức**. Agent cho bạn **một quyết định đã được tính trên số của chính bạn**, kèm việc đã làm xong.

## Bên trong nó chạy vòng lặp gì

Khi bạn giao đầu việc "tối ưu đóng gói", Hermes không trả lời một câu rồi nghỉ. Nó chạy một vòng lặp:

1. **Đọc** — mở file đơn hàng (Excel/CSV, hoặc gọi API sàn nếu bạn nối), lấy cân nặng, kích thước, địa chỉ, phí ship thực trả.
2. **Nghiên cứu** — nhóm đơn theo trọng lượng và tuyến giao, tìm bảng giá hãng vận chuyển để biết mốc nào bị nhảy giá.
3. **Nghĩ** — đây là phần đắt nhất: nó tự đề xuất bộ hộp tối thiểu, quy tắc gộp đơn, và mốc "đơn dưới X gam thì dùng túi thay hộp".
4. **Làm** — xuất ra file bảng hướng dẫn đóng gói, đủ gọn để in ra dán ở bàn đóng hàng.
5. **Tự kiểm tra (quality gate)** — cộng lại số tiền tiết kiệm, đối chiếu xem có đề xuất nào vượt quy định hãng ship không. Sai thì nó tự sửa trước khi đưa bạn.
6. **Lưu** — cất file vào thư mục theo tuần, không đè bản cũ để bạn còn so sánh.
7. **Lên lịch** — hẹn 21h mỗi tối tự chạy lại với dữ liệu mới.
8. **Báo cáo** — sáng ra bạn có một tin nhắn ngắn: tuần này gộp được bao nhiêu đơn, tiết kiệm bao nhiêu, đề xuất mới là gì.

Bạn chỉ làm đúng một việc trong cả chuỗi này: **duyệt**.

## Câu lệnh giao việc kiểu CEO

Đừng viết "giúp tôi tối ưu đóng gói". Viết như đang giao cho nhân viên vận hành — có bối cảnh, có kết quả mong muốn, có giới hạn, có chuẩn nghiệm thu:

> Tôi bán quần áo online, khoảng 40–60 đơn/ngày, ship chủ yếu nội thành và liên tỉnh. File đơn hàng ở `data/donhang.csv` (có cột cân nặng, phí ship thực trả, địa chỉ).
>
> Việc của bạn: phân tích và đề xuất cách đóng gói tiết kiệm phí ship nhất.
>
> Kết quả cần: (1) bộ hộp/túi tối thiểu nên dùng, tối đa 4 loại; (2) quy tắc gộp đơn cho nhân viên, viết đơn giản, không thuật ngữ; (3) một bảng in được dán ở bàn đóng hàng.
>
> Giới hạn: chỉ dùng loại hộp/túi mua được phổ thông ngoài thị trường, không đổi hãng vận chuyển, không đề xuất gì phải thuê thêm người.
>
> Tự kiểm tra trước khi giao: cộng lại số tiền tiết kiệm dự kiến và ghi rõ dựa trên bao nhiêu đơn. Nếu dữ liệu thiếu thì ghi rõ thiếu gì, đừng đoán.
>
> Sau đó: 21h mỗi tối tự chạy lại với dữ liệu mới, sáng gửi tôi báo cáo ngắn 5 dòng.

Câu cuối là câu biến nó từ "một lần" thành "chạy hoài". Nhiều người bỏ mất đúng câu đó — rồi tưởng Agent cũng chỉ như chatbot.

## Con số WOW

- Làm tay: mở file, lọc, cộng, so sánh, viết bảng — **một buổi tối, khoảng 2 tiếng**, và mỗi tuần phải làm lại nếu muốn cập nhật.
- Giao Agent: bạn viết brief **một lần khoảng 5 phút**. Nó chạy tầm 10–15 phút cho lần đầu.
- Từ hôm sau: **0 phút của bạn**. 21h nó tự chạy, sáng có báo cáo. Bạn đang ngủ, việc vẫn xong.
- Tính theo tháng: khoảng **8 tiếng ngồi tính toán** biến thành 8 tiếng bạn đi bán hàng, hoặc đi ngủ sớm.

Cái tiết kiệm lớn nhất ở đây không phải tiền hộp carton. Là việc bạn **không phải nhớ** rằng tối nay tới hạn phải xem lại chuyện đóng gói.

## Mẹo: giao đúng kiểu đầu não – cánh tay

Bạn là đầu não, Hermes là cánh tay. Đầu não làm 3 việc, không làm việc thứ tư:

- **Quyết định mục tiêu**: tiết kiệm phí ship, hay đóng nhanh hơn? Hai hướng cho ra hai đề xuất khác nhau — bạn phải chọn, nó không đoán hộ bạn.
- **Đặt giới hạn**: không đổi hãng ship, không thuê thêm người. Không có giới hạn thì Agent đề xuất trời trăng, đọc xong không dùng được.
- **Đặt chuẩn nghiệm thu**: "cộng lại số, ghi rõ dựa trên bao nhiêu đơn". Đây là cái buộc nó tự soi mình trước khi giao — khác biệt giữa một bản báo cáo dùng được và một bài văn hay.

Việc thứ tư — mở file, lọc, cộng, viết bảng, nhớ hạn, lặp lại mỗi tối — **đừng làm nữa**. Đó là việc của cánh tay.

📎 Đọc thêm: [Vòng lặp 8 bước Hermes tự chạy](/posts/hermes-vong-lap-8-buoc/)

## Kết

Điều làm người ta giật mình khi dùng Agent thật không phải là "nó viết hay". Là lần đầu bạn mở điện thoại buổi sáng, thấy một báo cáo mình không hề yêu cầu hôm nay — vì hôm qua bạn đã yêu cầu một lần, và nó vẫn đang làm.

Nếu bạn đang một mình gánh cả shop, đây là thứ đáng học trước tiên: không phải học viết prompt cho hay, mà học **giao việc cho một cái Agent biết tự chạy**.

👉 Khoá **Nhân Sự Toàn Năng Hermes** — 37 bài, dạy đúng cách giao việc kiểu này cho người không biết code. Đang early-bird **199K** (sau 499K), **hoàn tiền trong 7 ngày** nếu bạn thấy không dùng được: [speedreading.vn/pshermes](https://speedreading.vn/pshermes)
