#!/usr/bin/env python3
import urllib.request, json, re
def get(u, timeout=25):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Firefox/120.0"})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")
u = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=" + urllib.request.quote("Email marketing") + "&format=json"
d = json.loads(get(u))
pages = d.get("query", {}).get("pages", {})
for pid, p in pages.items():
    txt = p.get("extract", "")
    for line in txt.split("\n"):
        if re.search(r"open rate|open-rate|click[- ]through|%|percent", line, re.I):
            print(line.strip()[:300])
