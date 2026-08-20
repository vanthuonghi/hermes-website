---
title: "1 bài cũ = 5 bài mới: Cho AI Agent viết lại content cũ, rảnh tay mà blog vẫn lớn"
date: 2026-08-21
draft: false
description: "Chatbot chỉ viết khi bạn bảo. Hermes là AI Agent — đọc toàn bộ kho bài cũ của bạn, tự tìm góc nhìn mới, viết lại thành nhiều bài, tối ưu SEO, lên lịch đăng và báo cáo. 40 bài cũ thành 87 bài mới trong một buổi chiều, thời gian viết mỗi bài từ 3 tiếng xuống 22 phút."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-viet-lai-noi-dung.webp"
share_teaser: |
  Hỉ có một "nghĩa địa" content: 40 bài blog viết năm ngoái, xong để đấy, chẳng ai đọc nữa.
  Tuần trước Hỉ thử giao cho Hermes (AI Agent) cái kho đó. Nó đọc hết 40 bài, tự tìm ra mỗi bài có thể viết lại theo 2 góc nhìn mới, rồi... 1 buổi chiều có 87 bài mới sẵn sàng đăng. Hỉ chỉ ngồi duyệt.
  Điểm khác chatbot: ChatGPT bạn phải bảo "viết lại bài này" từng cái. Còn Agent giao 1 lần: đọc hết -> tìm góc nhìn -> viết lại -> tối ưu -> lên lịch -> báo cáo. Bạn không rờ tới giữa chừng.
  👉 Hermes đang làm cái này mượt thật — chi tiết + link ở BÌNH LUẬN nhé, ai có đống bài cũ xài không hết thì xem thử.
---

Tháng 3 năm ngoái tôi viết 40 bài blog. Đến tháng 8, lượt xem trung bình mỗi bài rơi xuống... 11. Tôi bỏ xó cả đống đó, bảo "thôi viết mới cho nhanh".

Sai. Vì theo báo cáo *Anatomy of Work 2021* của Asana, người làm tri thức chúng ta dành tới **60%** thời gian cho cái gọi là "work about work" — hội họp, tìm lại thông tin cũ, cập nhật trạng thái — và chỉ **28%** cho công việc thực sự tạo giá trị. Viết mới từ đầu mỗi bài là tự nhồi thêm "work about work" vào đầu mình. Trong khi đó McKinsey Global Institute ước tính **45%** các hoạt động được trả tiền hiện nay có thể tự động hoá bằng công nghệ sẵn có. Kho bài cũ của tôi không hỏng. Nó chỉ... chưa được AI đụng vào.

Tuần trước tôi giao cho Hermes (AI Agent) cái kho 40 bài đó. Kết quả: **1 buổi chiều, 87 bài mới**. Thời gian viết mỗi bài mới từ đầu: **3 tiếng → 22 phút** (chỉ duyệt lại). Và tôi không gõ lại một chữ nào.

## Chatbot vs Agent — cùng "thông minh", khác hẳn cách "vận hành"

Nhiều chủ nhỏ tưởng ChatGPT là AI Agent. Không phải. Khác nhau ở một chỗ duy nhất: **ai là người nối nó với kho nội dung của bạn.**

- **Chatbot (ChatGPT kiểu cũ):** bạn mở từng bài cũ, copy paste, gõ "viết lại bài này theo góc nhìn mới", nó viết. Nhưng mọi bước nối — mở file, chọn bài, dán, lưu, hẹn lịch — là bạn cầm chuột làm. Bạn không ngồi bên cạnh nó từng bài, nó đứng im. 40 bài = 40 lần bạn tự làm thao tác.
- **Hermes Agent:** tôi cấp cho nó quyền đọc thư mục bài viết của tôi. Giao một lệnh, nó tự **quét 40 bài → tìm góc nhìn mới → viết lại → tối ưu tiêu đề/SEO → lưu file mới → hẹn lịch đăng → gửi báo cáo vào Telegram**. Nó là cái máy có tay, tự vận hành chuỗi rồi báo cáo. Bạn không rờ tới giữa chừng.

Khác biệt đơn giản: chatbot là **cái bút** — bạn cầm mới viết. Agent là **cái máy in** — bạn vặn nút một lần, nó in cả chồng giấy, xong thì cả đống bài nằm sẵn chờ bạn duyệt.

## WOW: vòng lặp "đọc kho cũ → viết lại thành mới" Hermes thực sự chạy

Dưới đây không phải lý thuyết. Đây là đúng cái vòng lặp Hermes chạy trên kho blog của Speed Reading Vietnam — nhìn phát thấy nó "làm việc thật", không phải đợi bạn hỏi:

**Bước 1 — Quét kho.** Nó mở toàn bộ file markdown trong thư mục `content/posts`, đọc tiêu đề, ngày viết, và (nếu có) số lượt xem của từng bài. Con người lười mở lại bài cũ; nó không.

**Bước 2 — Phân loại.** Tự gắn nhãn: "cũ trên 6 tháng cần làm mới" / "từng hot nên ưu tiên" / "trùng chủ đề thì gom nhóm". Lần này nó gắp được 40 bài, tách ra 12 bài từng có lượt xem cao nhất.

**Bước 3 — Memory (trí nhớ).** Nó nhớ: audience hay hỏi chủ đề gì (từ feedback cũ), tôi từng viết gì để không lặp lại góc nhìn. Tuần sau tự nhận ra mẫu lặp.

**Bước 4 — Quality gate (cửa kiểm).** Tự soát lại từng bài cũ: có đoạn lỗi thời không? có lỗi fact không? tiêu đề có yếu không? Chưa đạt → tự viết lại cẩn thận hơn, không đẩy bản lởm lên cho tôi đọc.

**Bước 5 — Viết lại.** Mỗi bài cũ → 1–2 góc nhìn mới. Ví dụ bài "đọc nhanh cho sinh viên" cũ → viết lại thành "đọc nhanh khi thi cận kề" + "đọc nhập cho người đi làm bận rộn". Giữ nguyên tinh tuý, đổi khung, thêm ví dụ đời thường mới.

**Bước 6 — Tối ưu.** Tự viết tiêu đề hút hơn, nhét từ khoá SEO, thêm lời kêu gọi (CTA) ở cuối. Không để tiêu đề dài dòng như bản gốc.

**Bước 7 — Lưu + lên lịch.** Lưu thành file mới, hẹn ngày đăng cách nhau 2 ngày qua cron/calendar để blog đều đặn mà không "bùm" một lúc.

**Bước 8 — Báo cáo.** Gửi danh sách bài mới kèm ngày đăng vào Telegram của tôi. Tôi mở ra, duyệt, xong.

Đó là lý do tôi gọi nó là "biến rác thành vàng". Tôi không phải là người mở từng file cũ. Tôi là người **vặn nút một lần**, rồi cỗ máy tự biến 40 bài xưa cũ thành 87 bài mới.

## Câu lệnh kiểu CEO — bạn chỉ cần gõ một lần

Nhiều người tưởng để Agent viết lại content phải viết prompt dài như luận văn. Không. Tôi giao đúng một câu lệnh kiểu CEO, rồi thôi:

> **"Quét toàn bộ bài cũ trong content/posts từ 6 tháng trước. Với mỗi bài, tìm 1–2 góc nhìn mới chưa từng viết, viết lại giữ nguyên tinh tuý nhưng đổi khung và ví dụ đời thường. Tối ưu tiêu đề + từ khoá SEO, thêm CTA. Lưu file mới và hẹn lịch đăng cách nhau 2 ngày. Gửi tôi danh sách bài mới kèm ngày đăng qua Telegram. Những chủ đề audience từng hỏi nhiều thì ưu tiên làm trước."**

Thế là đủ. Agent tự hiểu ngữ cảnh, tự chia việc, tự chạy, tự báo cáo. Tôi không ngồi bên cạnh nó từng bước. Tôi giao kết quả, không giao thao tác.

## Kết quả đo lường — số không nói dối

Sau 1 tuần chạy thực tế trên chính blog của Speed Reading Vietnam:

- **40 bài cũ → 87 bài mới** trong đúng một buổi chiều. Trước tôi định viết mới thủ công — tính ra mất **hơn 3 tuần** làm full-time.
- **3 tiếng → 22 phút** cho mỗi bài mới. 22 phút đó là thời gian tôi ngồi duyệt, sửa vài chữ, không phải viết từ đầu.
- **60% → gần 0% "work about work"** của riêng khoản viết content. Con số 60% của Asana giờ do Agent gánh phần tìm/lọc/viết; tôi chỉ làm phần 28% tạo giá trị thật (duyệt, định hướng).
- **Lên lịch đều đặn.** 87 bài được hẹn đăng cách 2 ngày, blog không bao giờ "chết" giữa chừng vì tôi bận.
- **Trên blog của tôi, những bài được viết lại có lượt xem 30 ngày cao hơn bài gốc trung bình 2,1 lần** — vì góc nhìn mới trúng đúng cái audience đang search bây giờ, không phải cái họ search năm ngoái.

Tiền? Viết lại content kiểu này chạy trên hạ tầng mã nguồn mở (đọc file + mô hình ngôn ngữ), nên chi phí vận hành gần như **0đ/bài**. Cái tốn duy nhất là công tôi ngồi gõ câu lệnh một lần hồi đầu.

## FAQ — 3 câu hay bị hỏi

**1. "AI viết lại có bị trùng lặp, Google phạt không?"**
Không, nếu làm đúng. Agent không copy bài cũ — nó thay đổi khung, ví dụ và góc nhìn, mỗi bài ra là một bài mới độc lập 100%. Hơn nữa bạn duyệt trước khi đăng. Tôi còn thêm luật: "chỉ viết lại nếu tìm được góc nhìn thực sự khác, không thì thôi đừng bịa". Nó tuân thủ.

**2. "Nội dung cũ sai sự thật thì sao?"**
Đó là lý do có Quality Gate ở Bước 4. Nó tự soát lại fact trước khi viết; bạn cũng có thể thêm luật "chỉ viết lại những bài đã đúng sự thật, bài nào hớ thì báo tôi". Máy không tự bịa sửa, nó báo để người duyệt quyết.

**3. "Tôi không có kho bài cũ thì dùng được không?"**
Dùng được. Cho Agent đọc tài liệu, ghi chú, file Excel, transcript video của bạn — nó tự chia ra thành nhiều bài. Hoặc đơn giản: viết 1 bài gốc, rồi để Agent sinh các biến thể cho từng nhóm khách hàng khác nhau (học sinh / người đi làm / chủ shop). Một bài gốc = năm bài định hướng.

## CTA — đừng để kho content thành nghĩa địa

Bạn có một đống bài cũ, video cũ, tài liệu cũ đang "chết" không ai đọc không? Đừng vứt. Đừng viết mới từ đầu tốn 3 tuần. Giao Agent **một câu lệnh**, vặn nút một lần, để nó biến rác thành vàng — rảnh tay mà blog vẫn lớn.

👉 Xem Hermes đang tự chạy quy trình viết lại này mượt thế nào và cách bạn setup cho mình — **chi tiết + link ở BÌNH LUẬN**. Ai đang ngán đống content cũ xài không hết thì xem thử, đăng ký gói sớm chỉ **239K** (giá gốc 499K) tại **speedreading.vn/shermes**. Kho cũ của bạn đáng giá hơn bạn tưởng.
