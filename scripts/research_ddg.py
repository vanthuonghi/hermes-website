#!/usr/bin/env python3
"""
research_ddg.py — Research thay thế Firecrawl (0đ, không key).
Bước 1: DuckDuckGo HTML scrape lấy kết quả (title+link) tiếng Việt.
        - Có retry/backoff (DDG hay block IP nếu gọi dồn dập).
        - Fallback sang lite endpoint nếu html trắng.
Bước 2: Jina Reader (r.jina.ai/<url>) đọc sâu top-2 link THẬT (bỏ link redirect quảng cáo
        của DDG vì Jina không đọc được → lỗi 422).
Usage: python3 research_ddg.py "từ khóa" [số_kết_quả_mặc_định_10]
In ra markdown tóm tắt để agent dùng làm research.
"""
import sys, urllib.request, urllib.parse, re, time

DDG_HTML = "https://html.duckduckgo.com/html/?q="
DDG_LITE = "https://lite.duckduckgo.com/lite/?q="
JINA = "https://r.jina.ai/"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
      "Referer": "https://duckduckgo.com/", "Accept-Language": "vi-VN"}

def _fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")

def _parse_html(data):
    titles = re.findall(r'result__a[^>]*>(.*?)</a>', data, re.S)
    links = re.findall(r'result__a[^>]*href="([^"]+)"', data)
    out = []
    for i in range(min(len(titles), len(links))):
        t = re.sub(r'<[^>]+>', '', titles[i]).strip()
        m = re.search(r'uddg=([^&]+)', links[i])
        url = urllib.parse.unquote(m.group(1)) if m else links[i]
        if t and url and "duckduckgo.com" not in url:
            out.append((t, url))
    return out

def _parse_lite(data):
    out = []
    for m in re.findall(r'<a[^>]+class="result-link"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', data, re.S):
        url, t = m[0], re.sub(r'<[^>]+>', '', m[1]).strip()
        if t and url and url.startswith("http"):
            out.append((t, url))
    return out

def ddg(query, n=10, retries=3):
    last = []
    for attempt in range(retries):
        try:
            data = _fetch(DDG_HTML + urllib.parse.quote(query))
            res = _parse_html(data)
            if res:
                return res[:n]
            last = res
        except Exception:
            pass
        # fallback lite
        try:
            data = _fetch(DDG_LITE + urllib.parse.quote(query))
            res = _parse_lite(data)
            if res:
                return res[:n]
        except Exception:
            pass
        if attempt < retries - 1:
            time.sleep(5 * (attempt + 1))  # backoff 5s, 10s
    return last

def jina(url, max_chars=2500):
    try:
        txt = _fetch(JINA + url, timeout=30)
        return txt.strip()[:max_chars]
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
        print("[DDG không trả về kết quả — đổi từ khóa hoặc thử lại sau (có thể bị IP block tạm thời)]")
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
