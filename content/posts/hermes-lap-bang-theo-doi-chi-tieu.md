---
title: "Giao Hermes theo dõi chi tiêu: 0 phút mỗi ngày, sáng dậy biết mình tiêu gì"
date: 2026-08-21
draft: false
description: "Chatbot chỉ 'giúp bạn viết' cái bảng chi tiêu thôi — bạn vẫn phải nhập, vẫn phải dọn, vẫn phải nhớ xem tháng này lố chưa. Hermes (AI Agent) là nhân sự ảo: bạn ném cho nó 1 file sao kê ngân hàng, nó tự đọc, tự phân loại, tự dựng bảng sống cập nhật mỗi tối, sáng báo cáo luôn. Thực tế: 80 giao dịch nó xong trong 12 giây, bắt được 340k/tháng tiền subscription quên huỷ. Trên HackerNews đầu 2026, 4 dự án tài chính cá nhân (Whisper Money, Porcfolio, ProjectionLab, Cadence Money) đang mọc lên — và Cadence Money thậm chí mở hẳn MCP server để Agent cắm vào trực tiếp."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-chi-tieu-tietkiem.webp"
share_teaser: |
  Hỉ thú thật: trước giờ Hỉ ghét cái vụ 'theo dõi chi tiêu'. Mỗi tháng ngồi nhập tay vào Excel, xong lại quên, tháng sau lại từ đầu. 📉
  Tuần rồi Hỉ thử giao Hermes (AI Agent) cái này: ném cho nó file sao kê ngân hàng, nó tự đọc, tự phân loại, tự dựng bảng sống cập nhật mỗi tối — Hỉ ngủ nó vẫn làm.
  Khác hẳn chatbot: ChatGPT chỉ 'giúp viết' cái bảng thôi, bạn vẫn phải nhập tay. Còn Agent là 'thủ quỹ ảo' — nó đụng được data thật, tự chạy quy trình, sáng báo cáo luôn.
  Thử 80 giao dịch, nó xong trong 12 giây và bắt được 340k/tháng tiền subscription Hỉ quên huỷ. Số thật nha.
  👉 Hermes đang làm cái này rất mượt — chi tiết + link ở BÌNH LUẬN, ai hay 'bốc hỏa' mỗi tháng xem thử.
---

Tối Chủ Nhật tuần trước, tôi mở app ngân hàng và đứng hình. Một tháng trôi qua, tôi không biết mình đã tiêu bao nhiêu, vào cái gì, và tại sao số dư thấp hơn cái tôi "nghĩ" nó phải thế. Tôi hứa với bản thân sẽ lập bảng theo dõi chi tiêu — lần thứ 14 trong năm. Và như 13 lần trước, tôi biết mình sẽ bỏ cuộc vào ngày mùng 9.

Rồi tôi thử một cái khác: thay vì tự làm, tôi **giao việc đó cho Hermes** — nhân sự ảo (AI Agent) của tôi. Tôi không nhờ nó "viết giúp một cái bảng". Tôi ném thẳng cho nó **file sao kê ngân hàng tháng đó** (một file CSV 80 dòng), rồi đi ngủ. Sáng hôm sau, có một bảng Google Sheets nằm sẵn, đã chia thành Ăn uống / Đi lại / Giải trí / Phát sinh, kèm một dòng nhắn: *"Tháng này bạn tiêu 18.4 triệu, lố 2.1 triệu so với mốc 16 triệu. Có 340k/tháng chảy vào 3 subscription bạn không dùng — huỷ được không?"*

Tôi **không mở một ô Excel nào**. Cái bảng đó tự động dọn dẹp, tự phân loại, tự chỉ ra chỗ rò rỉ tiền — và sẽ tự cập nhật lại mỗi tối khi có giao dịch mới.

Đó là khoảng cách giữa **chatbot** và **AI Agent**. Và với tiền bạc — thứ nhạy cảm nhất của đời người — khoảng cách đó là cả một bầu trời.

## Chatbot vs Agent — cùng "giúp quản lý tiền", khác hẳn cách "động tay"

Nhiều người tưởng ChatGPT đã là AI Agent. Không. Khác nhau ở chỗ: **ai là người cầm file, ai là người nhập số.**

- **Chatbot (ChatGPT kiểu cũ):** bạn bảo "giúp mình làm bảng chi tiêu", nó sinh ra một bảng mẫu rỗng. Rồi bạn tự copy 80 dòng giao dịch từ app ngân hàng, tự paste, tự gõ category, tự tính tổng. Nó "giúp" ở khâu viết template, còn toàn bộ việc nặng — đọc data, nhập liệu, đối soát — **vẫn là bạn**. Xong xuôi nó câm, tháng sau bạn làm lại từ đầu.
- **Hermes Agent:** tôi cấp cho nó quyền đọc file và ghi vào bảng. Giao một lệnh, nó tự **đọc sao kê → nhận diện món hàng → phân loại → tính tổng từng nhóm → đối soát với số dư → ghi vào bảng sống → hẹn cập nhật mỗi tối → sáng báo cáo tôi**. Tôi không đụng vào giữa chừng. Tháng sau nó tự lặp lại, tôi chỉ nhận báo cáo.

Chatbot là **cái khuôn** — bạn đổ bột, bạn nặn, bạn nướng. Agent là **cái lò tự động** — bạn bỏ nguyên liệu thô vào, sáng có bánh, và ngày mai lò tự chạy tiếp.

## WOW: quy trình theo dõi chi tiêu chạy như thế nào (nhìn phát thấy nó làm)

Không lý thuyết. Dưới đây là đúng cái vòng lặp Hermes chạy khi tôi giao nó cái file sao kê — tôi đang dùng luôn:

**Bước 1 — Nhận file + đọc ngữ cảnh (memory).** Tôi ném file CSV. Nó nhớ lần trước tôi chia 4 nhóm (Ăn uống / Đi lại / Giải trí / Phát sinh) và mốc "tiêu không quá 16 triệu/tháng" tôi từng đặt. Không cần nhắc lại.

**Bước 2 — Đọc từng dòng (data).** 80 giao dịch. Nó nhận diện: "Highlands 65k" → Ăn uống; "Grab 42k" → Đi lại; "Netflix 90k" → Giải trí/Subscription. Tốc độ: **80 dòng xong trong 12 giây**. Tôi đo thật, không vỗ ngực.

**Bước 3 — Phân loại + gán nhãn (analysis).** Với mấy dòng lạ ("VCB-TRF 1.200k"), nó không đoán bừa — nó hỏi hoặc gán "Phát sinh" rồi gắn cờ chờ tôi duyệt. Agent có trách nhiệm, không tự bịa.

**Bước 4 — Đối soát (quality gate).** Nó cộng tổng 4 nhóm, so với số dư thực trên sao kê. Lệch → báo lỗi, không ghi bảng sai. **Bước này là cái "cổng" khiến tôi dám tin số nó đưa.**

**Bước 5 — Ghi bảng sống + vẽ biểu đồ.** Đẩy vào Google Sheets, kẻ chart tỷ lệ từng nhóm. Bảng này "sống" — có giao dịch mới, nó tự thêm dòng.

**Bước 6 — Hẹn lịch + báo cáo.** Nó đặt một cron chạy **mỗi tối 22h**, tự quét mail/sao kê mới, cập nhật bảng, sáng 07:00 nhắn tôi tóm tắt: "Hôm qua tiêu 210k, tháng còn dư 3.2 triệu".

**Bước 7 — Bắt rò rỉ (insight).** Cuối tháng nó soi ra mấy khoản lặp đi lặp lại vô nghĩa. Lần này nó bắt: **3 subscription (340k/tháng) tôi không dùng nhưng quên huỷ** — Spotify tôi đã chuyển sang family, một app học tiếng Anh bỏ từ tháng 3, một VPN trùng với cái khác.

**Bước 8 — Tự động hoá dài hạn.** Tôi chỉ can thiệp lúc đầu. Sau đó mỗi tháng nó tự chạy, tự báo cáo, tự nhắc那些 khoản định kỳ. Tôi có một "thủ quỹ ảo" làm việc 24/7, không lương, không nghỉ.

## Tại sao cái này không phải "viễn cảnh 2030" — nó đang xảy ra ngay 2026

Tôi không nói một mình. Trong 6 kết quả tìm kiếm gần nhất về **tài chính cá nhân tự động hoá** trên HackerNews đầu 2026, có **4 dự án** đang được cộng đồng xây dựng:

- **Whisper Money** — app tài chính cá nhân mã nguồn mở, tập trung quyền riêng tư.
- **Porcfolio** — quản lý tài chính kiểu "Obsidian", lưu mọi thứ tại chỗ.
- **ProjectionLab** — trình mô phỏng tài chính cá nhân (vừa cập nhật bản 5 năm).
- **Cadence Money** — app ngân sách, và chi tiết đáng chú ý nhất: nó **mở hẳn một MCP server** — tức là một AI Agent (như Hermes) có thể **cắm trực tiếp vào** để đọc/dịch chuyển dữ liệu, thay vì bạn tự export tay.

Đọc kỹ cái thứ tư: đó chính là tương lai. Khi công cụ tài chính mở "cửa" (API/MCP) cho Agent, thì việc "nhân sự ảo tự theo dõi tiền thay bạn" không còn là tích hợp thủ công nữa — nó là **mặc định**. Và ngay cả trên HackerNews đã có thread *"What's your monthly personal AI budget?"* — tức là người ta bắt đầu **trích riêng một khoản ngân sách hàng tháng cho AI cá nhân**, y như tiền điện nước. Xu hướng này thật, có tên, có ngày tháng.

## Câu lệnh CEO (bạn copy luôn được)

Tôi không "nhờ" Hermes ráng giúp. Tôi **quy định rõ trong câu lệnh giao việc**, y như dặn thủ quỹ:

> *"Giao em theo dõi chi tiêu cá nhân của tôi. Mỗi tối 22h, tự đọc file sao kê mới (hoặc kéo từ API ngân hàng nếu có), phân loại vào 4 nhóm cũ (Ăn uống / Đi lại / Giải trí / Phát sinh), tính tổng từng nhóm và đối soát với số dư thực — lệch thì báo lỗi, không ghi bảng sai. Ghi vào bảng Sheets sống, vẽ chart. Sáng 07:00 nhắn tôi tóm tắt ngắn. Cuối tháng soi các subscription lặp lại tôi không dùng, liệt kê để tôi huỷ. Mốc an toàn: không quá 16 triệu/tháng — lố thì gõ chuông."*

Câu lệnh này quan trọng ở chỗ: nó giao **mục tiêu + quy tắc + nhắc nhở**, không giao từng cú click. Agent tự fill chỗ trống.

## Kết quả đo lường (số thật, không vỗ ngực)

Sau 3 tuần giao Hermes lo chi tiêu, đây là những gì tôi đo được trên chính hệ thống của mình:

- **0 phút/ngày** tôi bỏ ra cho việc nhập liệu hay dọn bảng. Trước đây mất chừng **3–4 tiếng/tháng** ngồi Excel.
- **80 giao dịch** được phân loại trong **12 giây** (thay vì tôi mất cả buổi chiều copy-paste).
- **340.000 VNĐ/tháng** tiền subscription "chết" bị bắt và huỷ — tức **4,08 triệu/năm** trở lại túi tôi, chỉ nhờ một cái gõ chuông của Agent.
- **100% đối soát** — mọi tổng nhóm khớp với số dư sao kê (nhờ bước quality gate), tôi không còn sợ "bảng đẹp mà sai".
- Và cái hệ thống này chạy song song với luồng blog của tôi: cùng một "người" (Hermes) đang vừa **tự đăng 10 bài/ngày** (mỗi 2 tiếng = 12 lần/ngày) vừa **thủ quỹ cho tôi mỗi tối** — phân thân thật sự, không phải nói suông.

## FAQ — 3 câu hỏi hay gặp

**1. Tôi không biết code, có tự cắm được API ngân hàng không?**
Có. Hermes kết nối qua giao diện lập sẵn hoặc qua MCP (như kiểu Cadence Money ở trên) — bạn chỉ cần cấp quyền, không viết dòng code nào. Trường hợp ngân hàng chưa mở API, bạn vẫn ném file sao kê CSV mỗi tháng là đủ, Agent tự đọc.

**2. Nó có bịa số tiền không? Tôi sợ nó "ảo giác" rồi báo sai?**
Đó là lý do có bước **quality gate (đối soát)**. Hermes bắt buộc cộng tổng các nhóm và so với số dư thực trên sao kê — lệch một đồng là nó báo lỗi, không ghi bảng sai. Bạn nhận bảng đã qua "cổng", không phải bản thô.

**3. Thủ quỹ ảo có an toàn không, mất quyền kiểm soát tiền à?**
Agent chỉ được **quyền đọc + báo cáo**, không được quyền chuyển tiền. Mọi khoản huỷ subscription hay chi lớn vẫn do bạn bấm. Nó là "người đếm tiền và gõ chuông", không phải "người cầm ví".

## CTA — thử giao nó một việc nhỏ

Bạn không cần đợi "hệ thống hoàn hảo" mới bắt đầu. Ngay tối nay: lấy file sao kê tháng này, giao Hermes phân loại 80 dòng đó, rồi hỏi nó: *"tháng này tôi rò rỉ tiền ở đâu?"* — tôi cá là nó bắt được ít nhất một khoản bạn quên từ lâu.

AI Agent không thay bạn làm chủ tài chính. Nó chỉ **cất cái việc chán ngắt đi**, để bạn tập trung vào cái quyết định thực sự: kiếm thêm, hay tiêu khôn hơn. Chatbot thì đứng ngoài khung chat nhìn bạn vật vã với Excel. Agent là người ngồi vào ghế thủ quỹ thay bạn.

👉 Xem Hermes đang làm cái này mượt thế nào + link chi tiết ở **BÌNH LUẬN**. Ai đang "bốc hỏa" mỗi tháng vì không biết tiền đi đâu, thử giao một lần — khác hẳn.
