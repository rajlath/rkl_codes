n = input()
c = {}
for x in [int(x) for x in input().split()]:
    u, t = x, 0
    while 0 == u%3:
        u /= 3
        t += 1
    c[t] = c.get(t, []) + [x]
for x in sorted(c)[::-1]:
    for y in sorted(c[x]):
        print(y, end=' ')