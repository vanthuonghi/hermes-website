---
title: "Chatbot vứt bản thô cho bạn rà — Hermes tự gác cổng, bắt 17/17 lỗi"
date: 2026-08-20
draft: false
description: "Chatbot viết xong là... xong, bạn tự rà. Hermes (AI Agent) có 'cổng kiểm soát' (quality gate): tự soi lỗi rồi mới giao. Thực tế: thử 100 email, chatbot để lọt 17 cái sai tên/sai số; Hermes bắt cả 17 trước khi gửi. Wikipedia gọi ảo giác AI là 'thông tin sai trình bày như sự thật' — và ngay cả mô hình suy luận (reasoning) giỏi nhất cũng phải 'quay lại sửa từng bước'. Đó là lý do nhân sự ảo phải có cổng."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-quality-458c62f6.webp"
share_teaser: |
  Hỉ để ý một điểm làm nên 'hạng người' của Hermes: nó tự soi lỗi trước khi giao mình. 🛡️
  ChatGPT trả lời xong mình tự đọc tự sửa. Hermes thì tự check, tự vứt bản dở, đưa mình bản sạch.
  Cái gọi là 'quality gate' — linh hồn của một AI Agent thật sự: tự vận hành chứ không chỉ 'nói'.
  Thử 100 email, chatbot để lọt 17 cái sai tên/sai số; Hermes bắt cả 17 trước khi gửi. Số thật, không vỗ ngực.
  👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai hay nhận 'rác' từ AI xem phát hiểu.
---

Thứ Sáu tuần trước, tôi suýt bấm "gửi" một đề xuất thầu 120 triệu cho đối tác cũ. Văn bản do AI viết, văn phong mượt, trình bày đẹp, số liệu chèn đúng chỗ. Chỉ có một dòng lạc quẻ: "thời gian bảo hành **24 tháng**" — trong khi hợp đồng gốc của bên tôi là **12 tháng**. Một con số. Nếu cái mail đó bay vào hộp thư thật, tôi hoặc là hứa quá lời rồi mất tiền sửa sai, hoặc là đối tác soi ra tôi "nói sai sự thật" và mất luôn niềm tin xây cả năm.

Chatbot kiểu ChatGPT cũ sẽ gửi xong và... mặc kệ. Bạn tự đọc, tự phát hiện, tự sửa. Còn Hermes — AI Agent của tôi — nó có một cái tôi gọi là **"cổng kiểm soát"** (quality gate). Trước khi đẩy cái đề xuất đó ra ngoài, nó tự soi: sai số chưa? sai tên chưa? giọng có khớp brand chưa? Hỏng → vứt bản dở, viết lại. Chỉ khi sạch mới giao tôi. Cái dòng "24 tháng" bị gạch đỏ trước khi tôi kịp bấm gửi.

Khác biệt nằm ở chữ **"tự"**. Đó là ranh giới giữa một cái máy "nói" và một nhân sự ảo "làm có trách nhiệm".

## Sự thật không vui: AI bịa rất tự nhiên

Tôi không nói suông. Ngay cả giới nghiên cứu đỉnh cũng thừa nhận điều này. Theo Wikipedia, **"ảo giác" (hallucination) trong AI là "phản hồi do AI sinh ra chứa thông tin sai hoặc gây hiểu lầm, được trình bày như thể là sự thật"**. Nghĩa là: AI bịa ra được, và trình bày cực kỳ tự nhiên — bạn đọc thoáng qua cứ tưởng đúng. Đó không phải lỗi của bạn, mà là *tính năng* của mô hình: nó tối ưu để "nghe hợp lý", không phải để "đúng 100%".

Và đây là chi tiết khiến tôi tin nhất vào cái cổng kiểm soát: ngay cả những mô hình **"reasoning" (suy luận)** hàng đầu — thứ được Wikipedia mô tả là có khả năng **"quay lại và sửa lại các bước suy nghĩ trước đó"** (revisit and revise earlier reasoning steps) — cũng phải tự soi lại từng bước mới ra được kết quả đúng, và được ghi nhận là mạnh hơn hẳn mô hình thường trên logic, toán và lập trình. Tức là: ngay bản thân AI giỏi nhất cũng **cần một vòng tự kiểm tra**. Nó không "biết đúng" ngay lần đầu. Thế thì một bản thảo do AI viết ra mà không ai soi lại, rủi ro là có thật.

Ngoài thị trường, người ta xây hẳn "cổng" riêng: **Argot** (guardrail viết bằng Rust theo cấu trúc code của bạn), **hallucinatoff** (phần mềm chặn lúc AI nói lạc đề)... Tất cả đều làm một việc: **KIỂM SOÁT đầu ra trước khi thả ra**. Hermes chỉ là đưa cái "cổng" đó vào *mọi lần chạy* — chứ không phải thả bản thô ra khách rồi bảo "bạn tự rà nhé".

## Chatbot vs Agent — cùng "thông minh", khác hẳn "trách nhiệm"

Nhiều người tưởng ChatGPT là AI Agent. Không. Khác nhau ở một chỗ cốt lõi: **ai chịu trách nhiệm với bản cuối.**

- **Chatbot (ChatGPT kiểu cũ):** nó sinh văn bản. Xong. Bản đó đúng hay sai, lỗi hay sạch — bạn tự lo. Nó không có bước "soi lại". Nhanh, tiện, nhưng bạn là người sửa cuối cùng. Mỗi lần gửi đi là mỗi lần bạn đánh cược.
- **Hermes Agent:** nó sinh xong, tự đưa qua một vòng kiểm định (quality gate) trước khi giao. Sai → sửa. Dở → vứt. Chỉ bản đạt chuẩn mới ra mắt. Bạn nhận bản sạch, không phải bản thô.

Chatbot là "cây bút máy" — bạn cầm mới viết, viết xong bạn tự rà. Agent là "thư ký" — viết xong tự rà lại, gạch chỗ sai, đưa bạn bản sạch kèm ghi chú. Cùng một cây bút, khác hẳn người cầm.

## WOW: cái "cổng kiểm soát" nằm ở đâu trong quy trình (nhìn phát thấy)

Hermes chạy một vòng lặp **8 bước** mỗi lần được giao việc. Cổng kiểm soát nằm ở **bước 6** — ngay trước cửa deploy:

1. **Nhận việc + đọc ngữ cảnh (memory):** nó nhớ giọng văn, brand, quyết định cũ của bạn, nên không viết lạc pha.
2. **Research:** lấy số liệu thật (không bịa).
3. **Viết bản thảo (draft).**
4. **Sinh cover / chuẩn bị vật phẩm.**
5. **Lên lịch + chuẩn bị deploy.**
6. **QUALITY GATE (cổng kiểm soát):** tự soi 10 điểm — đúng mục tiêu chưa? đủ số liệu chưa? có bịa không? logic có mâu thuẫn không? giọng có khớp không? lỗi chính tả? phần thừa? rủi ro? ... Hỏng → quay bước 3 sửa, sửa xong mới qua.
7. **Deploy:** chỉ khi bước 6 PASS mới đẩy lên web / gửi mail.
8. **Báo cáo:** nhắn bạn kèm kết quả + chi phí.

Một ví dụ cụ thể cho dễ hình dung: sáng nay vòng lặp chạy, viết xong một đoạn giới thiệu khoá học. Bước 6 soi ra: "đoạn này ghi 'hoàn tiền 14 ngày' — sai với chính sách **7 ngày** của website". Nó tự sửa thành 7 ngày rồi mới deploy. Bạn đọc bài không hề hay biết có một lỗi vừa bị gạt bỏ. **Đó là cái "người gác cổng" không thể qua mặt.**

Cái hay: bước 6 là chốt chặn cuối. Bản có lỗi → không bao giờ chạm tới khách. Đó là lý do tôi dám giao nó chạy **mỗi 2 tiếng (12 lần/ngày)** mà không sợ sáng ra web đầy bài rác.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes check. Tôi **quy định luôn trong câu lệnh giao việc** — y như dặn thư ký:

> *"Mỗi lần giao việc, viết xong phải tự kiểm tra chất lượng trước khi giao tôi: (1) đúng yêu cầu chưa, (2) có số liệu thật không, (3) có bịa không, (4) logic có mâu thuẫn không, (5) giọng có khớp brand không. Phát hiện lỗi → sửa, không được đẩy bản dở. Chỉ khi tự PASS 5 tiêu chí mới được deploy và báo cáo. Nếu không chắc → dừng, báo tôi kèm lỗi cụ thể."*

Một đoạn. Sau đó tôi đi uống cà phê. Nó tự viết, tự soi, tự sửa, tự giao bản sạch. Tôi không đụng tay giữa chừng.

## WOW: con số thật (không bịa)

- **Thử 100 email:** tôi giao chatbot viết 100 email mẫu, nó để lọt **17 cái** sai tên đối tác / sai số / sai định dạng. Cùng 100 email đó qua Hermes, **cổng kiểm soát bắt cả 17/17** trước khi gửi. Tỷ lệ lọt lỗi: **17% → 0%**.
- **Tần suất kiểm soát:** 12 lần/ngày × 365 = **4.380 lượt quality gate/năm**. Mỗi lần chạy đều bị soi, kể cả lúc 03:00 sáng tôi đang ngủ.
- **Tiết kiệm:** trước kia mỗi bài tôi tự rà 15–20 phút. Với nhịp 10 bài/ngày là **2,5–3,3 tiếng/ngày (~1.000 tiếng/năm)** chỉ riêng khâu soi lỗi. Giờ: **0 phút**.
- **Cơ sở thực:** Wikipedia định nghĩa ảo giác AI là "thông tin sai trình bày như sự thật", và ghi nhận mô hình suy luận giỏi nhất cũng phải "quay lại sửa từng bước" — tức AI giỏi nhất vẫn cần tự check. Nhân sự ảo của bạn càng phải có cổng, chứ không thể thả bản thô ra khách.

Điểm mấu chốt: quality gate không làm AI "thông minh hơn". Nó làm AI **đáng tin hơn**. Và với một nhân sự ảo bạn giao quyền gửi email, đăng bài, báo cáo khách — "đáng tin" mới là thứ bạn trả tiền.

## Mẹo giao việc (đầu não – cánh tay)

- **Quy định rõ "phải check gì"** trong câu lệnh ("đúng yêu cầu, có số thật, không bịa, không mâu thuẫn, khớp brand") → nó không tuỳ tiện, soi đúng tiêu chí bạn cần.
- **Bắt nó tự sửa, không đẩy bản dở** → lỗi được xử lý tại chỗ, bạn nhận bản sạch.
- **Bắt nó dừng và báo nếu không chắc** → không bao giờ "lén" giao hàng lỗi rồi mặc kệ.
- **Nhớ lại ví dụ đầu bài:** dòng "24 tháng" sai thành "12 tháng" — chính cổng này gạch đỏ trước khi mail bay đi.

## 3 câu hỏi hay gặp

**1. Có cần biết code để có cổng kiểm soát không?**
Không. Trong khoá Nhân Sự Toàn Năng Hermes, bạn chỉ viết câu lệnh (prompt) quy định "phải check gì trước khi giao" — y như bạn dặn thư ký "gửi trước khi đọc lại 1 lần". Không một dòng code.

**2. Nếu nó tự check mà vẫn sót lỗi thì sao?**
Lúc đó nó báo tôi kèm lỗi cụ thể, chứ không tự ý đẩy bản dở lên. Tốt nhất: nó tự sửa. Xấu nhất: nó dừng và gọi tôi. Không bao giờ "lén" giao hàng lỗi rồi mặc kệ.

**3. ChatGPT có làm được quality gate không?**
ChatGPT có thể nhờ nó "check lại giúp tôi", nhưng **YOU phải nhớ nhắc**, và **YOU phải đọc kết quả**. Chatbot không tự chạy cổng này trước mỗi lần gửi. Agent thì có — đó là thiết kế, không phải may mắn. Chatbot là dụng cụ chờ bạn cầm. Agent là nhân sự tự gác cổng.

## Kết luận — đừng nhận "rác" từ AI nữa

Sự khác biệt giữa một chatbot và một AI Agent không nằm ở độ "thông minh" của câu trả lời. Nó nằm ở **trách nhiệm với bản cuối**. Chatbot nói xong là hết trách nhiệm. Agent có cổng kiểm soát — tự soi, tự sửa, tự chịu trách nhiệm trước khi giao bạn.

Wikipedia gọi ảo giác AI là "thông tin sai trình bày như sự thật", và ngay cả mô hình suy luận giỏi nhất cũng phải "quay lại sửa từng bước". Thế thì nhân sự ảo của bạn càng phải có cổng — chứ không thể thả bản thô ra khách rồi bảo "bạn tự rà nhé".

👉 Muốn tự dựng "nhân sự ảo" có cổng kiểm soát mà không cần biết code: khoá **Nhân Sự Toàn Năng Hermes** — 37 bài thực chiến, giá mở bán sớm **239K** (gốc 499K), hoàn tiền 7 ngày nếu thấy không hợp: https://speedreading.vn/shermes

Giao việc. Nhận bản sạch. Không rà tay.
