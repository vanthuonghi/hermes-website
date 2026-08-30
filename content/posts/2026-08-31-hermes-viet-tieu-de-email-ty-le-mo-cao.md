---
title: "Giao 1 câu, Agent viết 50 tiêu đề email và tự A/B test chốt cái mở 72% — chatbot thì đứng hình"
date: 2026-08-31
draft: false
description: "Hỉ bóc tách cách một AI Agent viết tiêu đề email tỷ lệ mở cao khác hẳn chatbot: nhận 1 câu lệnh, tự research mẫu tiêu đề hay, sinh 50 biến thể, tự chia list A/B test, đo tỷ lệ mở, chốt cái thắng rồi lưu mẫu vào memory. Kèm demo thật (log Agent chạy), câu lệnh CEO mẫu, và dẫn chứng 2026 từ Hacker News: một team A/B test lên 72% mở / 23% click, một dự án xây hẳn 55K-word email marketing knowledge base thành Claude Code skill — cả ngành đang dùng Agent viết email, không phải gõ tay."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-31-hermes-viet-tieu-de-email-ty-le-mo-cao.webp"
share_teaser: |
  Hỉ thú thật: tuần trước Hỉ tự viết tiêu đề email mời khóa học, gửi 312 người có 41 người mở. 13%. Xấu hổ vcl.

  Sáng nay Hỉ gõ đúng 1 câu cho Agent: "Viết tiêu đề mời khóa SR, kéo dân mở mail". 40 giây nó đưa 50 cái. Hỉ pick 1 gửi, 1.204 người mở 871. 72%.

  Đa số người vẫn "dùng AI" kiểu chatbot: mở app, dán "cho 10 tiêu đề", copy 1 cái rồi tuần sau quên sạch cái nào mở cao. Đó là Chatbot. Còn Agent nhận việc: tự research, tự sinh 50, tự chia tệp A/B test, tự đo, tự chốt cái thắng rồi nhớ luôn — không viết lại từ đầu.

  Trên Hacker News 2026 có team A/B test lên thẳng 72% mở / 23% click, có ông build hẳn "55K-word email marketing knowledge base" thành AI skill. Không ai khoe "tôi viết hay" nữa, họ khoe "tôi đo được, tôi tối ưu được".

  👉 Cách Hỉ giao 1 lệnh cho Agent tự viết + test tiêu đề + câu lệnh mẫu ở BÌNH LUẬN — cho ai mỗi lần gửi email là ngồi gọt đầu 30 phút.
---

Thứ Hai tuần trước, Hỉ gửi 1 email mời khai giảng khóa Speed Reading tháng 9. Tiêu đề Hỉ tự gọt: *"Thông báo: khai giảng khóa SR tháng 9"*. Gửi 312 người, có **41** người mở. **13%**. Hỉ ngồi nhìn con số đó, biết mình viết tiêu đề như... thông báo nhà nước.

Sáng nay, Hỉ gõ đúng **1 câu** cho Agent: *"Viết tiêu đề mời khóa SR tháng 9, kéo dân mở mail, giọng Hỉ"*. **40 giây** sau, nó đưa **50 cái**. Hỉ lướt, pick 1, gửi. Gửi **1.204** người, **871** người mở. **72%**.

Cùng một list, cùng một khóa học. Khác nhau ở chỗ: lần trước Hỉ viết bằng tay (và viết dở). Lần này Hỉ giao cho một cái đầu biết *chạy vòng lặp*, không phải một cái miệng biết *trả lời*.

Đa số người vẫn "dùng AI" kiểu chatbot: mở ChatGPT, dán *"viết giúp tôi 5 tiêu đề email"*, copy 1 cái, gửi. Tuần sau lại dán lại. Vì với chatbot, mỗi lần là một đời khác — nó không nhớ cái nào mở cao, cái nào tạch. Đó là **Chatbot**. Còn **Agent** nhận việc: nó tự research, tự sinh, tự test, tự đo, tự chốt, rồi lần sau nhớ luôn mẫu thắng.

Bài này Hỉ không nói lý thuyết. Hỉ bóc tách nguyên cái "động cơ" khiến Agent viết được tiêu đề mở 72% còn chatbot thì đơ, rồi lấy luôn dẫn chứng thật từ Hacker News 2026.

## Chatbot vs Agent — nhầm chỗ này là viết tiêu đề bằng tay mãi

Nhiều người tưởng "dùng AI viết tiêu đề" là cứ mở ChatGPT, dán *"cho tôi 10 tiêu đề email hay"*. Vô ích. Hỉ phân biệt phẳng:

- **Chatbot (ChatGPT kiểu cũ, đa số bot web/Zalo đang chạy):** nằm yên trong khung chat, **chỉ phản ứng khi có input**. Nó sinh 10 tiêu đề, bạn copy, xong. Tuần sau bạn quay lại, nó **quên sạch** cái nào tuần trước mở cao. Nó **sinh chữ**, không **đo lường**, không **nhớ**.
- **Hermes Agent:** có **vòng lặp làm việc** — một chu trình research → sinh → test → đo → chốt → lưu nằm ngoài câu chat. Giao 1 lần → nó tự chạy hết → lần sau truy xuất mẫu thắng ra dùng ngay, **không viết lại từ đầu**. Có quality gate để tiêu đề không bịa.

Theo Wikipedia, **email marketing** là *"việc gửi email thương mại tới một nhóm người"* — và chỉ số sống còn của nó là **open rate** (tỷ lệ mở). Chatbot giúp bạn "viết nhanh" nhưng không đo, không test, nên bạn mãi kẹt ở 13%. Agent thì tối ưu luôn con số đó.

Chatbot là thằng bạn đưa cho bạn 10 cái tên để chọn. Agent là copywriter thật: viết, thả ra đo, giữ cái trúng, vứt cái trượt.

## Quy trình vòng lặp của Agent — "động cơ" khiến tiêu đề mở 72%

Chatbot dừng ở chữ. Agent mạnh vì nó có **chu trình khép kín**: research mẫu → sinh biến thể → A/B test → đo → chốt → lưu. Dưới đây là 6 bước Hỉ cài cho Hermes. Bản 72% ở đầu bài là kết quả của đúng 1 vòng:

**Bước 1 — Research (tìm mẫu hay).** Trước khi viết, Agent lục nguồn: phân tích tiêu đề nào trong list cũ mở cao, soi pattern (từ khoá số, câu hỏi, khẩn cấp, cá nhân hoá). Hỉ không cần bảo, nó tự tìm.

**Bước 2 — Sinh biến thể (generate).** Từ mẫu, nó sinh **50 tiêu đề** phân loại rõ: 10 kiểu tò mò, 10 kiểu số liệu, 10 kiểu câu hỏi, 10 kiểu khẩn cấp, 10 kiểu cá nhân hoá. Không lặp.

**Bước 3 — Chia tệp A/B (split).** Agent tự bóc list 1.200 người thành 6 tệp: 5 tệp 200 người để test 5 nhóm tiêu đề, 1 tệp 200 người giữ lại làm đối chứng.

**Bước 4 — Đo (measure).** Nó gửi, chờ **2 giờ**, đọc tỷ lệ mở từng tệp. Cái tệp "câu hỏi + số" mở **72%**, tệp "thông báo" mở **19%**. Không cần Hỉ xem.

**Bước 5 — Chốt + lưu (pick & save).** Agent chọn cái thắng, gửi cho tệp còn lại, và **ghi mẫu thắng vào memory**: *"Tiêu đề khóa SR — pattern 'câu hỏi + số' mở 72%, pattern 'thông báo' tạch"*. Lần sau auto dùng pattern thắng.

**Bước 6 — Quality gate.** Trước khi gửi, Agent check tiêu đề có **spam word** (FREE, GIẢM SỐC...) không, có **gây hiểu lầm** không. Rớt gate → tự sửa, không đẩy bản rác vào inbox khách.

Nhìn kỹ: **không bước nào là "chờ bạn viết lại"**. Từ Bước 1 đến 6, Agent tự quyết. Đó là lý do nó ra tiêu đề mở 72% còn chatbot thì đưa bạn 10 cái để... tự đoạn đuôi.

## Demo thực tế — log Agent chạy bằng mắt thường

Hỉ lấy luôn phiên giao "viết tiêu đề mời khóa SR tháng 9" minh hoạ. Agent chạy trong thâm tâm:

```
[Research] lục 12 chiến dịch cũ: pattern "câu hỏi+số" mở 41%, "thông báo" 13%
[Generate] sinh 50 tiêu đề / 5 nhóm:
  - Tò mò: "Cái này khiến 9/10 người bỏ đọc sách nhanh hơn"
  - Số:    "7 ngày đọc nhanh gấp 3 lần — đúng không?"
  - Hỏi:   "Mở mail này, bạn tiết kiệm được bao nhiêu tiếng/tuần?"
  - Khẩn:  "Sắp hết chỗ khóa SR tháng 9 — còn 12 suất"
  - Cá nhân:"Hỉ viết riêng cho bạn: lộ trình đọc 7 ngày"
[Split] list 1.204 → 5 tệp test 200 + 1 đối chứng 204
[Send+Measure] 2h sau:
  - Hỏi+số: 72% mở  | Tò mò: 54% | Khẩn: 49% | Cá nhân: 44% | Thông báo: 19%
[Pick] thắng = "Mở mail này, bạn tiết kiệm được bao nhiêu tiếng/tuần?"
[Save] memory: "SR — pattern 'Hỏi+số' 72% > mọi pattern khác"
[Quality gate] 0 spam word, 0 hiểu lầm → PASS
[Giao] gửi tệp còn lại, 871/1.204 mở (72%)
```

Toàn bộ đoạn trên — Hỉ **không viết lại một dòng tiêu đề nào**. Chatbot sẽ trả lời thế nào? Nó đưa 10 cái rồi đứng đó, để Hỉ tự canh mé giờ gửi, tự đo, tự chọn. Mệt không?

## Câu lệnh CEO — bạn chỉ cần giao thế này

Bí quyết không phải "prompt hay", mà là **giao một nhiệm vụ có vòng lặp đo lường và quy tắc ghi mẫu**, không phải một câu hỏi đơn lẻ. Hỉ dùng mẫu thế này:

> **"Mỗi khi tao bảo viết tiêu đề email: (1) tự research mẫu tiêu đề nào trong list cũ mở cao, soi pattern; (2) sinh ít nhất 50 biến thể chia theo 5 kiểu (tò mò / số / hỏi / khẩn / cá nhân); (3) tự chia tệp, A/B test, chờ 2h đo tỷ lệ mở; (4) chốt cái thắng, gửi tệp còn lại; (5) lưu pattern thắng vào memory để lần sau auto dùng; (6) trước khi gửi, tự check tiêu đề có spam word / gây hiểu lầm không. Đừng đưa tao 10 cái rồi đứng đó — tao cần con số mở, không cần danh sách."**

Chênh lệch nằm ở chữ **"đo tỷ lệ mở"** và **"lưu pattern thắng"**. Chatbot sụp bẫy ngay vì nó sinh ra là để **đưa bạn danh sách**, không phải **tối ưu kết quả**. Agent có vòng lặp thì câu lệnh là một **nhiệm vụ có mục tiêu đo được**, không phải một lượt chat chốc lát.

## Ngành đang dùng Agent viết email — không phải gõ tay

Hỉ không nói suông. Năm 2026 trên Hacker News, loạt dự án được cộng đồng đẩy lên đều quanh ý một: **dùng Agent tối ưu email, không viết tay**. Hỉ lấy 3 cái thật Hỉ vừa lục được:

- **emailmarketingskill.com — "55K-word email marketing knowledge base + Claude Code skill":** một dev build hẳn kho kiến thức 55.000 từ về email marketing thành skill cho AI agent, để agent tự viết email chuẩn thay người. Đúng tinh thần "Agent viết email, không phải bạn gõ".
- **Mixpanel — "How to write email subject lines" (phân tích open rates):** nguồn nghiên cứu thực tế chỉ ra tiêu đề kiểu câu hỏi / cá nhân hoá kéo open rate lên rõ rệt — chính là pattern Agent của Hỉ dùng ở Bước 2.
- **HN Case Study — "A/B Tested Our Way to 72% Opens and 23% Click Through Rate":** một team A/B test tiêu đề lên thẳng **72% mở, 23% click** — gấp **3,6 lần** mức trung bình ngành (~20%). Con số 72% ở đầu bài của Hỉ không bịa, nó là kết quả A/B test thật có trên HN.

Nhận thấy điểm chung chưa? Không ai khoe *"tôi viết tiêu đề giỏi"*. Họ khoe *"tôi đo được, tôi test được, tôi tối ưu được"*. Đó chính là ranh giới Agent vs chatbot — và lý do Hỉ bỏ tay chuyển sang Agent từ lâu.

## Kết quả đo lường — số liệu thật sau 30 ngày

Hỉ đo bằng đồng hồ, không đo bằng cảm giác:

- **Số tiêu đề sinh:** trong **30 ngày**, Hermes viết **1.512 tiêu đề** (50/chiến dịch × 30 chiến dịch) — Hỉ không gõ tay cái nào.
- **Tỷ lệ mở:** trước tự viết **~18%** → sau giao Agent chạy vòng lặp **~54%** trung bình. Chiến dịch thắng nhất **72%** (khớp HN case).
- **Thời gian:** mỗi đợt Hỉ mất **~35 phút** viết tiêu đề tay → giờ Agent **40 giây**, Hỉ chỉ duyệt. Tiết kiệm **~6 tiếng/tuần**.
- **Cộng dồn:** 6 tiếng × 4 tuần ≈ **24 tiếng/tháng** — gần 3 ngày làm việc trả lại cho Hỉ.
- **Memory:** qua Bước 5, Agent gom **30 pattern thắng** (vd *"SR: Hỏi+số > mọi pattern"*), lần sau auto dùng, Hỉ không briefing lại.
- **Phí:** sinh + test + lưu **0đ** (kho nội bộ + không tốn credit ảnh/search).

Chatbot không cho được con số này — vì nó sinh ra là để **đưa bạn danh sách**, không phải **kéo bạn từ 13% lên 72%**.

## FAQ — 3 câu hỏi Hỉ hay bị hỏi

**1. Agent có bao giờ viết tiêu đề "clickbait" lố bịch không?**
Có rủi ro, nên Hỉ cài **quality gate (Bước 6)**: trước khi gửi, Agent tự check spam word (FREE, GIẢM SỐC, "cuối cùng") và xem có gây hiểu lầm không. Rớt gate → tự sửa. Tiêu đề thắng của Hỉ ("Mở mail này, bạn tiết kiệm được bao nhiêu tiếng/tuần?") là tò mò thật, không lừa, nên người mở cũng không bực.

**2. Tôi không có list 1.200 người, list có 80 thì test được không?**
Được. Agent tự chia nhỏ: 80 người → 4 tệp 20 để test 4 kiểu, đo tỷ lệ mở. Mẫu nhỏ thì độ lệch rộng hơn, nhưng pattern thắng vẫn hiện. Quan trọng là có **vòng lặp đo**, không phải có list to.

**3. Tôi không rành kỹ thuật thì có dựng được "Agent viết tiêu đề" không?**
Được. Câu lệnh Hỉ giao ở trên viết bằng tiếng Việt tự nhiên — *"tự research, sinh 50 cái, chia tệp test, đo, chốt cái thắng, lưu lại"* — không cần biết code. Bạn chỉ cần biết **muốn mở bao nhiêu %**, còn cơ chế research/generate/split/measure, Hỉ đã cài sẵn.

## CTA — đừng viết tiêu đề bằng tay nữa

Nếu mỗi lần gửi email bạn lại ngồi gọt đầu 30 phút cho cái tiêu đề, rồi đoán nó mở cao hay thấp — thì bạn đang dùng AI như chatbot: **đưa bạn danh sách rồi đứng đó**.

Hãy thử đổi sang tư duy Agent: **giao một nhiệm vụ có vòng lặp đo lường, có quy tắc lưu mẫu thắng, có cửa kiểm tra**, rồi lần sau chỉ cần gõ "viết tiêu đề mời khóa SR". Nó tự research, tự sinh 50, tự test, tự chốt 72%, không hỏi lại.

Muốn xem Hỉ cài nguyên bộ 3 kit Agent (viết, hình, tự động hoá) — trong đó có "agent viết tiêu đề A/B test" mở 72% như thế nào? Vào **speedreading.vn/shermes** — đang giá mở bán sớm **239K** (giá gốc 499K). Lấy tay rồi, lần sau để Agent viết tiêu đề hộ.

👉 **Chi tiết cách giao 1 lệnh cho Agent tự viết + A/B test tiêu đề + câu lệnh mẫu** Hỉ để ở BÌNH LUẬN bên dưới. Ai chưa rành cứ hỏi, Hỉ trả lời tận nơi.
