import urllib.request, urllib.parse, json

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")

print("=== HN Algolia: AI agent customer service ===")
q = urllib.parse.quote("AI agent customer service automation")
url = f"https://hn.algolia.com/api/v1/search?query={q}&tags=story&hitsPerPage=6"
try:
    d = json.loads(get(url))
    for h in d["hits"]:
        if h.get("title"):
            print("-", h["title"], "|", h.get("points"), "pts")
except Exception as e:
    print("HN err:", e)

print("\n=== Wiki: Software agent ===")
for title in ["Software_agent", "Chatbot", "Customer_service"]:
    try:
        u = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        d = json.loads(get(u))
        print(f"[{title}]", d.get("extract", "")[:400])
        print()
    except Exception as e:
        print(f"Wiki {title} err:", e)
