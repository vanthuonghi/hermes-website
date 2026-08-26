---
title: "Cuộc họp 90 phút, biên bản 4 phút — Hermes viết thay, không sót một đầu việc"
date: 2026-08-27
draft: false
description: "Hỉ từng họp xong rồi... quên luôn ai gánh việc gì, tới 2 tuần sau mới hỏi 'cái đó ai làm nhỉ'. Giờ giao Hermes — một AI Agent có vòng lặp, có trí nhớ, phân thân phiên âm song song — nó tự ghi biên bản +action items ngay khi họp tắt, 4 phút cho cuộc họp 90 phút. Bài này bóc tách tại sao chatbot (chỉ chờ bạn dán từng đoạn) không làm được, còn Agent thì làm, và show luôn 8 bước nó chạy."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-27-hermes-tom-tat-cuoc-hop-thanh-bien-ban.webp"
share_teaser: |
  Hỉ có một vết sẹo: họp team chiều thứ Sáu xong, ai về nấy, tới thứ Sáu tuần sau mới nhớ ra hỏi "cái báo cáo đó ai làm nhỉ?" — im re. 😅
  Lý do không phải lười. Là sau 90 phút họp, não ai cũng lùng bùng: quyết định gì, ai làm, deadline bao nhiêu... chả ai ghi đàng hoàng. Mà cái chatbot các bạn hay xài? Nó ngồi chờ bạn dán từng đoạn rồi mới tóm tắt — bạn vẫn là người phải nghe, phải bấm, phải tự ghi.
  Hermes khác: nó là AGENT. Cuộc họp vừa tắt, nó tự băm file ghi âm, phân thân vài "bản sao" phiên âm song song, rút đúng quyết định + người chịu trách nhiệm + hạn chót, chạy quality gate soi 3 lỗi, xong đẩy biên bản vào điện thoại bạn. Lần gần nhất: 90 phút họp → biên bản + 12 action items trong 4 phút.
  Chatbot là "bạn dán, nó mới tóm tắt". Agent là "họp xong, biên bản có ngay". 👉 Chi tiết + link ở BÌNH LUẬN cho ai cũng từng họp xong rồi quên mình phải làm gì.
---

8h05 tối. Họp team online vừa tắt. Điện thoại reo. Không phải tin nhắn vô thưởng: một file `biendan_2026-08-27.md` dài 1 trang — đúng 12 đầu việc, mỗi cái gắn tên người chịu trách nhiệm và ngày phải xong, kèm 3 quyết định cả team vừa chốt. Tổng thời gian Hermes chạy: **4 phút 12 giây** cho cuộc họp **90 phút**.

Cách đây nửa năm, kịch bản này của tôi là một trò cười buồn. Họp chiều thứ Sáu, 6 người, xong ai về nấy. Thứ Hai tôi mở note, thấy có đúng 2 dòng mình ghi vội lúc họp: "làm cái landing page" và "gửi báo cáo". Không rõ ai làm, không rõ khi nào xong. Thứ Sáu tuần sau tôi hỏi "cái landing page ai làm rồi?", im re. Hoá ra tuần trước chả ai ghi, chả ai nhớ, và cái task bay màu luôn.

Sự khác biệt giữa hai kịch bản ấy không nằm ở đội của tôi. Nó nằm ở một chữ: **Agent**. Cái cũ là chatbot — tôi phải tự nghe, tự ghi, tự quên. Cái mới là một AI Agent có vòng lặp, có trí nhớ, phân thân phiên âm song song — tôi họp xong, nó làm tiếp phần tôi hay quên. Bài này Hỉ bóc tách rành mạch tại sao chatbot không ghi nổi biên bản ra hồn, và show luôn 8 bước cái Agent chạy.

## Chatbot vs Agent — đừng nhầm, vụ biên bản họp là minh chứng sống

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ):** một hộp chat. Bạn mở file ghi âm, copy 1 đoạn transcript dán vào → nó tóm tắt đoạn đó → xong. Vấn đề: (1) nó **không tự mở** file ghi âm, bạn phải ngồi lôi transcript ra; (2) nó **không nhớ** cuộc họp tuần trước, nên không biết "cái task landing page" thực ra đã bị hoãn tuần trước; (3) nó **không gán người** — bạn hỏi "ai làm?", nó bảo "dựa trên transcript thì không rõ". Nó là "thư ký tạm vụ": bạn đưa gì, nó xử lý đó, còn phần nghe và ghi thay thì bạn tự lo.
- **Hermes Agent:** một nhân sự ảo có **tay** (mở được file ghi âm/local, gọi được API lịch), **trí nhớ** (nhớ task tuần trước để không trùng lặp), **phân thân** (chạy nhiều bản sao phiên âm song song), và **cổng kiểm**. Bạn giao "họp xong thì viết biên bản" → nó tự bắt file, tự băm, tự gán người, tự soi, tự gửi. Nó là "thư ký hội nghị": giao việc, họp xong có bản tóm tắt.

Khoảng cách nằm ở chữ **"tự"**. Chatbot đợi bạn dán từng đoạn. Agent đi họp thay bạn — kể cả khi bạn đã tắt máy, đi ăn.

## WOW: 8 bước Hermes viết biên bản (lấy luôn cuộc họp 8h05 tối nay)

Không nói chữ. Dưới đây là đúng cái Hermes chạy lúc **8h05 tối nay** với file `meeting_team_2026-08-27.mp3` (90 phút, 6 người):

**Bước 1 — NHẬN VIỆC (ĐỒNG HỒ):** cron hẹn "khi có file ghi âm mới rớt vào thư mục họp". File vừa tắt lúc 8h00, nó tự thức. Bạn đi ăn, nó vẫn chạy.

**Bước 2 — ĐỌC MEMORY (TRÍ NHỚ):** nó mở file memory, biết tuần trước team đang kẹt "landing page" và "báo cáo đối tác", nên sáng nay nó ưu tiên soi xem hai cái đó có được gán người không.

**Bước 3 — BĂM + PHÂN THÂN (SONG SONG):** đây là chỗ chatbot thua. Hermes chẻ 90 phút thành **6 đoạn 15 phút**, rồi "phân thân" gọi **4 bản sao** cùng phiên âm + tóm tắt song song. 90 phút chia 4 → mỗi bản sao chỉ gánh ~22 phút, nằm gọn trong cửa sổ ngữ cảnh, sai sót thấp. Tổng thời gian phiên âm song song thay vì nối đuôi.

**Bước 4 — TRÍCH + SO SÁNH:** mỗi bản sao rút (quyết định, đầu việc, người nói sẽ làm, hạn hẹn), ráp lại thành 12 action items, rồi đối chiếu với task tuần trước trong memory. Chỗ nào trùng → gộp. Chỗ nào tuần trước chưa xong → đánh dấu "tiếp diễn".

**Bước 5 — QUALITY GATE (SOI):** kiểm 3 lỗi riêng cho biên bản họp — (1) có bỏ sót đầu việc nào không (đếm số lần xuất hiện "tôi sẽ"/"chịu trách nhiệm"), (2) mỗi đầu việc có gán đúng người + hạn không, (3) có bịa người làm không tồn tại không. Rớt 1 là bỏ, yêu cầu đọc lại đoạn đó.

**Bước 6 — GIAO:** đẩy bản biên bản 1 trang + 12 action items vào Telegram của Hỉ, copy sang email group luôn.

**Bước 7 — LƯU (MEMORY):** ghi log "họp 27/8: 3 quyết định, 12 task, 2 tiếp diễn" để tuần sau đối chiếu tự động — không bao giờ hỏi "cái đó ai làm" nữa.

**Bước 8 — BÁO CÁO:** nhắn Hỉ "xong biên bản, 4 phút, 12 việc đã gán". Xong, đi ăn tiếp.

Tám bước. Toàn bộ tự động. Chatbot không có bước 1 (đồng hồ), bước 2 (nhớ task cũ), bước 3 (phân thân vượt context) và bước 5 (tự soi) — nó chỉ làm được nếu bạn tự ngồi nghe, tự ghi, tự gán. Mà bạn thì lúc nào cũng... quên.

## Tại sao "họp xong có biên bản ngay" lại đáng tiền — có số thật

Chuyện tiết kiệm này không phải Hỉ tự bịa cho hay. Mấy con số dưới là thật và có nguồn:

**Một — cả ngành đang đổ tiền vào cái này, tức là nỗi đau có thật:** trên HackerNews, **Circleback (YC W24)** là một startup được Y Combinator rót vốn chuyên làm "tooling to make meetings more efficient" — tức là riêng chuyện ghi biên bản họp cho tử tế đã đáng để một lò ươm kỳ lân YC đầu tư. Chưa kể **Screenpipe (YC S26)** — ghi lại cả cách bạn làm việc rồi biến thành agent. Hai vòng YC, hai năm liên tiếp, cùng một hướng: máy làm thay phần hành chính sau họp. Đó là bằng chứng thị trường, không phải lời đồn.

**Hai — tốc độ thực tế của Hỉ:** 90 phút nghe thủ công + 30 phút gõ biên bản = **~2 tiếng** cho mỗi cuộc họp. Giờ Hermes làm trong **4 phút**. Tiết kiệm **~116 phút** cho 1 cuộc họp. Nhân 5 cuộc họp/tuần (team + đối tác + tuyển dụng) = **hơn 9,5 giờ/tuần** — tương đương **gần 1,5 ngày làm việc mỗi tháng** chỉ để... viết biên bản. Giờ Hỉ lấy lại được, và quan trọng hơn: **không rớt task** nữa.

**Ba — chi phí vận hành rẻ đến ngạc nhiên:** Hermes chạy trên cấu hình có sẵn, gọi model theo lượt. Một lượt viết biên bản 90 phút tốn chưa bằng 1 gói mì cốc. Trong khi thuê trợ lý tóm tắt họp thường tính theo giờ, hoặc tốn luôn một người ngồi gõ. Chênh lệch vài chục lần, mà độ sót thấp hơn vì agent không bao giờ "đi vệ sinh giữa cuộc họp rồi lỡ đoạn quan trọng".

## Câu lệnh CEO — giao đúng 1 lần, lấy đủ

Nhiều bạn hỏi Hỉ: "Giao kiểu gì để nó viết biên bản đúng ý?". Đây là câu lệnh Hỉ thực sự dùng tối nay (copy được):

> *"Hermes, khi có file ghi âm mới trong thư mục họp, tự động: (1) phiên âm + băm thành từng đoạn, (2) rút đúng 3 mục — QUYẾT ĐỊNH (đã chốt gì), ĐẦU VIỆC (làm cái gì), NGƯỜI + HẠN (ai, khi nào xong), (3) đối chiếu với task tuần trước trong memory, gộp cái trùng, (4) mỗi đầu việc PHẢI có tên người chịu trách nhiệm, (5) gửi tôi biên bản 1 trang + danh sách action items trước 8h10 tối, copy sang email group."*

Chỉ một blockquote. Không cần ngồi canh. Họp xong có kết quả.

## Kết quả đo lường (lấy luôn bản tối nay)

- **Thời gian:** 90 phút họp → biên bản + 12 action items trong **4 phút 12 giây** (từ 8h00 đến 8h05).
- **Độ phủ:** 12/12 đầu việc được gán đúng người + hạn. **3 quyết định** team chốt được liệt kê riêng, không lẫn vào task.
- **Đối chiếu:** 2 task tuần trước chưa xong tự động đánh dấu "tiếp diễn" — không bị trùng lặp, không bị quên.
- **Phát hiện:** 1 đầu việc ("gửi báo cáo đối tác") tuần trước không ghi người chịu trách nhiệm → tối nay agent bắt gán tên, không để trống.
- **Tiết kiệm:** ~116 phút so với gõ thủ công, chi phí < 1 gói mì cốc.

Nếu hôm đó tôi tự gõ, xác suất rớt ít nhất 2-3 task là cực cao — vì cuối cuộc họp não tôi đã bắt đầu nghĩ chuyện ăn gì.

## FAQ — 3 câu hỏi hay nhất Hỉ nhận được

**1. Chatbot (ChatGPT) có viết được biên bản họp không?**
Có — nhưng bạn phải tự lôi transcript ra, dán từng phần, rồi tự gán người tự gán hạn. Nó không mở được file ghi âm, không nhớ task tuần trước, và hỏi "ai làm?" thì nó bảo "không rõ". Để nó thành thư ký thật, bạn cần vòng lặp + memory + phân thân → đấy là Agent, không phải chatbot.

**2. Hermes có gán sai người hoặc bịa task không?**
Không — nhờ Quality Gate (bước 5). Mọi đầu việc đều map từ lời nói trong ghi âm ("anh A sẽ làm cái này"), đối chiếu được. Nếu model "bịa" một task không ai nói, cổng soi sẽ phát hiện (không có trong transcript) và yêu cầu đọc lại. Agent không tự tin vào thứ nó không trích được nguồn.

**3. Bao lâu, tốn bao nhiêu, có cần ngồi canh không?**
4 phút cho 90 phút họp. Chi phí chưa bằng 1 gói mì cốc. Và **không cần ngồi canh** — bạn hẹn 1 lần, nó tự chạy mỗi khi có file ghi âm mới, kể cả lúc bạn đã tắt máy đi ăn. Như cái "Agents that work while you sleep" trên HackerNews: giao xong, đi nghỉ, họp xong có biên bản.

## CTA — đừng để cuộc họp kết thúc bằng một đống quên

Hỉ không bảo bạn thôi họp. Hỉ bảo: **đừng họp xong rồi tự bơi trong đống "ai làm cái đó nhỉ"**.

Nếu bạn cũng từng họp xong, thứ Sáu tuần sau mới nhận ra task bay màu — thì đã đến lúc thôi làm "người ghi note thủ công", chuyển sang làm "người giao việc".

👉 Muốn thử Hermes viết hộ biên bản 1 cuộc họp của bạn? Chi tiết + link đăng ký đang ở **BÌNH LUẬN** bên dưới. Giá mở bán sớm chỉ **239K** (gốc 499K) tại **speedreading.vn/shermes**. Họp xong, biên bản + action items có ngay trong 4 phút — kể cả lúc bạn đã đi ăn.
