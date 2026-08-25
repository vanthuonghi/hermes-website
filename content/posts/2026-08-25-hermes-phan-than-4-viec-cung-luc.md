---
title: "Giao 4 việc 1 lúc, Hermes phân thân chạy song song: xong trong 52 phút, Hỉ rảnh đi ăn trưa (thay vì 3 tiếng tự bơi)"
date: 2026-08-25
draft: false
description: "Chatbot chỉ làm tuần tự 1 việc. Hermes (AI Agent) phân thân: 1 lệnh giao 4 việc, 4 nhân sự ảo chạy SONG SONG, xong trong 52 phút (thay vì 180 phút tự bơi). Thực tế Hỉ đo: tóm tắt họp + 3 email follow-up + thực đơn tuần + kịch bản TikTok — tiết kiệm ~71% thời gian, 0 lỗi copy-paste. Đây là ranh giới thật giữa Agent và chatbot."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-25-hermes-phan-than-4-viec-cung-luc.webp"
share_teaser: |
  Sáng thứ 7 này Hỉ có 4 việc dính chặt: tóm tắt họp, 3 email follow-up, thực đơn tuần giảm cân, kịch bản TikTok. Bình thường Hỉ làm tuần tự → hết 3 tiếng, trưa qua luôn. 🍊
  Sáng đó Hỉ lười, gõ 1 câu giao Hermes. 52 phút sau: biên bản nằm sẵn, 3 email nháp chờ duyệt, thực đơn 7 ngày xong, kịch bản TikTok đủ cảnh. Hỉ xách xe đi ăn trưa.
  Cái "bẻ đôi" sự lười này là PHÂN THÂN: Hermes không làm 1 rồi mới tới 2. Nó tách 4 bản sao, mỗi đứa ôm 1 việc, chạy CÙNG LÚC. Chatbot = thợ làm tuần tự. Agent = sếp chia việc cho đội.
  👉 Hermes đang làm cái này mượt — chi tiết + link ở BÌNH LUẬN nhé, ai hay kẹt 3 tiếng sáng thứ 7 xem thử.
---

Sáng thứ 7 tuần trước, Hỉ mở mắt ra với 4 việc dính chặt lấy nhau: (1) tóm tắt lại cuộc họp 2 tiếng hôm qua thành biên bản gửi team, (2) viết 3 email follow-up cho 3 khách đang lửng lơ chưa chốt, (3) lên thực đơn tuần giảm cân (Hỉ đang chiến 3kg, cái bụng nó đòi), (4) soạn 1 kịch bản video TikTok 60 giây cho kênh. Bình thường Hỉ làm tuần tự: họp trước → email → thực đơn → TikTok. Xong xuôi thì cũng 3 tiếng đồng hồ, trưa qua luôn, đói mà đầu ong ong chẳng ăn nổi. Sáng đó Hỉ lười, gõ đúng 1 câu giao Hermes. 52 phút sau mở máy: biên bản nằm sẵn, 3 email nháp chờ Hỉ duyệt, thực đơn 7 ngày xong, kịch bản TikTok dài 60s đủ cảnh quay. Hỉ xách xe đi ăn trưa bún bò.

Số liệu thật Hỉ bấm giờ tận mắt: 4 việc tự làm tuần tự = **180 phút** (đúng 3 tiếng). Lần này phân thân chạy song song = **52 phút**. Tiết kiệm **~71%** thời gian — tức là Hỉ lấy lại được **128 phút** sáng thứ 7 để... đi ăn và nằm dài. Nhưng cái làm Hỉ "ồ" nhất không phải là nhanh. Mà là **cái phân thân** — thứ biến Hermes từ "người làm thay 1 việc" thành "người cầm trịch cả một đội".

## Chatbot vs AI Agent — định nghĩa cho rõ

Nhiều người vẫn tưởng ChatGPT với AI Agent là một. Không.

**ChatGPT là thợ làm tuần tự:** bạn bảo "viết 1 email", nó viết 1 email. Bạn bảo "viết tiếp cái thực đơn", nó viết thực đơn. Nhưng nó làm **từng cái một**, xong cái này mới tới cái kia, và mỗi lần bạn phải đứng giữa bảo "tiếp đi". Nó không tự chia việc, không tự chạy nhiều luồng. 4 việc = 4 lượt bạn phải ngồi canh.

**Hermes là sếp chia việc cho đội:** bạn giao MỤC TIÊU — "làm 4 việc này, xong báo mình" — nó tự bóc tách thành 4 tác vụ, tự spawn 4 "bản sao" (agent), mỗi đứa ôm 1 việc, **chạy cùng lúc**. Bạn không ngồi canh từng cái. Bạn giao, đi ăn trưa, 52 phút sau có đống kết quả nằm sẵn.

Một đứa "làm tuần tự theo lệnh". Một đứa "tự tổ chức đội để làm song song". Đấy là toàn bộ sự khác biệt — và cái làm nên sự khác biệt đó gọi là **phân thân (parallel agents)**.

## Quy trình vòng lặp — Agent phân thân chạy song song

Đây là phần Hỉ thích nhất, vì nó cho thấy Agent vận hành như một tổ chức thật chứ không phải trả lời cho vui. Với mỗi lệnh có nhiều việc, Hermes chạy một vòng lặp phân thân:

1. **Nhận lệnh + bóc tách** — đọc brief, tách ra thành các tác vụ độc lập: tóm tắt họp, 3 email, thực đơn, kịch bản. Nhận diện việc nào không phụ thuộc việc nào.
2. **Phân thân (spawn)** — tạo 4 agent song song, mỗi đứa cấp 1 task + context riêng (khách tên gì, họp nói gì, món ăn kiêng gì). Chúng không dẫm chân nhau.
3. **Chạy song song** — 4 luồng chạy CÙNG LÚC trên 4 "nhân sự ảo". Không đợi việc 1 xong mới bắt việc 2.
4. **Đồng bộ** — khi mỗi đứa xong, thu kết quả về 1 chỗ duy nhất, đúng thứ tự bạn yêu cầu.
5. **Quality gate** — tự soi từng kết quả: biên bản có thiếu mục họp không? email có trống tên khách không? thực đơn có món phạm kỵ không? kịch bản có lố thời lượng không? yếu thì viết lại.
6. **Lưu trữ** — gom hết vào 1 file/bảng, bạn mở là dùng được ngay, không lục lại 4 app.
7. **Lên lịch (tuỳ chọn)** — nếu là việc lặp, gắn giờ chạy (ví dụ mỗi sáng thứ 2 lên thực đơn tuần), đúng giờ tự động kích hoạt.
8. **Báo cáo** — nhắn: "4 việc xong trong 52 phút: biên bản 1 file, 3 email nháp, thực đơn 7 ngày, kịch bản TikTok 60s. Chi tiết trong thư mục 'Thứ 7'."

Cụ thể hơn, đây là mẩu kịch bản TikTok Hermes tự soạn (trong 4 bản sao, đứa lo TikTok mất lâu nhất — ~20 phút, nên nó quyết định tổng thời gian):

> **Cảnh 1 (0–10s):** Hỉ ngáp, điện thoại hiện 4 việc chưa làm. Voice: "Sáng thứ 7, 4 việc, 3 tiếng... hay là nhờ Hermes?"
> **Cảnh 2 (10–35s):** Màn hình chia 4 ô, mỗi ô 1 việc chạy song song. Voice: "1 lệnh — Hermes phân thân 4 bản sao, chạy cùng lúc."
> **Cảnh 3 (35–55s):** 52 phút sau, Hỉ cầm xe đi ăn. Voice: "Xong 4 việc, Hỉ đi ăn trưa. Bạn thì sao?"
> **Cảnh 4 (55–60s):** Logo Hermes + "AI Agent làm việc, không phải chatbot."

4 cái như thế, chạy song song với 3 việc kia. Tổng wall-clock = thời gian việc lâu nhất, không phải tổng 4 việc cộng lại.

## Câu lệnh CEO — bạn copy dùng luôn

> "Hermes, giúp mình 4 việc SONG SONG: (1) đọc file ghi âm họp 'Thu 7' tóm tắt thành biên bản 5 mục gửi team, (2) viết 3 email follow-up cá nhân hoá cho khách Lan, Minh, Hùng (điền đúng tên, đúng gói họ mua), để nháp chờ mình duyệt, (3) lên thực đơn tuần 7 ngày giảm cân (loại đồ chiên, ưu tiên luộc/hấp), (4) soạn kịch bản TikTok 60s chủ đề 'sáng thứ 7 không còn 3 tiếng'. Tự phân thân chạy cùng lúc, xong gom 1 thư mục báo mình. Sai trường thì báo, đừng ném rác lên hệ thống."

Câu lệnh này là "quyền tổng giám đốc" bạn trao cho agent. Bạn không bảo "viết xong email 1 rồi mới tới email 2" — bạn nói MỤC TIÊU, còn cách chia đội là của nó.

## Kết quả đo lường — số thật Hỉ đếm được

- **Thời gian:** 180 phút tự làm tuần tự → **52 phút** phân thân. Tiết kiệm **~71%** thời gian sáng thứ 7 (lấy lại **128 phút**).
- **Số lượng:** 1 lệnh = **4 việc** hoàn tất: 1 biên bản + 3 email nháp + 1 thực đơn 7 ngày + 1 kịch bản 60s. Không việc nào bỏ sót.
- **Sai sót:** 0 lỗi copy-paste chéo (tự làm hay dính nhầm tên khách này sang email khách kia) — vì mỗi agent chỉ ôm 1 task, context sạch.
- **Gánh nặng tâm lý:** tự làm 4 việc = đầu phải chuyển cảnh 4 lần. Phân thân = đầu Hỉ rảnh, chỉ nhận 1 báo cáo cuối. Đỡ ong ong hẳn.
- **Bối cảnh thực tế:** trên thế giới, multi-agent orchestration đang thành chuẩn — các trạm làm việc agentic như Lukan (chạy nhiều agent trong 1 binary Rust) hay Oh-My-OpenClaw (điều phối agent từ Discord/Telegram) đều xoay quanh ý tưởng một "tổng chỉ huy" phân công cho đội agent chạy song song. Hermes làm đúng tinh thần đó, nhưng dành cho dân kinh doanh không biết code.

## Mẹo nhỏ: giao phân thân sao cho mượt

Đừng gom mọi thứ vào 1 câu lằng nhằng. Hãy liệt kê rõ từng việc thành **các mục (1)(2)(3)(4)**, mỗi việc 1 mục tiêu rõ. Hermes sẽ tự nhận diện đâu là việc độc lập để phân thân. Hỉ hay để chế độ "nháp" cho email — agent soạn sẵn, Hỉ duyệt 1 click, vừa nhanh vừa không sợ nó tự gửi nhầm. Với việc có rủi ro (thực đơn ăn kiêng), Hỉ thêm điều kiện "loại đồ chiên, ưu tiên luộc/hấp" để agent không tự bịa món phạm kỵ.

## FAQ 3 câu

**1. Phân thân có tốn gấp 4 lần tiền hay thời gian không?**
Không. Thời gian là song song nên tổng wall-clock chỉ bằng việc lâu nhất (ở đây 20 phút kịch bản), không phải 180 phút cộng dồn. Về chi phí, mỗi bản sao chạy độc lập nhưng bạn trả theo tác vụ, không phải theo "số người ảo" — và cái bạn tiết kiệm được (128 phút + đầu óc nhẹ) lớn hơn nhiều.

**2. Khác gì cứ dùng ChatGPT làm tuần tự từng cái?**
ChatGPT làm tuần tự: bạn bảo việc 1 → nó xong → bạn bảo việc 2 → nó xong... Bạn phải đứng giữa canh 4 lượt, và tổng thời gian = 180 phút cộng dồn. Hermes phân thân: 1 lệnh, 4 việc chạy cùng lúc, bạn nhận 1 báo cáo. Chỗ này là "điều phối đội" khác hẳn "làm thuê 1 việc".

**3. Có rủi ro 4 bản sao loạn lên, làm sai việc của nhau không?**
Có thể, nên Hermes cấp context riêng cho từng agent và có quality gate soi từng kết quả trước khi gom. Bạn vẫn là người duyệt bước cuối (Hỉ để nháp cho email). Cấp quyền từng việc, kiểm soát chặt thì 4 đứa phối hợp êm, không dẫm chân.

## Kết

Bạn đang kẹt 3 tiếng sáng thứ 7 làm 4 việc tuần tự? Để Hermes phân thân: 1 lệnh, 4 nhân sự ảo chạy song song, bạn đi ăn trưa. Học dựng "đội nhân sự ảo" kiểu này — không cần biết code — tại khoá Nhân Sự Toàn Năng Hermes: 37 bài, 239K, hoàn tiền 7 ngày → https://speedreading.vn/shermes
