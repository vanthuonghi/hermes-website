import sys, urllib.request, json
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"}
for t in sys.argv[1:]:
    u = "https://en.wikipedia.org/api/rest_v1/page/summary/" + t
    try:
        req = urllib.request.Request(u, headers=UA)
        d = json.loads(urllib.request.urlopen(req, timeout=20).read().decode())
        print("=====", t, "=====")
        print(d.get("extract", "")[:1100])
        print()
    except Exception as e:
        print(t, "ERR", e)
