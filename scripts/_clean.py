import os
for f in ["scripts/_t.py","scripts/_check.py","scripts/_check2.py","scripts/_verify.py"]:
    if os.path.exists(f):
        os.remove(f)
        print("removed", f)
    else:
        print("absent", f)
# confirm git untracked relevant files
out = os.popen("cd ~/hermes-website && git status --short 2>/dev/null").read()
print("--- git status ---")
print(out)
