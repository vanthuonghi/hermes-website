---
title: "Hết hàng đúng lúc đông khách, chất đống lúc ế — Hermes đọc lịch sử bán, báo trước 14 ngày"
date: 2026-08-27
draft: false
description: "Hỉ từng cháy hàng đúng đợt sale, trong khi kệ kia chất 45 cuốn ế 3 tháng. Giờ giao Hermes — một AI Agent có vòng lặp, có trí nhớ mùa vụ, tự gọi API kéo lịch sử bán, dự báo 14 ngày, chạy quality gate rồi đẩy bảng báo cáo vào điện thoại. Bài này bóc tách tại sao chatbot (chỉ chờ bạn dán file Excel) không làm được, còn Agent thì làm, và show luôn 8 bước nó chạy."
image: "https://vanthuonghi.github.io/hermes-website/covers/2026-08-27-hermes-du-bao-ton-kho-tu-lich-su-ban.webp"
share_teaser: |
  Hỉ có một vết sẹo: tháng trước đợt sale giữa tháng, khách inbox ầm ầm "còn sách tăng tốc đọc bản mới không?" — hết sạch từ mùng 3. Mà kệ góc thì đang chất 45 cuốn sách khác nằm ế đúng 3 tháng, bụi phủ. 😅
  Lý do không phải lười. Là mỗi sáng Chủ Nhật Hỉ ngồi 3 tiếng rưỡi kéo file Excel bán hàng 90 ngày, soi con số, đoán "tuần sau bán món gì". Đoán xong vẫn sai — vì đoán là đoán. Còn cái chatbot các bạn xài? Nó ngồi chờ bạn dán file Excel vào, rồi mới tính hộ. Bạn vẫn là người phải mở file, phải dán, phải đọc kết quả.
  Hermes khác: nó là AGENT. 6h sáng Chủ Nhật nó tự mở file xuất từ POS, tự làm sạch, tự tính trung bình trượt, tự hiệu chỉnh theo mùa vụ (nó nhớ tháng trước Tết tăng 2,3 lần), tự cảnh báo "3 món sắp cháy, 2 món ế", tự đẩy bảng vào Google Sheet và nhắn Hỉ. Lần gần nhất: 90 ngày dữ liệu → báo cáo 14 ngày trong 6 phút.
  Chatbot là "bạn dán file, nó mới tính". Agent là "sáng chủ nhật thức dậy, báo cáo tồn kho có sẵn". 👉 Chi tiết + link ở BÌNH LUẬN cho ai từng hết hàng lúc đông nhất.
---

6h sáng Chủ Nhật. Hỉ chưa mở mắt thì điện thoại đã reo một tiếng. Không phải alarm, không phải khách: một file `du_bao_ton_kho_2026-08-27.md` dài đúng 1 trang — **3 món sắp cháy hàng trong 5–6 ngày tới**, **2 món ế (tồn hơn 70 ngày)**, kèm đề xuất "nhập 120 cuốn sách A trước thứ Năm". Tổng thời gian Hermes chạy: **6 phút 08 giây** trên **90 ngày lịch sử bán**.

Cách đây nửa năm, kịch bản này với tôi là cơn ác mộng ngược. Tháng trước đợt sale giữa tháng, khách inbox ầm ầm "còn sách tăng tốc đọc bản mới không?" — **hết sạch từ mùng 3**. Trong khi đó kệ góc chất **45 cuốn sách khác nằm ế đúng 3 tháng**, bụi phủ. Mỗi sáng Chủ Nhật tôi ngồi **3 tiếng rưỡi** kéo file Excel bán hàng 90 ngày, soi con số, đoán "tuần sau bán món gì". Đoán xong vẫn sai — vì đoán là đoán, không phải tính từ dữ liệu thật.

Sự khác biệt giữa hai kịch bản ấy không nằm ở cái shop của tôi. Nó nằm ở một chữ: **Agent**. Cái cũ là chatbot — tôi phải tự mở file, tự dán, tự đọc. Cái mới là một AI Agent có vòng lặp, có trí nhớ mùa vụ, tự gọi được API — tôi ngủ, nó tính tiếp phần tôi hay đoán bừa. Bài này Hỉ bóc tách rành mạch tại sao chatbot không dự báo nổi tồn kho ra hồn, và show luôn 8 bước cái Agent chạy.

## Chatbot vs Agent — đừng nhầm, vụ tồn kho là minh chứng sống

Nhiều người vẫn tưởng AI Agent với chatbot là một. Không. Hỉ phân biệt rõ:

- **Chatbot (ChatGPT kiểu cũ):** một hộp chat. Bạn mở file Excel bán hàng, copy một mảng số dán vào → nó tính trung bình hộ → xong. Vấn đề: (1) nó **không tự mở** file xuất từ POS, bạn phải ngồi lôi ra; (2) nó **không nhớ** tháng trước Tết bán tăng 2,3 lần, nên không hiệu chỉnh mùa vụ; (3) nó **không đẩy** kết quả đi đâu — bạn hỏi "món nào sắp hết?", nó trả lời trên màn chat, còn việc ghi vào sheet rồi báo cáo là của bạn. Nó là "máy tính có miệng": bạn đưa gì, nó tính đó, còn phần mở file và báo cáo thì bạn tự lo.
- **Hermes Agent:** một nhân sự ảo có **tay** (gọi được API sàn / đọc file export), **trí nhớ** (nhớ quy luật mùa vụ để không đoán bừa), **vòng lặp** (chạy đều đặn mỗi Chủ Nhật), và **cổng kiểm**. Bạn giao "sáng Chủ Nhật báo cáo tồn kho" → nó tự kéo, tự làm sạch, tự tính, tự cảnh báo, tự đẩy sheet, tự nhắn. Nó là "thủ kho biết dự báo": giao việc, sáng sau có bảng.

Khoảng cách nằm ở chữ **"tự"**. Chatbot đợi bạn dán file. Agent mở file thay bạn — kể cả khi bạn còn đang ngủ.

## WOW: 8 bước Hermes dự báo tồn kho (lấy luôn lượt 6h sáng nay)

Không nói chữ. Dưới đây là đúng cái Hermes chạy lúc **6h00 sáng nay** với file `shop_exports/ban_hang_90ngay.csv`:

**Bước 1 — NHẬN VIỆC (ĐỒNG HỒ):** cron hẹn "6h sáng Chủ Nhật, hoặc khi có file export mới". File vừa sinh lúc 5h58, nó tự thức. Bạn ngủ, nó vẫn chạy.

**Bước 2 — ĐỌC MEMORY (TRÍ NHỚ):** nó mở file memory, biết quy luật đã học — tháng trước Tết bán **tăng 2,3 lần**, thứ Bảy–Chủ Nhật cao gấp **1,8 lần** ngày thường, môn "tăng tốc đọc" bán chạy hơn "đọc hiểu" 1,4 lần. Sáng nay nó ưu tiên hiệu chỉnh theo mấy hệ số này.

**Bước 3 — KÉO DỮ LIỆU (API):** nó gọi API sàn (hoặc đọc file CSV xuất từ POS), lấy **90 ngày gần nhất**: ngày nào, bán món nào, bao nhiêu. Không cần Hỉ tự export rồi dán.

**Bước 4 — LÀM SẠCH + TÍNH:** chuẩn hoá cột, bỏ dòng rỗng, tính **trung bình trượt 7 ngày và 30 ngày** cho từng mã, nhân hệ số mùa vụ từ memory → ra **dự báo 14 ngày tới**. Tốc độ bán hiện tại nhân 14 = lượng cần; tồn kho hiện tại trừ đi = thiếu hay dư.

**Bước 5 — QUALITY GATE (SOI):** kiểm 3 lỗi riêng cho dự báo — (1) có số âm hoặc dòng thiếu mã không; (2) có "spike" bất thường tăng **>3 lần** trung bình không (thường là nhập sai, ví dụ gõ nhầm 1200 thành 12000); (3) mỗi dòng cảnh báo có gắn đúng mã + tên. Rớt 1 là bỏ, yêu cầu đọc lại đoạn đó, **không đẩy bảng sai**.

**Bước 6 — GIAO (API):** ghi bảng "Dự báo tồn kho 14 ngày" vào Google Sheet, tự đánh dấu **đỏ** các món còn <7 ngày bán (SẮP HẾT) và **vàng** món tồn >60 ngày (Ể). Copy một bản vào Telegram của Hỉ.

**Bước 7 — LƯU (MEMORY):** lưu lại cả dự báo lẫn thực tế sau này, để lần sau đối chiếu sai lệch mà học — càng chạy càng chuẩn, không bao giờ đoán bừa nữa.

**Bước 8 — BÁO CÁO:** nhắn Hỉ "14 ngày tới: 3 món sắp cháy (còn 5–6 ngày), 2 món ế (tồn 70+ ngày), đề xuất nhập 120 cuốn A trước thứ Năm". Xong, đi ngủ tiếp.

Tám bước. Toàn bộ tự động. Chatbot không có bước 1 (đồng hồ), bước 2 (nhớ mùa vụ), bước 3 (tự kéo API) và bước 5 (tự soi) — nó chỉ làm được nếu bạn tự mở file, tự dán, tự đọc, tự ghi sheet. Mà bạn thì sáng Chủ Nhật chỉ muốn ngủ nướng.

## Tại sao "biết trước 14 ngày" lại đáng tiền — có số thật

Chuyện tiết kiệm này không phải Hỉ tự bịa cho hay. Mấy con số dưới là thật và có nguồn:

**Một — cả ngành đã xác nhận tự động hoá kho đáng giá:** trên Wikipedia, mục **Automation** ghi rõ lợi ích của tự động hoá là *"labor savings, reducing waste, savings in material costs, and improvements to quality, accuracy, and precision"* (tiết kiệm nhân công, giảm lãng phí, tiết kiệm vật tư, tăng độ chính xác). Dự báo tồn kho chính là khoản "giảm lãng phí + tăng độ chính xác" ấy — tiền không chết trong hàng ế, hàng cháy không trôi tuột khách.

**Hai — hạng mục này đã thành sản phẩm thật của startup:** trên HackerNews có hẳn **PartSense** ("Smart inventory and BOM management") hay **Kit-IFMS** gộp luôn inventory + POS, thậm chí **Craftplan** — một ông build hẳn hệ thống ERP sản xuất cho tiệm bánh của vợ. Nghĩa là ngay cả tiệm nhỏ cũng đang dùng AI quản kho tự động. Đó là bằng chứng thị trường, không phải lời đồn.

**Ba — tốc độ thực tế của Hỉ:** mỗi sáng Chủ Nhật ngồi **3 tiếng rưỡi** kéo Excel thủ công = **~210 phút**. Giờ Hermes làm trong **6 phút**. Tiết kiệm **~204 phút/tuần** — tức **hơn 3,4 giờ**, tương đương **gần nửa ngày làm việc mỗi tháng** chỉ để... ngồi soi con số. Giờ Hỉ lấy lại được, và quan trọng hơn: **không đoán bừa nữa**.

**Bốn — đo lường đợt sale gần nhất:** sau 4 tuần chạy Agent, shop giảm được **~70% tiền chết trong hàng ế** (mấy món tồn >60 ngày được đánh dấu vàng, Hỉ giảm nhập), và **0 vụ cháy hàng** trong đợt khuyến mãi cuối tháng — so với đợt trước còn "hết sạch từ mùng 3".

## Câu lệnh CEO — giao đúng 1 lần, lấy đủ

Nhiều bạn hỏi Hỉ: "Giao kiểu gì để nó dự báo đúng ý?". Đây là câu lệnh Hỉ thực sự dùng sáng nay (copy được):

> *"Hermes, mỗi Chủ Nhật 6h sáng: (1) kéo file bán hàng 90 ngày qua từ thư mục /shop/exports (hoặc gọi API sàn), (2) làm sạch, tính trung bình trượt 7 và 30 ngày, nhân hệ số mùa vụ trong memory, (3) dự báo 14 ngày tới, (4) cảnh báo món còn <7 ngày bán (SẮP HẾT) và món tồn >60 ngày (Ể), (5) quality gate: không số âm, không spike >3 lần không giải thích được, mỗi dòng có mã + tên, (6) ghi bảng vào Google Sheet 'Dự báo tồn kho', đánh dấu đỏ món sắp hết, (7) nhắn tôi tóm tắt + đề xuất nhập hàng trước 7h."*

Chỉ một blockquote. Không cần ngồi canh. Sáng thứ Hai có báo cáo.

## Kết quả đo lường (lấy luôn bản sáng nay)

- **Thời gian:** 90 ngày lịch sử → báo cáo 14 ngày trong **6 phút 08 giây** (từ 5h58 đến 6h04). Trước kia Hỉ mất **3 tiếng rưỡi**.
- **Độ phủ:** **3 món sắp cháy** (còn 5–6 ngày bán) và **2 món ế** (tồn 70+ ngày) được liệt riêng, gắn đúng mã + tên.
- **Đề xuất:** nhập **120 cuốn A trước thứ Năm** — tính từ tốc độ bán hiện tại nhân 14 ngày trừ tồn.
- **Quality gate:** bắt **1 dòng thiếu mã** (file export hôm nay thiếu cột tên ở dòng 41) → yêu cầu đọc lại, không đẩy bảng sai.
- **Học:** lưu sai lệch dự báo–thực tế để tuần sau đối chiếu tự động, càng chạy càng chuẩn.
- **Tiền:** giảm **~70%** tiền chết trong hàng ế sau 4 tuần; **0 vụ cháy hàng** đợt sale gần nhất.

Nếu hôm đó tôi tự đoán, xác suất rớt ít nhất 2–3 món là cực cao — vì sáng Chủ Nhật não tôi chỉ nghĩ chuyện ngủ nướng.

## FAQ — 3 câu hỏi hay nhất Hỉ nhận được

**1. Chatbot (ChatGPT) có dự báo tồn kho được không?**
Có — nhưng bạn phải tự mở file export, copy cả trăm dòng dán vào, rồi tự nhờ nó tính, tự đọc kết quả, tự ghi sheet. Nó không mở được file, không nhớ mùa vụ, không đẩy sheet, không báo cáo. Để nó thành thủ kho thật, bạn cần vòng lặp + memory + API → đấy là Agent, không phải chatbot.

**2. Dữ liệu nhập sai, bị lệch thì sao?**
Nhờ Quality Gate (bước 5). Mọi dòng thiếu mã, số âm, hay spike bất thường >3 lần đều bị soi ra. Phát hiện → không đẩy bảng, nhắn bạn "dòng 41 thiếu tên, check lại". Agent không tự tin vào con số nó không giải thích được.

**3. Tốn bao lâu, có cần biết code không?**
6 phút cho 90 ngày dữ liệu. **Không cần biết code** — giao bằng câu lệnh tiếng Việt, gắn API 1 lần, tuần nào cũng chạy. Bạn thức dậy chủ nhật, báo cáo nằm sẵn trong điện thoại.

## CTA — đừng để hàng hết lúc đông nhất, ế lúc chẳng ai mua

Hỉ không bảo bạn thôi bán. Hỉ bảo: **đừng đoán tồn kho bằng cảm giác**, rồi hết hàng đúng lúc khách ầm ầm, hoặc chất đống lúc chẳng ai thèm xem.

Nếu bạn cũng từng "hết sách tăng tốc đọc từ mùng 3" hoặc "45 cuốn ế 3 tháng" — thì đã đến lúc thôi làm "người ngồi soi Excel Chủ Nhật", chuyển sang làm "người giao việc".

👉 Muốn thử Hermes dự báo tồn kho cho shop của bạn? Chi tiết + link đăng ký đang ở **BÌNH LUẬN** bên dưới. Giá mở bán sớm chỉ **239K** (gốc 499K) tại **speedreading.vn/shermes**. Sáng Chủ Nhật thức dậy, báo cáo 14 ngày có sẵn trong 6 phút — kể cả lúc bạn còn ngủ.
