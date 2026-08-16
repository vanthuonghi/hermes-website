#!/usr/bin/env python3
"""
or_image.py — Sinh cover AI thật qua OpenRouter (RẺ NHẤT: google/gemini-3.1-flash-lite-image).
Giá ảnh thực tế ~0đ (img price=0, chỉ tốn prompt token nhỏ). Key đọc từ ~/.hermes/.env OPENROUTER_API_KEY.
Ảnh trả về dạng data url trong message.images[0].image_url.url -> lưu .webp.

Usage:
  python3 or_image.py --topic "phan-than" --out static/covers/ai-xxx.webp
Nếu không truyền --out, tự đặt tên theo hash(topic+time).
Prompt: cảnh ấm, người + dashboard tự chạy, KHÔNG chữ (tránh lỗi text).
"""
import sys, os, json, base64, argparse, hashlib, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "..", "static", "covers")
ENV = os.path.join(os.path.expanduser("~"), ".hermes", ".env")
MODEL = "google/gemini-3.1-flash-lite-image"
API = "https://openrouter.ai/api/v1/chat/completions"

# Prompt theo chủ đề (cảnh ấm, người thong dong, máy tự chạy, KHÔNG chữ)
TOPIC_PROMPTS = {
    "default": "Warm cozy minimalist scene: a relaxed person drinking coffee while multiple screens show automated dashboards running by themselves. Soft amber home-office lighting. NO text, NO words, NO letters.",
    "phan-than": "Warm scene: one person relaxed while several translucent clone silhouettes work on separate screens in parallel. Cozy room, amber light. NO text.",
    "memory": "Warm scene: a person calmly reviewing a floating glowing memory timeline of past tasks, screens showing remembered context. Cozy. NO text.",
    "api": "Warm scene: a person connecting many app icons into one hub, data flowing automatically. Cozy desk, amber light. NO text.",
    "tiet-kiem": "Warm scene: a person sleeping peacefully while screens quietly finish a pile of tasks overnight. Cozy bedroom, moonlight + amber lamp. NO text.",
    "bao-cao": "Warm scene: a person wakes to a ready weekly report on screen, dashboard auto-generated. Cozy morning light. NO text.",
    "email": "Warm scene: a person sipping tea while inbox self-sorts and drafts emails on screen. Cozy. NO text.",
    "ke-hoach": "Warm scene: a person reviews a calm monthly plan on screen while AI arranges weekly cards. Cozy. NO text.",
    "vong-lap": "Warm scene: circular flow of tasks (find->research->do->check) animated on screens around a relaxed person. Cozy. NO text.",
    "quality": "Warm scene: a gatekeeper checking a draft then passing a clean version to a relaxed person. Cozy. NO text.",
    "content": "Warm scene: screens auto-writing blog posts and social cards while person relaxes. Cozy. NO text.",
    "kit": "Warm scene: three glowing toolkits (starter, life, business) floating around a happy person. Cozy. NO text.",
    "khac-chatgpt": "Warm split scene: left a person typing to a chatbot, right a person relaxing while an agent does the work. Cozy. NO text.",
}

def get_key():
    try:
        for line in open(ENV, encoding="utf-8"):
            if line.startswith("OPENROUTER_API_KEY="):
                return line.strip().split("=", 1)[1]
    except Exception:
        pass
    return os.environ.get("OPENROUTER_API_KEY", "")

def gen(topic):
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
        raise RuntimeError("no image returned: " + json.dumps(msg, ensure_ascii=False)[:200])
    iu = imgs[0].get("image_url")
    url = iu["url"] if isinstance(iu, dict) else iu
    raw = url.split(",", 1)[1] if url.startswith("data:") else url
    return base64.b64decode(raw)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default="default")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    data = gen(a.topic)
    if not a.out:
        h = hashlib.md5((a.topic + str(os.urandom(4))).encode()).hexdigest()[:8]
        a.out = f"ai-{a.topic}-{h}.webp"
    out_path = a.out if (os.path.isabs(a.out) or a.out.startswith("static/")) else os.path.join(OUT_DIR, a.out)
    # convert to webp
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(data)).convert("RGB")
        img.save(out_path, "WEBP", quality=90)
    except Exception:
        # fallback: save raw (likely jpeg)
        with open(out_path, "wb") as f:
            f.write(data)
    print("/covers/" + os.path.basename(out_path))

if __name__ == "__main__":
    main()
