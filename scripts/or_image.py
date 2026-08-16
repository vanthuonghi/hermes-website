#!/usr/bin/env python3
"""
or_image.py — Sinh cover AI thật qua OpenRouter (gemini-3.1-flash-lite-image) + đè TEXT tiêu đề/badge bằng PIL.
Mục tiêu: SIÊU CHẤT LƯỢNG (đã tốn ~$0.034/ảnh thì phải đẹp).
- Ảnh nền: Gemini sinh cảnh cinematic ấm, người + dashboard, KHÔNG chữ (tránh lỗi text lộn xộn)
- Overlay: gradient tối đáy + tiêu đề bài (DejaVu Bold) + badge WOW-Agent + footer brand
- Output: WebP 1200x630 (chuẩn OG/blog cover)

Usage:
  python3 or_image.py --title "..." --topic "phan-than" --badge "PHÂN THÂN SONG SONG" --out static/covers/ai-xxx.webp
"""
import sys, os, json, base64, argparse, hashlib, urllib.request, io
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "..", "static", "covers")
ENV = os.path.join(os.path.expanduser("~"), ".hermes", ".env")
MODEL = "google/gemini-3.1-flash-lite-image"
API = "https://openrouter.ai/api/v1/chat/completions"
W, H = 1200, 630

TOPIC_PROMPTS = {
    "default": "Cinematic warm lifestyle photography: a relaxed person drinking coffee while multiple screens show automated dashboards running by themselves, soft amber home-office light, shallow depth of field, professional color grading, bokeh. NO text, NO words, NO letters, NO logos.",
    "phan-than": "Cinematic warm scene: one person relaxed in armchair while several glowing translucent clone silhouettes work on separate screens in parallel, cozy room amber light, depth of field, professional photography. NO text, NO words.",
    "memory": "Cinematic warm scene: a person calmly reviewing a floating glowing memory timeline of past tasks, screens showing remembered context, cozy room, soft light, photographic. NO text, NO words.",
    "api": "Cinematic warm scene: a person connecting many glowing app icons into one central hub, data flowing automatically, cozy desk amber light, photographic. NO text, NO words.",
    "tiet-kiem": "Cinematic warm night scene: a person sleeping peacefully while screens quietly finish a pile of tasks overnight, cozy bedroom moonlight + amber lamp, photographic. NO text, NO words.",
    "bao-cao": "Cinematic warm morning scene: a person wakes to a ready weekly report on screen, dashboard auto-generated, cozy morning light, photographic. NO text, NO words.",
    "email": "Cinematic warm scene: a person sipping tea while inbox self-sorts and drafts emails on screen, cozy, photographic. NO text, NO words.",
    "ke-hoach": "Cinematic warm scene: a person reviews a calm monthly plan on screen while AI arranges weekly cards, cozy desk, amber light, photographic. NO text, NO words.",
    "vong-lap": "Cinematic warm scene: circular flow of tasks animated on screens around a relaxed person, cozy room, photographic. NO text, NO words.",
    "quality": "Cinematic warm scene: a gatekeeper checking a draft then passing a clean version to a relaxed person, cozy, photographic. NO text, NO words.",
    "content": "Cinematic warm scene: screens auto-writing blog posts and social cards while person relaxes, cozy, photographic. NO text, NO words.",
    "kit": "Cinematic warm scene: three glowing toolkits floating around a happy person, cozy, photographic. NO text, NO words.",
    "khac-chatgpt": "Cinematic split scene: left a person typing to a chatbot, right a person relaxing while an agent does the work, cozy, photographic. NO text, NO words.",
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def get_key():
    try:
        for line in open(ENV, encoding="utf-8"):
            if line.startswith("OPENROUTER_API_KEY="):
                return line.strip().split("=", 1)[1]
    except Exception:
        pass
    return os.environ.get("OPENROUTER_API_KEY", "")

def gen_image(topic):
    prompt = TOPIC_PROMPTS.get(topic, TOPIC_PROMPTS["default"])
    key = get_key()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY not found")
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1200,
    }).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read().decode())
    msg = d["choices"][0]["message"]
    imgs = msg.get("images", [])
    if not imgs:
        raise RuntimeError("no image: " + json.dumps(msg, ensure_ascii=False)[:200])
    iu = imgs[0].get("image_url")
    url = iu["url"] if isinstance(iu, dict) else iu
    raw = url.split(",", 1)[1] if url.startswith("data:") else url
    return base64.b64decode(raw)

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

def overlay(img_bytes, title, badge):
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = img.resize((W, H))
    d = ImageDraw.Draw(img)
    # bottom gradient dark
    for i in range(220):
        a = int(150 * (i / 220))
        d.rectangle([0, H - 220 + i, W, H - 220 + i + 1], fill=(10, 8, 6, a))
    # badge top-left
    try: f_b = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 26)
    except: f_b = ImageFont.load_default()
    if badge:
        bw = int(d.textlength(badge, font=f_b)) + 36
        d.rounded_rectangle([48, 42, 48 + bw, 42 + 50], radius=12, fill=(240, 92, 40))
        d.text((66, 54), badge, font=f_b, fill=(20, 16, 12))
    # title bottom
    try: f_t = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 46)
    except: f_t = ImageFont.load_default()
    lines = wrap(title, f_t, W - 120, d)[:3]
    y = H - 60 - len(lines) * 58
    for ln in lines:
        d.text((60, y), ln, font=f_t, fill=(248, 248, 245))
        y += 58
    # footer brand
    try: f_f = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans.ttf", 24)
    except: f_f = ImageFont.load_default()
    d.text((60, H - 42), "Nhân Sự Toàn Năng Hermes · speedreading.vn/shermes", font=f_f, fill=(220, 200, 180))
    return img

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="Hermes tự động hóa công việc")
    ap.add_argument("--topic", default="default")
    ap.add_argument("--badge", default="")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    data = gen_image(a.topic)
    img = overlay(data, a.title, a.badge)
    if not a.out:
        h = hashlib.md5((a.topic + a.title).encode()).hexdigest()[:8]
        a.out = f"ai-{a.topic}-{h}.webp"
    out_path = a.out if (os.path.isabs(a.out) or a.out.startswith("static/")) else os.path.join(OUT_DIR, a.out)
    img.save(out_path, "WEBP", quality=92)
    print("/covers/" + os.path.basename(out_path))

if __name__ == "__main__":
    main()
