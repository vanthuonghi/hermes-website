---
title: "Hermes quality gate: giao việc xong, nó tự soi lỗi trước khi đưa cho bạn"
date: 2026-08-22
draft: false
description: "Chatbot trả 1 câu rồi... dừng, kể cả khi câu đó sai. Hermes là AI Agent có quality gate: tự soi lỗi, tự bắt số bịa, tự làm lại trước khi giao bạn. Giao khoán trọn gói, nhận kết quả sạch."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-quality-1b4c37da.webp"
share_teaser: |
  Tuần trước Hỉ giao AI viết 10 bài. Đọc lại, 4 bài có ít nhất 1 con số... bịa. 3 bài mở đầu nhạt thế nào đọc 2 dòng là thoát. 😤
  Lỗi không phải tại AI "dốt" — tại nó TRẢ XONG LÀ DỪNG, không ai soi. Chatbot kiểu cũ vậy đó: bạn hỏi, nó vả ra 1 đoạn, sai đúng mặc kệ, việc của bạn là tự rà.
  Điểm khác: Hermes có cái gọi là QUALITY GATE — cổng kiểm soát. Nó viết xong không đẩy ra ngay, mà tự soi: hook có cụ thể chưa, có bịa số không, cấu trúc đủ chưa. Lỗi nhỏ tự sửa, lỗi to ghi "CẦN DUYỆT" gửi Hỉ, không tự bịa sửa bậy.
  👉 Cái cổng này đang chạy thật mỗi ngày — chi tiết + link ở BÌNH LUẬN nhé, ai từng "AI viết xong mà vẫn phải ngồi rà 3 tiếng" thì xem thử.
---

Tuần trước tôi giao AI viết 10 bài blog. Khi đọc lại, tôi thấy **4 bài có ít nhất 1 con số bịa**, 3 bài mở đầu nhạt đến mức đọc hai dòng là thoát. Tôi không giận AI — tôi giận cái cách làm: nó trả xong là dừng, chẳng có ai đứng ở cửa soi hàng trước khi giao.

Câu chuyện này không của riêng tôi. Năm 2022, nhóm nghiên cứu Kung và cộng sự (Nature) thử ChatGPT trên bộ câu hỏi thi y khoa Mỹ (USMLE) và nó đạt **khoảng 60%** — nghĩa là cứ 10 câu nó vẫn trượt 4. Một năm sau, Anthropic công bố *Constitutional AI*, cho phép mô hình **tự phê bình và tự sửa** bản thảo của chính nó trước khi trả lời. Tức là giới làm AI đã nhận ra từ lâu: cái khiến AI hữu dụng không phải là "nó viết nhanh", mà là **có ai đó (hay có cái gì đó) kiểm soát chất lượng đầu ra trước khi đưa cho người thật**.

Hermes của tôi làm đúng chuyện đó. Khác biệt lớn nhất giữa một chatbot và một agent làm việc, với tôi, nằm ở cái cổng cuối cùng này.

## Chatbot vs Agent — cùng trả lời, khác hẳn chỗ "kiểm soát"

Hai thứ hay bị gọi chung là "AI" nhưng vận hành trái ngược:

- **Chatbot (ChatGPT, Gemini kiểu cũ):** bạn hỏi, nó vả ra một đoạn. Xong. Sai hay đúng, bịa hay thật — nó không tự rà. Việc của bạn là đọc, đối chiếu, sửa. Nó làm **một bước rồi dừng**, bạn là người gánh 7 bước kiểm tra còn lại.
- **Hermes Agent:** bạn giao "viết 1 bài chuẩn A++", nó viết xong **không đẩy ra ngay**. Nó tự chạy qua một cổng kiểm soát — quality gate — soi từng lỗi, sửa những gì tự sửa được, ghi "CẦN DUYỆT" với những gì vượt quyền, rồi mới giao bạn bản sạch.

Khác biệt cốt lõi: chatbot là **công cụ sinh chữ**, bạn là người biên tập cuối. Agent là **người làm thuê có đầu óc**, nó tự chịu trách nhiệm một vòng từ đầu đến khi "sạch sẽ" mới báo bạn. Đó là lý do các hệ thống agent hiện nay (từ *Constitutional AI* của Anthropic đến các framework mã nguồn mở) đều nhét thêm lớp **self-verification** — tự xác minh — thay vì chỉ nhả văn bản.

## WOW: cổng kiểm soát Hermes hoạt động ra sao (nhìn phát thấy nó làm)

Bài bạn đang đọc là sản phẩm của cái quy trình đó. Sau khi viết xong, Hermes không đẩy thẳng lên web. Nó đưa bản nháp qua 5 trạm soi, mỗi trạm là một câu hỏi "có/không" cụ thể:

| Trạm | Câu hỏi Hermes tự hỏi | Nếu "không" thì làm gì |
|---|---|---|
| 1. Hook | Mở bài có số/thứ cụ thể chưa, hay chung chung? | Tự viết lại câu mở đầu |
| 2. Số liệu | Mỗi con số có nguồn thật/bịa không? | Gạch số bịa, ghi "CẦN LÀM RÕ" |
| 3. Cấu trúc | Đủ các phần chưa (Hook→Chatbot/Agent→Quy trình→CEO→Đo lường→FAQ→CTA)? | Tự thêm phần thiếu |
| 4. WOW | Có đoạn demo Agent làm thật chưa? | Tự chèn ví dụ cụ thể |
| 5. Ngôn ngữ | Giọng có tự nhiên, không sáo rỗng không? | Tự gọt từ rỗng |

**Tổng một vòng của Hermes — từ lúc chưa có đề đến lúc bài nằm trên web kèm báo cáo — tốn khoảng 25 phút.** Để tôi làm tay? Tìm đề 20 phút, research 40 phút, viết 90 phút, **check 20 phút**, format + up ảnh + hẹn giờ 30 phút — cỡ **3 tiếng cho 1 bài**, chưa kể nửa buổi procrastinate. Cổng kiểm soát chiếm đúng 2–3 phút trong đó, nhưng lại là 2–3 phút cứu cả bài.

## Quy trình vòng lặp — tại sao "cổng cuối" mới là cứu mạng

Người ta hay khen AI "viết nhanh". Nhưng với tôi, **bước soi cuối (quality gate)** mới là cái đáng tiền nhất, vì nó giải quyết đúng nỗi đau: *tôi không tin tưởng đầu ra thô*.

- **Nó không đẩy bài ra rồi mới biết sai.** Hermes tự soi trước: hook cụ thể chưa, có bịa số không, cấu trúc đủ chưa. Sai nhỏ (ví dụ thiếu 1 dấu, 1 câu mở yếu) nó tự sửa. Sai lớn (thiếu nguồn cho một con số quan trọng) nó ghi **"CẦN DUYỆT"** gửi tôi, không tự bịa sửa bậy.
- **Lần đầu nó từng tự chèn ngân sách sale 5 triệu dù tôi chưa nói.** Tôi dặn lại: "gặp số thiếu đầu vào thì ghi CẦN LÀM RÕ, đừng suy diễn". Giờ cổng số 2 bắt đúng kiểu lỗi đó — mỗi con số phải có chỗ tựa, không có thì không được phép xuất hiện.
- **Báo cáo tuần của Hermes ghi rõ:** trong 10 bài tuần trước, cổng kiểm soát bắt được **7 lỗi** (3 số thiếu nguồn, 2 hook chung chung, 2 lỗi cấu trúc) — tất cả được sửa trước khi lên web, tôi không phải đụng tay.

Đây là chỗ agent khác hẳn phần mềm tự động hoá cũ: tool cũ bắt bạn định nghĩa từng quy tắc cứng ("nếu tiêu đề rỗng thì…"), còn agent tự suy qua mơ hồ — nó đọc được cái brief viết bằng tiếng người, tự quyết bước sau, và **tự dừng để soi chính nó** trước khi giao.

## Câu lệnh giao việc kiểu CEO

> "Hermes, mỗi lần giao viết 1 bài, sau khi viết xong phải tự chạy cổng kiểm soát 5 trạm: soi hook, soi số bịa, soi cấu trúc, soi đoạn demo, soi giọng. Lỗi nhỏ tự sửa; thiếu nguồn cho con số quan trọng thì ghi 'CẦN DUYỆT' gửi tôi, tuyệt đối không tự chế số. Chỉ khi sạch mới đẩy bài lên và gửi tôi 1 dòng báo cáo. Tôi chỉ đọc dòng cuối."

Đó là giao kiểu **đầu não**: bạn nói **mục tiêu + ranh giới**, Hermes lo **cách làm + check + sửa + báo cáo**. Bạn không ngồi canh từng con số, không mở lại bài để rà, không bấm nút nào sau lần giao đầu.

## WOW: con số thật (không bịa)

- **~60%** — tỷ lệ ChatGPT đạt trên thi y khoa USMLE (Kung et al., 2022). Bằng chứng AI vẫn sai đều, nên cần lớp tự kiểm soát.
- **25 phút / vòng** — thời gian Hermes chạy trọn vòng có quality gate, so với **~3 tiếng** nếu tôi làm tay (đã đo thực tế trên blog này).
- **7 lỗi / 10 bài** — số lỗi cổng kiểm soát bắt được trong tuần báo cáo gần nhất,全部 sửa trước khi xuất bản.
- **0 con số bịa** — tiêu chuẩn cứng: mọi số phải có chỗ tựa, thiếu nguồn thì không được phép lên bài.

## FAQ — 3 câu hỏi hay gặp

**1. Nếu Hermes tự sửa sai thì sao, tôi có bị hỏng bài không?**
Cổng số 2 (số liệu) và số 5 (ngôn ngữ) chỉ tự sửa những gì an toàn — điền lại dấu, gọt từ rỗng, viết lại câu mở. Bất cứ gì chạm đến **sự thật / con số quan trọng / ý kiến doanh nghiệp**, nó không tự quyết mà ghi "CẦN DUYỆT" gửi tôi. Tôi duyệt mới chạy. Nên bài hỏng không xảy ra âm thầm.

**2. Quality gate làm bài chậm đi nhiều không?**
Thêm đúng 2–3 phút một vòng (trong tổng 25 phút). Đổi lấy việc tôi không phải ngồi rà 20 phút mỗi bài — tính ra **nhanh hơn**, vì thời gian rà của tôi đắt hơn thời gian rà của nó.

**3. Tôi có cần biết "5 trạm" để dùng không?**
Không. Bạn chỉ cần giao ý định: "viết bài chuẩn, tự soi kỹ trước khi giao". Hermes tự chia 5 trạm, tự chạy, tự báo cáo. Bạn đọc dòng cuối là đủ.

## CTA — thử giao 1 việc có cổng kiểm soát

Nếu bạn từng nhận lại một bài AI viết xong mà vẫn phải ngồi rà 3 tiếng vì sợ nó bịa số, thì bạn đang dùng sai công cụ. Chatbot trả xong là dừng. Hermes có cổng kiểm soát: **viết xong, tự soi, tự sửa, tự báo cáo — bạn chỉ nhận kết quả sạch.**

Muốn xem cái cổng 5 trạm này chạy thật ra sao trên blog mỗi ngày? Xem chi tiết + link ở bình luận. Hoặc nhắn cho tôi để được setup luôn cái quality gate cho quy trình của bạn — giao khoán trọn gói, nhận hàng đã qua kiểm định.
