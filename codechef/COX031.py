nol, st = [x for x in input().split()]
nol = int(nol)
Fortune = True
Lucky   = False
for x in st:
    if x not in ["4", "7", "0"]:
        Fortune = False
        break
if Fortune:
    left = sum([int(x) for x in st[:nol//2]])
    rite = sum([int(x) for x in st[nol//2:]])
    if left == rite : Lucky = True
print("YES" if Lucky else "NO")
