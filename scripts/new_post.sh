#!/usr/bin/env bash
# new_post.sh <slug> <image_url_or_path>
# Build + deploy 1 bài blog Hermes qua API (repo chặn git push). In ra URL live.
set -e
SLUG="$1"
IMG="$2"
REPO=/home/ubuntu/hermes-website
cd "$REPO"
TOKEN="$(cat ~/.hermes/github_token)"
API="https://api.github.com/repos/vanthuonghi/hermes-website/contents"

POST="content/posts/$SLUG.md"
[ -f "$POST" ] || { echo "THIEU FILE $POST"; exit 1; }

# Download + convert cover webp (no-text image)
COVER="static/covers/$SLUG.webp"
if [[ "$IMG" == http* ]]; then curl -sS -m 40 -o /tmp/$SLUG.png "$IMG" 2>/dev/null || true; else [ "$(readlink -f "$IMG")" = "/tmp/$SLUG.png" ] || cp "$IMG" /tmp/$SLUG.png 2>/dev/null || true; fi
if python3 -c "from PIL import Image; im=Image.open('/tmp/$SLUG.png').convert('RGB'); im=im.resize((1200,630)); im.save('$COVER',format='WEBP',quality=72,method=4)" 2>/dev/null; then
  echo "cover ok"
else
  echo "cover fallback -> og"
  cp static/og-image.webp "$COVER" 2>/dev/null
  sed -i "s#covers/$SLUG.webp#og-image.webp#" "$POST" 2>/dev/null || true
fi

# Build
rm -rf public && hugo --minify >/dev/null 2>&1

# Push via API
push_file () {
  f="$1"; [ -f "$f" ] || return
  B64=$(base64 -w0 "$f")
  SHA=$(curl -s -H "Authorization: Bearer $TOKEN" "$API/$f" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('sha',''))" 2>/dev/null)
  if [ -n "$SHA" ]; then BODY="{\"message\":\"post $SLUG\",\"sha\":\"$SHA\",\"content\":\"$B64\"}"; else BODY="{\"message\":\"post $SLUG\",\"content\":\"$B64\"}"; fi
  curl -s -X PUT -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" -d "$BODY" "$API/$f" >/dev/null 2>&1
}
push_file "$POST"
push_file "$COVER"

# Wait Actions build
for i in $(seq 1 12); do
  sleep 15
  ST=$(curl -s -H "Authorization: Bearer $TOKEN" "https://api.github.com/repos/vanthuonghi/hermes-website/actions/runs?per_page=1" 2>/dev/null | python3 -c "import sys,json;d=json.load(sys.stdin);r=d['workflow_runs'][0];print(r['status'],r['conclusion'])" 2>/dev/null)
  if echo "$ST" | grep -q "completed success"; then break; fi
done

echo "https://vanthuonghi.github.io/hermes-website/posts/$SLUG/"
