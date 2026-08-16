---
title: "1 file Excel cũ 3 năm — Hermes đọc 1 phút, nhớ thay tôi cả cái shop"
date: 2026-08-16
draft: false
description: "Chatbot không đọc được quá khứ. Hermes (AI Agent) đọc file Excel cũ của shop, 'học' và nhớ: mặt hàng bán chạy, khách ruột, ngày cao điểm — rồi áp dụng cho mọi việc sau. Thực tế Agent có trí nhớ chủ động, không cần biết code."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-hoc-tu-file-excel-cu.webp"
share_teaser: |
  Hỉ kể thật: có 1 file Excel để xó 3 năm, mở lên đau đầu nên thôi.
  Hermes đọc xong 1 phút, nó nhớ hộ mình luôn: món nào chạy, khách nào ruột, ngày nào đông.
  Chatbot thì không làm được cái này — nó đọc xong cũng quên ngay. Agent là đọc xong là 'nhớ' luôn.
  👉 Chi tiết + link mình để ở BÌNH LUẬN nha.
---

Cái tủ kéo rách có một file Excel tôi tạo từ 3 năm trước. 1.400 dòng đơn hàng shop mỹ phẩm, 8 cột, đủ thứ ngày giờ tên khách số tiền. Tôi mở lên đúng một lần, hoa mắt, tắt đi, để đó. Ba năm sau nó vẫn nằm ở đó, dưới đống hoá đơn. Đến lúc cần biết "món nào bán chạy nhất để order lại", tôi lại ngồi lật tay, mất cả buổi chiều mà cuối cùng vẫn đoán mò — vì chẳng ai nhớ nổi 1.400 dòng cả.

Đó là cách làm của người. Còn tuần trước tôi ném nguyên cái file đó cho Hermes. Một phút sau nó trả lại: 12 mặt hàng nên order gấp, 3 khách hàng chiếm 38% doanh thu, và thứ Bảy là ngày bán chạy nhất. Tôi không dặn nó tìm mấy cái đó. Nó tự tìm. Và quan trọng nhất: từ hôm đó, mỗi lần tôi hỏi gì, nó đều lôi mấy con số đó ra — vì nó ĐÃ NHỚ.

## Chatbot thì đọc xong cũng quên — Agent là đọc xong là nhớ

Phải phân biệt rõ, vì nhiều người đang nhầm hai thứ này thành một:

- **Chatbot** (kiểu ChatGPT hỏi–đáp): bạn dán file Excel vào, nó tóm tắt giúp. Xong. Lần sau bạn mở lại, nó không biết cái file đó là gì. Bạn phải dán lại. Nó giống cái loa phát thanh: nói xong là hết, không giữ lại được gì.
- **Agent** (Hermes): bạn ném file vào MỘT LẦN, nó không những đọc mà còn **học và lưu**. Lần sau bạn không cần dán lại. Nó tự lấy thông tin cũ ra áp dụng cho việc mới. Nó là cộng sự có trí nhớ: làm xong là ghi nhớ, lần sau tự biết.

Khác nhau cốt lõi nằm ở chỗ: chatbot xử lý tại chỗ rồi quên; Agent xử lý xong thì đưa kết quả vào bộ nhớ dài hạn. Càng dùng, nó càng hiểu cái shop của bạn — chứ không phải mỗi lần gặp lại như người lạ.

Để thấy rõ, thử hình dung một tình huống thật:

> **Với chatbot:** "File đơn hàng của tôi, món nào bán chạy nhất?" → nó trả lời. Sang tuần bạn bảo "Viết giúp tôi một cái caption kêu gọi mua" → nó viết chung chung, vì nó đã quên cái file tuần trước. Bạn lại phải dán file, lại giải thích. Mệt.
>
> **Với Agent:** "Đọc file đơn hàng, nhớ giúp tôi món bán chạy" → nó đọc, nhớ. Tuần sau: "Viết caption" → nó tự ưu tiên 12 món đó, không cần bạn nhắc. Bạn không lặp lại chính mình lần nào.

## Câu chuyện thật: tôi từng đốt 4 triệu vì 'cảm giác'

Nói cho cùng, cái file 3 năm nằm xó không phải tại tôi lười. Tại vì trước đây tôi LÀM SAI và không biết mình sai.

Hồi mới mở shop, tôi thấy hũ serum xanh mỗi lần lên tay khách là họ khen thơm. Thế là tôi "cảm giác nó chạy", order một lúc 50 hũ. Kết quả: nằm kho nửa năm không hết, đọng vốn tận 4 triệu, tiền đó đáng lẽ quay vòng được mấy món khác. Lúc đó tôi không có số liệu, chỉ có cảm giác — và cảm giác của chủ shop nhỏ thì hay trật lất.

Sau khi Hermes đọc xong file, nó bảo thẳng: serum xanh chỉ đứng thứ 9 trong 50 món, trong khi 12 món kia bán gấp đôi mà tôi order quá ít, hay cháy hàng. Tôi vừa xót cái 4 triệu vứt đi, vừa mừng vì từ giờ không phải đoán nữa — có người (à nhân sự ảo) nhớ hộ mình rồi. Cảm giác thật lúc đó là: giá biết cái này sớm hơn một năm.

## Bên trong: Hermes "học" file Excel cũ thế nào?

Khi tôi ném file `donhang_2023_2025.xlsx` cho Hermes, bên trong nó chạy một vòng lặp có thật — không phải chỉ trả lời một câu rồi thôi:

1. **Đọc & hiểu cấu trúc:** mở file, nhận diện từng cột (ngày, mã SP, số lượng, khách, tiền), tự bỏ dòng rác và dòng trùng.
2. **Trích xuất insight:** tính tổng lượng bán từng mã, nhóm khách theo giá trị, tìm ngày cao điểm trong tuần, phát hiện mặt hàng tồn đọng lâu ngày.
3. **Ghi nhớ (memory):** phim những kết luận này vào bộ nhớ dài hạn của nó, gắn tag "shop mỹ phẩm của Hỉ" để không lẫn với dữ liệu khác.
4. **Áp dụng chủ động:** lần sau tôi bảo "viết caption kêu gọi mua", nó tự ưu tiên 12 món bán chạy đã nhớ — không cần tôi nhắc lại.
5. **Cập nhật:** tháng sau tôi ném file mới, nó gộp vào, bức tranh càng chuẩn, tư vấn càng sát.

> Không phải "AI đọc giúp tôi". Là "AI NHỚ HỘ tôi" — và cái nhớ đó phục vụ mọi việc sau, chứ không nằm chết trong một cuộc chat rồi bay hơi.

Đây cũng là lúc nên nói rõ một chữ hay bị lầm: **cửa sổ ngữ cảnh (context window) không phải trí nhớ.** Context chỉ giữ được trong một phiên rồi reset. Trí nhớ thật sự của Agent là thứ sống sót qua các phiên, và lấy ra ĐÚNG cái cần — chứ không ép bạn dán lại mọi thứ mỗi lần.

## Câu lệnh giao việc kiểu CEO

Tôi không dạy nó từng bước. Tôi chỉ nói mục tiêu, giống một ông chủ giao cho trợ lý giỏi:

> "Hermes, đọc file `donhang_2023_2025.xlsx` trong thư mục shop. Rút ra: 10 món bán chạy nhất, 5 khách giá trị nhất, ngày đông nhất. Lưu hết vào memory, gắn tag 'shop Hỉ'. Từ giờ mỗi bài viết, mỗi email, tự động ưu tiên mấy con số đó — đừng hỏi lại tôi mấy cái này nữa."

Đó là giao kiểu đầu não: tôi nêu cái cần nhớ, Agent lo đọc, tính, và nhớ. Tôi không ngồi xử lý 1.400 dòng. Tôi chỉ duyệt kết quả. Bạn là CEO nêu mục tiêu + giới hạn, Hermes lo cách làm và nhớ lấy.

## WOW: con số thật

- **1.400 dòng → 40 giây.** Hermes đọc và trích xuất xong file 3 năm của tôi trong chưa tới một phút. Con người lật tay mất cả buổi chiều — tôi từng thử và bỏ cuộc.
- **38% doanh thu từ 3 khách.** Nó phát hiện quy luật 80/20 tôi không để ý: 3 khách ruột đóng góp 38% đơn. Từ đó tôi ưu tiên chăm sóc họ thay vì dàn đều như trước.
- **~9 giờ/tuần.** Theo McKinsey, nhân viên văn phòng mất trung bình gần 9 giờ mỗi tuần chỉ để tìm lại thông tin cũ. Giờ Agent nhớ hộ, tôi lấy lại bằng đúng một câu hỏi.
- **60–70%.** Cũng McKinsey ước tính: AI có thể tự động hóa 60–70% hoạt động công việc hiện tại. "Đọc và nhớ file cũ" chỉ là một mẩu nhỏ trong đó — nhưng với chủ shop nhỏ như tôi, mẩu nhỏ đó cứu được cả đống tiền tồn kho.

## Kết quả đo lường sau 1 tuần

- **Order sai mặt hàng:** từ "hay đoán mò, cháy hàng liên tục" → có **12 món được gợi ý sẵn**, tôi chỉ duyệt, không phải nghĩ.
- **Thời gian làm báo cáo tuần:** từ **cả buổi chiều ngồi lật Excel** → **6 phút** (nó lấy từ memory, viết lại, tôi đọc và gửi).
- **Khách ruột:** có **danh sách 5 người** để gửi ưu đãi trước người ta quên mình, thay vì nhớ mơ hồ "hình như bà nào hay mua nhiều".

## Mẹo giao việc (cho chủ shop không biết code)

- **Ném file cũ một lần, bảo "nhớ vào memory":** các việc sau tự chuẩn, không dán lại lần nào.
- **Gắn tag rõ:** "shop Hỉ", "khóa học", "nhà cửa" → nó không lẫn dữ liệu giữa các mảng đời sống.
- **Mỗi tháng ném file mới, bảo "cập nhật":** trí nhớ càng dày, tư vấn càng chuẩn, gợi ý càng trúng.
- **Hỏi bằng câu thường:** "món nào tôi nên order gấp?" — nó lôi từ memory ra, bạn không cần mở file.

## FAQ

**1. File Excel của tôi lộn xộn, nhiều sheet, Agent có đọc được không?**
Được. Hermes quét nhiều sheet, gộp các cột trùng tên, bỏ dòng rỗng, chuẩn hoá ngày tháng. Lộn xộn đến mức nào cứ ném thử — nó báo lại chỗ nào không hiểu để bạn sửa, chứ không "ngáo" im lặng như chatbot rồi trả kết quả bậy.

**2. Nó nhớ mãi à, hay vài hôm lại quên như chatbot?**
Nhớ vào bộ nhớ dài hạn, sống sót qua các phiên. Bạn tắt máy, tuần sau mở lại, nó vẫn nhớ nguyên. Chatbot mới là cái quên sạch sau mỗi lần chat — gặp lại là người lạ.

**3. Tôi không biết code, có tự làm được không?**
Có. Toàn bộ là giao việc bằng tiếng Việt: "đọc file X, nhớ vào memory, ưu tiên khi viết". Không cần viết một dòng code, không cần hiểu thuật toán — bạn chỉ cần file và mục tiêu.

## Kết luận

Cái file Excel 3 năm của tôi không còn nằm xó. Hermes đọc một lần, nhớ hộ tôi mặt hàng bán chạy, khách ruột, ngày đông — và áp dụng cho mọi bài viết, email, báo cáo sau. Chatbot thì đọc xong quên. Agent là đọc xong là nhớ, rồi làm tiếp cho bạn, không bắt bạn giải thích lại lần nào.

Muốn có nhân sự ảo "đọc file cũ, nhớ thay bạn" mà không cần biết code?

👉 Học bài bản: [khoá Nhân Sự Toàn Năng Hermes](https://speedreading.vn/shermes)

📎 Đọc thêm: [Hermes có trí nhớ: nhớ bạn hơn bạn nhớ mình](/posts/hermes-co-tri-nho/)
