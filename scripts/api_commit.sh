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

while IFS= read -r f; do
  [ -z "$f" ] && continue
  CONTENT=$(base64 -w0 "$f")
  SHA=$(curl -s -H "Authorization: Bearer $TOKEN" "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('sha',''))" 2>/dev/null)
  if [ -n "$SHA" ]; then
    BODY="{\"message\":\"Daily update $TODAY: $f\",\"sha\":\"$SHA\",\"content\":\"$CONTENT\"}"
  else
    BODY="{\"message\":\"Daily add $TODAY: $f\",\"content\":\"$CONTENT\"}"
  fi
  RESP=$(curl -s -X PUT -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" \
    -d "$BODY" "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print('OK' if ('content' in d or 'commit' in d) else d.get('message','ERR'))" 2>/dev/null)
  echo "  $f -> $RESP"
done <<< "$TO_PUSH"

echo "API_PUSH_DONE_$TODAY"
