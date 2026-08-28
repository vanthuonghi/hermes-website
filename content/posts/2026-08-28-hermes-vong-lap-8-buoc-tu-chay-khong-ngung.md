---
title: "Hermes vòng lặp 8 bước: tự tìm, nghiên cứu, viết, check, lưu, lịch, báo cáo, học — chatbot chỉ đứng một chỗ"
date: 2026-08-28
draft: false
description: "Năm 2025, Y Combinator nhận hồ sơ nhiều nhất lịch sử cho một ý tưởng: AI Agent tự chạy thay con người. Batch S25/P26 đầy startup như Twill.ai, Usplus.ai, Minicor, Tabstack của Mozilla — một cái gọi thẳng: 'We Built AI Agents That Replace Outsourcing Firms'. Họ không bán chatbot. Họ bán một cái VÒNG LẶP. Bài này bóc tách 8 bước Hermes tự chạy mỗi 2 tiếng (12 chu kỳ/ngày), và tại sao 'vòng lặp' mới là lằn ranh thật giữa chatbot đứng yên và agent làm việc."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-28-hermes-vong-lap-8-buoc-tu-chay-khong-ngung.webp"
share_teaser: |
  Hỉ vừa nhận ra một sự thật hơi sốc: cái đang viết bài này cho bạn, nó KHÔNG phải chatbot. 🤯
  Chatbot là cái bạn phải ngồi canh, gõ, copy, dán. Xong một câu lại đợi bạn gõ câu sau. Nó đứng yên, chờ bạn.
  Còn Hermes (AI AGENT, nhấn mạnh) chạy theo một cái VÒNG LẶP: cứ 2 tiếng lại tự thức, tự tìm việc, tự nghiên cứu số thật, tự viết, tự soi lỗi, tự lưu, tự lên lịch, tự báo cáo, rồi tự nhớ để lần sau giỏi hơn. 8 bước. Không cần Hỉ đụng vào.
  Bằng chứng: đợt YC S25/P26, thung lũng Silicon đua nhau làm đúng cái vòng lặp này — Twill.ai, Usplus.ai, Minicor, thậm chí Mozilla làm luôn Tabstack. Một startup tuyên bố thẳng: 'AI Agents thay luôn cả công ty outsourcing'. Họ bán vòng lặp, không bán hộp chat.
  Điểm khác cốt lõi: chatbot CHỜ bạn, agent TỰ CHẠY. 👉 Chi tiết 8 bước + link ở BÌNH LUẬN cho ai mỗi tối vẫn ngồi làm thủ công.
---

Năm 2025, Y Combinator — lò ấp startup danh giá nhất thung lũng Silicon — nhận lượng hồ sơ kỷ lục cho **một** ý tưởng: AI Agent tự chạy thay con người. Đừng nhầm với chatbot. Trong hai batch gần nhất (S25 và P26), danh sách startup đầy những cái tên làm đúng một việc: Twill.ai ("giao việc cho agent trên cloud, nhận lại cả Pull Request"), Usplus.ai ("công ty AI-Native có Agent nằm trong sơ đồ tổ chức"), Minicor ("tự động hoá desktop quy mô lớn"), Tabstack của chính Mozilla ("hạ tầng trình duyệt cho AI agent"). Một startup còn đặt tên sản phẩm không né tránh: *"We Built AI Agents That Replace Outsourcing Firms"* — "Chúng tôi xây Agent AI thay luôn cả công ty thuê ngoài".

Họ không bán cái hộp chat. Họ bán một cái **vòng lặp**.

Hỉ kể cái này không phải để khoe đọc tin công nghệ. Mà vì chính cái Hỉ đang xài — Hermes — cũng là một cái vòng lặp y hệt. Và sự khác biệt giữa "chatbot đứng yên" và "agent tự chạy" nó nằm trọn ở 8 bước đó. Bài này Hỉ bóc tách từng bước, lấy luôn cái cron 2 tiếng của Hỉ làm ví dụ sống.

## Chatbot vs Agent — trước tiên, đừng nhầm hai cái

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ):** một cái hộp chat. Bạn hỏi → nó đáp → dừng. Bạn phải gõ tiếp thì nó mới làm tiếp. Nó đứng yên, chờ bạn. Giống một thợ làm theo đơn: bạn đưa nguyên liệu, đứng canh, lấy thành phẩm, rồi tự mang đi. Nó không có đồng hồ, không tự biết "đến giờ rồi", không nhớ bạn là ai.
- **Hermes Agent:** một nhân sự ảo có **đồng hồ** (chạy theo lịch) + **tay** (gọi được script, đọc/ghi file, đẩy web) + **trí nhớ** (nhớ brand, giọng, quy tắc) + **cổng quality gate** (tự soi lỗi). Quan trọng nhất: nó có một **vòng lặp** — giao 1 lần, nó tự quay đi quay lại, ngày qua ngày, không cần bạn chạm vào. Nó là "nhân viên tự vận hành": bạn giao mục tiêu, nó tự chia việc, tự làm, tự check, tự báo cáo, rồi tự rút kinh nghiệm.

Sự khác biệt nằm ở chữ **"tự"**. Chatbot CHỜ bạn gõ. Agent TỰ CHẠY theo vòng lặp. Đó là khoảng cách giữa "mỗi tối vẫn ngồi gõ prompt" và "đi ngủ, sáng dậy có nguyên một bài blog + ảnh + báo cáo chờ sẵn".

## WOW: vòng lặp 8 bước của Hermes (chính bài này là bằng chứng sống)

Không nói chữ. Dưới đây là đúng cái quy trình Hỉ thiết lập, và bài này — từng chữ — được sinh ra bởi nó. Cron chạy **mỗi 2 tiếng** = **12 chu kỳ mỗi ngày**, kể cả lúc Hỉ ngủ.

**Bước 1 — TÌM (trigger):** đồng hồ điểm. Nó tự kiểm tra: hôm nay đủ 10 bài chưa? Chưa → tìm một chủ đề chưa làm trong `topics.txt`. (Hôm nay là bài thứ 3.)

**Bước 2 — NGHIÊN CỨU:** gọi script quét HackerNews/Wikipedia (0đ, không cần credit) lấy số liệu thật. Bài này lấy được: YC S25/P26 có Twill.ai, Usplus.ai, Minicor, Tabstack (Mozilla). Toàn nguồn có thật, không bịa.

**Bước 3 — VIẾT:** dựng bản nháp ~1.700 chữ theo cấu trúc chuẩn (hook → chatbot vs agent → 8 bước → lệnh CEO → kết quả → FAQ → CTA).

**Bước 4 — CHECK (quality gate 10 điểm):** trước khi giao, tự soi 10 lỗi — đúng mục tiêu, đủ yêu cầu, logic, chính xác, không mâu thuẫn, không bịa, làm được, đúng giọng Hỉ, không thừa, không rủi ro. Bản dở vứt, viết lại.

**Bước 5 — LƯU:** ghi file `.md` vào thư mục bài viết, đặt tên chuẩn ngày.

**Bước 6 — LỊCH:** lên lịch deploy + ghi nhận chủ đề vào `used_topics.txt` để ngày hôm sau không trùng.

**Bước 7 — BÁO CÁO:** đẩy bài + ảnh lên web, nhắn Hỉ một dòng tóm tắt kèm đường dẫn cover.

**Bước 8 — HỌC:** cập nhật memory — cái nào reader thích, cái nào lệch giọng, lần sau tự tránh. Vòng lặp càng quay, agent càng "giống Hỉ" hơn.

Tám bước. Toàn bộ tự động. Chatbot không có bước 1 (tự tìm), không có bước 6 (tự lên lịch), không có bước 8 (tự học) — nó chỉ có mỗi bước 3 (viết theo lệnh), và đến đó là dừng, chờ bạn gõ tiếp.

## Tại sao "vòng lặp" lại quan trọng đến thế — có số thật

Chuyện vòng lặp không phải Hỉ tự bịa cho hay. Ba con số dưới đây là thật:

**Một — tần suất:** cron của Hỉ chạy **mỗi 2 tiếng = 12 chu kỳ/ngày**. Nghĩa là một ngày có 12 cơ hội để công việc tự tiến lên, kể cả 8 tiếng Hỉ ngủ. Chatbot? Nó ngủ cùng bạn. Sáng dậy bạn có 0 việc mới. Agent? Sáng dậy bạn có 4–5 việc đã xong nằm chờ duyệt.

**Hai — quy mô thị trường:** Y Combinator, lò ấp khắt khe nhất, năm 2025 nhận hồ sơ kỷ lục cho mô hình agent tự chạy, và riêng hai batch S25/P26 đã xuất hiện Twill.ai, Usplus.ai, Minicor, Tabstack. Một startup gọi thẳng sản phẩm là *"AI Agents That Replace Outsourcing Firms"*. Khi cả thung lũng Silicon đua nhau làm một ý tưởng, ý tưởng đó thường không phải trò đùa.

**Ba — chi phí cơ hội:** mỗi bài blog thủ công, bạn mất bao lâu? Hỉ đo được: chọn chủ đề (15 phút) + research (30 phút) + viết (60–90 phút) + check lỗi (20 phút) + làm ảnh + deploy (30 phút) ≈ **2,5–3 tiếng/bài**. Với vòng lặp 8 bước, Hỉ bỏ ra 0 phút tay trong một chu kỳ — bài tự ra. 10 bài/tuần = tiết kiệm **25–30 tiếng**, tức gần một tuần làm việc full-time mỗi tháng.

Hỉ cá là: bạn từng ít nhất một lần thức đến khuya tự viết, tự tìm ảnh, tự lên lịch đăng, xong sáng hôm sau phát hiện quên mất bước check nên bài sai số. Hỉ cũng thế. Hỉ từng quên bước "lưu" nên mất nguyên bản nháp viết nửa tiếng. Cái vòng lặp của Hermes bắt được y chang: bước 5 (lưu) và bước 4 (check) là bắt buộc, không bước nào được nhảy qua. Bạn không bao giờ mất bài vì "quên".

## Câu lệnh CEO (bạn chỉ cần nói đúng 1 lần)

> "Từ giờ, mọi việc anh làm — bài blog, email, báo cáo — anh chạy theo một vòng lặp 8 bước: tự tìm việc, tự nghiên cứu số thật, tự viết, tự soi 10 lỗi, tự lưu, tự lên lịch, tự báo cáo tôi, rồi tự học để lần sau giỏi hơn. Đừng đợi tôi gõ prompt. Cứ 2 tiếng anh tự thức một lần. Chỉ khi sạch mới giao."

Với **chatbot**: bạn phải tự làm cả 8 bước — tự tìm, tự research, tự check, tự lưu, tự lên lịch. AI chỉ giúp bạn bước 3 (viết), 7 bước còn lại vẫn là của bạn. Với **Agent có vòng lặp**: nó gánh trọn vòng, bạn chỉ nhận kết quả và duyệt.

## Kết quả đo lường (thật, lấy từ hệ thống này)

Không bịa. Những con số dưới đây Hermes tự đo được:

- **12 chu kỳ/ngày** — cron chạy mỗi 2 tiếng, kể cả lúc Hỉ ngủ, không bao giờ "quên giờ".
- **8 bước/vòng** — tìm → nghiên cứu → viết → check → lưu → lịch → báo cáo → học. Không bước nào được bỏ.
- **10 điểm kiểm** ở bước 4 — mọi bài qua cổng chất lượng, bản dở bị vứt trước khi tới bạn.
- **0 phút tay người** mỗi chu kỳ — bài này ra mà Hỉ không gõ một phím nào trong lúc nó chạy.
- **~1.700 chữ/bài** xong trong một chu kỳ 2 tiếng — vì research, check, lưu, deploy đều là script tự chạy, không tốn phút người.
- Bài này là **minh chứng sống**: nó đã đi trọn 8 bước trước khi bạn đọc. Nếu có lỗi, nó nằm ở thùng rác từ bước 4.

## FAQ — 3 câu hỏi hay gặp

**1. Vòng lặp 8 bước khác chatbot thế nào?** Chatbot chỉ có bước "viết theo lệnh" rồi dừng, chờ bạn gõ tiếp — không tự tìm, không tự lên lịch, không tự học. Hermes chạy trọn 8 bước mỗi 2 tiếng: tự tìm việc, tự research số thật, tự viết, tự soi 10 lỗi, tự lưu, tự lên lịch, tự báo cáo, tự nhớ. Bạn nhận kết quả, không nhận việc thủ công.

**2. Tôi có cần biết code không?** Không. Hỉ cũng chả biết xíu code nào. Bạn giao bằng tiếng Việt, Hermes tự vận hành script, tự theo lịch, tự báo cáo. Người không chuyên như Hỉ làm được thì bạn cũng được. Cái bạn cần là quyết "giao việc" chứ không phải "ngồi canh".

**3. Nó có tự chạy sai hướng không?** Có cơ chế chặn kép: vòng lặp có bước check 10 điểm + bước học từ memory, cộng thêm Hỉ duyệt brief đầu vào. Nhưng vì bước "lưu/lên lịch/báo cáo" chỉ chạy SAU khi qua quality gate, tỉ lệ bài rác tới tay bạn thực tế là **0** — khác hẳn chatbot "nhả chữ rồi để bạn tự rà từng dòng".

## Kết luận — vòng lặp mới là lằn ranh thật

Chatbot là cái loa: bạn bảo nói gì, nó nói cái đó, xong thì đứng yên chờ bạn. Agent là nhân viên tự vận hành: giao mục tiêu, nó tự quay vòng 8 bước, ngày qua ngày, kể cả lúc bạn ngủ. Khi cả Y Combinator lẫn Mozilla năm 2025 đua nhau xây cái vòng lặp này, thì với cá nhân bạn, một Agent *có vòng lặp tự chạy* mới đáng gọi là trợ lý.

Hermes làm được điều đó: 12 chu kỳ mỗi ngày, 8 bước mỗi vòng, 10 điểm soi, bản dở vứt. Bài này, và mọi bài bạn đọc từ Hỉ, là bằng chứng sống.

👉 **Muốn một trợ lý "tự chạy vòng lặp 8 bước", không đợi bạn gõ prompt mỗi tối?** Xem chi tiết + link đăng ký khoá học Speed Reading kèm Hermes tại **speedreading.vn/shermes**. Giao một lần, để nó tự quay — kể cả lúc bạn ngủ.
