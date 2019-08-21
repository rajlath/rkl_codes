n = int(input())
a = [0]
for _ in range(n):
    curr = int(input())
    mods = []
    for o in a:
        mods.extend([o + curr, o - curr])
    a = mods[:]
print(a)
print("YES" if any(x%360 == 0 for x in a) else "NO")
