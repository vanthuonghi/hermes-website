#!/usr/bin/env python3
"""
pick_cover.py — Chọn cover tĩnh có sẵn (không gen mới, 0đ).
Luân phiên theo thứ tự file để mỗi bài dùng 1 ảnh khác nhau.
Usage: python3 pick_cover.py
In ra đường dẫn URL tương đối (vd: /covers/hermes-bao-cao.webp)
"""
import os, glob, json
COVER_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "covers")
files = sorted(glob.glob(os.path.join(COVER_DIR, "*.webp")))
if not files:
    print("")
    sys.exit(0)
# đọc chỉ số luân phiên từ file state
state = os.path.join(os.path.dirname(__file__), ".cover_idx")
idx = 0
try:
    idx = int(open(state).read().strip() or "0")
except Exception:
    idx = 0
idx = idx % len(files)
chosen = files[idx]
# ghi chỉ số tiếp theo
try:
    open(state, "w").write(str((idx + 1) % len(files)))
except Exception:
    pass
name = os.path.basename(chosen)
print(f"/covers/{name}")
