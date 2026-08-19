---
title: "Cổng kiểm soát của Hermes: tại sao AI Agent tự soi lỗi trước khi giao bạn"
date: 2026-08-19
draft: false
description: "Chatbot viết xong là... thôi, bạn tự rà. Hermes (AI Agent) có 'cổng kiểm soát' (quality gate): tự soi 10 lỗi trước khi giao. Thực tế: 1 email sai tên đối tác đã bị chặn lại trước khi gửi. Wikipedia gọi ảo giác AI là 'thông tin sai trình bày như sự thật' — và OOPSLA 2026 vẫn đang nghiên cứu giảm nó. Đó là lý do nhân sự ảo phải có cổng."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-quality-gate.webp"
share_teaser: |
  Hỉ để ý một điểm làm nên 'hạng người' của Hermes: nó tự soi lỗi trước khi giao bạn. 🛡️
  ChatGPT trả lời xong bạn tự đọc tự sửa. Hermes thì tự check, tự vứt bản dở, đưa bạn bản sạch.
  Cái gọi là 'quality gate' — linh hồn của một AI Agent thật sự: tự vận hành chứ không chỉ 'nói'.
  👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai hay nhận 'rác' từ AI xem phát hiểu.
---

Tuần trước tôi suýt gửi một email "do AI viết" cho đối tác. Văn phong mượt, đoạn chốt đẹp, số liệu chèn đúng chỗ. Chỉ có một điều: nó ghi sai tên công ty đối tác — "Công ty Minh Anh" thành "Công ty Bình Anh". Một chữ. Nhưng nếu cái email đó bay vào hộp thư thật, tôi mất luôn cái uy tín xây cả năm.

Chatbot kiểu ChatGPT cũ sẽ trả lời xong và... thôi. Bạn tự đọc, tự phát hiện, tự sửa. Còn Hermes — AI Agent của tôi — nó có một cái tôi gọi là **"cổng kiểm soát"** (quality gate). Trước khi đẩy cái email đó ra ngoài, nó tự soi: sai tên chưa? sai số chưa? giọng có khớp brand chưa? Hỏng → vứt bản dở, viết lại. Chỉ khi sạch mới giao tôi.

Khác biệt nằm ở chữ **"tự"**. Đó là ranh giới giữa một cái máy "nói" và một nhân sự ảo "làm có trách nhiệm".

## Sự thật không vui: AI bịa rất tự nhiên

Tôi không nói suông. Ngay cả giới nghiên cứu đỉnh cũng thừa nhận điều này. Theo Wikipedia, **"ảo giác" (hallucination) trong AI là "phản hồi do AI sinh ra chứa thông tin sai hoặc gây hiểu lầm được trình bày như sự thật"**. Nghĩa là: AI bịa ra được, và trình bày cực kỳ tự nhiên — bạn đọc thoáng qua cứ tưởng đúng.

Chính vì thế, tại hội nghị **OOPSLA 2026**, một bài báo mang tên *"Reducing Hallucinations in LLM-Generated Code via Semantic Triangulation"* được chấp nhận — tức cả giới học thuật đỉnh cao vẫn đang vật lộn để **giảm** ảo giác. Ngoài thị trường, người ta xây hẳn "cổng" riêng: **Argot** (guardrail viết bằng Rust theo cấu trúc code của bạn), **hallucinatoff** (phần mềm chặn lúc AI nói lạc đề)... Tất cả đều làm một việc: **KIỂM SOÁT đầu ra trước khi thả ra**.

Hermes chỉ là đưa cái "cổng" đó vào *mọi lần chạy* — chứ không phải thảa bản thô ra khách rồi bảo "bạn tự rà nhé".

## Chatbot vs Agent — cùng "thông minh", khác hẳn "trách nhiệm"

Nhiều người tưởng ChatGPT là AI Agent. Không. Khác nhau ở một chỗ cốt lõi: **ai chịu trách nhiệm với bản cuối.**

- **Chatbot (ChatGPT kiểu cũ):** nó sinh văn bản. Xong. Bản đó đúng hay sai, lỗi hay sạch — bạn tự lo. Nó không có bước "soi lại". Nhanh, tiện, nhưng bạn là người sửa cuối cùng. Mỗi lần gửi đi là mỗi lần bạn đánh cược.
- **Hermes Agent:** nó sinh xong, tự đưa qua một vòng kiểm định (quality gate) trước khi giao. Sai → sửa. Dở → vứt. Chỉ bản đạt chuẩn mới ra mắt. Bạn nhận bản sạch, không phải bản thô.

Chatbot là "cây bút máy" — bạn cầm mới viết, viết xong bạn tự rà. Agent là "thư ký" — viết xong tự rà lại, gạch chỗ sai, đưa bạn bản sạch kèm ghi chú. Cùng một cây bút, khác hẳn người cầm.

## WOW: cái "cổng kiểm soát" nằm ở đâu trong quy trình (nhìn phát thấy)

Hermes chạy một vòng lặp **8 bước** mỗi lần được giao việc. Cổng kiểm soát nằm ở **bước 6** — ngay trước cửa deploy:

**Bước 1 — Nhận việc + đọc ngữ cảnh (memory):** nó nhớ giọng văn, brand, quyết định cũ của bạn, nên không viết lạc pha.
**Bước 2 — Research:** lấy số liệu thật (không bịa).
**Bước 3 — Viết bản thảo (draft).**
**Bước 4 — Sinh cover / chuẩn bị vật phẩm.**
**Bước 5 — Lên lịch + chuẩn bị deploy.**
**Bước 6 — QUALITY GATE (cổng kiểm soát):** tự soi 10 điểm — đúng mục tiêu chưa? đủ số liệu chưa? có bịa không? logic có mâu thuẫn không? giọng có khớp không? lỗi chính tả? phần thừa? rủi ro? ... Hỏng → quay bước 3 sửa, sửa xong mới qua.
**Bước 7 — Deploy:** chỉ khi bước 6 PASS mới đẩy lên web / gửi mail.
**Bước 8 — Báo cáo:** nhắn bạn kèm kết quả + chi phí.

Một ví dụ cụ thể cho dễ hình dung: sáng nay vòng lặp chạy, viết xong một đoạn giới thiệu khoá học. Bước 6 soi ra: "đoạn này ghi 'hoàn tiền 14 ngày' — sai với chính sách 7 ngày của website". Nó tự sửa thành 7 ngày rồi mới deploy. Bạn đọc bài không hề hay biết có một lỗi vừa bị gạt bỏ. **Đó là cái "người gác cổng" không thể qua mặt.**

Cái hay: bước 6 là chốt chặn cuối. Bản có lỗi → không bao giờ chạm tới khách. Đó là lý do tôi dám giao nó chạy **mỗi 2 tiếng (12 lần/ngày)** mà không sợ sáng ra web đầy bài rác.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes check. Tôi **quy định luôn trong câu lệnh giao việc** — y như dặn thư ký:

> *"Mỗi lần giao việc, viết xong phải tự kiểm tra chất lượng trước khi giao tôi: (1) đúng yêu cầu chưa, (2) có số liệu thật không, (3) có bịa không, (4) logic có mâu thuẫn không, (5) giọng có khớp brand không. Phát hiện lỗi → sửa, không được đẩy bản dở. Chỉ khi tự PASS 5 tiêu chí mới được deploy và báo cáo. Nếu không chắc → dừng, báo tôi kèm lỗi cụ thể."*

Một đoạn. Sau đó tôi đi uống cà phê. Nó tự viết, tự soi, tự sửa, tự giao bản sạch. Tôi không đụng tay giữa chừng.

## Kết quả đo lường (số thật, không vỗ ngực)

- **Tần suất kiểm soát:** 12 lần/ngày × 365 = **4.380 lượt quality gate/năm**. Mỗi lần chạy đều bị soi, kể cả lúc 03:00 sáng tôi đang ngủ.
- **Tỷ lệ "bài rác" lọt mạng:** tiến tới **0** — vì không bản nào qua được bước 6 khi còn lỗi. Thực tế: cái email sai tên "Minh Anh/Bình Anh" ở đầu bài chính là do cổng này chặn lại trước khi gửi.
- **Tiết kiệm:** trước kia mỗi bài tôi tự rà 15–20 phút. Với nhịp 10 bài/ngày là **2,5–3,3 tiếng/ngày (~1.000 tiếng/năm)** chỉ riêng khâu soi lỗi. Giờ: **0 phút**.
- **Quy mô:** một dự án AI agent thực tế từng "tiêu **200 tỷ token trong 1 tháng**" để decompile cả một tựa game (theo một bài trên HackerNews) — chứng tỏ agent làm việc thật ở quy mô lớn, và càng lớn càng **CẦN** cổng kiểm soát để không bừa bãi.

Điểm mấu chốt: quality gate không làm AI "thông minh hơn". Nó làm AI **đáng tin hơn**. Và với một nhân sự ảo bạn giao quyền gửi email, đăng bài, báo cáo khách — "đáng tin" mới là thứ bạn trả tiền.

## FAQ — 3 câu hỏi hay gặp

**1. Có cần biết code để có cổng kiểm soát không?**
Không. Trong khoá Nhân Sự Toàn Năng Hermes, bạn chỉ viết câu lệnh (prompt) quy định "phải check gì trước khi giao" — y như bạn dặn thư ký "gửi trước khi đọc lại 1 lần". Không một dòng code.

**2. Nếu nó tự check mà vẫn sót lỗi thì sao?**
Lúc đó nó báo tôi kèm lỗi cụ thể, chứ không tự ý đẩy bản dở lên. Tốt nhất: nó tự sửa. Xấu nhất: nó dừng và gọi tôi. Không bao giờ "lén" giao hàng lỗi rồi mặc kệ.

**3. ChatGPT có làm được quality gate không?**
ChatGPT có thể nhờ nó "check lại giúp tôi", nhưng **YOU phải nhớ nhắc**, và **YOU phải đọc kết quả**. Chatbot không tự chạy cổng này trước mỗi lần gửi. Agent thì có — đó là thiết kế, không phải may mắn. Chatbot là dụng cụ chờ bạn cầm. Agent là nhân sự tự gác cổng.

## Kết luận — đừng nhận "rác" từ AI nữa

Sự khác biệt giữa một chatbot và một AI Agent không nằm ở độ "thông minh" của câu trả lời. Nó nằm ở **trách nhiệm với bản cuối**. Chatbot nói xong là hết trách nhiệm. Agent có cổng kiểm soát — tự soi, tự sửa, tự chịu trách nhiệm trước khi giao bạn.

Wikipedia gọi ảo giác AI là "thông tin sai trình bày như sự thật". OOPSLA 2026 vẫn đang nghiên cứu giảm nó. Argot, hallucinatoff ra đời chỉ để chặn nó. Thế thì nhân sự ảo của bạn càng phải có cổng — chứ không thể thả bản thô ra khách rồi bảo "bạn tự rà nhé".

👉 Muốn tự dựng "nhân sự ảo" có cổng kiểm soát mà không cần biết code: khoá **Nhân Sự Toàn Năng Hermes** — 37 bài thực chiến, giá mở bán sớm **239K** (gốc 499K), hoàn tiền 7 ngày nếu thấy không hợp: https://speedreading.vn/shermes

Giao việc. Nhận bản sạch. Không rà tay.
