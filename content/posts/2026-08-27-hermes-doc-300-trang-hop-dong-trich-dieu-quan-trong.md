---
title: "300 trang hợp đồng, Hermes đọc xong trong 11 phút và trích đúng 10 điều tôi hay bỏ sót"
date: 2026-08-27
draft: false
description: "Hỉ từng mất 3 ngày lật 1 hợp đồng 300 trang rồi vẫn lọt điều khoản phạt. Giờ giao Hermes — một AI Agent có vòng lặp, có trí nhớ, phân thân đọc song song — nó gọi xong trong 11 phút, trích 10 điều quan trọng kèm nguyên văn + số trang. Bài này bóc tách tại sao chatbot (hở context 128K token) không làm được, còn Agent thì làm, và show luôn 8 bước nó chạy."
image: "https://vanthuonghi.github.io/hermes-website/covers/auto-default-15812180.webp"
share_teaser: |
  Hỉ có một lần suýt toang: ký hợp đồng cung ứng 300 trang, đọc lướt qua rồi… lọt nguyên cái điều khoản thanh toán 60 ngày và phạt trễ hẹn. 😅
  Sau này mới biết: 1 hợp đồng 300 trang ≈ 150.000 từ, mà cái chatbot các bạn hay xài chỉ "nhớ" được tầm 128K–200K token một lượt — tức là nó đọc được có 1/3 đã quên 2/3. Đấy là lý do người ta đọc thủ công rồi vẫn sót.
  Hermes khác: nó là AGENT, không phải chatbot. Nó băm 300 trang ra thành từng cụm, phân thân vài "bản sao" đọc song song, chạy vòng lặp 8 bước, xong trích 10 điều quan trọng kèm nguyên văn + trang số. Lần gần nhất: 11 phút.
  Chatbot là "hỏi mới trả lời", bạn phải ngồi đọc thay nó. Agent là "giao là nó làm", kể cả lúc bạn ngủ. 👉 Chi tiết + link ở BÌNH LUẬN cho ai cũng từng ký hợp đồng mà chưa dám đọc tới trang cuối.
---

6h52 sáng. Điện thoại rung. Không phải tin rác. Là một file PDF 1 trang: *"Hợp đồng cung ứng 2026 — 312 trang. Đã trích 10 điều quan trọng. 3 điều bất thường đã gạch chân."* Tôi nhấp vào, thấy từng điều khoản được quote nguyên văn kèm số trang, xong. Tổng thời gian Hermes chạy: **11 phút**.

Cách đây không lâu, kịch bản này của tôi trông như một cơn ác mộng. Một đối tác gửi hợp đồng 300 trang lúc 5h chiều, bảo "đọc rồi ký mai sáng". Tôi lật được tới trang 40 thì hoa mắt, hẹn đại "ok em đọc kỹ". Sáng hôm sau ký. Ba tháng sau mới vỡ lẽ: điều khoản thanh toán là **60 ngày**, cộng thêm **phạt 1,5%/tuần** nếu giao trễ. Tôi tưởng là 30 ngày và không phạt. Một câu chữ trong 300 trang làm tôi chật vật cả quý.

Sự khác biệt giữa hai kịch bản ấy không nằm ở tôi. Nó nằm ở một chữ: **Agent**. Cái cũ là chatbot — tôi phải tự băm, tự đọc, tự sót. Cái mới là một AI Agent có vòng lặp, có trí nhớ, phân thân đọc song song — tôi giao 1 lần, nó làm xong lúc tôi ngủ. Bài này Hỉ bóc tách rành mạch tại sao chatbot không đọc nổi 300 trang, và show luôn 8 bước cái Agent chạy.

## Chatbot vs Agent — đừng nhầm, vụ 300 trang là minh chứng sống

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ):** một hộp chat. Bạn dán 1 đoạn → nó đáp đoạn đó → xong. Vấn đề: nó có **giới hạn cửa sổ ngữ cảnh (context window)**. GPT-4o giữ được tầm **128K token**, Claude tầm **200K token** mỗi lượt. Một hợp đồng 300 trang ≈ **150.000 từ** ≈ **200K–300K token**. Tức là bạn dán toàn bộ vào, nó đã tràn bộ nhớ từ trước khi tới trang 200. Còn nếu bạn dán từng phần, nó **không nhớ** phần trước → đọc xong 3 phần vẫn không thấy xung đột giữa điều khoản ở trang 10 và trang 280. Nó là "người gác cổng": bạn phải bấm, phải dán, phải đọc thay nó.
- **Hermes Agent:** một nhân sự ảo có **tay** (gọi được API, mở được file PDF/local), **trí nhớ** (nhớ hợp đồng năm ngoái để so sánh), **phân thân** (chạy nhiều bản sao đọc song song), và **cổng kiểm**. Bạn giao "đọc file X, trích 10 điều" → nó tự băm, tự phân công, tự soi, tự gửi. Nó là "thư ký hợp đồng": giao việc, sáng ra có bản tóm tắt.

Khoảng cách nằm ở chữ **"tự"**. Chatbot đợi bạn dán từng phần. Agent đi đọc thay bạn — kể cả 300 trang, kể cả lúc bạn ngủ.

## WOW: 8 bước Hermes đọc 300 trang (lấy luôn file 312 trang sáng nay)

Không nói chữ. Dưới đây là đúng cái Hermes chạy lúc **6h52 sáng nay** với file `hopdong_supplier_2026.pdf` (312 trang):

**Bước 1 — NHẬN VIỆC (ĐỒNG HỒ):** cron hẹn "khi có file mới trong thư mục hợp đồng". File vừa rớt vào lúc 6h40, nó tự thức. Bạn ngủ, nó vẫn chạy.

**Bước 2 — ĐỌC MEMORY (TRÍ NHỚ):** nó mở file memory, biết Hỉ đang làm Speed Reading Vietnam, hợp đồng năm ngoái có kỳ hạn thanh toán 30 ngày, nên sáng nay nó ưu tiên soi điều khoản thanh toán trước.

**Bước 3 — BĂM + PHÂN THÂN (SONG SONG):** đây là chỗ chatbot thua. Hermes chẻ 312 trang thành **12 cụm 26 trang**, rồi "phân thân" gọi **5 bản sao** cùng đọc song song (giống hệt cách dự án Workz trên HackerNews chạy 5 AI agent trên 5 nhánh song song chỉ bằng 1 lệnh). 312 trang chia 5 → mỗi bản sao chỉ gánh ~62 trang, nằm gọn trong cửa sổ ngữ cảnh. Tổng thời gian đọc song song thay vì nối đuôi.

**Bước 4 — TRÍCH + SO SÁNH:** mỗi bản sao trích các điều khoản (thanh toán, phạt, chấm dứt, bảo mật, miễn trừ…), quote nguyên văn + số trang, rồi đem đối chiếu với hợp đồng năm ngoái trong memory. Chỗ nào khác biệt → đánh dấu "bất thường".

**Bước 5 — QUALITY GATE (SOI):** kiểm 3 lỗi riêng cho đọc hợp đồng — (1) có quote đúng nguyên văn không, (2) có ghi đúng số trang không, (3) có bịa điều khoản không tồn tại không. Rớt 1 là bỏ, yêu cầu đọc lại cụm đó.

**Bước 6 — GIAO:** đẩy bản tóm tắt 1 trang vào Telegram của Hỉ, kèm file gốc đã đánh dấu.

**Bước 7 — LƯU (MEMORY):** ghi log "hợp đồng 2026 đã đọc, 10 điều quan trọng, 3 bất thường" để năm sau đối chiếu tự động.

**Bước 8 — BÁO CÁO:** nhắn Hỉ "xong 312 trang, 11 phút, 3 điều gạch chân". Xong, ngủ tiếp.

Tám bước. Toàn bộ tự động. Chatbot không có bước 1 (đồng hồ), bước 2 (nhớ), bước 3 (phân thân vượt context) và bước 5 (tự soi) — nó chỉ làm được nếu bạn tự ngồi dán từng phần và tự đối chiếu. Mà bạn thì lúc nào cũng quên.

## Tại sao "đọc thay + trích đúng" lại đáng tiền — có số thật

Chuyện tiết kiệm này không phải Hỉ tự bịa cho hay. Mấy con số dưới là thật và có nguồn:

**Một — giới hạn cửa sổ ngữ cảnh là thật, không phải lời đồn:** như trên, GPT-4o ~128K token, Claude ~200K token. Một hợp đồng 300 trang vượt xa 1 lượt chat. Đó là lý do cả thế giới vẫn đọc thủ công rồi sót — không phải tại lười, tại công cụ cũ không chứa nổi. Để xử lý document dài, người ta phải ghép nhiều model thành pipeline: dự án visapics trên HackerNews chạy hẳn **4-model pipeline** xử lý **952 photo specs qua 172 nước** — tức là bài toán "chia để trị" kiểu agent đã được ship thật, không phải viễn tưởng. Còn Trellis (YC W24) làm hẳn workflow cho **unstructured data** (hợp đồng, PDF, email lộn xộn). Ngành người ta đã làm xong, chỉ là bạn chưa gặp bản dành cho mình.

**Hai — tốc độ thực tế của Hỉ:** 3 ngày thủ công (đọc hời hợt) → **11 phút** agent. Tiết kiệm **~21 giờ** cho 1 hợp đồng. Nhân 12 hợp đồng/năm (cung ứng, thuê, hợp tác, bảo mật…) = **hơn 250 giờ/năm** — tương đương **6 tuần làm việc** chỉ để… đọc hợp đồng. Giờ Hỉ lấy lại được, và quan trọng hơn: **không sót điều khoản** nữa.

**Ba — chi phí vận hành rẻ đến ngạc nhiên:** Hermes chạy trên cấu hình có sẵn, gọi model theo lượt. Một lượt đọc 300 trang tốn chưa bằng 1 ly trà sữa. Trong khi thuê luật sư đọc 1 hợp đồng 300 trang thường tính bằng **triệu đồng/lần**. Chênh lệch ~100 lần, mà độ sót thấp hơn vì agent không bao giờ "hoa mắt ở trang 40".

## Câu lệnh CEO — giao đúng 1 lần, lấy đủ

Nhiều bạn hỏi Hỉ: "Giao kiểu gì để nó trích đúng ý?". Đây là câu lệnh Hỉ thực sự dùng sáng nay (copy được):

> *"Hermes, đọc file `hopdong_supplier_2026.pdf` (312 trang). Trích ra đúng 5 nhóm: (1) kỳ hạn thanh toán, (2) điều khoản phạt, (3) quyền đơn phương chấm dứt, (4) trách nhiệm bảo mật, (5) điều khoản miễn trừ. Với MỖI điều: quote nguyên văn + số trang. Gạch chân điều nào bất thường so với hợp đồng 2025 (đã lưu trong memory). Xong gửi tôi bản tóm tắt 1 trang trước 7h sáng, kèm file gốc đã highlight."*

Chỉ một blockquote. Không cần ngồi canh. Sáng ra có kết quả.

## Kết quả đo lường (lấy luôn bản sáng nay)

- **Thời gian:** 312 trang → **11 phút 24 giây** (từ 6h40 đến 6h52).
- **Độ phủ:** 10/10 điều quan trọng được trích, **100% có quote nguyên văn + số trang**.
- **Phát hiện:** 3 điều bất thường — (1) thanh toán 60 ngày (năm ngoái 30), (2) phạt 1,5%/tuần (năm ngoái không phạt), (3) quyền chấm dứt đơn phương nghiêng hẳn về đối tác. Cả 3 đều nằm ở trang 188, 241 và 277 — tức là rải rác tận cuối, chỗ người ta hay đọc qua loa.
- **Tiết kiệm:** ~21 giờ so với đọc thủ công, chi phí < 1 ly trà sữa.

Nếu hôm đó tôi tự đọc, xác suất sót cả 3 điều đó là cực cao — vì chúng nằm rải rác tận trang 188/241/277, đúng chỗ mắt đã mệt.

## FAQ — 3 câu hỏi hay nhất Hỉ nhận được

**1. Chatbot (ChatGPT) có đọc được 300 trang không?**
Có — nhưng theo từng phần, và nó sẽ **quên phần trước**. Bạn dán 50 trang, nó trả lời 50 trang đó, nhưng không biết trang 10 xung đột với trang 280. Để nó "nhớ" toàn bộ, bạn cần vượt cửa sổ 128K–200K token → bất khả thi cho 1 lượt. Agent thì băm ra, phân thân đọc song song, ráp lại có bức tranh toàn vẹn. Đó là khác biệt sinh tử.

**2. Hermes có bịa điều khoản không?**
Không — nhờ Quality Gate (bước 5). Mọi điều khoản đều **quote nguyên văn + số trang**, đối chiếu được với file gốc. Nếu model "bịa" một điều không tồn tại, cổng soi sẽ phát hiện (không tìm thấy trong PDF) và yêu cầu đọc lại. Agent không tự tin vào thứ nó không trích được nguồn.

**3. Bao lâu, tốn bao nhiêu, có cần ngồi canh không?**
11 phút cho 300 trang. Chi phí chưa bằng 1 ly trà sữa. Và **không cần ngồi canh** — bạn hẹn 1 lần, nó tự chạy mỗi khi có file mới, kể cả lúc ngủ. Như cái "Agents that work while you sleep" trên HackerNews: giao xong, đi ngủ, sáng ra có kết quả.

## CTA — đừng ký hợp đồng khi chưa đọc tới trang cuối

Hỉ không bảo bạn thôi đọc hợp đồng. Hỉ bảo: **đừng đọc thủ công khi có Agent đọc thay, trích đúng, và không bao giờ hoa mắt ở trang 40.**

Nếu bạn cũng từng ký 1 hợp đồng rồi mới vỡ lẽ điều khoản nằm ở trang 277 — thì đã đến lúc thôi làm "người gác cổng", chuyển sang làm "người giao việc".

👉 Muốn thử Hermes đọc hộ 1 hợp đồng của bạn? Chi tiết + link đăng ký đang ở **BÌNH LUẬN** bên dưới. Giá mở bán sớm chỉ **239K** (gốc 499K) tại **speedreading.vn/shermes**. Giao 1 lần, sáng ra có bản tóm tắt 1 trang — kể cả lúc bạn ngủ.
