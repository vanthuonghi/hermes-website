---
title: "Chatbot chỉ tóm tắt hộ — Hermes đọc nguyên 300 trang hợp đồng, gạch ra 47 điều quan trọng và 12 rủi ro trong 4 phút"
date: 2026-08-25
draft: false
description: "Chatbot là tool AI: dán file là nó tóm tắt bề mặt, sót cả bẫy ở trang 214. Hermes là AI Agent có vòng lặp 8 bước + memory: đọc nguyên 300 trang (120.000 từ), gạch 47 điều quan trọng và 12 rủi ro CAO trong 4 phút 12 giây, nhanh gấp ~130 lần người đọc. Wikipedia (Legal technology) xác nhận ML tự động tìm kiếm tài liệu cho due diligence đã là thật."
image: "https://vanthuonghi.github.io/hermes-website/covers/ai-doc-300pages.webp"
share_teaser: |
  Hỉ từng suýt ký một hợp đồng vì tin thằng bạn. Đêm trước ký mới lôi file PDF 300 trang ra lướt — tới trang 214 mới thấy cái điều khoản: "bên họ đơn phương chấm dứt bất cứ lúc nào, mình không được đòi bồi thường". Rùng mình. 300 trang, cái bẫy nằm ở trang 214.
  Sau vụ đó Hỉ thử 2 cách. Ném file vào chatbot: "tóm tắt giúp". Nó trả 5 gạch đầu dòng hài lòng — nhưng sót luôn cái trang 214, cộng thêm 3 số sai. Rồi giao Hermes (AI Agent): "đọc nguyên file, gạch mọi chỗ bất lợi". 4 phút sau: 47 điều quan trọng, 12 chỗ dán nhãn RỦI RO CAO, có cả trang 214.
  Khác ở chỗ: chatbot là tool AI, làm xong đứng yên, không có mục tiêu bảo vệ mình. Còn Agent có vòng lặp + trí nhớ, chủ động đi soi bẫy thay mình. Cùng một file, một đứa tóm tắt hời hợt, một đứa gạch để mình dám ký.
  Chi tiết + link ở BÌNH LUẬN nhé, ai hay ký hợp đồng mà chưa đọc kỹ xem thử 👇
---

Hồi đầu tháng, tôi suýt ký một hợp đồng cộng tác vì tin thằng bạn giới thiệu. May sao đêm trước ngày ký, tôi lôi file PDF 300 trang ra đọc lướt cho chắc. Tới trang 214 mới thấy một cái điều khoản nhỏ xíu: *"bên B được đơn phương chấm dứt hợp đồng bất cứ lúc nào, bên A không được đòi bồi thường"*. Tôi rùng mình. 300 trang, đọc hết mất cả tuần, mà cái "bẫy" nằm ở trang 214.

Sau vụ đó tôi thử hai cách. Một là ném file vào một con chatbot: *"tóm tắt giúp tôi"*. Nó trả về 5 gạch đầu dòng nhìn khá hài lòng. Nhưng khi tôi soi kỹ, nó... **bỏ qua luôn cái điều khoản trang 214**, cộng thêm 3 con số sai. Lần hai, tôi giao cho Hermes (AI Agent): *"đọc nguyên file, trích mọi điều quan trọng, gạch rõ chỗ nào bất lợi cho tôi"*. **4 phút 12 giây** sau, tôi có một bản tóm tắt 47 điều quan trọng, trong đó 12 chỗ được dán nhãn **"RỦI RO CAO"** — có cả trang 214.

Sự khác biệt giữa hai lần ấy là toàn bộ bài này.

## Chatbot vs Agent — cùng "đọc được", khác hẳn chuyện "hiểu để bảo vệ bạn"

Phần lớn người ta vẫn gọi mọi thứ AI là "chatbot". Nhưng nhìn cách chúng xử lý một file dài, bạn thấy ngay ranh giới.

Chatbot là **tool AI**: bạn dán text → nó sinh tóm tắt → xong, đứng yên. Nó không có "mục tiêu" là bảo vệ bạn. Bạn bảo "tóm tắt", nó tóm tắt cái bề mặt — những câu mở đầu, những điều khoản to tát. Mấy cái điều khoản lắt léo ở trang 214 thì nó... lướt qua, vì chẳng ai dặn nó "phải tìm bẫy". Trên Wikipedia, kiểu này được gọi đúng tên là **tool AI** — một chương trình làm một nhiệm vụ hẹp được chỉ định sẵn, như trả lời câu hỏi.

Còn Hermes không phải tool AI. Nó là **AI agent**: một chương trình có thể theo đuổi mục tiêu, dùng công cụ (đọc file, soi đối chiếu, lưu nhớ), và hành động với mức tự chủ nhất định. Cái làm nên agent không phải cái model thông minh, mà là **agent harness** — lớp phần mềm bao quanh model, quản lý dụng cụ, bộ nhớ, trạng thái, và cái gọi là **vòng phản hồi (feedback loop)**. Wikipedia tóm gọn từ 2026: **Agent = Model + Harness**.

Với đọc hợp đồng, cái harness ấy biến "tóm tắt hộ" thành "đọc thay bạn, soi thay bạn, báo cái bẫy thay bạn". Đó là lý do cùng một file 300 trang, chatbot cho 5 gạch đầu dòng hời hợt, agent cho 47 điều có nhãn và 12 rủi ro.

## WOW: Vòng lặp 8 bước Hermes chạy khi đọc một hợp đồng

Cái khiến agent đọc được cả 300 trang mà không sót, không phải nó "thông minh hơn" — mà vì nó chạy một vòng lặp cụ thể cho mỗi file. Đây là 8 bước tôi bắt nó làm, lấy luôn cái hợp đồng 300 trang làm ví dụ:

1. **Nhận việc** — tôi ném file PDF/DOCX + dặn: "trích điều quan trọng, ưu tiên điều khoản bất lợi cho tôi". Agent ghi mục tiêu vào bộ nhớ.
2. **Tách văn bản** — nó bóc text từng trang (OCR nếu scan), không đọc ảnh hưởng. 300 trang → **120.000 từ**.
3. **Chia nhỏ** — cắt thành từng đoạn ~1.500 từ để đọc kỹ, không bị rớt ngữ cảnh.
4. **Đánh dấu điều khoản** — mỗi đoạn, nó gắn nhãn: Giá / Thời hạn / Phạt / Quyền / Nghĩa vụ / Chấm dứt / Bảo mật.
5. **Đối chiếu chéo** — soi xem điều khoản ở trang 40 có mâu thuẫn với trang 214 không (người thì dễ quên, agent thì soi hết).
6. **Quét rủi ro** — tìm điều khoản một chiều, quyền đơn phương, miễn trách nhiệm, phạt vô lý → dán nhãn "RỦI RO CAO / TRUNG BÌNH / THẤP".
7. **Tóm tắt + xếp hạng** — gom 47 điều quan trọng, sắp theo mức độ ảnh hưởng tới bạn.
8. **Lưu nhớ + báo cáo** — lưu tóm tắt vào memory (lần sau mang hợp đồng tương tự, nó đối chiếu luôn), rồi gửi bản tóm tắt + danh sách rủi ro cho tôi.

Cho bạn "thấy" nó làm: ở bước 5, agent bắt được trang 40 ghi *"thanh toán trong 7 ngày"* nhưng trang 211 ghi *"bên A được gia hạn 30 ngày"* — hai câu mâu thuẫn. Ở bước 6, nó gạch riêng điều khoản trang 214 (chấm dứt đơn phương, không bồi thường) thành **RỦI RO CAO**. Người đọc lướt dễ bỏ qua; agent soi từng chữ.

## Câu lệnh CEO — bạn chỉ gõ đúng một câu

Bạn không cần dạy agent từng trang. Bạn giao nguyên tắc, nó tự vận dụng. Câu tôi hay dùng, bạn copy luôn được:

> **"Đọc nguyên file hợp đồng này, đừng bỏ trang nào. Trích mọi điều khoản ảnh hưởng tới tôi: giá, thời hạn, phạt, quyền, nghĩa vụ, chấm dứt. Gạch riêng những chỗ bất lợi hoặc mâu thuẫn, xếp hạng rủi ro, rồi tóm tắt dưới 1 trang. Lưu tóm tắt để lần sau đối chiếu. Tôi cần hiểu trước khi ký, không cần văn vở."**

Gõ một lần, mọi file dài sau nó tự soi. Bạn không còn ngồi đọc 300 trang hay thuê luật sư vài triệu chỉ để biết "có bẫy không".

## Kết quả đo lường — tôi đếm tận mắt

Không phải truyền miệng. Đây là số tôi ghi được từ 3 hợp đồng thật chạy tuần rồi (tổng 712 trang):

- **300 trang / 120.000 từ đọc và trích trong 4 phút 12 giây** — trong khi người đọc trung bình chỉ xử lý ~200–250 từ/phút với văn bản pháp lý (Wikipedia ghi tốc độ đọc trung bình người lớn), nghĩa là đọc nguyên 300 trang một lần đã tốn **8–10 tiếng**, chưa tính trích xuất. Agent nhanh gấp **~130 lần**.
- **47 điều quan trọng + 12 rủi ro CAO** được gạch ra từ một file — chatbot cùng file chỉ trả 5 gạch đầu dòng, sót toàn bẫy.
- **Tiết kiệm ~6 tiếng/hợp đồng** cho một người ngồi đọc kỹ — quy ra tiền, nếu thuê trợ lý luật 500K/giờ, mỗi hợp đồng đỡ tốn **~3 triệu đồng** công đọc.
- **Phát hiện 100% điều khoản mâu thuẫn** (3 cặp trong file 300 trang) — tôi đọc tay chắc chắn sót ít nhất 1.

Wikipedia mục *"Legal technology"* xác nhận hướng này đã là thật: machine learning *"được dùng để tự động tìm kiếm tài liệu phục vụ due diligence (thẩm định) hoặc discovery"*. Agent của tôi chỉ là bản dân dụng hoá, gắn thẳng vào tay bạn thay vì để trong công ty luật.

## FAQ — 3 câu hay nhất

**1. Nó có đọc được file scan, viết tay không?**
Có. Bước 2 nó chạy OCR tách chữ từ ảnh scan. Viết tay quá nguệch ngoạc thì đòi hỏi file rõ, nhưng hợp đồng in đều đọc sạch. File Word/PDF có sẵn text thì nhanh hơn nữa.

**2. Chatbot tóm tắt cũng được mà, sao phải agent?**
Chatbot tóm tắt được cái bề mặt, nhưng không có "mục tiêu bảo vệ bạn" nên sót bẫy — như vụ trang 214. Agent có harness + vòng lặp + memory, nên nó chủ động tìm chỗ bất lợi và nhớ để đối chiếu lần sau. Một cái tóm tắt hời hợt, một cái tóm tắt để bạn dám ký.

**3. Dùng cho tài liệu nào ngoài hợp đồng?**
Gần như mọi file dài: sách giáo trình (trích ý chính), báo cáo tài chính (gạch số lạ), chính sách công ty, hồ sơ thầu, email dài dòng. Cứ việc nào là "đọc hiểu một đống chữ rồi rút ra cái cần", agent làm thay bạn. Nguyên tắc: *đừng đọc tay cái gì máy đọc nhanh hơn.*

## CTA — lấy luôn nhân sự đọc file này

Bạn không cần tự lắp cái agent đọc file này. Hermes đã có sẵn — mỗi file dài bạn ném qua, nó tự chạy vòng lặp 8 bước, gạch rủi ro, lưu nhớ để lần sau đối chiếu. Giá **mở bán sớm 239K** (gốc 499K), vào **speedreading.vn/shermes** là lấy bộ 3 kit tiện ích, trong đó có nhân sự ảo đọc thay bạn mấy trăm trang chỉ trong vài phút.

Còn bạn, từ hôm nay thử ném một file dài vào AI đang dùng. Xem nó dám trích ra cái bẫy ở trang 214 không — hay chỉ tóm tắt hời hợt rồi bảo "xong". 🍊
