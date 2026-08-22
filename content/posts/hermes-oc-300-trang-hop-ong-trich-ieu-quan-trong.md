---
title: "Hợp đồng 300 trang, AI Agent đọc xong và trích đúng điều quan trọng trong 3 phút — việc mà con người mất cả buổi"
date: 2026-08-22
draft: false
description: "Chatbot chỉ đọc được những gì bạn dán vào. Hermes là AI Agent: bạn thả nguyên 300 trang hợp đồng, nó tự đọc song song, trích điều khoản rủi ro, tự động gia hạn, phạt, rồi báo cáo. Thực tế: 312 trang — Hermes gom 47 điểm rủi ro trong 3 phút; McKinsey ước tính 23% thời gian luật sư có thể tự động hoá, rà soát tài liệu là việc dễ tự động nhất."
image: "https://vanthuonghi.github.io/hermes-website/covers/hermes-oc-300-trang-hop-ong-trich-ieu-quan-trong.webp"
share_teaser: |
  Hỉ vừa thoát một cơn ác mộng: bộ hợp đồng đối tác cũ đổ về 312 trang. 📄
  Ngày xưa Hỉ mở từng file, ctrl+F từ khoá, copy điều khoản dán sang bảng — mất nửa ngày mà vẫn sợ sót.
  Tuần này Hỉ thả nguyên thư mục vào Hermes (AI Agent) và giao 1 câu: "đọc hết, trích điều rủi ro, báo sáng mai". Đi uống cafe về, có bảng 47 điểm cần coi chữ đỏ sẵn.
  Đây là điểm khác hẳn ChatGPT: chatbot chỉ đọc được cái BẠN dán vào khung chat. Còn Agent (nhân sự ảo) tự mở file, tự lật 300 trang, tự trích, tự nhớ để lần sau đối chiếu. Bạn không đụng tay.
  👉 Chi tiết + link ở BÌNH LUẬN nhé, ai từng ngồi rà hợp đồng cả buổi xem thử.
---

Tuần trước, bộ phận đối tác gửi sang một thư mục. Tôi mở ra, đếm nhanh: **312 trang** hợp đồng — 14 đối tác cũ, mỗi bên một đống phụ lục, điều khoản, cam kết gia hạn. Việc tôi cần: rà xem có điều nào tự động gia hạn âm thầm, điều nào phạt nặng, điều nào cho họ quyền chấm dứt bất cứ lúc nào.

Ngày xưa, tôi biết mình sẽ mất **nửa ngày**. Mở file 1, ctrl+F "gia hạn", chép dòng đó sang Excel. Mở file 2, lại ctrl+F, lại chép. Mắt hoa, tay mỏi, và cái sợ lớn nhất: **sót**. Sót một chữ "tự động" là tháng sau bị trừ tiền oan không biết kêu ai.

Lần này tôi làm khác. Tôi thả nguyên thư mục vào Hermes — AI Agent của mình — và giao đúng một câu. Đi pha cà phê. Quay lại, có một bảng 47 điểm cần "coi chữ" đánh dấu đỏ nằm sẵn. Tôi **không mở nổi một file PDF nào**.

Sự khác biệt nằm ở một ranh giới mà ai cũng nhầm: **chatbot và AI Agent là hai con vật khác hẳn nhau.**

## Chatbot vs Agent — cùng "đọc được", nhưng chỉ một bên "tự làm được"

Nhiều người tưởng ChatGPT là AI Agent. Không phải. Khác nhau ở chỗ: **ai là người mở file, ai là người lật từng trang.**

- **Chatbot (ChatGPT kiểu cũ):** nó chỉ đọc được cái *bạn dán vào khung chat*. Bạn muốn nó rà 312 trang? Thế thì bạn tự mở 14 file, tự copy từng đoạn dán vào, rồi hỏi. Chatbot đứng yên trong cái ô chat, không mở được ổ đĩa, không lật được thư mục, không nhớ được lần trước bạn rà cái gì. Nó là cuốn từ điển thông minh — mở tới đâu biết tới đó.
- **Hermes Agent:** tôi cấp cho nó quyền đọc thư mục của tôi. Giao một lệnh, nó tự **mở 14 file → lật 312 trang → trích điều khoản → soi điều rủi ro → gom bảng → hẹn giờ nhắc tôi sáng mai**. Nó là một "trợ lý pháp lý" có tay chân, tự đi lật hồ sơ thay tôi. Tôi không đụng vào giữa chừng.

Một con chỉ *trả lời*, một con *đi làm*. Đó là toàn bộ câu chuyện.

## Cái WOW thật: Agent đọc 300 trang như thế nào

Tôi sẽ kể cụ thể để bạn "thấy" nó làm, chứ không nói suông.

Sáng thứ Sáu, tôi thả thư mục `/hop-dong-2026` vào Hermes. Nó không đọc tuần tự như người — nó **chia 312 trang thành nhiều mảnh, đọc song song**, mỗi mảnh một luồng. Trong vòng chưa tới vài phút, nó đã quét xong và bắt đầu trích. Kết quả nó trả về không phải "văn bản tóm tắt lằng nhằng", mà một **bảng có cấu trúc**:

| Đối tác | Thời hạn | Tự động gia hạn | Phạt vi phạm | Quyền chấm dứt | Mức độ rủi ro |
|---|---|---|---|---|---|
| A | 12 tháng | ⚠️ Có, âm thầm | 15% giá trị | Họ được, tôi không | 🔴 Cao |
| B | 6 tháng | Không | 8% | Đôi bên | 🟡 Trung bình |
| … | … | … | … | … | … |

Con số cụ thể nó gom được: **47 điểm rủi ro** cần tôi xem lại, trong đó **12 điều khoản tự động gia hạn** (cái tôi sợ nhất), **8 điều phạt** trên 10% giá trị hợp đồng. Tất cả nằm gọn trong một bảng tôi chỉ việc lướt mắt.

Và cái khiến tôi thích nhất: nó **lưu hồ sơ vào memory**. Lần sau tôi ký đối tác mới, nó tự đối chiếu "điều này từng xuất hiện ở hợp đồng A, hồi đó rủi ro cao đấy" — tôi không cần nhắc lại từ đầu.

## Quy trình vòng lặp: giao 1 lần, nó chạy cả chuỗi

Đây là "vòng lặp 8 bước" thu gọn cho việc rà hợp đồng — bạn thấy Agent khác chatbot ở chỗ nó tự đi hết vòng, không dừng ở bước "viết xong":

1. **Nhận việc** — tôi giao: "đọc thư mục, trích 5 mục, báo sáng mai".
2. **Nạp dữ liệu** — nó tự mở 14 file PDF/docx, không cần tôi dán.
3. **Đọc song song** — chia mảnh, lật 312 trang cùng lúc.
4. **Trích xuất** — kéo ra bên, thời hạn, gia hạn, phạt, chấm dứt.
5. **Đối chiếu** — soi điều khoản mâu thuẫn, gắn cờ rủi ro.
6. **Báo cáo** — gom bảng, đánh dấu đỏ, viết tóm tắt 1 đoạn cho tôi.
7. **Lưu memory** — ghi hồ sơ để lần sau đối chiếu chéo.
8. **Nhắc & báo** — hẹn 8h sáng mai gửi tôi, rồi chờ lệnh tiếp.

Điểm mấu chốt: **tôi chỉ làm bước 1 và bước 8 (duyệt).** Sáu bước giữa nó tự lo. Chatbot dừng ở đâu? Dừng ở bước 4 — bạn hỏi gì nó trả lời đó, còn nối tiếp sang bước 5, 6, 7, 8 là bạn tự làm.

## Câu lệnh CEO — bạn copy luôn được

Tôi hay nói: một AI Agent hay hay dở, 80% nằm ở câu lệnh giao việc. Câu tôi dùng lần này:

> **"Đọc toàn bộ 312 trang hợp đồng trong thư mục `/hop-dong-2026`. Trích ra: (1) tên bên, (2) thời hạn, (3) điều khoản tự động gia hạn, (4) điều khoản phạt vi phạm, (5) quyền chấm dứt. Gom thành bảng, đánh dấu đỏ những điều rủi ro, viết 1 đoạn tóm tắt cho tôi. Nhắc tôi lúc 8h sáng mai. Lưu hồ sơ vào memory để lần sau đối chiếu."**

Một câu, đủ 5 mục cụ thể + định dạng bảng + tiêu chí rủi ro + giờ nhắc + lưu nhớ. Agent hiểu và chạy. Chatbot đọc câu này xong cũng chỉ… viết lại thành một đoạn văn, chứ không mở được thư mục.

## Kết quả đo lường — số thật, không phải lời quảng cáo

Tôi giữ thói quen đo mọi thứ bằng số, nên đây là con số thực tế tuần này:

- **312 trang** → Hermes xử lý và trích xong trong **dưới 3 phút** (tôi canh đồng hồ đi pha cà phê, về thấy bảng sẵn).
- **Cách đây không lâu, tôi tự làm** một bộ 80 trang mất **5 tiếng** thì xong sơ sơ. Quy ra, rà 312 trang tay có khi **cả buổi,甚至 nửa ngày**. Agent tiết kiệm cho tôi khoảng **vài tiếng mỗi đợt rà**.
- **47 điểm rủi ro** được gom tự động — con số này quan trọng hơn "nhanh": nó là thứ tôi sợ sót nhất khi làm tay.
- Theo **McKinsey Global Institute**, khoảng **23% thời gian của một luật sư có thể tự động hoá** bằng công nghệ hiện có, và **rà soát tài liệu (document review) là việc dễ tự động hoá nhất** trong nghề. Tức là cái tôi vừa làm không phải trò hề cá nhân — nó là đúng hướng cả ngành đang đi.
- Trên **HackerNews 2026**, tôi thấy hàng loạt bản phát hành agent "đọc và hiểu tài liệu thật" (như Screenpipe — ghi lại cách bạn làm việc rồi biến thành agent, hay các dự án agent đọc PLC/thiết bị công nghiệp). Nghĩa là hướng "Agent tự đọc hồ sơ" không phải tôi tưởng tượng — nó đang được ship thật ngoài kia.

## FAQ — 3 câu hỏi hay gặp

**1. Hermes đọc được mọi định dạng không — kể cả PDF scan, ảnh chụp?**
Được. Nó qua được PDF, Word, cả ảnh chụp hợp đồng (nhờ khả năng đọc ảnh). Miễn là file nằm trong thư mục bạn cấp quyền — bạn không cần copy tay từng dòng. Với bản scan mờ, nó báo "trang này không rõ, cần bạn xác nhận" chứ không bịa nội dung.

**2. Nó có sót điều khoản quan trọng không?**
Tôi dùng thêm bước **quality gate**: sau khi trích, Agent tự đọc lại bảng đối chiếu với bản gốc, gắn cờ chỗ thiếu. Như lần này nó tự bắt được 2 điều khoản "tự động gia hạn" nằm ở phụ lục cuối mà tôi từng hay bỏ qua. Nhưng tôi vẫn duyệt bước cuối — nó là trợ lý, không thay tôi ký tên.

**3. Giấy tờ nhạy cảm thế này, bảo mật sao?**
Nguyên tắc: tài liệu nằm trong không gian bạn cấp quyền, Agent xử lý trong luồng đó chứ không "đem đi" chỗ khác. Tôi không đẩy hợp đồng đối tác lên một server lạ. Quyền đọc là quyền bạn mở khoá, bạn rút bất cứ lúc nào.

## Kết — bạn đọc xong, làm gì tiếp?

Tôi kể chuyện này không phải để khoe máy móc. Mà vì năm nay tôi nhận ra: **thời gian của mình đắt hơn việc lật từng trang.** Cái đợt 312 trang kia, nếu làm tay tôi mất nửa ngày — nửa ngày đó đổi được bao nhiêu việc có ích hơn?

AI Agent không phải cái hộp "nói hay". Nó là **người cộng sự thật**: bạn thả việc vào, nó tự đi làm, tự kiểm tra, tự nhắc, rồi báo cáo. Chatbot đợi bạn hỏi. Agent nhận việc và chạy.

Nếu bạn cũng ngán cảnh ngồi rà hợp đồng, feedback, báo cáo thủ công — tôi đang mở khoá **Nhân Sự Toàn Năng Hermes**: 37 bài thực chiến, giá mở bán sớm **239K** (giá gốc 499K), hoàn tiền 7 ngày nếu không hợp. Xem chi tiết tại **speedreading.vn/shermes**.

Còn bây giờ, tôi đi duyệt 47 điểm đỏ kia — nhẹ nhõm vì không phải lật tay từng trang.
