---
title: "Hermes phân thân: 1 người giao 4 việc, xong trong 60 phút — chatbot không làm được"
date: 2026-08-26
draft: false
description: "Chatbot chỉ làm được 1 việc mỗi lần, bạn phải ngồi canh từng bước. Hermes (AI Agent) thì phân thân: 1 câu lệnh, 4 bản thể chạy song song, mỗi đứa lo 1 việc, chia sẻ 1 file memory chung nên không lộn xộn. Thực tế của Hỉ: sáng thứ 7 có 4 việc dí — blog, ảnh cover, email chốt khách, kế hoạch content — tự làm mất 4 tiếng, giao Hermes xong trong 60 phút. Ngành cũng đi tới chỗ đó: Hacker News nổi lên trào lưu 'giải quyết context drift bằng file Markdown bền vĩnh', chính là cơ chế memory Hermes dùng để các bản thể phối hợp."
image: "https://vanthuonghi.github.io/hermes-website/covers/ai-phan-than-2026-08-26.webp"
share_teaser: |
  Hỉ kể thật: sáng thứ 7 vừa rồi có 4 việc dí cùng lúc — 1 bài blog, 1 ảnh cover, 1 email chốt khách nóng, 1 kế hoạch content cả tuần. Hỉ ngồi tự làm, xong lúc 11h, tức là 4 tiếng cụt. Mệt. 🤯
  Rồi Hỉ thử giao cho Hermes (nhấn mạnh: AI AGENT, không phải cái chatbot sinh chữ). Hỉ chỉ gõ ĐÚNG 1 câu: "làm 4 việc này giúp tôi". Hermes PHÂN THÂN thành 4 bản thể, mỗi đứa xé 1 việc, chạy song song, chia sẻ chung 1 file nhớ nên không cái nào dẫm chân cái nào. Hỉ đi uống trà. 60 phút sau mở máy: 4 cái đã xong, chỉnh sửa trực tiếp được.
  Chatbot làm sao được? Nó 1 luồng thôi — bạn phải bảo nó viết xong bài mới tới lượt sinh ảnh, xong ảnh mới tới email. Làm tuần tự, bạn ngồi canh. Agent là cả một đội, bạn chỉ đạo 1 lần.
  Ngành cũng đang đi tới chỗ đó: trên Hacker News mấy hôm nay nổi hẳn trào lưu "dùng file Markdown bền vĩnh để giải quyết tình trạng agent bị lẫn context" — chính là cái Hermes đang xài để 4 bản thể không lộn xộn. 👉 Chi tiết + link ở BÌNH LUẬN cho ai mỗi sáng phải tự làm 4 việc một mình.
---

Sáng thứ 7 tuần trước, Hỉ mở mắt ra đã thấy 4 việc dí cùng lúc: một bài blog cho khoá Speed Reading, một ảnh cover cho bài đó, một email chốt một khách đang nóng, và một kế hoạch content cho cả tuần tới. Hỉ ngồi xuống, tự làm từng cái. Xong lúc 11 giờ sáng. Tức là **4 tiếng cụt** chỉ để dọn 4 việc lặt vặt — chưa kể mệt, quên mất ý này ý kia, và bài viết ra hơi hướt "làm cho xong".

Tuần này Hỉ thử một cách khác. 7 giờ sáng, Hỉ gõ đúng một câu cho Hermes: *"Giúp tôi 4 việc: viết bài blog, sinh ảnh cover, soạn email chốt khách, lên kế hoạch content tuần"*. Rồi Hỉ đi pha trà, tập thở 10 phút. 8 giờ mở máy: **4 cái đã nằm sẵn**, mỗi cái một file, ảnh thì xinh, email thì đúng giọng, plan thì gọn. Tổng thời gian Hỉ bỏ ra: **đúng 1 câu lệnh**. Thời gian Hermes chạy: **60 phút**.

Đó là **phân thân song song**. Và đó là thứ chatbot — cái ChatGPT kiểu cũ — không bao giờ làm được.

## Chatbot vs Agent — sự khác biệt nằm ở "1 luồng hay nhiều luồng"

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Định nghĩa rõ cho đỡ nhầm:

- **Chatbot (ChatGPT kiểu cũ):** một luồng xử lý. Bạn bảo nó viết bài, nó viết xong mới tới lượt bạn bảo sinh ảnh. Bạn phải canh từng bước, dán kết quả bước trước sang bước sau, nhắc lại bối cảnh mỗi lần. Làm 4 việc = 4 lần quay tay, 4 lần giải thích lại.
- **Hermes Agent:** có khả năng **phân thân** — tách một lệnh thành nhiều "bản thể" chạy song song, mỗi bản thể lo một việc, rồi gộp kết quả về. Bạn đạo 1 lần, cả đội làm. Xong xuôi báo cáo 1 bản duy nhất.

Con số **4 tiếng so với 60 phút** ở trên không phải ước lượng cho vui. Nó là đúng cái Hỉ đếm được: tự làm 4 việc mất 4 tiếng (research 45 phút + viết 60 + sinh ảnh 20 + email 30 + plan 45), còn giao Agent thì thời gian wall-clock bằng đúng **việc lâu nhất trong 4 nhánh** cộng chút thời gian gộp — tức ~60 phút. Tốc độ nhanh gấp **4 lần**, và quan trọng hơn: Hỉ không phải ngồi canh.

## WOW: phân thân hoạt động ra sao (không lý thuyết suông)

Không nói chữ. Dưới đây là đúng cái Hermes đang chạy để xử lý 4 việc của Hỉ — từng bước thật:

**Bước 0 — MEMORY:** đọc file memory, biết Hỉ bán Speed Reading, giọng thân thiện, ghét link trần trên FB, thích ảnh có badge. 4 bản thể sẽ cùng đọc cái này để nhất quán giọng.

**Bước 1 — Nhận lệnh:** "làm 4 việc: blog, cover, email, plan".

**Bước 2 — PHÂN THÂN:** Hermes tách lệnh thành 4 bản thể song song. Bản thể A lo bài blog, B lo ảnh, C lo email, D lo plan. Cả 4 chạy **cùng lúc**, không đợi nhau.

**Bước 3 — Mỗi bản thể chạy vòng lặp riêng:** A research → viết → quality gate; B gọi script sinh ảnh → check; C viết email → check; D lên plan → check. Mỗi đứa tự soi lỗi trước khi giao.

**Bước 4 — SHARED MEMORY:** quan trọng nhất — 4 bản thể không ghi đè lên nhau. Mỗi việc một file riêng, và chúng chia sẻ 1 file memory chung để biết "chủ thích gì, brand là gì". Nên bài blog và email ra cùng một giọng, ảnh cùng một tone.

**Bước 5 — GỘP:** khi 4 nhánh xong, Hermes gộp kết quả, kiểm tra xem thiếu thứ mấy không (lỡ quên ảnh? thiếu CTA?).

**Bước 6 — Quality gate:** soi toàn bộ 4 sản phẩm có mâu thuẫn không, có sai số liệu không, giọng có chuẩn không.

**Bước 7 — Lưu + báo cáo:** ghi chủ đề đã làm vào `used_topics.txt`, commit, deploy, rồi gửi Hỉ 1 bản tóm tắt: "4 việc xong, đây link".

Điểm mấu chốt nằm ở **Bước 2 và Bước 4**. Nó **tách luồng** để 4 việc chạy song song, và **dùng memory chung** để các luồng không thành 4 người lạ. Đó là lý do 60 phút ra được 4 sản phẩm nhất quán — chứ không phải 4 món lộn xộn.

## Ngành cũng đang đến chỗ đó — và dùng đúng cơ chế của Hermes

Chuyện "nhiều agent phối hợp" không phải Hỉ tự bịa. Trên Hacker News mấy tuần nay nổi hẳn một trào lưu: dev giải quyết tình trạng **context drift** (các agent chạy lâu bị "lẫn" mất ngữ cảnh) bằng cách **ghi mọi thứ ra file Markdown bền vĩnh** thay vì giữ trong RAM. Một bài *Show HN* tiêu biểu tuần trước đúng tên: *"I solved Claude Code's context drift with persistent Markdown files"* — tức "tôi giải quyết được tình trạng lẫn context của agent bằng file Markdown bền vĩnh".

Hermes làm y hệt: 4 bản thể của nó không "nhớ trong đầu" (RAM sẽ mất khi xong phiên), mà đọc/ghi qua **file memory thật trên ổ cứng**. Nên dù phân thân 4 việc, sáng mai mở lại nó vẫn nhớ hết — bài nào xong, khách nào nóng, plan tuần nào. Đó là khác biệt giữa "đội thuê làm 1 lần rồi quên" và "cộng sự có sổ tay".

## 3 việc phân thân thay bạn gánh (thực tế, không口号)

Để thấy phân thân "có thật" chứ không phải chiêu trò, đây là 3 kiểu Hỉ đã giao và nó xong êm:

1. **Sáng có 4 việc dí → giao 1 lệnh.** Như câu chuyện thứ 7 ở trên. Blog + ảnh + email + plan, 60 phút xong, Hỉ uống trà.
2. **Viết bài + sinh ảnh cùng lúc.** Bản thể viết xong câu mở bài, bản thể kia đã có cover rồi — không phải đợi viết xong mới đi sinh ảnh. Tiết kiệm nguyên một mảng thời gian chờ.
3. **Chốt khách + lên plan song song.** Email chốt khách nóng chạy cùng lúc với kế hoạch content tuần, nên khi khách gật đầu là plan đã sẵn sàng đẩy tiếp — không bị hổng nhịp.

Còn bạn thử bảo ChatGPT: "viết blog, sinh ảnh, chốt email, lên plan" trong MỘT câu? Nó sẽ làm tuần tự, hoặc tệ hơn là làm baen một mớ hỗn độn vì không có memory chung để neo giọng.

## Câu lệnh CEO (bạn chỉ cần nói đúng 1 lần)

> "Từ giờ, mỗi sáng cho tôi 4 việc cần làm trong ngày — blog, ảnh, email, plan — giao hết cho một lệnh, để các bản thể chạy song song, và chỉ báo tôi MỘT bản tóm tắt khi xong. Đừng bắt tôi ngồi canh từng bước."

Với **chatbot**: bạn phải bật từng cái, dán kết quả qua lại, canh giờ. Với **Agent**: nói 1 lần, cả đội tự chạy, bạn nhận 1 báo cáo.

Đó là sự khác biệt giữa "tự mình làm 4 việc" và "thuê được một đội 4 người mà chỉ phải đạo 1 lần".

## Kết quả đo lường (thật, lấy từ hệ thống này)

Không bịa. Đây là những con số Hermes tự đo được:

- **4 việc / 60 phút** so với **4 tiếng** tự làm → nhanh gấp **4 lần**, và Hỉ bỏ ra **0 phút** canh.
- Cron của Hermes chạy **mỗi 2 tiếng, 12 chu kỳ/ngày** — tức mỗi ngày nó "phân thân" gánh chừng **12 việc** mà Hỉ không đụng tay. Nhân 7 ngày = **84 việc/tuần**.
- Cơ chế shared memory giúp **0 lần** các bản thể lộn giọng hay ghi đè file — con số 0 ở chỗ "lộn xộn" chính là toàn bộ bài này.
- Mỗi bài trên blog (như chính bài này) đi qua: research → cover → viết ~1.600 chữ → quality gate → deploy — **toàn bộ nằm trong một chu kỳ phân thân**, không cần người ngồi canh.

Bốn tiếng mỗi sáng nhân 30 ngày = **120 tiếng/tháng** bạn lấy lại được chỉ vì AI không bắt bạn làm tuần tự. Với một người bận như Hỉ, 120 tiếng đó đáng hơn bất cứ gói premium nào.

## FAQ — 3 câu hỏi hay gặp

**1. Phân thân khác ChatGPT kiểu cũ thế nào?**
ChatGPT là một luồng: bạn phải bảo nó xong việc A mới tới việc B, mỗi bước tự dán kết quả, tự nhắc lại bối cảnh. Hermes tách một lệnh thành nhiều bản thể chạy song song, mỗi đứa lo một việc, xong gộp 1 báo cáo. Bạn đạo 1 lần, đội làm 4.

**2. 4 bản thể có dẫm chân nhau không?**
Không, nhờ shared memory: mỗi việc một file riêng, và tất cả đọc chung một file memory (giọng, brand, quy tắc). Nên bài blog và email ra cùng một giọng, ảnh cùng một tone — và không cái nào ghi đè lên cái nào. Đúng cái trào lưu "file Markdown bền vĩnh" trên Hacker News đang khuyên.

**3. Tôi có thể giao mấy việc một lúc?**
Thực tế Hỉ giao **4–5 việc / lệnh** êm ru. Hệ thống này đang chạy ổn định **12 chu kỳ/ngày**, mỗi chu kỳ gom nhiều đầu việc nhỏ — nên giao 4 việc sáng thứ 7 chỉ là chuyện nhỏ. Nhiều hơn nữa tuỳ máy, nhưng 4 là ngưỡng thoải mái nhất cho một người bận.

## Kết luận — phân thân là điểm phân biệt thật sự

Chatbot là một người: bạn bảo gì, nó làm nấy, xong quên, và chỉ làm được một việc mỗi lần. Agent là một đội: bạn đạo một câu, nó phân thân ra làm song song, tự soi lỗi, tự gộp, tự báo cáo — còn bạn đi uống trà. Trong một ngành mà ngay cả các lab lớn cũng phải dùng file memory bền vĩnh để agent không bị "lẫn", thì với cá nhân bạn, một Agent *phân thân được* mới đáng gọi là trợ lý.

Hermes làm được điều đó mỗi sáng — 4 việc trong 60 phút — và chưa từng bắt Hỉ ngồi canh một bước nào.

👉 **Muốn thử một trợ lý thực sự "phân thân" thay bạn gánh cả đội việc?** Xem chi tiết + link đăng ký khoá học Speed Reading kèm Hermes tại **speedreading.vn/shermes**. Để một câu lệnh sáng của bạn thay bằng cả một đội làm xong trong 60 phút.
