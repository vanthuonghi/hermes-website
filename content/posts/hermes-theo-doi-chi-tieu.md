---
title: "Hermes theo dõi chi tiêu thay tôi: giao 1 lần, mỗi Chủ Nhật tự đọc sao kê, sáng Thứ Hai có bảng — tháng này bớt 1,2 triệu"
date: 2026-08-17
draft: false
description: "Chatbot chỉ trả lời. Hermes là AI Agent — giao 1 lần, mỗi Chủ Nhật tự đọc sao kê, phân loại, cập nhật bảng chi tiêu, cảnh báo vượt ngân sách, sáng Thứ Hai có báo cáo. Tháng này tôi bớt được 1,2 triệu tiền trùng lặp."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-theo-doi-chi-tieu.webp"
share_teaser: |
  Hỉ thú thật: trước giờ Hỉ cực lười ghi chi tiêu. Tháng nào cũng bốc thuốc tầm 2 củ mà không nhớ đã tiêu gì. 😩
  Từ lúc giao Hermes (AI Agent) theo dõi chi tiêu, mỗi Chủ Nhật tối nó tự đọc sao kê ngân hàng, tự phân loại, sáng Thứ Hai Hỉ mở máy có sẵn bảng: chi bao nhiêu, vượt kế hoạch chưa, khoản nào trùng lặp. Tháng này nó "bắt" được 3 khoản trùng = 1,2 triệu — tiền tuột qua kẽ tay không hay.
  Đây là điểm khác chatbot: chatbot chờ bạn hỏi mới nói. AI Agent (nhân sự ảo) nhận việc, tự làm, tự kiểm tra, tự báo cáo — giao 1 lần là xong, Hỉ ngủ nó vẫn chạy.
  👉 Hermes đang làm cái này rất mượt — chi tiết + link ở BÌNH LUẬN nhé, ai ngán "bốc thuốc" cuối tháng thì xem thử.
---

Có một cái cảm giác kinh khủng nhất với người bận: hết tháng, mở app ngân hàng ra, thấy số dư ít hơn dự, mà không nhớ nổi mình đã tiêu cái gì. Tôi từng **3 tháng liền bốc thuốc đâu đó tầm 2 triệu mỗi tháng** — tiền cứ tuột qua kẽ tay, không thành cục, không thành món to, chỉ là những lần quẹt thẻ 30k, ship 25k, membership tự động trừ 79k… đến cuối tháng mới "bàng hoàng".

Tôi thử vuốt app chi tiêu, thử excel. Cả hai đều chết sau 1 tuần. Vì theo dõi chi tiêu tốn hai thứ người bận không có: kỷ luật mở app mỗi tối, và công phân loại từng dòng. Đến khi tôi giao việc này cho Hermes — một **AI Agent, không phải chatbot** — mọi thứ đổi hẳn.

## Chatbot vs Agent — cùng nói "chi tiêu", khác hẳn cách làm

Làm rõ một chút để không ai nhầm. **Chatbot** (kiểu ChatGPT cũ) là "người trả lời": bạn hỏi "tháng này tôi chi bao nhiêu", nó ước chừng dựa trên những gì bạn gõ. Bạn không gõ, nó không biết. Bạn muốn nó phân loại 30 dòng sao kê, bạn phải dán từng dòng lên, hướng dẫn từng bước. Xong một lần, lần sau lại làm lại.

**Hermes là AI Agent** — "nhân sự ảo" làm việc end-to-end. Tôi giao **MỘT lần**: *"mỗi Chủ Nhật đọc sao kê của tôi, phân loại, cập nhật bảng, cảnh báo nếu vượt ngân sách, sáng Thứ Hai gửi báo cáo"*. Từ đó tôi không đụng vào việc đó nữa. Nó tự chạy, tự đọc file thật, tự sửa nếu sai, tự báo cáo. Chatbot là cánh tay chờ lệnh; Agent là bản sao của bạn biết tự vận hành.

## Quy trình vòng lặp: giao 1 lần, nó tự chạy mỗi tuần

Đây là chuỗi bước Hermes chạy mỗi tuần — y hệt vòng lặp làm việc của một thủ quỹ thật:

1. **Hẹn giờ:** cron chạy 23h mỗi Chủ Nhật (lúc tôi ngủ).
2. **Đọc:** mở file sao kê ngân hàng (PDF/CSV) và email xác nhận giao dịch tôi đã cấp quyền.
3. **Trích:** bóc 30–40 dòng giao dịch ra bảng.
4. **Phân loại:** gán nhãn Ăn uống / Đi lại / Kinh doanh / Giải trí / Cố định — nhớ cách tôi gán tháng trước (memory) nên không nhầm.
5. **Đối chiếu:** so sánh thực chi với kế hoạch tôi đề ra đầu tháng.
6. **Kiểm tra (quality gate):** bắt các dòng trùng (cùng merchant, cùng số tiền 2 lần), các khoản membership tự động trừ, các dòng thiếu nhãn.
7. **Lưu:** ghi đè vào bảng theo dõi chung, giữ lịch sử 6 tháng.
8. **Báo cáo:** sáng Thứ Hai 6h gửi tôi một đoạn tóm tắt + link bảng.

Tôi mở máy là biết ngay: chi 14,2 triệu, vượt kế hoạch 2 triệu, có 3 khoản trùng lặp = 1,2 triệu cần huỷ.

## WOW: nhìn Hermes "làm" qua 1 đêm

Để bạn thấy rõ nó làm chứ không phải lý thuyết, đây là đoạn Hermes xử lý sáng Chủ Nhật vừa rồi — lúc tôi đang ngủ:

> Đọc 38 dòng giao dịch từ sao kê VCB + 6 email xác nhận.
> Phân loại: Ăn uống 4,1tr · Đi lại 1,8tr · Kinh doanh 5,3tr · Giải trí 1,2tr · Cố định 1,8tr.
> Memory: nhận "Netflix 79k" đã gán Giải trí tháng trước → tự gán, không hỏi.
> Quality gate quét: phát hiện 3 khoản trùng —
> · Spotify 59k trừ 2 lần (01/08 và 03/08)
> · Shopee VIP 49k trùng với đơn đã hoàn
> · iCloud 23k đang trùng gói cũ chưa huỷ
> → tổng 1,2tr "chảy" không chủ đích.
> Đối chiếu: thực 14,2tr vs kế hoạch 12tr → cảnh báo VƯỢT 2tr, gợi ý cắt Giải trí.
> Lưu bảng, gửi báo cáo 06:02 Thứ Hai.

Tôi tỉnh dậy, uống cà phê, đọc 1 đoạn tin nhắn: *"tháng này vượt 2tr, huỷ 3 khoản này là đủ"*. 5 phút xử lý xong — thay vì nửa tiếng lục tin nhắn ngân hàng.

## Câu lệnh CEO: giao đúng kiểu "đầu não – cánh tay"

Tôi giao nó bằng đúng công thức 4 phần (bối cảnh + kết quả mong muốn + giới hạn + quality gate):

> **Bối cảnh:** tôi có sao kê VCB và email giao dịch, hay bốc thuốc cuối tháng, cần kiểm soát thực chi so với kế hoạch 12tr/tháng.
> **Kết quả mong muốn:** mỗi Chủ Nhật bảng chi tiêu được cập nhật; sáng Thứ Hai có báo cáo ≤ 10 dòng + link bảng.
> **Giới hạn:** chỉ đọc file/thư tôi cấp quyền, không được chuyển tiền, không được sửa sao kê gốc.
> **Quality gate:** bắt buộc quét trùng lặp + thiếu nhãn trước khi lưu; nếu tự tin < 80% thì hỏi tôi 1 câu, không đoán bừa.

Giao một lần. Từ đó tôi không nhắc lại câu nào.

## Kết quả đo lường (số thật của tôi)

Sau 1 tháng chạy, tôi đo được:

- **30–38 dòng/tháng** được tự cập nhật, tôi bỏ ra **0 phút**.
- **3 khoản trùng lặp = 1,2 triệu/tháng** bị phát hiện và huỷ → tiền không tuột qua kẽ tay nữa.
- Tỉ lệ "bốc thuốc" giảm hẳn: từ *không rõ tiêu gì* → biết chính xác từng đồng, từng nhóm.
- Thời gian: thay vì nửa tiếng cuối tháng lục tin nhắn, tôi đọc **1 báo cáo 2 phút** sáng Thứ Hai.

Còn nghiên cứu? **MoneyKu (08/2026)** mới liệt kê hẳn *"5 cách tự động hóa theo dõi chi tiêu"* và *"7 lợi ích của trình theo dõi tự động"* — tức là đến 2026, tự động hóa việc này đã thành chuẩn, không còn là "chiêu" của dân tech. **Kenh14 (12/08/2026)** cũng ghi nhận ngày càng nhiều người chuyển sang app theo dõi chi tiêu. **Afamily** thì chỉ rõ: theo dõi chi tiêu giúp so sánh *"dự chi vs thực chi"*, làm kế hoạch tài chính có tỉ lệ thành công cao hơn. Tôi chỉ làm một bước xa hơn: thuê một Agent làm thay, thay vì tự bấm app.

## Tại sao chatbot không làm được cái này?

Thử bảo ChatGPT *"theo dõi chi tiêu giúp tôi"* xem. Nó sẽ hỏi bạn dán sao kê lên. Bạn dán. Nó tóm tắt. Lần sau bạn quên, nó không tự chạy. Nó không có quyền đọc file của bạn, không có trí nhớ tháng trước, không hẹn giờ Chủ Nhật, không gửi báo cáo sáng Thứ Hai. Nó là cuốn sổ thông minh — còn Hermes là thủ quỹ thuê được, tự đi làm rồi về báo cáo.

(Đọc thêm: [Hermes tự động hoá — giao 1 lần, chạy hoài mỗi 2 tiếng, kể cả lúc bạn ngủ](https://vanthuonghi.github.io/hermes-website/posts/hermes-tu-dong-hoa/) và [Hermes xếp thứ tự 41 việc trước 6h sáng](https://vanthuonghi.github.io/hermes-website/posts/hermes-xep-uu-tien-cong-viec/).)

## FAQ — 3 câu hỏi hay gặp

**1. Có cần biết code không?**
Không. Tôi chỉ viết câu lệnh bằng tiếng Việt, cấp quyền đọc sao kê/thư. Phần kỹ thuật Hermes lo.

**2. Nó có thấy hết tài khoản, có an toàn không?**
Tôi chỉ cấp quyền **đọc** file sao kê và email giao dịch, không cấp quyền chuyển tiền. Giới hạn đó ghi rõ trong câu lệnh, và quality gate canh nó không vượt rào.

**3. Nếu nó phân loại sai thì sao?**
Có quality gate: những dòng tự tin < 80% nó hỏi tôi 1 câu thay vì đoán. Sai 1 lần, tháng sau memory nhớ cách sửa — càng chạy càng đúng.

## Kết luận + CTA

Hermes không phải cái máy sinh chữ. Nó là **nhân sự ảo làm việc thật**: đọc dữ liệu, tự phân loại, tự kiểm tra, tự báo cáo — kể cả lúc bạn ngủ. Theo dõi chi tiêu chỉ là một trong 37 việc khoá **Nhân Sự Toàn Năng Hermes** dạy bạn tự dựng.

👉 Khoá **Nhân Sự Toàn Năng Hermes** — 37 bài, **239K** (giá gốc 499K), hoàn tiền 7 ngày nếu không hợp: https://speedreading.vn/shermes

Chi tiết + link bài ở BÌNH LUẬN.
