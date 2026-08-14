#!/usr/bin/env bash
# gen_social.sh <slug>  — sinh draft post FB/Zalo + hook YouTube short từ 1 bài blog
# In ra file markdown sẵn sàng copy đăng. (Chưa auto-post lên mạng xã hội — user tự đăng hoặc nối API sau.)
set -e
SLUG="$1"
POST="content/posts/$SLUG.md"
[ -f "$POST" ] || { echo "THIEU $POST"; exit 1; }
cd /home/ubuntu/hermes-website
URL="https://vanthuonghi.github.io/hermes-website/posts/$SLUG/"
TITLE=$(grep -m1 '^title:' "$POST" | sed 's/title: *"//;s/"$//')
OUT="scripts/social_$SLUG.md"
cat > "$OUT" <<EOF
# 📢 SOCIAL DRAFT — $TITLE

🔗 Link bài: $URL

---

## 📘 FACEBOOK / ZALO POST (copy đăng)
$H = $(python3 -c "import textwrap;print('')")
**$TITLE**

Bạn có biết: Hermes không phải chatbot viết chữ — nó là Agent tự động hoá cả quy trình, chạy hoài kể cả khi bạn ngủ?

Tôi vừa viết chi tiết thực tế ở đây 👇
$URL

💡 Ai muốn có nhân sự ảo riêng mà không cần biết code — comment "Hermes" mình gửi khoá học 199K (hoàn tiền 7 ngày).

#Hermes #AIAgent #TuDongHoa #Nhansuao

---

## 🎬 YOUTUBE SHORT HOOK (15s mở đầu)
"Nhiều người tưởng AI chỉ viết được chữ. Sai. Tôi giao Hermes 1 việc, sáng nào cũng có sẵn, tôi ngủ nó vẫn chạy. Chi tiết ở link dưới 👇 $URL"

## 🎬 TITLE GỢI Ý
- Hermes không phải ChatGPT — và đây là lý do
- Giao 1 lần, AI tự làm cả tuần (thật hay lừa?)
- Nhân sự ảo 199K: có đáng hay không?

---

⚠️ Hình đi kèm: dùng cover webp của bài (static/covers/$SLUG.webp) — KHÔNG để chữ lên ảnh, chữ thêm ở Caption/Canva.
EOF
echo "WROTE $OUT"
echo "---- PREVIEW ----"
cat "$OUT"