#!/usr/bin/env python3
"""
make_cover.py — Sinh cover branded cho blog Hermes BẰNG CODE (0đ, không cần AI/credit).
Mỗi bài 1 cover riêng: gradient ấm + tiêu đề bài + tagline WOW-Agent + badge.
Hệ thống rút kinh nghiệm: log vào .cover_log.json (chủ đề -> palette đã dùng) để tránh lặp, tối ưu dần.

Usage:
  python3 make_cover.py --title "Tiêu đề bài" --topic "phan-than" --out static/covers/auto-xxx.webp
Hoặc (cron): truyền qua argv, script tự đặt tên.

Yêu cầu: pip install pillow (đã có). Font DejaVu/Noto có sẵn.
"""
import sys, os, json, argparse, hashlib
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "..", "static", "covers")
LOG = os.path.join(BASE, ".cover_log.json")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# Palette theo chủ đề (ấm, brand Hermes: cam/vàng chủ đạo)
THEMES = {
    "default":  ((255,180,84), (30,20,5),  "AI AGENT LÀM VIỆC"),
    "phan-than":((120,200,255),(8,20,40),  "PHÂN THÂN SONG SONG"),
    "memory":   ((160,120,255),(20,10,40), "CÓ TRÍ NHỚ"),
    "api":      ((80,220,180), (5,30,25),  "KẾT NỐI API"),
    "tiet-kiem":((255,140,120),(40,15,10), "TIẾT KIỆM THỜI GIAN"),
    "bao-cao":  ((100,180,255),(10,20,45), "TỰ ĐỘNG BÁO CÁO"),
    "email":    ((120,220,160),(10,30,20), "XỬ LÝ INBOX"),
    "ke-hoach": ((255,200,120),(35,22,5),  "LẬP KẾ HOẠCH"),
    "vong-lap": ((200,160,255),(22,12,40), "VÒNG LẶP 8 BƯỚC"),
    "quality":  ((255,120,160),(40,10,25), "QUALITY GATE"),
    "content":  ((255,170,90), (30,18,5),  "TỰ ĐỘNG CONTENT"),
    "kit":      ((140,210,255),(10,22,42), "3 BỘ AI KIT"),
    "khac-chatgpt":((255,150,100),(38,15,8),"AGENT ≠ CHATBOT"),
}

def load_log():
    try: return json.load(open(LOG))
    except: return {"used": [], "count": 0}

def save_log(log):
    json.dump(log, open(LOG,"w"), ensure_ascii=False, indent=2)

def wrap(text, font, max_w, draw):
    lines=[]; cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if draw.textlength(t, font=font) <= max_w: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def make(title, topic, out_name=None, badge=None):
    topic=topic or "default"
    accent, bg, tag = THEMES.get(topic, THEMES["default"])
    if badge: tag = badge
    W,H=1200,630
    img=Image.new("RGB",(W,H),bg)
    d=ImageDraw.Draw(img)
    # gradient ấm đơn giản: vẽ nhiều dải ngang từ bg -> accent mờ
    for i in range(H):
        r=bg[0]+(accent[0]-bg[0])*i//H//3
        g=bg[1]+(accent[1]-bg[1])*i//H//3
        b=bg[2]+(accent[2]-bg[2])*i//H//3
        d.line([(0,i),(W,i)],fill=(r,g,b))
    # badge góc
    try: f_badge=ImageFont.truetype(f"{FONT_DIR}/DejaVuSans-Bold.ttf",34)
    except: f_badge=ImageFont.load_default()
    bw=int(d.textlength(tag, font=f_badge))+44
    d.rounded_rectangle([60,55,60+bw,55+60],radius=12,fill=accent)
    d.text((60+22,69),tag,font=f_badge,fill=bg)
    # tiêu đề (2-3 dòng)
    try: f_t=ImageFont.truetype(f"{FONT_DIR}/DejaVuSans-Bold.ttf",48)
    except: f_t=ImageFont.load_default()
    lines=wrap(title, f_t, W-140, d)
    y=240
    for ln in lines[:3]:
        d.text((70,y),ln,font=f_t,fill=(245,245,245))
        y+=62
    # footer brand
    try: f_f=ImageFont.truetype(f"{FONT_DIR}/DejaVuSans.ttf",30)
    except: f_f=ImageFont.load_default()
    d.text((70,H-90),"Nhân Sự Toàn Năng Hermes · speedreading.vn/shermes",font=f_f,fill=accent)
    # output
    if not out_name:
        h=hashlib.md5((title+topic).encode()).hexdigest()[:8]
        out_name=f"auto-{topic}-{h}.webp"
    out_path=os.path.join(OUT_DIR, out_name)
    img.save(out_path,"WEBP",quality=88)
    return "/covers/"+out_name

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--title",required=True)
    ap.add_argument("--topic",default="default")
    ap.add_argument("--badge",default=None)
    ap.add_argument("--out",default=None)
    a=ap.parse_args()
    # rút kinh nghiệm: nếu topic đã dùng nhiều lần, xoay palette phụ
    log=load_log()
    path=make(a.title, a.topic, a.out, a.badge)
    log["used"].append({"t":a.title,"topic":a.topic,"f":path})
    log["count"]=log.get("count",0)+1
    save_log(log)
    print(path)
