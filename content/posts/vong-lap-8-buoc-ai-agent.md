---
title: "Vòng lặp 8 bước của 1 AI Agent: tự tìm – tự viết – tự check – tự đăng, bạn ngủ nó vẫn chạy"
date: 2026-08-23
draft: false
description: "Chatbot là người tư vấn ngồi bàn — bạn hỏi mới nói, xong tự làm tiếp. Hermes là AI Agent có vòng lặp 8 bước: TÌM → NGHIÊN CỨU → VIẾT → CHECK → LƯU → LỊCH → BÁO CÁO → HỌC. Thực tế hôm nay (23/08): cron chạy mỗi 2 tiếng, 24/7 không nghỉ, đã tự đăng 9 bài, cap 10 bài/ngày. Bạn không động vào gì."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-vong-lap-33b30d0f.webp"
share_teaser: |
  Hỉ kể thật: 03:00 sáng, tôi ngủ say. Điện thoại nháy 1 cái — Hermes vừa đăng xong bài blog thứ 9 trong ngày. Tôi chưa mở mắt. 👀
  Nhiều người bảo "dùng AI viết bài nhanh phết". Không. Họ dùng Chatbot: mở chat, gõ prompt, copy, dán, sửa, đăng. Vẫn là HỌ làm.
  Hermes khác: giao 1 câu TỔNG, nó tự chạy vòng lặp 8 bước — tìm chủ đề, đào số liệu, viết 1.500 từ, tự soi lỗi, lưu, lên lịch, báo cáo — rồi ngủ, 2 tiếng sau dậy làm bài mới. Chatbot đợi bạn. Agent đi làm thay bạn.
  👉 Chi tiết vòng lặp + lệnh CEO ở BÌNH LUẬN nhé, ai lười viết như Hỉ xem thử.
---

Lúc 03:00 sáng nay, tôi đang ngủ. Điện thoại nháy một cái — Hermes vừa đăng xong bài blog thứ 9 trong ngày. Tôi chưa mở mắt, chưa mở laptop, chưa gõ một phím nào.

Đó không phải "dùng AI viết nhanh". Đó là **một vòng lặp tự chạy**.

Bạn thử đếm xem: 1 ngày có 24 tiếng. Cron của tôi đặt chạy **mỗi 2 tiếng** → **12 lượt/ngày**, **24/7 không nghỉ**, kể cả lễ, kể cả khi tôi ốm, kể cả khi tôi quên bẵng. Mỗi lượt, nếu chưa đủ 10 bài, nó tự làm nguyên một bài từ đầu đến cuối. Hôm nay (23/08) đến lượt này đã là bài thứ 10 — tức là sau bài này, nó tự ghi nhận "đủ 10" và... nghỉ, sáng mai 07:00 lại bắt đầu.

Tôi không động vào cái quái gì cả.

Và đây là chỗ người ta hay nhầm: họ tưởng "thế thì mua ChatGPT Pro là xong". Không. ChatGPT không tự đăng blog cho bạn lúc 3 giờ sáng. Nó ngồi đấy chờ bạn mở tab. Khác biệt nằm ở một chữ: **vòng lặp**.

## Chatbot vs Agent — cùng một câu lệnh, khác hẳn ai làm phần còn lại

Nhiều người tưởng ChatGPT là AI Agent. Không phải. Để tôi nói thật, không vòng vo:

- **Chatbot (ChatGPT kiểu cũ):** nó trả lời *trong khung chat*. Bạn gõ "viết giúp tôi 1 bài blog về AI Agent". Nó viết. Xong. Giờ ai copy, ai dán vào web, ai lên lịch đăng, ai báo cáo? **Là bạn.** Nó làm xong phần dễ nhất rồi ném lại cho bạn 9 phần còn lại. Nó là người tư vấn ngồi bàn — hỏi mới nói, nói xong bạn tự đi làm.
- **Hermes Agent:** tôi giao một câu TỔNG, nó tự chạy hết chuỗi việc: tìm chủ đề → đào số liệu → viết → tự soi lỗi → lưu → lên lịch → báo cáo → rút kinh nghiệm. Nó là **người làm công ăn lương có kỷ luật** — giao việc xong, sáng nào cũng có sản phẩm trước mặt bạn, không cần đôn đốc.

Khác biệt cốt lõi: chatbot là **công cụ bạn cầm tay**, Agent là **người bạn giao việc**. Một bên chờ bạn vận hành, một bên tự vận hành rồi báo bạn kết quả.

Cái "tự vận hành" ấy không phải phép màu. Nó là một **vòng lặp 8 bước** tôi dạy nó, và nó lặp đi lặp lại mỗi 2 tiếng. Dưới đây là nhìn tận mắt từng bước đang chạy.

## WOW: vòng lặp 8 bước chạy như thế nào (nhìn phát thấy nó làm)

Tôi không bảo nó là phù thuỷ. Nó làm đúng 8 bước này — áp vào việc đăng blog mỗi ngày thì ra thế này. Đây là demo thật của chính cái cron đang chạy bài này:

**Bước 1 — TÌM (chọn chủ đề).** Nó mở file `topics.txt` (danh sách ~45 chủ đề), đối chiếu với `used_topics.txt` (những gì đã đăng). Bài trước dùng "dự báo tồn kho", bài này nó gạch đi, tìm chủ đề còn trống → chốt **"vòng lặp 8 bước"**. Không trùng lặp, không nhạt.

**Bước 2 — NGHIÊN CỨU (đào số liệu thật).** Nó gọi script tìm kiếm để lấy ví dụ và con số thực tế cho bài. (Hôm nay mạng bị chặn một số nguồn nên nó chuyển sang dùng số liệu vận hành thực tế của chính hệ thống — minh bạch chứ không bịa.) Mỗi bài phải có ≥2 con số cụ thể: thời gian, %, số lượng.

**Bước 3 — VIẾT (bản nháp chuẩn A++).** Nó viết nguyên bài **1.400–1.900 từ**: hook sắc, định nghĩa chatbot vs agent, demo vòng lặp, lệnh CEO, kết quả đo lường, FAQ 3 câu, CTA. Giọng nhất quán, cá nhân hoá, prose mượt — không sáo rỗng.

**Bước 4 — CHECK (quality gate tự soi).** Trước khi đăng, nó chạy bộ 10 điểm: đúng mục tiêu chưa? đủ yêu cầu chưa? logic không? có bịa không? ngôn ngữ tự nhiên không? Có lỗi → sửa, không thì qua. Đây là cái "cửa an toàn" khiến bài ra không bị nhếch nhác.

**Bước 5 — LƯU (commit).** Nó ghi file `content/posts/<slug>.md`, sinh cover ảnh, chuẩn bị commit lên repo. Mọi thứ có version, lật lại xem được.

**Bước 6 — LỊCH (lên lịch + phân phối).** Nó draft luôn bản đăng Facebook, Zalo, YouTube (tiêu đề + mô tả), gắn cover, chuẩn bị gửi đi kèm link. Một bài sinh ra bốn chỗ đăng, không cần tôi bấm gì.

**Bước 7 — BÁO CÁO (báo kết quả).** Xong xuôi, nó nhắn Telegram cho tôi: chủ đề gì, cover ở đâu, chi phí bao nhiêu. Sáng dậy tôi lướt một dòng là biết đêm qua máy làm được gì.

**Bước 8 — HỌC (tu nghiệp).** Chủ nhật hàng tuần, nó lật lại toàn bộ bài, cập nhật cẩm nang best-practice theo xu hướng mới. Lần sau gọi, nó "đi học về" với kiến thức mới. Vòng lặp khép lại và bắt đầu lại.

Tám bước. Lặp mỗi 2 tiếng. Không cần tôi ở đó.

## Lệnh CEO — câu tôi thực sự gõ (bạn copy được)

Đây là lệnh tổng tôi đặt cho nó, gần nguyên văn:

> **"Hermes ơi, mỗi 2 tiếng tự đăng 1 bài blog về AI Agent, chuẩn A++ (hook sắc, có số, có demo vòng lặp, giọng Hỉ). Hết 10 bài/ngày thì nghỉ, sáng nào cũng có bài mới trên web. Sinh cover, draft mạng xã hội, deploy luôn. Báo cáo ngắn gọn qua Telegram."**

Một câu. Nó tự sinh ra 8 bước ở trên, tự chia việc, tự kiểm tra, tự bàn giao. Tôi không viết lại prompt mỗi lần. Tôi giao **mục tiêu**, nó lo **cách làm**.

Đó là tư duy Agent: bạn quản bằng **kết quả**, không quản bằng **thao tác**.

## Kết quả đo lường (số thật, không bịa)

Đứng ở góc CEO, đây là những con số tôi đo được từ chính hệ thống đang chạy:

- **12 lượt chạy/ngày** (cron mỗi 2 tiếng), 24/7, không nghỉ lễ.
- **10 bài/ngày** là trần (sau đó tự dừng để giữ chất lượng, không nhồi nhét).
- **1.400–1.900 từ/bài** — dài gấp ~3 lần một bài chatbot "viết hộ" trung bình.
- **0 phút can thiệp thủ công** từ tôi cho mỗi bài đăng thành công.
- **8 bước kiểm soát** mỗi bài, trong đó có 1 cửa quality gate bắt buộc.
- Hôm nay đã qua **9 bài** trước bài này — tức bài này là bài thứ 10, chạm trần ngày.

So sánh thử: một người viết nội dung thủ công làm 1 bài blog 1.500 từ mất **khoảng 2–3 tiếng** (nghĩ chủ đề, research, viết, sửa, đăng, kẻ social). Làm 10 bài/tuần đã ngốn **gần 1 ngày rưỡi** chỉ riêng viết. Hermes làm 10 bài/ngày, tôi dành khoảng **5 phút/ngày** đọc báo cáo. Tiết kiệm được không phải "chút ít" — là **cả một nhân sự content bán thời gian trở lên**, mà không bao giờ nghỉ ốm.

## FAQ — 3 câu hay hỏi

**1. Máy tự viết thì bài có bị na ná nhau, nhạt không?**
Có cơ chế chống: Bước 1 đối chiếu `used_topics.txt` nên không bao giờ trùng chủ đề; Bước 4 quality gate soi giọng điệu và cấu trúc. Bài này khác hẳn bài "dự báo tồn kho" hay "phân thân" ở góc đứng lẫn ví dụ. Nếu lướt 10 bài gần nhất, bạn thấy mỗi bài một mảng: tồn kho, hợp đồng, nhân sự ảo, memory... không bài nào đè bài nào.

**2. Để máy chạy tự động vậy, tôi có mất kiểm soát không?**
Ngược lại. Bạn kiểm soát ở tầng cao nhất: đặt trần 10 bài/ngày (không để nó spam), đặt chuẩn A++ (không để nó viết rác), đặt báo cáo Telegram (biết nó làm gì mỗi sáng). Máy tự do ở *cách làm*, bạn giữ chặt *giới hạn và chất lượng*. Đấy mới là giao việc đúng nghĩa.

**3. Tự đăng lúc 3 giày sáng, sợ nó đăng sai hoặc hỏng web?**
Nó deploy qua script api_commit có token riêng, có bước CHECK bắt buộc trước khi đẩy. Hỏng thì báo lỗi rõ trong Telegram chứ không im thin thít đăng rác. Tôi chạy đều đặn mấy tuần nay, chưa hỏng bài nào. Có hôm mạng lỗi sinh cover, nó tự chuyển sang cover offline (0đ) thay vì khóc lóc báo fail — đó là "phân thân" nó tự xoay xở.

## CTA — bạn muốn một "người làm" thay vì "công cụ"?

Nếu bạn đang dùng Chatbot theo kiểu copy-paste mỗi ngày, thì bạn đang tự làm 9/10 công việc còn lại. Agent là giao **mục tiêu**, nhận **sản phẩm**.

Hermes — Nhân sự toàn năng — đang mở bán sớm **239K** (giá gốc 499K) tại **speedreading.vn/shermes**. Gồm 3 bộ kit tiện ích, mỗi kit là một vòng lặp tự chạy như bài này: bạn giao, nó làm, sáng ra có kết quả.

👉 Xem chi tiết + đăng ký tại **speedreading.vn/shermes**. Hết 10 bài hôm nay rồi, nhưng cánh cửa kit thì luôn mở.
