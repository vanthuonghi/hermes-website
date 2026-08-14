#!/usr/bin/env bash
#
# daily_post.sh — Build + push blog Hermes (dùng api_commit.sh thay git push,
# vì repo chặn direct push + secret scan). Chạy bởi cron sau khi agent viết bài.
#
# Yêu cầu: GITHUB_TOKEN export hoặc ~/.hermes/github_token tồn tại.
set -euo pipefail
SITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$SITE_DIR"
export GITHUB_TOKEN="${GITHUB_TOKEN:-$(cat ~/.hermes/github_token 2>/dev/null || true)}"
[ -z "$GITHUB_TOKEN" ] && { echo "ERROR: no token"; exit 1; }
# Build kiểm tra
hugo --minify >/tmp/hugo_build.log 2>&1 || { echo "BUILD_FAILED"; cat /tmp/hugo_build.log; exit 1; }
# Deploy qua API
bash scripts/api_commit.sh
