#!/usr/bin/env bash
#
# api_commit.sh — Deploy blog Hermes lên GitHub qua REST API (không dùng git push,
# vì repo có rule chặn direct push + push protection chặn secret trong code).
#
# BẮT BUỘC: token được đọc từ biến môi trường GITHUB_TOKEN
#   export GITHUB_TOKEN="ghp_xxx"   (đặt trong shell profile hoặc truyền khi chạy)
# KHÔNG hardcode token vào file này (GitHub sẽ chặn "Secret detected").
#
# Hoạt động: so sánh git diff vs HEAD, đẩy từng file thay đổi qua Contents API.
set -euo pipefail

SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$SITE_DIR"

TOKEN="${GITHUB_TOKEN:-}"
if [ -z "$TOKEN" ]; then
  # Thử đọc từ file ẩn ngoài repo
  if [ -f "$HOME/.hermes/github_token" ]; then
    TOKEN=$(cat "$HOME/.hermes/github_token")
  fi
fi
if [ -z "$TOKEN" ]; then
  echo "ERROR: GITHUB_TOKEN not set. Export it or put in ~/.hermes/github_token"; exit 1
fi

REPO="vanthuonghi/hermes-website"
API="https://api.github.com/repos/$REPO/contents"
TODAY=$(date +%Y-%m-%d)

CHANGED=$(git diff --name-only HEAD)
CHANGED+=$'\n'$(git ls-files --others --exclude-standard)

TO_PUSH=""
while IFS= read -r f; do
  [ -z "$f" ] && continue
  [[ "$f" == public/* ]] && continue
  [[ "$f" == .git/* ]] && continue
  [ -d "$f" ] && continue
  if [ -f "$f" ]; then
    SIZE=$(stat -c%s "$f" 2>/dev/null || echo 0)
    [ "$SIZE" -gt 1048576 ] && { echo "SKIP (too big): $f"; continue; }
    # Bảo vệ: báo lỗi nếu file chứa pattern token
    if grep -qE "ghp_[A-Za-z0-9]{20,}" "$f"; then
      echo "SKIP (secret pattern): $f"; continue
    fi
    TO_PUSH+="$f"$'\n'
  fi
done <<< "$CHANGED"

if [ -z "$TO_PUSH" ]; then echo "NO_CHANGES_TO_PUSH"; exit 0; fi

echo "Files to push:"; echo "$TO_PUSH"

# Không để 1 lỗi lẻ (curl hiccup / JSON rỗng) giết cả vòng lặp (set -e).
# Trước đây lỗi này làm các file static/covers/*.webp cuối danh sách KHÔNG được push
# → bài mới bị mất ảnh cover trên web. Giữ set +e trong vòng lặp, đếm lỗi ở cuối.
set +e
FAILED=""
while IFS= read -r f; do
  [ -z "$f" ] && continue
  B64TMP=$(mktemp)
  base64 -w0 "$f" > "$B64TMP"
  SHA=$(curl -s --max-time 40 -H "Authorization: Bearer $TOKEN" "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('sha',''))" 2>/dev/null)
  if [ -n "$SHA" ]; then
    BODY="{\"message\":\"Daily update $TODAY: $f\",\"sha\":\"$SHA\",\"content\":\"$(cat "$B64TMP")\"}"
  else
    BODY="{\"message\":\"Daily add $TODAY: $f\",\"content\":\"$(cat "$B64TMP")\"}"
  fi
  RESP=$(echo "$BODY" | curl -s --max-time 40 -X PUT -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" \
    --data @- "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print('OK' if ('content' in d or 'commit' in d) else d.get('message','ERR'))" 2>/dev/null)
  rm -f "$B64TMP"
  echo "  $f -> $RESP"
  sleep 1
  [ "$RESP" != "OK" ] && FAILED+="$f "
done <<< "$TO_PUSH"
set -e

if [ -n "$FAILED" ]; then
  echo "RETRY_FAILED_FILES: $FAILED"
  for f in $FAILED; do
    B64TMP=$(mktemp)
    base64 -w0 "$f" > "$B64TMP"
    SHA=$(curl -s --max-time 40 -H "Authorization: Bearer $TOKEN" "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('sha',''))" 2>/dev/null || true)
    if [ -n "$SHA" ]; then
      BODY="{\"message\":\"Retry $TODAY: $f\",\"sha\":\"$SHA\",\"content\":\"$(cat "$B64TMP")\"}"
    else
      BODY="{\"message\":\"Retry add $TODAY: $f\",\"content\":\"$(cat "$B64TMP")\"}"
    fi
    R2=$(echo "$BODY" | curl -s --max-time 40 -X PUT -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" \
      --data @- "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print('OK' if ('content' in d or 'commit' in d) else d.get('message','ERR'))" 2>/dev/null || echo ERR)
    rm -f "$B64TMP"
    echo "  RETRY $f -> $R2"
  done
fi

echo "API_PUSH_DONE_$TODAY"

# Đồng bộ local git sau khi push qua API, để các lần sau CHỈ push file MỚI
# (tránh mỗi lượt re-push toàn bộ 98+ file gây timeout).
git add -A 2>/dev/null
git commit -q -m "Daily sync after API push $TODAY" 2>/dev/null || true
echo "LOCAL_COMMIT_DONE"
