---
title: "Gom mọi API Key vào 1 mối: 7 công cụ chạy như 1"
date: 2026-08-31
draft: false
description: "Tôi từng có 7 tài khoản AI, 7 cái key, 7 tab mở song song và một file Excel chép mật khẩu. Bài này kể cách tôi gom hết vào một mối duy nhất để Agent tự gọi công cụ nào nó cần — cùng 2 lần tôi làm sai, 1 lần suýt lộ key, và con số 6 phút 40 rút xuống 38 giây."
image: "https://vanthuonghi.github.io/hermes-website/covers/ai-api-6a80a96c.webp"
share_teaser: |
  Hỉ từng có 7 tài khoản AI. 7 cái key. 7 tab mở song song. Và một file Excel tên "keys_moi_nhat_final_2.xlsx" 😅
  Mỗi lần làm xong một việc nhỏ — viết bài, làm ảnh, đọc file, gửi báo cáo — là phải nhảy qua công cụ khác, đăng nhập lại, copy đoạn text vừa xong dán qua. Việc thật thì 2 phút, phần chạy lòng vòng mất gần 5 phút.
  Nhiều người vẫn tưởng AI là Chatbot: một cái ô để gõ, gõ xong nó trả chữ, còn lại BẠN tự bê qua bê lại. Agent thì khác — nó được nối vào các công cụ, tự quyết định lúc nào cần gọi cái nào, tự lấy kết quả cái này làm đầu vào cái kia, làm hết rồi mới báo.
  Từ 6 phút 40 xuống 38 giây, và Hỉ không còn mở file Excel mật khẩu nào nữa.
  👉 Cách gom key về một mối + 2 lần Hỉ làm sai phải sửa, để ở BÌNH LUẬN nha.
---

Có một giai đoạn máy tôi luôn mở đúng bảy tab.

Một tab để viết chữ. Một tab làm ảnh. Một tab đọc file PDF. Một tab dịch. Một tab quản việc. Một tab gửi mail. Và một tab Excel tên `keys_moi_nhat_final_2.xlsx` — chỗ tôi chép các đoạn ký tự dài loằng ngoằng bắt đầu bằng `sk-`.

Bảy tài khoản, bảy cái key, bảy lần đăng nhập, bảy chỗ trả tiền.

Tháng đó tôi bấm đồng hồ thử một việc rất thường: **viết một bài giới thiệu khoá học kèm ảnh bìa rồi gửi vào nhóm.** Việc suy nghĩ thật sự chỉ chiếm khoảng 2 phút. Tổng thời gian: **6 phút 40 giây.** Phần dư ra — hơn 4 phút — không phải làm việc. Là đi lại. Copy, dán, đổi tab, chờ load, đăng nhập lại vì hết session, tìm lại cái key trong Excel.

Bốn phút thì nhỏ. Nhân cho hai mươi lần một ngày thì không nhỏ nữa.

## Chatbot đưa chữ, Agent đưa việc đã xong

Chỗ này nhiều người hiểu lệch, nên tôi nói rõ.

**Chatbot** là một cái ô để gõ. Bạn gõ vào, nó trả chữ ra. Hết. Nó không biết bên ngoài cái ô đó có gì. Muốn cái chữ đó thành ảnh, thành file, thành mail đã gửi — **bạn** phải tự bê nó qua công cụ khác. Chatbot làm bạn gõ nhanh hơn; nó không làm bạn ít việc hơn.

**AI Agent** là một người làm việc được nối tay vào các công cụ. Nó không chỉ có ô để gõ, nó có **chìa khoá** — key của các dịch vụ nó được phép dùng. Vì có chìa, nó tự quyết định: việc này cần tìm thông tin, việc kia cần tạo ảnh, xong rồi cần lưu file, cuối cùng cần gửi đi. Nó tự lấy đầu ra của bước trước làm đầu vào bước sau, không cần bạn làm người đưa thư ở giữa.

Nói ngắn: Chatbot trả cho bạn **nguyên liệu**. Agent trả cho bạn **việc đã xong**.

Và cái làm nên khác biệt đó, phần lớn nằm ở chuyện rất khô khan: **key để đâu.**

## Gom về một mối nghĩa là gì

Tôi bỏ hẳn cái file Excel. Toàn bộ key giờ nằm trong **một chỗ duy nhất** mà Agent đọc được, còn tôi thì gần như không cần mở ra nữa.

Cấu trúc thực tế tôi đang dùng:

- Một file cấu hình duy nhất, nằm ngoài thư mục dự án, quyền đọc chỉ mình tôi.
- Mỗi dịch vụ một dòng, đặt tên theo **việc nó làm**, không theo tên hãng: `KEY_VIET`, `KEY_ANH`, `KEY_DOC_FILE`, `KEY_GUI_TIN`.
- Agent gọi theo tên việc. Ngày nào tôi đổi nhà cung cấp, tôi sửa đúng một dòng — không phải sửa lại toàn bộ chỗ khác.
- Không có key nào nằm trong bài viết, trong ảnh chụp màn hình, trong lịch sử chat.

Điểm hay không phải là "gọn mắt". Điểm hay là: **từ lúc key về một mối, Agent mới thật sự tự chạy chuỗi được.** Trước đó mỗi mắt xích đều đứt ở chỗ chờ tôi đăng nhập.

## Một vòng chạy thật, xem nó gọi gì

Đây là lệnh tôi gõ, đúng một câu, giọng của người giao việc chứ không phải người hỏi:

> Viết bài giới thiệu khoá học đọc nhanh cho người mới, khoảng 700 chữ, giọng gần gũi. Tự tìm 2 số liệu về tốc độ đọc trung bình để dẫn chứng. Làm luôn 1 ảnh bìa ngang. Đặt tên file theo ngày, lưu vào thư mục bài chờ. Tự đọc lại xem có chỗ nào hứa quá không, sửa rồi mới gửi cho tôi bản cuối kèm ảnh.

Nó chạy tám bước, và mỗi bước dùng một cái chìa khác nhau:

1. **Hiểu việc** — tách ra: cần chữ, cần số liệu, cần ảnh, cần file, cần kiểm tra.
2. **Tìm** — gọi key tra cứu, lấy số liệu tốc độ đọc.
3. **Viết** — gọi key mô hình ngôn ngữ, ra bản nháp 700 chữ.
4. **Làm ảnh** — gọi key tạo ảnh, dùng chính tiêu đề vừa viết làm mô tả cho ảnh. *Bước này là chỗ Chatbot không làm được: nó không tự lấy kết quả bước 3 làm đầu vào bước 4.*
5. **Lưu** — ghi file vào đúng thư mục, đặt tên theo ngày.
6. **Tự kiểm** — đọc lại bản nháp, soát đúng cái tôi dặn: có câu nào hứa quá không.
7. **Sửa** — nó bỏ một câu "đọc nhanh gấp 5 lần chỉ sau 3 ngày". Tôi không nhắc; tôi chỉ dặn "đừng hứa quá".
8. **Báo cáo** — gửi tôi bản cuối, ảnh, đường dẫn file.

Tôi bấm đồng hồ lại đúng việc cũ: **38 giây**, tính từ lúc gõ xong tới lúc nhận báo cáo. Trước là 6 phút 40. Chênh **hơn 90%**, và cái tiết kiệm không nằm ở chỗ máy viết nhanh hơn — nó nằm ở chỗ **không còn ai phải bê đồ giữa bảy cái tab.**

## Hai lần tôi làm sai

Tôi không muốn kể như thể mọi thứ mượt từ đầu.

**Lần một: tôi dán key vào trong file dự án.** Tiện thật, chạy được ngay. Tới hôm tôi đẩy dự án lên mạng để lưu trữ, đang đẩy thì lạnh sống lưng — cái key nằm nguyên trong đó, ai vào cũng đọc được. Tôi phải huỷ key, xin cái mới, dò lại từng chỗ. Từ đó có luật cứng: **key không bao giờ nằm cùng chỗ với nội dung.** File cấu hình để riêng, không đi kèm dự án.

**Lần hai: tôi đưa nó một cái key có quyền quá rộng.** Cái key đó vừa đọc được vừa xoá được. Nó không xoá gì, nhưng đêm đó tôi nghĩ lại và thấy vô lý — người viết bài thì cần quyền xoá làm gì. Tôi đổi sang key chỉ đủ quyền cho việc của nó. Nguyên tắc bây giờ: **đưa đúng cái chìa của căn phòng nó phải vào, không đưa cả chùm.**

Cả hai lỗi đều không phải lỗi công nghệ. Là lỗi tôi làm cho nhanh.

## FAQ

**Không biết code thì làm được không?**
Được. Việc bạn cần làm là **dán key vào đúng một file, một lần**, và đặt tên theo việc. Không phải viết chương trình. Phần khó là hôm đầu, khoảng 20–30 phút loay hoay. Sau đó bạn gần như không mở lại file đó nữa.

**Gom hết vào một chỗ thì mất chỗ đó có nguy hiểm không?**
Có, nên phải làm hai việc: đặt quyền đọc riêng mình, và **giữ một bản sao ở nơi khác máy** — tôi ghi ra một chỗ ngoại tuyến. Bù lại, gom một chỗ **an toàn hơn** rải rác bảy chỗ: bảy chỗ thì bạn không bao giờ biết đủ mình đang để hở chỗ nào. Một chỗ thì bạn khoá được.

**Có phải đăng ký hết bảy dịch vụ mới chạy được?**
Không. Tôi khuyên ngược lại: bắt đầu bằng **hai** — một cái để viết, một cái để gửi đi. Chạy trơn một chuỗi hai bước rồi hãy nối thêm. Người bỏ giữa đường thường vì hôm đầu cố nối cả bảy cái một lúc, sai chỗ nào cũng không biết.

## Chốt

Cái thay đổi lớn nhất không phải tôi làm nhanh hơn.

Là tôi thôi làm **người đưa thư** trong công việc của chính mình. Trước đó phần lớn thời gian tôi bỏ ra chỉ để bê một đoạn text từ cửa sổ này sang cửa sổ kia — chỗ đó không tạo ra giá trị nào, mà nó ăn của tôi hơn bốn phút mỗi việc.

Gom key về một mối là bước đầu tiên để Agent tự đi hết chuỗi. Trước bước đó, nó vẫn chỉ là một cái Chatbot thông minh phải chờ bạn dắt tay.

Nếu bạn cũng đang có một file Excel chép mật khẩu, chỗ đó là chỗ nên dọn trước.

👉 Xem cách vận hành Đội Trợ Lý AI làm việc thật: **[speedreading.vn/shermes](https://speedreading.vn/shermes)** — đang mở bán sớm **239K** (giá gốc 499K).
