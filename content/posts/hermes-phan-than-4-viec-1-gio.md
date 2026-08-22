---
title: "Hermes phân thân: giao 1 người 4 việc, Agent xong trong 1 giờ"
date: 2026-08-22
draft: false
description: "Chatbot trả lời 1 lượt rồi đứng im. AI Agent phân thân: 1 câu lệnh, 4 việc chạy song song, xong trong 1 giờ thay vì 2 ngày bạn xoay. Bài mổ xẻ cách Hermes mở 4 luồng, mỗi luồng tự chạy vòng lặp 8 bước rồi báo cáo."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-phan-than-629bbe79.webp"
share_teaser: |
  Hỉ thú nhận: hồi đầu dùng AI, mình cũng cậy nó như cái máy trả lời. Hỏi gì — nhận đoạn — rồi tự copy, tự sửa, tự đăng. 4 việc là ngồi xoay 2 ngày. 😅
  Sự khác mình mới ngộ ra: Chatbot (kiểu ChatGPT) trả lời 1 câu rồi ĐỨNG IM chờ bạn gõ tiếp. Còn AI Agent (Hermes) PHÂN THÂN: giao 1 lần 4 việc, nó mở 4 luồng chạy SONG SONG, mỗi luồng tự tìm → tự làm → tự soi lỗi → tự báo cáo. Mình đi ăn trưa, 1 tiếng sau nhận lại 4 cái đã xong.
  Hôm nay mình ghi rõ: 4 việc gì, giao câu lệnh ra sao, máy chạy những bước nào — chi tiết + link mình để ở BÌNH LUẬN nhé. Ai hay "1 mình cùm 4 việc" thì đọc, đỡ được cả ngày.
---

Tháng trước tôi nhận cùng lúc bốn việc: viết một bài đăng Facebook, soi hàng chục feedback khách hàng để tìm lỗi lặp lại, lên lịch đăng nguyên một tuần cho fanpage, và đọc tóm tắt một hợp đồng bốn mươi trang. Tôi làm tay. Kết quả: mất hai ngày, vẫn sót một việc, bài đăng nhầm khung giờ, và đến hôm sau tôi không nhớ nổi cái hợp đồng đó bảo gì.

Tại sao hai ngày? Vì tôi làm tuần tự. Sáng viết bài, trưa soi feedback, chiều lên lịch, tối mở hợp đồng — mà tối đó mệt nên bỏ ngang. Ngày hôm sau hợp đồng vẫn còn đó. Bốn việc chẳng lớn, nhưng cái "chuyển ngữ cảnh" giữa chúng mới là thứ ngốn thời gian: mỗi lần quay lại một việc, tôi phải đọc lại cái tôi đã làm để nhớ mình đang ở đâu.

Hôm nay tôi giao y hệt bốn việc đó cho Hermes — một câu lệnh duy nhất. Một tiếng sau tôi nhận lại bốn cái đã xong, mỗi cái kèm một dòng báo cáo ngắn. Tôi đi ăn trưa. Không mở máy tính lần nào.

Cái làm tôi bất ngờ không phải tốc độ. Là chuyện tôi không phải giữ bốn việc trong đầu nữa.

## Chatbot đứng im, Agent thì phân thân

Phần lớn người dùng AI ở Việt Nam — và tôi từng thế — chỉ dùng nó như một cái máy trả lời thông minh. Bạn hỏi, nó trả lời một đoạn, rồi đứng im chờ bạn gõ tiếp. Muốn có bài đăng, bạn phải tự copy đoạn đó ra, tự sửa, tự chọn ảnh, tự bấm đăng. Chatbot làm phần gõ chữ, còn phần vận hành — cái phần mệt nhất — vẫn là việc của bạn.

Đó là **chatbot**: một lượt hỏi — đáp, xong thì dừng.

**AI Agent** thì khác. Nó nhận một mục tiêu, rồi tự phân rã thành nhiều việc, mở nhiều luồng chạy song song, mỗi luồng tự đi hết một vòng: làm → tự kiểm → sửa → lưu nhớ → báo cáo. Nó có tay (chạy lệnh, ghi file, gọi API), có bộ nhớ để không lặp lại lỗi, và có tiêu chuẩn tự chấm điểm chính nó.

Một câu để nhớ: *chatbot sinh chữ, agent làm xong việc — và làm được nhiều việc cùng lúc.*

Trên thế giới, hướng này đang thành trào lưu hẳn. Đầu tháng 8/2026, loạt dự án trên Hacker News đều khoe cùng một ý: **đội agent** chạy song song. Cosmic ra mắt "team agents" quản lý cả hệ thống nội dung từ Slack, WhatsApp, Telegram. PolyMCP công bố công cụ điều phối nhiều agent tự chủ. KanVibe làm bảng Kanban tự theo dõi hàng loạt agent qua hook. Cùng một thông điệp: năm 2026 là năm của "phân thân" — một người điều khiển nhiều luồng AI cùng lúc, thay vì gõ từng lượt một.

## Phân thân hoạt động ra sao

Khi tôi giao "làm bốn việc", Hermes không làm tuần tự như tôi ngồi làm. Nó mở bốn luồng công việc độc lập. Mỗi luồng nhận đề bài riêng, rồi tự chạy cái **vòng lặp 8 bước** mà nó vẫn chạy mỗi ngày cho riêng bài blog:

1. **Định hướng** — hiểu rõ việc này cần ra cái gì.
2. **Nghiên cứu** — tự gom tư liệu, lọc cái dùng được.
3. **Sản xuất** — làm ra sản phẩm thô.
4. **Tự kiểm (quality gate)** — tự soi: đủ chuẩn chưa, có bịa không, giọng đúng chưa.
5. **Sửa** — chỗ chưa đạt thì viết lại, không đụng cả khối.
6. **Hình ảnh** — tự dựng ảnh, gắn tiêu đề.
7. **Lưu memory** — ghi lại để lần sau không trùng, không sót.
8. **Báo cáo** — gửi tôi dòng ngắn: xong việc gì, ra sao.

Bốn luồng chạy **song song**, không đợi nhau. Luồng nào xong trước báo trước. Tổng thời gian một tiếng đến từ chữ "song song" — chứ không phải vì máy viết nhanh hơn tôi. Nếu làm nối đuôi, bốn việc này vẫn mất cả buổi.

Điểm tinh tế: agent không mù quáng chạy song song mọi thứ. Nó tự nhận diện việc nào độc lập (viết bài, soi feedback) thì mở luồng riêng; việc nào phụ thuộc (lên lịch cần bài đã viết) thì xếp sau, nhưng vẫn chạy song song với mấy việc chờ được. Nó tự quản thứ tự thay tôi — cái chuyện tôi hay quên nhất.

Và bốn luồng **chia sẻ chung một bộ nhớ**. Việc 3 (lên lịch đăng) biết việc 1 (viết bài) đã xong để xếp lịch đúng bài; việc 7 (memory) ghi nhận cả bốn việc để hôm sau không ai trùng ai. Phân thân không phải là bốn cái máy rời rạc — là một đầu não điều bốn cánh tay, và bốn cánh tay cùng nhớ một chuyện.

## Bốn việc tôi giao hôm nay (demo thật)

Để không nói suông, đây đúng bốn việc tôi giao sáng nay — mỗi việc một kiểu, đủ để thấy agent không chỉ "sinh chữ":

- **Việc 1 — Viết bài đăng Facebook:** chủ đề "tại sao đọc nhanh mà không nhớ". Ra bài 400 chữ, có hook, có số, có CTA.
- **Việc 2 — Soi feedback khách:** đọc 30 ý kiến tuần này, trích 3 lỗi lặp lại (giá chưa rõ, không rõ ai dạy, sợ không dùng được), kèm gợi ý sửa.
- **Việc 3 — Lên lịch nguyên tuần:** xếp 7 bài vào khung 19h–21h (giờ vàng tương tác), tránh trùng chủ đề nhờ memory.
- **Việc 4 — Tóm tắt hợp đồng 40 trang:** trích 5 điều phải chú ý (thời hạn, điều khoản huỷ, trách nhiệm hai bên), bỏ qua râu ria.

Một tiếng sau tôi có: 1 bài FB sẵn sàng, 1 bảng 3 lỗi, 1 lịch 7 ngày, 1 trang tóm tắt hợp đồng. Tôi không mở bất cứ file nào trong lúc đó.

Cái khiến tôi tin nhất: trước đây tôi hay quên đăng hoặc đăng trùng chủ đề (từng có bạn nhắn "bài này đăng rồi anh ơi" — nhục). Giờ memory của agent giữ hộ cái đầu tôi. Bốn việc xong mà không sót một, không trùng một.

## Câu lệnh tôi giao (đúng kiểu giao việc cho người)

> "Hôm nay giúp tôi bốn việc: (1) viết một bài FB chủ đề đọc nhanh không nhớ, (2) soi 30 feedback khách trích 3 lỗi lặp, (3) lên lịch 7 bài cả tuần vào 19–21h, (4) tóm tắt hợp đồng 40 trang lấy 5 điều cần chú ý. Mở bốn luồng chạy song song, mỗi luồng tự chạy vòng lặp 8 bước, tự kiểm chất lượng và sửa tới khi đạt, dùng chung bộ nhớ để không trùng không sót, xong gửi tôi một dòng báo cáo từng việc. Không hỏi lại."

Để ý: tôi không viết nội dung. Tôi viết **mục tiêu + tiêu chuẩn + điều kiện dừng**. Câu quan trọng nhất là "tự kiểm chất lượng và sửa tới khi đạt" — nó biến bốn câu trả lời rời rạc thành bốn vòng lặp có kỷ luật. Và "dùng chung bộ nhớ" là cái biến bốn luồng thành một đội, không phải bốn kẻ mù.

## Kết quả đo được

- **2 ngày → 1 tiếng** máy chạy cho bốn việc khác loại. Phần tôi làm còn lại: đọc báo cáo và duyệt, chưa tới 5 phút.
- **4 việc, 0 sót, 0 trùng** nhờ memory chia sẻ — trước đây tôi sót đều mỗi lần nhận nhiều việc.
- **1 khâu cắt hẳn:** tự dựng ảnh và tự lên lịch, vốn mất tôi 20 phút mỗi việc.
- **12 lượt phân thân/ngày** nếu cần — vì agent chạy 24/7, kể cả lúc tôi ngủ, nên sáng ra tôi có sẵn đống việc đã xong.

Điều giá trị nhất với tôi không phải con số một tiếng. Là tôi không còn phải **giữ bốn việc trong đầu**. Trước kia, năng lượng tiêu vào việc "việc nào xong chưa, việc nào quên". Giờ cái danh sách nằm trong agent, đầu tôi rảnh để nghĩ chuyện đáng nghĩ: dạy gì, bán gì, nghỉ ở đâu.

## FAQ

**Phân thân khác gì gọi chatbot bốn lần?**
Gọi bốn lần chatbot thì bốn lần bạn phải nhận kết quả, tự ghép lại, tự thấy chỗ dở, tự bấm đăng. Phân thân là một mệnh lệnh, bốn luồng chạy tự động, chia sẻ memory, tự báo cáo chung. Bạn tiết kiệm không phải "thời gian gõ" mà là "thời gian vận hành" — cái mệt thật.

**Sợ một việc sai kéo theo ba việc khác?**
Đó là lý do có bước 4 (quality gate) trên từng luồng. Mỗi luồng tự soi lỗi của riêng nó trước khi báo xong; luồng nào chưa đạt thì tự sửa, không ảnh hưởng luồng khác. Muốn chắc hơn, đặt chế độ "viết xong gửi tôi duyệt rồi mới đăng" — vẫn tiết kiệm gần hết thời gian.

**Chỉ dùng cho content thôi à?**
Không. Xương sống là *một mục tiêu → nhiều luồng → mỗi luồng tự làm và tự báo*. Lắp vào đâu cũng được: mỗi sáng tổng hợp tin ngành thành 5 bản tin, mỗi tối chốt số bán hàng gửi 3 nhóm, mỗi tuần soi feedback tìm lỗi lặp, mỗi tháng dựng bộ nội dung 4 kênh. Đổi mục tiêu, giữ nguyên cơ chế phân thân.

---

Nếu bạn vẫn dùng AI theo kiểu hỏi–đáp từng lượt, bạn mới dùng chưa tới một phần mười sức của nó. Cái đáng đầu tư không phải mẹo viết prompt hay hơn, mà là **giao được cả một đội việc** cho agent tự phân thân làm.

👉 Bộ **Trợ Lý AI Hermes** đang mở bán sớm **239K** (giá gốc 499K) — hướng dẫn từng bước để bạn tự dựng cơ chế phân thân cho công việc mình, kèm 3 kit tiện ích dùng được ngay: **https://speedreading.vn/shermes**
