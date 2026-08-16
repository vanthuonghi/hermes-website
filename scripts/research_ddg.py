#!/usr/bin/env python3
"""
research_ddg.py — Research thay thế Firecrawl (0đ, không key).
Bước 1: DuckDuckGo HTML scrape lấy 10 kết quả (title+link) tiếng Việt.
Bước 2: Jina Reader (r.jina.ai/<url>) đọc sâu top-2 link -> markdown.
Usage: python3 research_ddg.py "từ khóa" [số_kết_quả_mặc_định_10]
In ra markdown tóm tắt để agent dùng làm research.
"""
import sys, urllib.request, urllib.parse, re, json

DDG = "https://html.duckduckgo.com/html/?q="
JINA = "https://r.jina.ai/"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
      "Referer": "https://duckduckgo.com/", "Accept-Language": "vi-VN"}

def ddg(query, n=10):
    req = urllib.request.Request(DDG + urllib.parse.quote(query), headers=UA)
    data = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
    titles = re.findall(r'result__a[^>]*>(.*?)</a>', data, re.S)
    links = re.findall(r'result__a[^>]*href="([^"]+)"', data)
    out = []
    for i in range(min(n, len(titles))):
        t = re.sub(r'<[^>]+>', '', titles[i]).strip()
        # decode duckduckgo redirect
        m = re.search(r'uddg=([^&]+)', links[i]) if i < len(links) else None
        url = urllib.parse.unquote(m.group(1)) if m else (links[i] if i < len(links) else '')
        if t and url:
            out.append((t, url))
    return out

def jina(url, max_chars=2500):
    try:
        req = urllib.request.Request(JINA + url, headers=UA)
        txt = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
        # cắt đoạn đầu hữu ích
        txt = txt.strip()
        return txt[:max_chars]
    except Exception as e:
        return f"[Jina lỗi: {e}]"

def main():
    if len(sys.argv) < 2:
        print("Usage: research_ddg.py \"từ khóa\"")
        sys.exit(1)
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print(f"# RESEARCH: {q}\n")
    results = ddg(q, n)
    if not results:
        print("[DDG không trả về kết quả — thử lại sau hoặc đổi từ khóa]")
        sys.exit(0)
    print(f"Tìm thấy {len(results)} nguồn:\n")
    for i, (t, u) in enumerate(results, 1):
        print(f"{i}. {t}\n   {u}")
    print("\n---\n# ĐỌC SÂU TOP 2 (Jina Reader)\n")
    for i, (t, u) in enumerate(results[:2], 1):
        print(f"## Nguồn {i}: {t}\n{u}\n")
        print(jina(u))
        print("\n")

if __name__ == "__main__":
    main()
