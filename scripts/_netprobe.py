#!/usr/bin/env python3
import urllib.request, json, re

def get(u, timeout=20):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Firefox/120.0"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")

# 1) Wikipedia REST summary
for art in ["Email_marketing", "Open_rate"]:
    try:
        d = json.loads(get("https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.request.quote(art)))
        print("REST", art, "->", (d.get("extract", "") or "")[:600])
    except Exception as e:
        print("REST", art, "ERR", e)

# 2) Wikipedia api.php search
try:
    u = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.request.quote("email marketing open rate") + "&format=json&srlimit=3"
    d = json.loads(get(u))
    for r in d.get("query", {}).get("search", []):
        t = r.get("title", "")
        sn = re.sub(r"<[^>]+>", "", r.get("snippet", ""))
        print("API", t, "::", sn[:200])
except Exception as e:
    print("API ERR", e)
