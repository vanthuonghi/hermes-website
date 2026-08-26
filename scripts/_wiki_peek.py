#!/usr/bin/env python3
import sys, urllib.request, json
arts = sys.argv[1:]
for art in arts:
    try:
        u = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.request.quote(art)
        d = json.loads(urllib.request.urlopen(u, timeout=20).read().decode())
        print("=====", art, "=====")
        print((d.get("extract", "") or "")[:700])
    except Exception as e:
        print(art, "ERR", e)
    print()
