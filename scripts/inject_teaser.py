#!/usr/bin/env python3
"""Inject per-post Facebook share teaser into each post's front-matter."""
import os, io

BASE = os.path.expanduser("~/hermes-website/content/posts")

TEASERS = {
"2026-08-14-hermes-tom-tat-sach.md": """Mới thử xong một cái mà Hỉ phải nói là... ồ hay thật. 🤯
Mình giao nó đọc nguyên cuốn sách 300 trang, sáng nào nó cũng tự nhắc ý chính — chứ không phải mấy app tóm tắt chết nhách.
Thực ra đây là 'AI Agent' (nhân sự ảo): khác hẳn ChatGPT. ChatGPT trả lời xong là thôi, còn Agent là 'cánh tay' tự làm việc: giao 1 lần, nó tự chạy, tự nhắc, tự báo cáo luôn.
👉 Hermes đang làm cái này rất tốt — chi tiết + link mình để ở BÌNH LUẬN nhé, xem rồi thử luôn.""",

"hermes-bao-cao.md": """Hỉ vừa được một thứ xịn: sáng thứ Hai mở mắt ra đã có báo cáo tuần nằm sẵn. 😴💼
Mình giao 1 lần cuối tuần, nó tự đọc Excel, tổng hợp, vẽ biểu đồ, lên lịch gửi — Hỉ ngủ nó vẫn chạy.
Đây gọi là AI Agent (nhân sự ảo) — không phải chatbot. Chatbot chỉ 'nói', Agent là 'làm': giao việc, nó tự vận hành rồi báo cáo cho bạn.
👉 Hermes đang làm cái này rất mượt — chi tiết + link ở BÌNH LUẬN, ai rảnh giờ báo cáo thủ công nữa.""",

"hermes-co-tri-nho.md": """Phát hiện một cái khiến Hỉ thích quá: nó nhớ mình hơn mình nhớ nó luôn. 🧠
Chatbot thì quên sạch sau mỗi lần chat. Còn Hermes (AI Agent) nhớ giọng văn, thói quen, quyết định cũ — giao 1 lần, lần sau tự hiểu, không cần nhắc lại.
AI Agent = nhân sự ảo có trí nhớ, khác hẳn mấy con chatbot hay 'ngáo' quên việc.
👉 Hermes đang làm cái này rất tốt — chi tiết + link mình để ở BÌNH LUẬN nhé.""",

"hermes-ket-noi-api.md": """Cái này Hỉ phải khoe: Hermes không chỉ 'nói' mà nó 'làm' thật. 🔌
Nó kết nối API — gom mọi công cụ, key, dữ liệu vào 1 mối rồi tự thao tác hệ thống thật: gửi mail, cập nhật CRM, đăng bài.
Đây là bản chất AI Agent: chatbot chỉ nằm trong khung chat, còn Agent là 'cánh tay' chạm được vào hạ tầng thật của bạn.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN nhé, coi nó 'đụng' được gì.""",

"hermes-khac-chatgpt.md": """Nhiều người vẫn nhầm: tưởng ChatGPT với AI Agent là một. Hỉ giải thích nôm na cho dễ hiểu nhé. 💡
ChatGPT = người trả lời câu hỏi. Hermes (AI Agent) = người đi làm và báo cáo. Một cái 'nói', một cái 'làm'.
Ví dụ thực tế mình để ở dưới — khác biệt rõ ràng luôn, không thể nhầm được.
👉 Chi tiết + link ở BÌNH LUẬN. Hermes đang làm cái này rất tốt, đọc xong tự thấy.""",

"hermes-khong-can-code.md": """Hỉ không biết xíu code nào, vậy mà giờ có hẳn 'đội nhân sự ảo' chạy việc thay. 😎
Bạn giao bằng tiếng Việt thôi, Agent tự vận hành, nhớ, báo cáo — không dòng code nào.
AI Agent (nhân sự ảo) khác chatbot ở chỗ: chatbot cần bạn 'hỏi', Agent tự 'làm' luôn quy trình.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, người không chuyên như Hỉ làm được thì bạn cũng được.""",

"hermes-kich-ban-tiktok-tu-y-tuong.md": """Hỉ giao nó làm 'đạo diễn' kênh video luôn, xong cái này tiện quá. 🎬
Sáng nào dậy là có kịch bản sẵn — giao 1 lần, nó tự tìm chủ đề, viết, check, lên lịch, chạy hoài kể cả lúc ngủ.
Đây là AI Agent tự động hoá: không phải chatbot viết chữ rồi thôi, mà là 'nhân viên' tự vận hành cả quy trình.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai làm content xem phát thèm.""",

"hermes-lam-lien-tuc.md": """Giao 1 mẻ 20 việc lúc 10h tối, sáng 7h dậy có đống kết quả. Hỉ thực sự sướng cái này. 😴→🌅
Nó chạy xuyên đêm, nhiều luồng, không nghỉ, không than. Chatbot thì 'nói' xong là ngưng.
AI Agent = nhân sự ảo thay bạn làm việc thật, không cần ngủ. Khác biệt căn bản với mấy con AI chỉ biết chat.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN nhé.""",

"hermes-len-ke-hoach.md": """Tháng 9 này Hỉ lười hẳn, vì đã giao Hermes lo kế hoạch rồi. 📅
Nó tự lập plan, chia việc theo tuần, lên lịch nhắc, báo cáo tiến độ — Hỉ chỉ ngồi duyệt.
Đây là AI Agent lập kế hoạch: khác hẳn chatbot. Chatbot 'viết giúp bạn', Agent 'tự chạy kế hoạch thay bạn'.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai hay quên việc thử đi.""",

"hermes-phan-than.md": """Cái 'phân thân' này Hỉ khoái nhất: giao 4 việc 1 lúc, 1 tiếng xong. 🌀
Chatbot làm 1 việc. Hermes chạy song song như có 4 người — bạn không cần thuê thêm ai cả.
AI Agent (nhân sự ảo) = bản sao bạn, làm nhiều việc cùng lúc, không lương không nghỉ.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai đang 'bơi' trong việc xem thử.""",

"hermes-quality-gate.md": """Hỉ để ý một điểm làm nên 'hạng người' của Hermes: nó tự soi lỗi trước khi giao bạn. 🛡️
ChatGPT trả lời xong bạn tự đọc tự sửa. Hermes thì tự check, tự vứt bản dở, đưa bạn bản sạch.
Cái gọi là 'quality gate' — linh hồn của một AI Agent thật sự: tự vận hành chứ không chỉ 'nói'.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai hay nhận 'rác' từ AI xem phát hiểu.""",

"hermes-quan-ly-5-nhan-su-ao.md": """Hỉ giờ 'sếp' của 5 nhân sự ảo luôn, mà chả tốn đồng lương nào. 🤯💼
Giao 5 đầu việc, Hermes chạy song song, báo cáo từng cái. Chatbot thì lẹt đẹt 1 việc.
AI Agent = đội ngũ nhân sự ảo thay bạn thuê người. Đây là khác biệt căn bản với mấy con chatbot chỉ biết 'nói'.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN nhé.""",

"hermes-tiet-kiem.md": """Sau 1 tháng giao việc cho Hermes, Hỉ rảnh thêm 25 tiếng/tuần. Con số thật nha. ⏰
30 bài tự đăng, 400 mail tự dọn — chứ không phải 'viết được bao nhiêu chữ'.
Đây là AI Agent tự vận hành: khác hẳn AI/Chatbot chỉ sinh chữ rồi thôi. Nó làm thật, báo cáo thật.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai tò mò bộ số thực tế xem thử.""",

"hermes-tra-email.md": """Sáng nào mở mắt ra inbox cũng sạch 50 mail — Hỉ chỉ việc duyệt. 📧✨
Giao 1 lần, nó tự phân loại, soạn, lên lịch gửi, báo cáo — chạy hoài mỗi sáng đúng giờ kể cả lúc ngủ.
AI Agent xử lý inbox: khác hẳn chatbot chỉ 'giúp soạn'. Agent là 'nhân viên' tự dọn dẹp luôn.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai ngập email thử đi sướng lắm.""",

"hermes-viet-caption.md": """Mỗi clip Hỉ giờ có tận 10 cái caption, mà lúc ngủ nó vẫn viết. 😴✍️
Giao 1 lần, nó tự viết 10 biến thể, lên lịch, test A/B, báo cáo — chạy hoài.
AI Agent lo caption: không phải chatbot viết 1 câu rồi thôi, mà là 'đội content' tự vận hành.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, ai làm video xem phát thèm.""",

"hermes-viet-content.md": """Sáng nào dậy cũng có 7 bài đăng sẵn — Hỉ ngủ nó vẫn viết. 📝🌙
Giao 1 lần, nó tự tìm chủ đề, nghiên cứu, viết, check, lên lịch, báo cáo — chạy hoài mỗi tuần.
Đây là AI Agent tự động hoá content: khác hẳn ChatGPT chỉ 'giúp viết'. Agent là 'tòa soạn' tự chạy.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, làm MMO xem phát mê.""",

"hermes-vong-lap-8-buoc.md": """Hỉ thấy cái hay nhất của Hermes là nó không 'trả lời 1 câu' rồi ngưng. 🔁
Giao 1 việc, nó tự chạy vòng lặp 8 bước: tìm → nghiên cứu → viết → check → lưu → lịch → báo cáo, rồi đưa bạn kết quả.
Đó là AI Agent thật: tự vận hành cả quy trình, không phải chatbot sinh chữ rập khuôn.
👉 Hermes đang làm cái này rất tốt — chi tiết + link ở BÌNH LUẬN, đọc xong tự thấy khác biệt.""",
}

def inject(path, teaser):
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    # find front-matter delimiters
    if not text.startswith("---"):
        print("SKIP (no FM):", path); return
    # first '\n---' marks the closing delimiter of front matter
    idx2 = text.index("\n---", 3) + 1  # start of line after closing '---'
    head = text[:idx2]   # includes closing '---' (line ends with \n)
    body = text[idx2:]
    block = "share_teaser: |\n"
    for line in teaser.strip("\n").split("\n"):
        block += "  " + line + "\n"
    new_head = head.rstrip("\n") + "\n" + block.rstrip("\n") + "\n"
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(new_head + body)
    print("OK:", os.path.basename(path))

for fn, te in TEASERS.items():
    p = os.path.join(BASE, fn)
    if os.path.exists(p):
        inject(p, te)
    else:
        print("MISSING:", fn)
print("DONE")
