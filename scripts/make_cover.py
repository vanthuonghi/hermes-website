#!/usr/bin/env python3
"""
make_cover.py — Offline fallback cover (0đ) khi OpenRouter image API bị 402.
Sinh nền gradient ấm + overlay tiêu đề/badge/footer bằng PIL (layout y hệt or_image.py).

Usage:
  python3 make_cover.py --title "..." --topic "api" --badge "KẾT NỐI MỘI API" \
      --out static/covers/2026-08-30-hermes-ket-noi-api-gom-moi-key.webp
"""
import sys, os, argparse, hashlib, io
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "..", "static", "covers")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
W, H = 1200, 630

# Gradient themes per topic: (top_color, bottom_color, glow_color)
THEMES = {
    "default": ((40, 30, 24), (16, 12, 10), (240, 150, 70)),
    "phan-than": ((44, 30, 40), (16, 11, 16), (240, 110, 150)),
    "memory": ((30, 36, 46), (12, 16, 22), (110, 170, 240)),
    "api": ((22, 34, 46), (10, 16, 24), (90, 190, 230)),
    "tiet-kiem": ((40, 30, 22), (15, 11, 8), (240, 160, 70)),
    "bao-cao": ((30, 40, 34), (12, 18, 15), (120, 210, 160)),
    "email": ((34, 30, 42), (14, 12, 18), (200, 150, 240)),
    "ke-hoach": ((36, 34, 26), (15, 14, 10), (230, 190, 90)),
    "vong-lap": ((34, 28, 40), (14, 11, 17), (220, 130, 220)),
    "quality": ((28, 38, 34), (11, 17, 15), (120, 220, 170)),
    "content": ((40, 30, 26), (16, 11, 9), (245, 140, 80)),
    "kit": ((38, 32, 28), (15, 13, 11), (240, 170, 90)),
    "khac-chatgpt": ((30, 32, 44), (12, 13, 20), (120, 180, 240)),
}

def vgrad(c_top, c_bot):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        r = int(c_top[0] + (c_bot[0] - c_top[0]) * t)
        g = int(c_top[1] + (c_bot[1] - c_top[1]) * t)
        b = int(c_top[2] + (c_bot[2] - c_top[2]) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    return img

def bg(topic):
    c_top, c_bot, glow = THEMES.get(topic, THEMES["default"])
    img = vgrad(c_top, c_bot)
    d = ImageDraw.Draw(img, "RGBA")
    # soft radial glow top-right
    cx, cy = int(W * 0.74), int(H * 0.34)
    for i in range(26, 0, -1):
        a = int(7 * (i / 26.0) ** 1.6)
        rad = int(i * 26)
        d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad],
                  fill=(glow[0], glow[1], glow[2], a))
    # a few bokeh dots
    import random
    random.seed(7)
    for _ in range(7):
        x = random.randint(80, W - 80)
        y = random.randint(60, H - 260)
        r = random.randint(6, 22)
        a = random.randint(10, 30)
        d.ellipse([x - r, y - r, x + r, y + r],
                  fill=(glow[0], glow[1], glow[2], a))
    return img.convert("RGB")

def get_font(bold, size):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(f"{FONT_DIR}/{name}", size)
    except Exception:
        return ImageFont.load_default()

def wrap(text, font, max_w, draw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def overlay(img, title, badge):
    d = ImageDraw.Draw(img)
    # bottom gradient dark for legibility
    for i in range(220):
        a = int(150 * (i / 220))
        d.rectangle([0, H - 220 + i, W, H - 220 + i + 1], fill=(10, 8, 6, a))
    f_b = get_font(True, 26)
    if badge:
        bw = int(d.textlength(badge, font=f_b)) + 36
        d.rounded_rectangle([48, 42, 48 + bw, 42 + 50], radius=12, fill=(240, 92, 40))
        d.text((66, 54), badge, font=f_b, fill=(20, 16, 12))
    f_t = get_font(True, 46)
    lines = wrap(title, f_t, W - 120, d)[:3]
    y = H - 60 - len(lines) * 58
    for ln in lines:
        d.text((60, y), ln, font=f_t, fill=(248, 248, 245))
        y += 58
    f_f = get_font(False, 24)
    d.text((60, H - 42), "Nhân Sự Toàn Năng Hermes · speedreading.vn/shermes",
           font=f_f, fill=(220, 200, 180))
    return img

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="Hermes tự động hóa công việc")
    ap.add_argument("--topic", default="default")
    ap.add_argument("--badge", default="")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    img = overlay(bg(a.topic), a.title, a.badge)
    if not a.out:
        h = hashlib.md5((a.topic + a.title).encode()).hexdigest()[:8]
        a.out = f"ai-{a.topic}-{h}.webp"
    out_path = a.out if (os.path.isabs(a.out) or a.out.startswith("static/")) else os.path.join(OUT_DIR, a.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "WEBP", quality=92)
    print("/covers/" + os.path.basename(out_path))

if __name__ == "__main__":
    main()
