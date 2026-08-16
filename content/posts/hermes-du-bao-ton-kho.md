---
title: "Hermes đọc lịch sử bán, dự báo tồn kho trước 3 tuần — tôi hết cảnh nhập bừa"
date: 2026-08-16
draft: false
description: "Chatbot đoán mò khi bạn hỏi 'nên nhập bao nhiêu'. Hermes tự mở file bán hàng 14 tháng, tính tốc độ bán từng mã, dự báo ngày hết hàng, 7h sáng thứ Hai gửi bảng 'NÊN NHẬP GÌ - BAO NHIÊU - VÌ SAO' — và tự lặp lại mỗi tuần kể cả khi tôi đi vắng."
image: "https://vanthuonghi.github.io/hermes-website/covers/ai-memory-1786854437.webp"
share_teaser: |
  Hỉ vừa được thứ xịn đến mức hơi ngượng: tuần trước Hỉ nhập 300 hộp một mã, tưởng bán chạy, kết quả nằm kho 5 tuần chưa hết nửa. Còn cái mã bán chạy thật thì… hết hàng đúng cuối tuần đông khách. 🤦
  Giờ 7h sáng thứ Hai Hỉ mở điện thoại đã có sẵn 1 bảng: mã nào còn bán được mấy ngày, mã nào sắp cháy, nên nhập bao nhiêu, vì sao. Hỉ không mở Excel một phút nào.
  Đây đúng chỗ Chatbot và AI Agent khác nhau: ChatGPT là đứa CHỜ HỎI — bạn hỏi "nên nhập bao nhiêu?", nó chưa từng thấy file bán hàng của bạn nên nó… đoán. Còn Agent là đứa ĐI LÀM — Hỉ giao MỘT LẦN: "mỗi thứ Hai 7h, tự mở file bán 14 tháng, tính tốc độ bán từng mã, dự báo ngày hết hàng, đề xuất số lượng nhập, ghi rõ vì sao". Từ đó nó tự chạy, tự nhớ mã nào Hỉ đã nói "đừng nhập nữa", tự báo cáo.
  👉 Chi tiết + link ở BÌNH LUẬN nhé.
---

Tuần trước tôi nhập 300 hộp một mã vì "cảm giác nó đang bán chạy". Đến hôm nay kho còn 190 hộp, nằm bất động. Cùng lúc đó, cái mã bán thật sự chạy — mã tôi tưởng bình thường — hết hàng đúng chiều thứ Bảy, ngày đông khách nhất tuần. Tôi mất 11 đơn chỉ vì nói với khách một câu: "chị ơi hết hàng rồi, tuần sau em có".

Vấn đề không phải tôi lười. Tôi có file bán hàng đầy đủ 14 tháng. Vấn đề là để biết "nên nhập gì, bao nhiêu", tôi phải ngồi lọc từng mã, cộng số bán 4 tuần gần nhất, chia ra tốc độ bán mỗi ngày, trừ tồn hiện tại, nhân thời gian hàng về... Làm tử tế cho 80 mã mất tôi khoảng **2 tiếng**. Và tôi không làm đủ đều — tháng nào bận là tôi nhập theo cảm giác. Cảm giác thì tính lãi bằng nước mắt.

Giờ việc đó mỗi thứ Hai 7h sáng đã có sẵn trên điện thoại, dạng một bảng ba cột. Tôi bấm đọc **6 phút**, gọi nhà cung cấp, xong.

## Chatbot đoán mò, Agent đọc số thật

Nếu bạn mang câu hỏi này vào một chatbot, cuộc hội thoại sẽ y như thế này:

> Bạn: "Shop tôi bán sữa và đồ khô, tháng này nên nhập bao nhiêu?"
> Chatbot: "Bạn nên căn cứ vào doanh số kỳ trước, tính đến yếu tố mùa vụ, duy trì mức tồn kho an toàn khoảng 20–30%, và theo dõi sát các mặt hàng bán chậm..."

Đúng hết. Và vô dụng hết. Vì nó **chưa từng nhìn thấy một dòng dữ liệu nào của bạn**. Nó cho bạn nguyên tắc chung mà bất kỳ ai đi làm 3 tháng cũng biết. Nó không thể nói "mã SM-102 còn bán được 9 ngày, nhập thêm 120 hộp" — vì nó không có số.

Hermes khi được giao làm **Agent** thì khác hẳn: nó không trả lời câu hỏi, nó **đi mở file của bạn ra làm**. Cụ thể trong trường hợp của tôi, nó được cấp quyền đọc đúng hai thứ: file xuất bán hàng 14 tháng (dạng Excel/CSV tôi tải từ phần mềm bán hàng) và file tồn kho hiện tại. Từ hai file đó nó tính thật, không đoán:

- Tốc độ bán bình quân mỗi mã theo **4 tuần gần nhất** (chứ không lấy cả 14 tháng, vì thị trường đổi).
- So sánh với cùng kỳ năm ngoái để nhận diện mùa vụ (tháng 8 mã bánh trung thu bắt đầu nhích, tôi hay quên).
- **Số ngày còn bán được** = tồn hiện tại ÷ tốc độ bán/ngày.
- Cảnh báo đỏ nếu số ngày đó **nhỏ hơn thời gian hàng về** (shop tôi 5–7 ngày).
- Danh sách hàng "chết": bán dưới 1 đơn vị/tuần trong 6 tuần liền → đề xuất xả, không nhập nữa.

Khác biệt cốt lõi: chatbot cho *lời khuyên chung*, Agent cho *một quyết định cụ thể trên số liệu của chính bạn*, đúng giờ, kể cả tuần đó bạn đi du lịch.

## Vòng lặp nó tự chạy mỗi thứ Hai

Đây là chỗ tôi thích nhất, vì nó cho thấy Hermes không phải "cái ô chat". Mỗi tuần nó tự đi qua 8 bước, không cần tôi nhắc:

1. **Tìm** — mở thư mục dữ liệu, lấy file bán hàng mới nhất và file tồn kho tôi vừa xuất.
2. **Nghiên cứu** — đọc, làm sạch (bỏ dòng trống, gộp mã bị gõ sai chính tả — cái này nó học từ lần tôi sửa tay).
3. **Làm** — tính tốc độ bán, số ngày còn hàng, đề xuất số lượng nhập cho từng mã.
4. **Check** — tự soi lại: mã nào thiếu dữ liệu thì ghi "không đủ số liệu", **không tự bịa** con số.
5. **Lưu** — ghi bảng kết quả ra file, đặt tên theo tuần, để tôi đối chiếu tuần trước.
6. **Lịch** — hẹn lại chính nó cho thứ Hai tuần sau, 7h sáng.
7. **Báo cáo** — gửi bảng gọn cho tôi qua tin nhắn, kèm 3 dòng tóm tắt "cần xử lý ngay".
8. **Nhớ** — cập nhật trí nhớ: mã nào tôi đã trả lời "ngưng nhập", mã nào tôi tăng gấp đôi vì có đơn sỉ.

Bước 8 là thứ chatbot không có. Tuần đầu nó đề xuất nhập 60 hộp một mã tôi đang muốn xả. Tôi nhắn lại một câu: *"mã này ngưng, đang xả tồn"*. Từ tuần sau trở đi nó không đề xuất nữa, và còn tự thêm dòng "đang xả — còn 24 hộp, tốc độ 6 hộp/tuần, dự kiến sạch sau 4 tuần". Tôi không phải giải thích lại lần hai. Với chatbot, mỗi lần mở tab mới là bạn kể lại từ đầu.

## Câu lệnh tôi giao — copy dùng được

Đây là nguyên văn phần lệnh (đã bỏ tên riêng). Bạn không cần biết code, chỉ cần nói rõ như nói với một nhân viên mới:

> "Mỗi thứ Hai 7h sáng, mở 2 file trong thư mục /kho: `banhang.csv` (14 tháng) và `tonkho.csv` (hiện tại).
> Với từng mã hàng: tính tốc độ bán bình quân 4 tuần gần nhất (đơn vị/ngày), so sánh cùng kỳ năm trước để ghi chú mùa vụ, tính số ngày còn bán được = tồn ÷ tốc độ.
> Thời gian hàng về của tôi là 6 ngày. Mã nào số ngày còn lại ≤ 10 → xếp nhóm CẦN NHẬP NGAY, đề xuất số lượng đủ bán 30 ngày, làm tròn theo thùng 12.
> Mã nào bán < 1 đơn vị/tuần suốt 6 tuần → nhóm HÀNG CHẾT, đề xuất xả, ghi số tồn và tiền đang nằm.
> Mã thiếu dữ liệu thì ghi 'không đủ số liệu', tuyệt đối không đoán số.
> Xuất 1 bảng: Mã | Tốc độ bán/ngày | Tồn | Còn bán được (ngày) | Đề xuất nhập | Vì sao.
> Gửi cho tôi qua tin nhắn, kèm 3 dòng 'cần xử lý ngay'. Lưu file lại theo tuần. Rồi tự hẹn lại tuần sau."

Một lệnh. Giao một lần. Nó chạy hoài.

## Kết quả tôi đo được sau 6 tuần

- **2 tiếng → 6 phút mỗi tuần.** Tôi không mở Excel nữa, chỉ đọc bảng. Tính ra tiết kiệm **khoảng 8 tiếng/tháng** — tương đương một ngày làm việc.
- **80 mã được soi hết, mỗi tuần.** Trước đây tôi chỉ đủ sức soi tay khoảng 20 mã bán chạy nhất, 60 mã còn lại nhập theo cảm giác. Giờ **100% mã** đều có số.
- **Từ 4 lần hết hàng/tháng xuống 1 lần.** Lần còn lại là do nhà cung cấp giao muộn, không phải do tôi không biết trước.
- **Giải phóng ~14 triệu tiền hàng chết.** Nó chỉ ra 9 mã đã nằm kho trên 6 tuần mà tôi vẫn tưởng "chắc sắp bán". Tôi xả bằng combo, thu tiền về nhập mã đang chạy.
- **6/6 tuần đúng hẹn.** Có tuần tôi đi Đà Lạt, tắt máy tính; 7h sáng thứ Hai bảng vẫn về điện thoại. Vì nó chạy trên máy chủ, không phụ thuộc máy tôi có bật hay không.

Mấy con số này tôi ghi lại thật, vì tôi hay quên nên bắt nó báo cáo luôn mỗi tuần: tuần này dự báo bao nhiêu mã, sai bao nhiêu mã. Tỷ lệ dự báo lệch dưới 15% ở 71/80 mã — đủ tốt để đặt hàng, và tốt hơn hẳn "cảm giác" của tôi.

## Chỗ nó từng làm sai, và cách tôi sửa

Không có gì hoàn hảo từ lượt đầu. Lượt đầu tôi giao hời hợt: *"phân tích file bán hàng giúp tôi"*. Nó trả về một bản phân tích rất đẹp — biểu đồ, xu hướng, nhận xét — mà tôi **không dùng được câu nào để đặt hàng**. Lỗi ở tôi: tôi không nói rõ đầu ra phải là *quyết định nhập bao nhiêu*, không nói thời gian hàng về, không nói thùng 12.

Tôi sửa một lần, thêm đúng ba dòng (đầu ra dạng bảng, hàng về 6 ngày, làm tròn thùng 12). Từ đó về sau đúng. Đó là bài học đắt nhất tôi học được khi dùng Agent: **nó làm y lời bạn nói, nên hãy nói ra con số và hình dạng đầu ra bạn muốn**. Với người mới, cứ nghĩ mình đang dặn một nhân viên mới vào làm ngày đầu.

## FAQ ngắn

**Hỏi: Tôi không rành kỹ thuật, làm nổi không?**
Nổi. Tôi không viết một dòng code. Tôi chỉ xuất 2 file từ phần mềm bán hàng ra thư mục, rồi giao lệnh bằng tiếng Việt như trên. Ai gõ được Zalo là làm được.

**Hỏi: Shop tôi ghi tay, không có phần mềm thì sao?**
Vẫn được, miễn bạn có bảng bán hàng dạng Excel/Google Sheet. Nó đọc được Google Sheet qua kết nối API, tức bạn cập nhật sheet như thường, nó tự vào lấy số.

**Hỏi: Dữ liệu bán hàng của tôi có bị lộ không?**
File nằm ở thư mục của bạn, bạn cấp quyền đọc đúng 2 file đó, không cấp thêm. Muốn chặt hơn thì để nó chỉ đọc bản sao đã xoá tên khách.

**Hỏi: Nó thay tôi quyết định nhập hàng luôn à?**
Không. Nó đưa đề xuất kèm lý do; bấm gọi nhà cung cấp vẫn là bạn. Đầu não là nó, cánh tay ký đơn vẫn là bạn — và đó là điều nên giữ.

**Hỏi: Một tuần một lần có đủ không?**
Tôi để thứ Hai vì tôi đặt hàng đầu tuần. Bạn bán mùa cao điểm thì bảo nó chạy mỗi ngày 7h — vẫn một lệnh, chỉ đổi lịch. Nó không kêu ca, không xin nghỉ phép.

## Kết luận

Cái làm tôi phục không phải là nó tính toán giỏi — mấy công thức này tôi biết cả. Cái làm tôi phục là **nó tự làm đều, mỗi tuần, kể cả tuần tôi mệt và lười, và nó nhớ hết những gì tôi đã dặn**. Chatbot là đứa chờ bạn hỏi rồi đoán. Agent là đứa bạn giao một lần, rồi nó tự mở dữ liệu, tự tính, tự kiểm tra, tự lưu, tự hẹn lịch, tự báo cáo.

Nhập hàng bằng cảm giác là cách đắt nhất để học bài học về tồn kho. Tôi trả tiền học phí 190 hộp rồi. Bạn thì không cần.

👉 Học cách giao việc kiểu này cho Hermes: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes) — 37 bài, 239K, hoàn tiền trong 7 ngày nếu bạn thấy không dùng được.
