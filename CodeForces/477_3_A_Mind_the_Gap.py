nol, gap = [int(x) for x in input().split()]
a = []
for _ in range(nol):
    a.append([int(x) for x in input().split()])
gaps = [(b[0]*60 + b[1]) - (a[0]*60 + a[1]) for a, b in zip(a, a[1:])]
has = False
for i,v  in enumerate(gaps):
    if v >= gap+1:
        print(*a[i])
        has = True
if not has:print(a[-1])
