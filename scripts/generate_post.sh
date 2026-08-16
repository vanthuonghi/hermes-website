#!/usr/bin/env bash
#
# generate_post.sh — Tạo 1 bài blog Hermes mới ngày hôm nay.
# Dùng bởi cron hoặc chạy tay. Sinh file .mdx rỗng + front matter,
# sau đó bạn (hoặc LLM) điền nội dung. Kịch bản này chỉ tạo khung
# để tránh trùng ngày; nội dung do Tổng Đạo Diễn viết.
#
# Usage: ./generate_post.sh "Tiêu đề bài viết"
#   Nếu không có arg, dùng tiêu đề mẫu theo ngày.

set -euo pipefail

SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
POSTS_DIR="$SITE_DIR/content/posts"
TODAY=$(date +%Y-%m-%d)
DATE_HUMAN=$(date +"%d/%m/%Y")

if [ $# -ge 1 ]; then
  TITLE="$1"
else
  TITLE="Ứng dụng Hermes ngày $(date +%d/%m): mẹo nhỏ cho người bận rộn"
fi

# Slug: lowercase, thay dấu/cách bởi dấu gạch, bỏ ký tự lạ
SLUG=$(echo "$TITLE" | iconv -t ascii//TRANSLIT | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
FILENAME="$POSTS_DIR/${TODAY}-${SLUG:0:40}.mdx"

if [ -f "$FILENAME" ]; then
  echo "ĐÃ TỒN TẠI: $FILENAME (bỏ qua)"
  exit 0
fi

mkdir -p "$POSTS_DIR"
cat > "$FILENAME" <<EOF
---
title: "$TITLE"
date: $TODAY
draft: true
---

(Bài này đang được Tổng Đạo Diễn viết — nội dung sẽ điền bởi agent.)

## Mở đầu

## Cách làm với Hermes

## Kết luận

👉 Học khoá Nhân Sự Toàn Năng Hermes: https://speedreading.vn/shermes
EOF

echo "ĐÃ TẠO: $FILENAME"
echo "Tiêu đề: $TITLE"
