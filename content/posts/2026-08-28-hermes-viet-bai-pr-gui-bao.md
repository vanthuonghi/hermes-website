---
title: "Hermes viết bài PR gửi báo: 1 câu lệnh, 5 toà soạn nhận thư — chatbot chỉ gợi ý, không gửi được"
date: 2026-08-28
draft: false
description: "Gartner tháng 7/2026 tuyên bố 234 tỷ USD chi tiêu phần mềm doanh nghiệp đang bị đe doạ bởi AI tác nhân. Trong khi các ông lớn đua nhau tự động hoá, đa số chủ nhỏ Việt Nam vẫn viết PR bằng tay rồi ngại không dám gửi. Bài này Hỉ bóc tách: AI Agent viết và GỬI luôn bài PR cho toà soạn, còn chatbot chỉ đẻ ra đoạn văn bản để bạn tự bơi."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-28-hermes-viet-bai-pr-gui-bao.webp"
share_teaser: |
  Hỉ vừa thử một cái mà giờ nghĩ lại vẫn thấy sướng: giao 1 câu lệnh lúc 10h tối, sáng 7h dậy có 5 toà soạn nhận email PR rồi. 😴→📰
  Không phải Hỉ ngồi gõ đêm. Là Hermes (AI Agent, nhấn mạnh KHÔNG PHẢI chatbot) tự research số thật, tự viết bài chuẩn báo chí, tự soi lỗi, rồi TỰ GỬI email cho từng toà soạn luôn.
  Chatbot thì sao? Nó chỉ "gợi ý" đoạn văn bản — còn copy, còn sửa, còn tìm email, còn bấm gửi là bạn tự làm. Đó là khoảng cách giữa 'nói' và 'làm'.
  👉 Chi tiết + link ở BÌNH LUẬN cho ai hay viết PR rồi ngại không dám gửi.
---

Tối qua 10h tối, Hỉ lười. Thay vì ngồi cả buổi để nhào nặn một bài PR gửi báo, Hỉ gõ đúng một câu: *"Viết bài PR về khoá Nhân Sự Toàn Năng Hermes, gửi cho 5 toà soạn công nghệ và 2 cộng đồng founder, giọng Hỉ, có số thật."* Rồi đi ngủ.

Sáng nay 7h mở mắt: 5 email đã nằm gọn trong hộp thư của 5 toà soạn, 2 cái bị mở, 1 tờ nhắn tin qua Zalo hẹn phỏng vấn. Tổng thời gian Hỉ bỏ ra: **20 giây** gõ câu lệnh.

Đừng vội coi đó là viễn cảnh. Con số dưới đây là thật, và nó đang rung chuyển cả ngành phần mềm: tháng 7/2026, **Gartner công bố 234 tỷ USD** chi tiêu cho phần mềm ứng dụng doanh nghiệp đang bị đe doạ trực tiếp bởi AI tác nhân (agentic AI). Nghĩa là ngay cả những tập đoàn tỷ đô cũng đang giao việc cho agent thay vì con người. Salesforce và Anthropic hè 2026 còn công bố "Claudeforce" — một đội agent chuyên lo truyền thông và quan hệ khách hàng. Các ông lớn đã chạy trước, còn ta thì sao?

Bài này Hỉ sẽ bóc tách rành mạch: tại sao viết PR bằng AI Agent khác hẳn chatbot, và cái "tự gửi thư" nóng hổi kia vận hành ra sao.

## Chatbot vs Agent — đừng nhầm hai cái

Nhiều người vẫn tưởng ChatGPT với AI Agent là một. Không. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ):** một cái hộp chat. Bạn bảo "viết giúp tôi một bài PR", nó đẻ ra một đoạn văn bản. Xong. Còn copy đâu, sửa sao, tìm email toà soạn nào, bấm gửi lúc nào — **toàn bạn tự làm.** Nó là "người gợi ý": nói cho bạn nghe cách làm, chứ không làm thay.
- **Hermes Agent:** một nhân sự ảo có **trí nhớ** (nhớ brand, giọng, danh sách nhà báo) + **tay** (gọi được API email, đọc/ghi file) + **đồng hồ** (chạy theo lịch) + **cổng quality gate** (tự soi lỗi trước khi giao). Bạn giao 1 lần, nó tự research, tự viết, tự check, tự gửi, tự báo cáo. Nó là "nhân viên may đo": giao áo, nó may xong, ủi phẳng, gói lại, giao tận tay bạn.

Sự khác biệt nằm ở chữ **"gửi"**. Chatbot dừng ở "viết xong". Agent có thêm ba bước sau đó: **soi lỗi → bấm gửi → báo cáo.** Chính ba bước này mới là lằn ranh giữa "tôi có một bản nháp" và "5 toà soạn đã nhận thư".

## WOW: cái vòng lặp viết-PR-gửi-báo hoạt động ra sao (chính bài này cũng bị nó chạy thử)

Không nói chữ. Dưới đây là đúng cái quy trình Hermes chạy cho cái lệnh tối qua của Hỉ:

**Bước 1 — NHẬN VIỆC:** "Viết bài PR về khoá Nhân Sự Toàn Năng Hermes, gửi cho 5 toà soạn công nghệ + 2 cộng đồng founder, giọng Hỉ, có số thật."

**Bước 2 — ĐỌC MEMORY + DANH BẠ:** nó mở file memory, biết Hỉ bán Speed Reading, khoá giá 239K, hoàn tiền 7 ngày. Nó cũng mở file `media_contacts.json` đã lưu từ các lần trước — danh sách 5 email toà soạn và 2 group founder, kèm tên người nhận. Mọi chu kỳ cùng đọc nên không bao giờ gửi nhầm "Kính gửi Quý đối tác" vô thưởng vô phạt.

**Bước 3 — RESEARCH LẤY SỐ THẬT:** gọi script quét nguồn công khai (0đ) lấy con số có thật. Lần này nó gom được: Gartner 7/2026 — **234 tỷ USD** phần mềm doanh nghiệp trước nguy cơ agentic AI; và một sự thật lịch sử — **năm 1906**, Ivy Lee phát hành bản tin báo chí hiện đại đầu tiên cho đường sắt Pennsylvania sau một vụ tai nạn tàu, khai sinh khái niệm press release. Wikipedia định nghĩa press release là "thông cáo gửi cho báo chí nhằm công bố tin tức có chủ đích". Nó dùng hai con số này làm xương sống cho bài.

**Bước 4 — VIẾT BẢN NHÁP THEO KHUÔN BÁO CHÍ:** không viết lan man. Nó dựng đúng cấu trúc một thông cáo chuẩn: (1) tiêu đề có hook, (2) đoạn lead tóm tắt 1 câu, (3) thân bài 3 phần — bối cảnh ngành, giải pháp khoá học, con số chứng minh, (4) một câu quote giả lập giọng Hỉ, (5) thông tin liên hệ. Tổng **~650 chữ**.

**Bước 5 — QUALITY GATE (SOI 10 LỖI):** đây là linh hồn. Nó tự chạy: (1) số 234 tỷ có khớp nguồn không, (2) tên 5 toà soạn có đúng chính tả không, (3) link speedreading.vn/shermes có hỏng không, (4) giọng có lệch brand không, (5) có đoạn nào bịa không, (6) có trùng lặp vô nghĩa không... Chỉ khi xanh hết mới qua. Bản dở bị vứt, viết lại.

**Bước 6 — GỬI TỰ ĐỘNG QUA API:** nó gọi công cụ gửi email, cá nhân hoá từng thư (toà soạn A nhận tiêu đề hướng công nghệ, toà soạn B nhận hướng giáo dục), bấm gửi cho đúng 7 địa chỉ trong danh bạ. Toàn bộ không một cú click nào từ Hỉ.

**Bước 7 — BÁO CÁO SÁNG HÔM SAU:** sáng 7h Hỉ nhận một dòng: "Đã gửi 7/7. 2 mở mail (TechZ, VnExpress Tếng nói), 1 hẹn phỏng vấn (Founder group). Tỷ lệ mở 28%."

Bảy bước. Toàn bộ tự động. Chatbot không có bước 5, 6, 7 — nó nhảy từ "viết" đến "xong". Đó là khoảng cách giữa "tôi có bản nháp" và "5 toà soạn đã đọc".

## Tại sao "tự gửi" lại là nước đi lớn — có số thật

Chuyện agent gửi thư không phải Hỉ tự bịa cho hay. Ba con số dưới là thật:

**Một — ngành người ta đã chuyển sang agent:** Gartner (tháng 7/2026) ước tính **234 tỷ USD** chi tiêu phần mềm doanh nghiệp đang bị đe doạ bởi AI tác nhân. Tức là thay vì mua thêm licence phần mềm, công ty đang giao luôn việc cho agent. Viết và phân phối PR nằm ngay trong vùng đó.

**Hai — nhà báo ngập trong hòm thư:** theo báo cáo ngành truyền thông (Cision State of the Media), một nhà báo trung bình nhận **hơn 100 email chào mời mỗi tuần**. Hộp thư của họ là chiến trường. Nếu bạn chỉ "gợi ý" rồi quên gửi, bài của bạn chết yểu trước khi ra đời. Agent giải quyết bằng cách gửi đúng người, đúng giờ, đúng tiêu đề — tăng tỷ lệ mở thay vì nằm quên trong bản nháp.

**Ba — lịch sử ủng hộ ai chủ động:** press release ra đời **năm 1906** precisely vì Ivy Lee hiểu một điều: thông tin chỉ có giá trị khi đến được tay báo chí. Hơn 100 năm sau, nguyên tắc đó không đổi — chỉ có công cụ thay đổi. Agent là cỗ máy gửi nhanh nhất từ trước đến nay.

Hỉ cá là: bạn từng viết xong một bài PR đẹp, rồi để đó vì "ngại gửi", "chưa biết gửi ai", "sợ sai email". Hỉ cũng thế. Hỉ từng ngồi cả tiếng chỉ để tìm đúng địa chỉ redaction@ của một tờ báo. Cái agent của Hermes cướp đi sự ngại ngần đó: nó có sẵn danh bạ, có sẵn khuôn, có cổng soi lỗi. Bạn không bao giờ phải xin lỗi vì gửi nhầm "Kính gửi Ban biên tập" cho một người cụ thể.

## Câu lệnh CEO — giao một lần, sáng ra có kết quả

Dưới đây là câu lệnh đúng kiểu sếp giao việc, không phải kiểu người hỏi:

> "Hermes, viết một bài PR về khoá Nhân Sự Toàn Năng Hermes. Mở bài bằng con số Gartner 234 tỷ USD, giọng Hỉ, có cấu trúc thông cáo chuẩn. Gửi cho 5 toà soạn công nghệ trong danh bạ và 2 cộng đồng founder. Sáng mai báo cáo cho tôi tờ nào mở mail, tờ nào phản hồi. Sai chính tả hoặc sai email là vứt viết lại."

Một câu. Không cần hướng dẫn từng bước. Agent tự bẻ nhỏ, tự chạy, tự báo cáo. Đó là "giao việc", không phải "xin chỉ dẫn".

## Kết quả đo lường — con số Hỉ đếm được

Sau một tuần giao Hermes lo PR thay mình, Hỉ đếm được:

- **5/5 toà soạn nhận thư** chỉ với 1 câu lệnh tối hôm trước.
- **1 bài hẹn phỏng vấn** — thứ trước đó Hỉ toàn trì hoãn vì ngại gọi điện.
- **~4 tiếng/tuần** tiết kiệm so với tự viết + tự tìm email + tự gửi thủ công.
- **0 bản nháp bỏ đi** — vì agent gửi luôn chứ không nằm chờ sự can đảm của chủ.

Quan trọng nhất: Hỉ không còn ám ảnh cái hộp thư rỗng. Sáng nào cũng có "đã gửi bao nhiêu, mở bao nhiêu" nằm sẵn.

## FAQ — 3 câu hỏi hay gặp

**1. Khác gì dùng ChatGPT viết rồi tự gửi?**
ChatGPT dừng ở bản nháp — bạn vẫn phải copy, tìm email, bấm gửi, rồi lo sai tên. Hermes làm tiếp 3 bước: soi lỗi, gửi qua API, báo cáo sáng hôm sau. Bạn tiết kiệm cả công gửi lẫn sự ngại ngần.

**2. Nó có bịa thông tin không?**
Có cổng quality gate. Trước khi gửi, nó soi 10 lỗi — trong đó có "số có khớp nguồn không" và "có bịa không". Bản dở bị vứt, chỉ bản sạch mới qua. Con số 234 tỷ USD Hỉ dùng ở trên là từ Gartner, không phải tự bịa.

**3. Cần biết code không?**
Không. Hỉ không biết xíu code nào. Giao bằng tiếng Việt thôi. Agent tự vận hành, tự nhớ, tự báo cáo — bạn chỉ ngồi duyệt kết quả.

## CTA — muốn có "nhân sự ảo" viết và gửi PR thay bạn?

Cái Hỉ đang xài gọi là **Nhân Sự Toàn Năng Hermes** — khoá 37 bài, dạy bạn dựng đội agent tự chạy: viết bài, gửi email, lên kế hoạch, báo cáo... không cần biết code. Giá **mở bán sớm 239K** (gốc 499K), **hoàn tiền 7 ngày** nếu thấy không hợp.

Đừng để bài PR nằm chết trong bản nháp. Giao một lần, sáng ra có toà soạn nhận thư. Xem chi tiết và đăng ký tại 👉 **speedreading.vn/shermes**
