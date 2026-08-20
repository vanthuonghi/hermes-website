import os, re
topics = open('scripts/topics.txt', encoding='utf-8').read().splitlines()
posts = [p for p in os.listdir('content/posts') if p.endswith('.md')]

def norm(s):
    s = s.lower().replace('hermes ', '').strip()
    s = re.sub(r'[^a-z0-9à-ỹ ]', '', s)
    return s

pn = set(norm(p[:-3]) for p in posts)
print("posts:", len(posts), "topics:", len(topics))
for t in topics:
    tn = norm(t)
    hit = any(tn in p or p in tn for p in pn)
    if not hit:
        print("NO POST:", t)
print("--- done ---")
