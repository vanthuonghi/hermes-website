---
title: "Hermes đọc 300 trang hợp đồng, trích đúng điều khoản chết người — bạn chỉ đọc 1 trang tóm tắt"
date: 2026-08-15
draft: false
description: "Giao Hermes cả folder hợp đồng PDF, nó tự đọc từng file, trích điều khoản rủi ro, đối chiếu chéo, xuất bảng, rồi nhắc bạn trước ngày hết hạn. Không phải chatbot tóm tắt — đây là AI Agent làm việc thật của một nhân sự pháp chế."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-doc-hop-dong.webp"
share_teaser: |
  Hỉ vừa quăng cho Hermes cả folder 300 trang hợp đồng PDF rồi đi ăn cơm. 🍚
  Về thì có sẵn 1 bảng: điều khoản phạt nằm trang nào, ngày hết hạn nào sắp tới, chỗ nào bất lợi cần thương lượng lại.
  Chatbot chỉ "tóm tắt" khi bạn dán chữ vào. Còn AI Agent thì tự mở file, tự đọc hết, tự đối chiếu, tự xuất bảng, tự nhắc bạn trước 30 ngày — bạn không cần ngồi đó.
  Khác biệt là: một cái nói, một cái LÀM.
  👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN nhé.
---

Tháng trước một anh chủ shop nhắn tôi: "Hỉ ơi, tôi ký cái hợp đồng thuê kho 40 trang, giờ bên kia đòi phạt 8% giá trị hợp đồng, tôi... không nhớ mình có ký khoản đó không."

Anh có ký. Nó nằm ở trang 31, mục 9.4, viết bằng thứ tiếng Việt dài dòng mà đọc tới dòng thứ ba là mắt tự động trượt xuống.

Không phải anh dở. Là vì đọc 300 trang hợp đồng bằng mắt người, tỉnh táo được 20 trang đầu là giỏi rồi.

## Chatbot vs Agent — cùng đưa một tập hợp đồng

**Chatbot:** bạn phải tự mở file, tự copy từng đoạn, dán vào khung chat, hỏi "tóm tắt giúp tôi". Nó trả về một đoạn văn mượt mà. Bạn đóng tab. Tuần sau cần lại — làm lại từ đầu. Nó không nhớ, không mở được file của bạn, và không bao giờ tự nhắc bạn điều gì.

**Agent:** bạn chỉ đưa nó cái **thư mục**.

Nó tự mở từng PDF (kể cả bản scan mờ), tự đọc hết, tự trích ra thứ bạn cần, tự đối chiếu hợp đồng này với hợp đồng kia xem có chỗ nào mâu thuẫn, tự ghi vào một bảng, tự lưu lại, rồi tự đặt lịch nhắc bạn trước ngày hết hạn 30 ngày.

Bạn không ngồi đó. Bạn đi ăn cơm.

## Vòng lặp Hermes chạy trên tập hợp đồng

Đây là chỗ mà người ta thường không hình dung được. Agent không làm 1 nhát rồi thôi — nó chạy **vòng lặp**, từng file, tự đi hết:

1. **Quét** — liệt kê mọi file trong folder `hop-dong/`, bỏ file trùng.
2. **Đọc** — mở từng PDF, bóc chữ ra (bản scan thì OCR).
3. **Trích** — lôi ra: các bên, giá trị, thời hạn, điều khoản phạt, điều kiện chấm dứt, điều khoản bất lợi.
4. **Đối chiếu** — so với các hợp đồng cũ đã lưu: điều nào lần này khắt khe hơn?
5. **Tự kiểm** (quality gate) — thiếu mục nào thì quay lại đọc kỹ lại file đó, không bịa.
6. **Xuất** — ghi vào một bảng duy nhất, kèm số trang để bạn mở kiểm tra được.
7. **Lưu + lên lịch** — nhớ vào bộ nhớ, đặt nhắc trước hạn 30 ngày.
8. **Báo cáo** — gửi bạn 1 trang: *"5 hợp đồng. 2 chỗ cần thương lượng lại. 1 cái hết hạn 14/9."*

Chatbot dừng ở bước 3, và chỉ khi bạn cầm tay dán chữ cho nó. Agent đi hết 8 bước một mình. (Chi tiết vòng lặp này tôi mổ kỹ ở bài [Hermes vòng lặp 8 bước](/hermes-website/posts/hermes-vong-lap-8-buoc/).)

## Câu lệnh tôi giao — nói như CEO nói với trợ lý

Đây là toàn bộ thứ tôi gõ. Không code, không cấu hình gì:

> Trong folder `hop-dong/` có tất cả hợp đồng của tôi. Đọc hết từng file, kể cả bản scan.
>
> Với mỗi hợp đồng, trích cho tôi: các bên, giá trị, thời hạn, điều khoản phạt, điều kiện chấm dứt, và mọi khoản mà tôi là bên bất lợi. Ghi rõ số trang từng mục để tôi mở kiểm tra được.
>
> Đối chiếu với các hợp đồng cũ đã lưu — chỗ nào lần này bất lợi hơn thì đánh dấu ĐỎ.
>
> Xuất ra 1 bảng Excel, cộng thêm 1 trang tóm tắt cho tôi đọc trong 2 phút.
>
> Hợp đồng nào sắp hết hạn trong 60 ngày tới: nhắc tôi trước 30 ngày. Nhớ luôn để tháng sau tôi thêm file mới thì tự làm lại, khỏi cần tôi giao lại.

Câu cuối là câu quan trọng nhất. **"Khỏi cần tôi giao lại"** — đó là ranh giới giữa dùng AI và có nhân sự.

## Con số làm tôi tỉnh người

Bộ 5 hợp đồng, tổng 287 trang. Trong đó 2 file là bản scan chụp bằng điện thoại, hơi lệch.

- Tôi tự đọc bằng mắt, có ghi chú tử tế: **khoảng 6 tiếng**, và tôi biết chắc mình sẽ bỏ sót.
- Thuê người soát bên ngoài: rẻ nhất cũng vài triệu, chờ 2–3 ngày.
- Hermes: giao lúc 11h47 trưa, tôi đi ăn, **12h09 có bảng** — 22 phút.

Nó bắt được 3 thứ tôi đã đọc qua mà không thấy: một khoản tự động gia hạn thêm 12 tháng nếu không thông báo trước 45 ngày (trang 19), một khoản phạt chậm thanh toán tính theo ngày chứ không theo tháng (trang 26), và một chỗ định nghĩa "trường hợp bất khả kháng" viết hẹp bất thường — nghiêng hết về phía bên kia.

Ba dòng đó, nếu bỏ sót, đắt hơn cả năm tiền khoá học.

Và tháng sau tôi ném thêm file mới vào folder. Không gõ gì cả. Nó tự làm lại.

## Mẹo giao việc kiểu này cho gọn

- **Đưa folder, đừng đưa từng file.** Agent làm việc theo lô. Đưa từng file là bạn đang tự biến nó thành chatbot.
- **Luôn bắt nó ghi số trang.** Đây là cách bạn kiểm tra nó trong 30 giây thay vì đọc lại 300 trang. Không có số trang thì không tin.
- **Nói rõ "tôi là bên nào".** Bất lợi cho bạn mới đáng đánh dấu đỏ. Không nói, nó soát trung tính, kém sắc.
- **Cấm bịa, cho phép nói "không tìm thấy".** Câu thêm vào: *"Mục nào hợp đồng không có thì ghi KHÔNG CÓ, tuyệt đối không suy diễn."*
- **Chốt bằng một câu tự động.** "Nhớ luôn, file mới thì tự làm lại." Một câu đó biến việc-một-lần thành quy trình chạy hoài.

## Nói thẳng

Hợp đồng là ví dụ. Cái thật sự đáng chú ý không phải "AI đọc được PDF" — đọc PDF thì nhiều thứ đọc được.

Đáng chú ý là: **bạn giao một lần, nó tự đi hết vòng lặp, tự kiểm, tự nhắc bạn, và tháng sau vẫn tự chạy khi bạn đã quên mất là mình từng giao.**

Đó là mô tả công việc của một nhân sự, không phải của một công cụ chat.

Nếu bạn đang tự làm hết mọi thứ vì "thuê người thì không đủ tiền, mà tự làm thì không đủ giờ" — thì cái bạn cần không phải thêm một app AI nữa. Là một Agent biết nhận việc.

👉 Tôi gói toàn bộ cách cài và giao việc cho Hermes vào khoá **Nhân Sự Toàn Năng Hermes** — 37 bài, làm theo là chạy được, không cần biết code. Early-bird **199K** (sau đó 499K), hoàn tiền trong 7 ngày nếu bạn thấy không dùng được: **[speedreading.vn/pshermes](https://speedreading.vn/pshermes)**

Đừng để một dòng ở trang 31 dạy bạn bài học đắt hơn cả khoá học.
