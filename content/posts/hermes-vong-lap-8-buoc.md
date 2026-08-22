---
title: "Vòng lặp 8 bước của Hermes: giao 1 lần, Agent tự chạy tới khi xong việc"
date: 2026-08-22
draft: false
description: "Chatbot trả lời 1 lượt rồi đứng im chờ bạn gõ tiếp. AI Agent thì chạy vòng lặp: tìm → nghiên cứu → viết → tự kiểm → sửa → lưu memory → hẹn giờ → báo cáo. Bài này mổ xẻ đúng 8 bước Hermes tự chạy mỗi ngày để ra 1 bài blog + 3 bản social, mất 6 phút máy chạy thay vì 2 tiếng người ngồi."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-vong-lap-d9e04e96.webp"
share_teaser: |
  Hỉ nhận ra một chuyện hơi buồn: 90% người dùng AI vẫn đang dùng nó như cái máy trả lời. Hỏi 1 câu — nhận 1 đoạn — rồi tự copy, tự sửa, tự đăng. Mệt vẫn mệt. 😅
  Khác biệt thật nằm ở chỗ này: Chatbot (kiểu ChatGPT) trả lời 1 lượt rồi ĐỨNG IM chờ bạn gõ tiếp. Còn AI Agent (Hermes) chạy VÒNG LẶP: nó tự tìm dữ liệu → tự nghiên cứu → tự viết → tự soi lỗi bài của chính nó → tự sửa → tự lưu vào bộ nhớ → tự hẹn giờ → tự báo cáo cho mình. Mình chỉ đọc kết quả.
  Hôm nay mình ngồi bấm đồng hồ: 8 bước đó máy chạy hết 6 phút. Cũng khối lượng ấy hồi mình làm tay: 2 tiếng.
  👉 Mình có mổ xẻ chi tiết đúng từng bước 1→8 (kèm câu lệnh mình giao) — chi tiết + link mình để ở BÌNH LUẬN nhé, ai đang làm content một mình thì nên xem.
---

Tôi đo thử một lần cho biết: viết 1 bài blog 1.500 từ có nghiên cứu, rồi cắt ra 3 bản đăng Facebook – Zalo – YouTube, tôi làm tay mất **khoảng 2 tiếng**. Không phải vì gõ chậm, mà vì cái vòng lặp ngầm: tìm tư liệu, đọc, viết, đọc lại thấy dở, sửa, đặt tiêu đề, chọn ảnh, hẹn giờ đăng.

Bây giờ khối lượng đó chạy trong **6 phút** — và tôi không ngồi đó. Không phải vì AI viết nhanh hơn tôi (thật ra chỗ nào nó cũng chậm hơn tôi gõ), mà vì nó **lặp** giúp tôi.

Đây là chỗ tôi nghĩ nhiều người đang hiểu sai về AI.

## Chatbot đứng im, Agent thì đi vòng

**Chatbot** — ChatGPT, Gemini, bạn hỏi gì cũng được — hoạt động theo nhịp *một hỏi, một đáp*. Trả lời xong nó **đứng im**, chờ bạn gõ tiếp. Bạn là người phải nhớ bước tiếp theo là gì, phải copy kết quả ra Word, phải tự thấy chỗ dở, phải tự bấm đăng. Nói thẳng: AI làm phần gõ chữ, bạn vẫn làm phần *vận hành*. Mà phần vận hành mới là phần mệt.

**AI Agent** — như Hermes — nhận một mục tiêu, rồi **tự đi hết vòng**: làm bước 1, lấy kết quả bước 1 làm nguyên liệu cho bước 2, tới bước 4 tự soi lỗi, thấy chưa đạt thì **quay lại sửa**, đạt rồi mới đi tiếp, cuối cùng tự lưu và tự báo cáo. Nó có tay (chạy được lệnh, ghi được file, gọi được API), có bộ nhớ, và có tiêu chuẩn để tự chấm điểm mình.

Một câu để nhớ: *chatbot sinh chữ, agent làm xong việc.*

Trên bảng tin AI mấy tuần nay cũng cùng một hướng — các nền tảng kiểu Keystroke hay Tines đều đang chào bán đúng một thứ: cho agent chạy **workflow tự động** thay vì chat từng lượt. Cái xu hướng này không phải mốt, nó là chỗ AI bắt đầu tiết kiệm thời gian thật.

## 8 bước Hermes tự chạy mỗi ngày

Đây là vòng lặp thật đang chạy trên blog này, hai tiếng một lần, kể cả lúc tôi ngủ:

**1. Định hướng.** Agent xem hôm nay đã ra bao nhiêu bài, còn thiếu mấy bài, chọn chủ đề chưa dùng trong danh sách. Không hỏi tôi.

**2. Nghiên cứu.** Nó tự chạy script gom tư liệu từ nguồn còn truy cập được, lọc lấy dữ kiện dùng được, bỏ nguồn rác. Bước này là lý do bài có số liệu chứ không chỉ có cảm xúc.

**3. Sản xuất.** Viết bài theo cấu trúc cố định: hook có số → phân biệt chatbot/agent → quy trình → câu lệnh mẫu → kết quả đo lường → FAQ → CTA. Cấu trúc là ràng buộc, nên bài không đi lạc.

**4. Tự kiểm (quality gate).** Nó tự đọc lại bài của chính nó và soi: đủ độ dài chưa, có số liệu chưa, có bịa nguồn không, giọng có đúng của tôi không, có câu sáo rỗng không.

**5. Sửa.** Chỗ nào chưa đạt thì viết lại chỗ đó — không viết lại cả bài. Bước 4→5 có thể lặp vài lượt, tôi không thấy, tôi chỉ nhận bản đã đạt.

**6. Hình ảnh.** Tự sinh ảnh cover, tự đè tiêu đề và badge chủ đề lên, tự nén rồi gắn vào bài. Trước đây riêng khâu này tôi mất 15 phút mỗi bài trong Canva.

**7. Lưu memory.** Ghi chủ đề vừa dùng vào bộ nhớ để **lần sau không viết trùng** — đúng cái lỗi tôi từng mắc: đăng lại gần y nguyên một chủ đề cách nhau 3 tuần, có bạn đọc nhắn "bài này đăng rồi mà anh". Nhục. Từ khi có memory thì hết.

**8. Xuất bản + báo cáo.** Tự đẩy lên web, tự soạn kèm bản đăng Facebook / Zalo / YouTube, rồi nhắn tôi một tin gọn: xong bài gì, ảnh nào, hết bao nhiêu tiền.

Bước 4→5 là bước làm tôi tin agent nhất. Chatbot không bao giờ tự nói "bài này tôi viết chưa đạt, để tôi sửa". Agent thì có tiêu chuẩn nên nó dám tự trả bài của mình.

## Câu lệnh tôi giao (đúng kiểu giao việc cho người)

> "Mỗi 2 tiếng, kiểm tra hôm nay đã đủ 10 bài chưa. Chưa đủ thì: chọn 1 chủ đề chưa dùng, nghiên cứu tư liệu, viết bài 1.400–1.900 từ theo cấu trúc chuẩn (hook có số liệu → chatbot vs agent → quy trình → câu lệnh mẫu → kết quả đo → FAQ 3 câu → CTA), tự chấm chất lượng và sửa tới khi đạt, sinh cover kèm tiêu đề, lưu chủ đề đã dùng, đăng web, soạn thêm bản Facebook + Zalo + YouTube rồi báo cáo cho tôi. Không hỏi lại, tự quyết."

Để ý cách viết: tôi không đưa *nội dung*, tôi đưa **mục tiêu + tiêu chuẩn + điều kiện dừng**. Đó là cách giao việc cho một nhân sự, không phải cách ra lệnh cho một cái máy trả lời. Câu quan trọng nhất trong cả đoạn là *"tự chấm chất lượng và sửa tới khi đạt"* — nó biến một lượt trả lời thành một vòng lặp.

## Kết quả đo được

- **2 tiếng → 6 phút** máy chạy cho cùng khối lượng (1 bài + 3 bản social). Phần tôi làm còn lại: đọc và duyệt, khoảng 3 phút.
- **12 lượt chạy/ngày**, 24/7, kể cả 3 giờ sáng. Trước đây tôi ra được 2–3 bài/tuần là hết hơi.
- **0 bài trùng chủ đề** kể từ khi bật memory ghi lại chủ đề đã dùng.
- **1 khâu tôi cắt hẳn**: dựng ảnh cover thủ công, 15 phút/bài.

Điều tôi thấy giá trị nhất không phải con số 6 phút. Là chuyện tôi không còn phải **giữ quy trình trong đầu**. Trước đây mỗi lần ngồi viết, nửa năng lượng dùng để nhớ "làm gì tiếp". Giờ vòng lặp nằm trong agent, đầu tôi rảnh ra để nghĩ chuyện đáng nghĩ hơn: dạy gì, bán gì, đi đâu.

## FAQ

**Không biết code thì làm được vòng lặp này không?**
Được. Bạn viết câu lệnh bằng tiếng Việt như đoạn ở trên. Phần khó — chạy lệnh, ghi file, hẹn giờ — là việc của agent, không phải việc của bạn. Cái bạn cần học là *cách giao việc rõ ràng*, kỹ năng này giống quản lý người hơn giống lập trình.

**Agent tự chạy có sợ nó làm sai rồi đăng luôn không?**
Đây đúng là rủi ro thật, và câu trả lời là bước 4: quality gate. Bạn viết sẵn tiêu chuẩn (độ dài, phải có số liệu, không bịa nguồn, giọng ai), agent phải qua cửa đó mới được đăng. Muốn chắc hơn thì đặt chế độ "viết xong gửi tôi duyệt rồi mới đăng" — vẫn tiết kiệm gần hết thời gian.

**Vòng lặp này chỉ dùng cho viết blog thôi à?**
Không. Xương sống của nó là *mục tiêu → làm → tự kiểm → sửa → lưu → báo cáo*, nên lắp vào việc gì cũng được: mỗi sáng tổng hợp tin ngành, mỗi tối chốt số bán hàng gửi báo cáo, mỗi tuần soi feedback khách tìm lỗi lặp lại, mỗi tháng dựng bộ nội dung fanpage. Đổi mục tiêu, giữ nguyên vòng lặp.

---

Nếu bạn đang dùng AI theo kiểu hỏi–đáp từng lượt, bạn mới dùng chưa tới một phần mười sức của nó. Thứ đáng để bạn đầu tư thời gian không phải mẹo viết prompt hay hơn, mà là **giao được cả một quy trình** cho agent tự chạy.

👉 Bộ **Trợ Lý AI Hermes** đang mở bán sớm **239K** (giá gốc 499K) — hướng dẫn từng bước để bạn tự dựng vòng lặp tự động cho công việc của mình, kèm 3 kit tiện ích dùng được ngay: **https://speedreading.vn/shermes**
