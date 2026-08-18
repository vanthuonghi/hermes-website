#!/usr/bin/env python3
"""
research_ddg.py — Research thay thế Firecrawl (0đ, không key).
Thực tế trên IP datacenter (Oracle VM): DuckDuckGo / Ecosia / Mojeek / SearXNG / Reddit
đều bị block (403 / trắng trang). Nên chuỗi fallback dùng các nguồn JSON công khai
datacenter-friendly:
  1. DuckDuckGo HTML   (dự phòng, sống khi IP không bị block)
  2. DuckDuckGo Lite  (dự phòng)
  3. HackerNews Algolia API  (LUÔN SỐNG trên Oracle — trending tech/AI, có link thật)
  4. Wikipedia REST API       (LUÔN SỐNG trên Oracle — bối cảnh nền tảng)
Mỗi engine trả (title, url) thật -> đọc sâu top-2 bằng Jina Reader.
Usage: python3 research_ddg.py "từ khóa" [số_kết_quả_mặc_định_10]
"""
import sys, urllib.request, urllib.parse, re, time, json

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
      "Accept-Language": "vi-VN,en-US;q=0.9"}

BLOCKLIST_HOST = ("duckduckgo.com", "ecosia.org", "mojeek.com", "searx", "marginalia",
                  "bing.com", "google.", "yandex.", "startpage.com", "brave.com",
                  "w3.org", "creativecommons.org", "ip2location.com")

def _fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")

def _clean_url(url):
    m = re.search(r"[?&]uddg=([^&]+)", url)
    if m:
        return urllib.parse.unquote(m.group(1))
    m = re.search(r"ecosia\.org/redirect\?url=([^&]+)", url)
    if m:
        return urllib.parse.unquote(m.group(1))
    return url

def _extract_links(html):
    out, seen = [], set()
    for m in re.finditer(r'<a\b[^>]*\bhref="(https?://[^"]+)"[^>]*>(.*?)</a>', html, re.S | re.I):
        url = _clean_url(m.group(1))
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if not url or not text:
            continue
        host = urllib.parse.urlparse(url).netloc.lower()
        if any(b in host for b in BLOCKLIST_HOST):
            continue
        if url in seen:
            continue
        seen.add(url)
        out.append((text, url))
    return out

def _ddg_html(q, n=None):
    return _extract_links(_fetch("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)))

def _ddg_lite(q, n=None):
    return _extract_links(_fetch("https://lite.duckduckgo.com/lite/?q=" + urllib.parse.quote(q)))

def _hn(q, n):
    # HackerNews Algolia: trending story, có link thật (hoặc thread HN nếu self-post)
    u = "https://hn.algolia.com/api/v1/search_by_date?query=" + urllib.parse.quote(q) + "&tags=story&hitsPerPage=" + str(n)
    try:
        d = json.loads(_fetch(u))
    except Exception:
        return []
    out = []
    for h in d.get("hits", []):
        title = h.get("title")
        if not title:
            continue
        url = h.get("url")
        if not url:  # self-post -> link thread HN
            url = "https://news.ycombinator.com/item?id=" + str(h.get("objectID", ""))
        out.append((title.strip(), url))
    return out

def _wiki(q, n):
    # Wikipedia REST: bối cảnh nền tảng, datacenter-friendly
    u = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(q) + "&format=json&srlimit=" + str(n)
    try:
        d = json.loads(_fetch(u))
    except Exception:
        return []
    out = []
    for r in d.get("query", {}).get("search", []):
        pid = r.get("pageid")
        if not pid:
            continue
        t = re.sub(r"<[^>]+>", "", r.get("title", "")).strip()
        out.append((t, f"https://en.wikipedia.org/?curid={pid}"))
    return out

ENGINES = [
    ("DuckDuckGo", _ddg_html),
    ("DuckDuckGo-Lite", _ddg_lite),
    ("HackerNews", lambda q, n: _hn(q, n)),
    ("Wikipedia", lambda q, n: _wiki(q, n)),
]

def search(query, n=10):
    for name, fn in ENGINES:
        try:
            res = fn(query, n)
            if res:
                print(f"[engine: {name}]", file=sys.stderr)
                return res[:n]
        except Exception as e:
            print(f"[engine {name} lỗi: {e}]", file=sys.stderr)
        time.sleep(1.0)
    return []

def _read_deep(url, max_chars=2500):
    """Đọc sâu nội dung. Trên IP Oracle: Jina/AllOrigins/Codetabs đều 522/403.
    Chỉ Wikipedia REST summary sống -> dùng cho link wiki; link khác bỏ qua."""
    if "wikipedia.org" in url or "wikimedia.org" in url:
        cur = re.search(r"curid=(\d+)", url)
        try:
            if cur:
                q = json.loads(_fetch("https://en.wikipedia.org/w/api.php?action=query&prop=info&inprop=url&pageids="
                                      + cur.group(1) + "&format=json"))
                title = q["query"]["pages"][cur.group(1)]["title"]
            else:
                title = urllib.parse.unquote(url.rsplit("/", 1)[-1]).replace("_", " ")
            d = json.loads(_fetch("https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(title)))
            return (d.get("extract", "") or "[wiki không có tóm tắt]")[:max_chars]
        except Exception as e:
            return f"[Wiki summary lỗi: {e}]"
    # link HN / website khác: Jina chết trên Oracle -> chỉ trả tiêu đề đã có
    return "[Đọc sâu bị bỏ qua: Jina/AllOrigins/Codetabs đều block IP Oracle (522/403). Dùng tiêu đề + link làm nguồn.]"

def main():
    if len(sys.argv) < 2:
        print("Usage: research_ddg.py \"từ khóa\" [số_kết_quả]")
        sys.exit(1)
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print(f"# RESEARCH: {q}\n")
    results = search(q, n)
    if not results:
        print("[TẤT CẢ engine đều không trả kết quả — có thể bị IP block đồng loạt. Đổi từ khóa hoặc thử lại sau.]")
        sys.exit(0)
    print(f"Tìm thấy {len(results)} nguồn:\n")
    for i, (t, u) in enumerate(results, 1):
        print(f"{i}. {t}\n   {u}")
    print("\n---\n# ĐỌC SÂU TOP 2 (Jina Reader)\n")
    for i, (t, u) in enumerate(results[:2], 1):
        print(f"## Nguồn {i}: {t}\n{u}\n")
        print(_read_deep(u))
        print("\n")

if __name__ == "__main__":
    main()
