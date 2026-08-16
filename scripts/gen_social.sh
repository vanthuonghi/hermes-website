#!/usr/bin/env bash
# gen_social.sh <slug>  — sinh draft post FB/Zalo + hook YouTube short từ 1 bài blog
# Ưu tiên dùng share_teaser trong front-matter (giọng seeding của Hỉ). Link để ở BÌNH LUẬN (FB chặn link trần).
set -e
SLUG="$1"
cd /home/ubuntu/hermes-website
POST="content/posts/$SLUG.md"
[ -f "$POST" ] || { echo "THIEU $POST"; exit 1; }
URL="https://vanthuonghi.github.io/hermes-website/posts/$SLUG/"
TITLE=$(grep -m1 '^title:' "$POST" | sed 's/title: *"//;s/"$//')
OUT="scripts/social_$SLUG.md"

# Lấy share_teaser (block scalar |) từ front-matter; fallback nếu bài không có
TEASER=$(python3 - "$POST" <<'PY'
import sys, re
src = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"^share_teaser:\s*\|\s*\n((?:[ \t]+.*\n|\n)+)", src, re.M)
if m:
    lines = [re.sub(r"^\s{2}", "", l) for l in m.group(1).rstrip().split("\n")]
    print("\n".join(lines).strip())
PY
)
if [ -z "$TEASER" ]; then
  TEASER="Hỉ vừa được thứ xịn: một AI Agent tự đi làm việc, không phải chatbot chờ hỏi.
Giao một lần, nó tự làm, tự kiểm tra, tự báo cáo — mình ngủ nó vẫn chạy.
Chatbot = chờ bạn hỏi mới nói. AI Agent = tự đi làm rồi báo cáo lại.
👉 Hermes đang làm đúng cái này — chi tiết + link ở BÌNH LUẬN nhé."
fi

cat > "$OUT" <<EOF
# 📢 SOCIAL DRAFT — $TITLE

🔗 Link bài (dán ở COMMENT ĐẦU TIÊN, không để trong post): $URL

---

## 📘 FACEBOOK / ZALO — POST CHÍNH (copy y nguyên, KHÔNG kèm link)

$TEASER

#Hermes #AIAgent #TuDongHoa #NhanSuAo #KinhDoanhOnline

---

## 💬 COMMENT ĐẦU TIÊN (tự comment ngay sau khi đăng)

Bài chi tiết mình viết ở đây nhé 👇
$URL

Ai muốn tự dựng "nhân sự ảo" kiểu này mà không cần biết code: khoá Nhân Sự Toàn Năng Hermes — 37 bài, early-bird 199K (sau 499K), hoàn tiền 7 ngày → https://speedreading.vn/pshermes

---

## 💬 COMMENT TRẢ LỜI (khi có người hỏi "khác gì ChatGPT?")

Khác chỗ này: ChatGPT trả lời rồi nghỉ — bạn hỏi mới nói. Agent thì nhận việc: nó tự đọc dữ liệu của bạn, tự làm, tự kiểm tra lại, tự lưu file, tự lên lịch chạy lại, rồi báo cáo. Giao một lần dùng hoài, mình đi ngủ nó vẫn làm.

---

## 🎬 YOUTUBE SHORT — HOOK 15 GIÂY

"Nhiều người tưởng AI chỉ biết viết chữ. Sai rồi. Cái này nó TỰ ĐI LÀM: tự đọc dữ liệu của tôi, tự làm, tự kiểm tra, sáng ra tôi có báo cáo sẵn — mà đêm qua tôi ngủ. Xem chi tiết ở link dưới 👇"

## 🎬 TITLE GỢI Ý
- Tôi ngủ, AI vẫn làm việc — đây là cách
- Chatbot vs AI Agent: khác nhau đúng một chỗ này
- Giao 1 lần, AI tự chạy mỗi ngày (không cần biết code)

---

⚠️ Hình đi kèm: dùng cover của bài (static/covers/$SLUG.webp) — ảnh KHÔNG chữ, chữ overlay thêm ở Canva.
EOF
echo "WROTE $OUT"
echo "---- PREVIEW ----"
cat "$OUT"
