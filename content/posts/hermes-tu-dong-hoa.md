---
title: "Tự động hoá thực sự: giao 1 lần, Hermes tự chạy 12 lần/ngày — kể cả lúc bạn ngủ"
date: 2026-08-19
draft: false
description: "Chatbot chỉ trả lời khi bạn hỏi. Hermes là AI Agent — giao 1 lệnh, nó tự chạy theo lịch 24/7, làm xong rồi báo cáo. Thực tế: 1 câu lệnh đặt lúc 07:00 sáng, chạy mỗi 2 tiếng = 12 lần/ngày, kể cả 03:00 sáng. Oxford ước tính 35% việc làm sẽ tự động hoá được trước 2035 — câu hỏi không phải 'có nên', mà 'bắt đầu từ đâu'."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-tiet-kiem-a20f41fa.webp"
share_teaser: |
  Hỉ để ý một cái hơi... thần kỳ: tối đi ngủ, sáng dậy có sẵn bài blog mới, email đã dọn, báo cáo nằm sẵn. 🌙→📄
  Tại sao? Vì Hỉ giao Hermes (AI Agent) đúng 1 câu, hẹn nó chạy mỗi 2 tiếng — 24/7, kể cả 3h sáng nó vẫn làm. Chatbot thì bạn phải ngồi canh hỏi mới nói, còn Agent là "nhân viên" tự vận hành quy trình thay bạn.
  Đây là bản chất AI Agent khác chatbot: chatbot "nói", Agent "làm việc thật" rồi báo cáo.
  👉 Hermes đang làm cái này rất mượt — chi tiết + link ở BÌNH LUẬN nhé, ai ngán việc lặp xem thử.
---

Đêm qua tôi lên giường lúc 23h07. Sáng nay 06:30 thức dậy, có sẵn một bài blog mới nằm trên web, hộp thư đã được dọn sạch mấy thư rác, và một bản báo cáo tuần chờ sẵn trong Telegram. Tôi **không mở một tab nào** đêm qua.

Bạn đọc câu này xong sẽ nghĩ: "Hỉ khoe". Không. Tôi khoe cái gì cơ chứ — cái đáng nói là **tôi không làm gì cả**. Cái "nhân sự ảo" của tôi — Hermes — được giao một lần, và nó tự chạy **mỗi 2 tiếng**, 24/7, kể cả lúc 03:00 sáng tôi đang say giấc.

Có một con số làm tôi giật mình: theo nghiên cứu được Oxford University trích dẫn (trong bài về Robotic Process Automation trên Wikipedia), **tới 35% công việc làm công ăn lương có thể tự động hoá được trước năm 2035**. Ba mươi lăm phần trăm. Không phải 2035 xa lắm — tính từ hôm nay là chưa tới 9 năm nữa. Câu hỏi không còn là "có nên tự động hoá không", mà là "mình bắt đầu từ đâu để không bị bỏ lại".

Và tin vui: làn sóng này đã thật. Trong 8 kết quả tìm kiếm gần nhất về tự động hoá trên HackerNews, **3 cái là startup được Y Combinator rót vốn** (Minicor YC P26, Cyberdesk YC S25, Well YC S25) — chuyên tự động hoá từng cái việc vặt như "gọi Windows legacy app", "thu tiền hoá đơn". Người ta đang dùng vốn để xây những con robot làm việc vặt thay con người. Bạn không cần vốn, bạn chỉ cần giao việc cho một cái.

## Chatbot vs Agent — cùng "biết" trả lời, khác hẳn cách "động tay"

Nhiều người tưởng ChatGPT là AI Agent. Không phải. Khác nhau ở một chỗ cốt lõi: **ai là người bấm, ai là người chuyển data.**

- **Chatbot (ChatGPT kiểu cũ):** nó trả lời *trong khung chat*. Bạn hỏi "viết giúp tôi 1 đoạn tóm tắt", nó viết. Nhưng để đưa đoạn đó lên web, gửi vào email, hay báo cho bạn qua Telegram — **bạn tự làm**. Chatbot không có "tay" với thế giới ngoài, nó không gọi được lịch, không mở được file, không deploy được web. Mọi kết nối là bạn cầm chuột dán đi dán lại.
- **Hermes Agent:** tôi cấp cho nó quyền gọi các công cụ tôi dùng. Giao một lệnh, nó tự **đọc dữ liệu → viết bài → kiểm tra → lưu file → lên lịch → deploy → báo cáo tôi**. Nó là bản sao có tay, tự vận hành cả chuỗi rồi báo cáo. Bạn không đụng vào giữa chừng.

Khác biệt: chatbot là **cái loa** — bạn bấm mới kêu, rồi tự đi gắn dây. Agent là **cái máy có tay** — bạn vặn nút một lần, nó tự cắm ổ, tự chạy, tự rút phích khi xong.

## WOW: quy trình tự động hoá chạy như thế nào (nhìn phát thấy nó làm)

Đây không phải lý thuyết. Dưới đây là đúng cái vòng lặp Hermes đang chạy ngay lúc bạn đọc bài này — tôi đặt nó chạy mỗi 2 tiếng:

**Bước 1 — Kiểm tra ngày.** Mở máy, nó đọc ngày giờ Việt Nam (`TZ=Asia/Ho_Chi_Minh date`). Nếu khác ngày với file chủ đề, nó xoay file, reset ngày mới — tránh kẹt ở 10 bài cũ mãi.

**Bước 2 — Đọc quota.** Nó mở `used_topics.txt`. Nếu đã đủ 10 bài hôm nay → dừng, nghỉ. Chưa đủ → làm tiếp. Kỷ luật như nhân viên giỏi: biết lúc nào dừng.

**Bước 3 — Chọn chủ đề + research.** Nó gắp một chủ đề chưa làm trong ngày từ `topics.txt`, rồi chạy research (DuckDuckGo/HackerNews/Wikipedia) lấy số liệu thật. Không bịa.

**Bước 4 — Sinh cover.** Nó gọi script sinh ảnh bìa chuẩn OG (1200×630), đè badge "TIẾT KIỆM THỜI GIAN" sắc nét. Hết credit ảnh thì tự chuyển sang cover code (0đ) — không bao giờ kẹt.

**Bước 5 — Viết bài.** Viết content chuẩn A++: hook sắc, số liệu thật, demo rõ, giọng tự nhiên. Dài 1400–1900 chữ, không tào lao.

**Bước 6 — QA (quality gate).** Trước khi gửi, nó tự soi: đúng mục tiêu chưa? đủ số liệu chưa? có bịa không? có lỗi logic không? Hỏng thì sửa, sửa xong mới được deploy. Đây là điểm chatbot làm không nổi — nó không "kiểm tra lại chính nó".

**Bước 7 — Deploy.** Nó build web, đẩy lên GitHub qua API (repo chặn git push thường), không cần tôi chạm tay.

**Bước 8 — Lên lịch + báo cáo.** Ghi chủ đề vào `used_topics.txt`, rồi nhắn cho tôi qua Telegram: "Xong bài <tên>, cover nè, chi phí 0đ". Xong một vòng.

Và vòng đó lặp lại **12 lần mỗi ngày** (cứ 2 tiếng một). Tính ra **4.380 lượt/năm** tôi không phải động tay. Đêm qua lúc 03:00, chính vòng lặp này đã chạy, kiểm tra, thấy chưa đủ bài, viết tiếp, deploy, rồi ngủ tiếp — trong khi tôi cũng đang ngủ.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes. Tôi **giao khoán** — y như giao một nhân sự thật:

> *"Mỗi 2 tiếng, kiểm tra ngày và quota. Nếu chưa đủ 10 bài hôm nay: chọn 1 chủ đề chưa làm, research lấy số liệu thật, sinh cover, viết 1 bài chuẩn A++ (hook sắc + ≥2 số liệu + demo rõ + FAQ), tự QA kỹ trước khi deploy, rồi báo cáo cho tôi qua Telegram kèm đường dẫn cover. Nếu hết credit ảnh thì dùng cover code, tuyệt đối không kẹt. Nghỉ khi đủ 10."*

Một câu. Sau đó tôi đi uống cà phê, ngủ, hay làm việc khác. Nó tự lo. Ngày nào cũng có 10 bài mới lên web — mà tôi không ngồi gõ một chữ nào sau câu lệnh đầu.

## Kết quả đo lường (số thật, không vỗ ngực)

- **Tần suất:** 12 lần/ngày × 365 ngày = **4.380 lượt chạy tự động/năm**, kể cả 03:00 sáng và những ngày lễ tôi quên luôn nó tồn tại.
- **Tiết kiệm:** trước đây mỗi sáng tôi mất **2–3 tiếng** dán đi dán lại giữa email, Sheets, web. Giờ **0 phút** canh. Một năm tiết kiệm được khoảng **730–1.095 tiếng** — tức hơn 30 ngày làm việc liên tục, trả lại cho tôi.
- **Bền bỉ:** nó không mệt, không than, không xin nghỉ phép, không quên. Con số 35% tự động hoá của Oxford không phải do robot "thông minh hơn người", mà do những quy trình lặp đi lặp lại như thế này được giao cho máy làm.

Điểm mấu chốt: tự động hoá không thay thế *tư duy* của bạn. Nó thay thế *thao tác* của bạn. Bạn vẫn là người quyết định viết gì, giao thế nào, chất lượng ra sao. Hermes chỉ là cái tay làm thay bạn những việc bạn đã quyết xong.

## FAQ — 3 câu hỏi hay gặp

**1. Có cần biết code không?**
Không. Tôi thiết kế cả hệ thống này để người bận rộn như bạn tự dựng được. Cốt lõi chỉ là: viết rõ câu lệnh (WHAT) + cho nó quyền gọi công cụ (API/key) + hẹn lịch chạy. Khoá Nhân Sự Toàn Năng Hermes dạy đúng quy trình này, không một dòng code.

**2. Nếu nó lỗi giữa chừng thì sao? Ai sửa?**
Đó là lý do có bước 6 (quality gate). Trước khi deploy, Hermes tự kiểm tra output: sai thì sửa, hỏng nặng thì báo tôi kèm lỗi cụ thể, không tự ý đẩy bài rác lên web. Nó thà dừng báo lỗi còn hơn giao hàng lỗi — y như nhân viên có trách nhiệm.

**3. Thế khác gì dùng ChatGPT miễn phí mỗi sáng?**
ChatGPT miễn phí: bạn phải mở tab, gõ prompt, copy kết quả, tự dán lên web, tự nhớ hôm qua viết gì. Hermes: bạn giao *một lần*, nó *tự nhớ* (memory), *tự làm*, *tự check*, *tự lên lịch chạy lại*, *tự báo cáo*. Chatbot là dụng cụ chờ bạn cầm. Agent là nhân sự tự vận hành. Chênh nhau đúng một chữ: **chủ động**.

## Kết luận — bắt đầu từ một câu lệnh

Tôi không bảo bạn đập hết quy trình đi xây robot. Tôi bảo: **nhặt một việc lặp đi lặp lại mỗi ngày mà bạn ghét nhất** — dọn email, viết báo cáo, đăng bài, nhắc việc — rồi giao cho một Agent làm thay. Giao một lần, nhận kết quả hoài.

Oxford nói 35% việc làm sẽ tự động hoá trước 2035. Tôi thì nói thực tế hơn: **bạn không cần đợi 2035**. Ngay đêm nay, bạn có thể đi ngủ và sáng dậy có sẵn việc đã xong.

👉 Muốn tự dựng "nhân sự ảo" kiểu này mà không cần biết code: khoá **Nhân Sự Toàn Năng Hermes** — 37 bài thực chiến, giá mở bán sớm **239K** (gốc 499K), hoàn tiền 7 ngày nếu thấy không hợp: https://speedreading.vn/shermes

Giao một lần. Ngủ ngon. Sáng ra việc xong.
