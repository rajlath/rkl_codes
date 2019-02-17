from bisect import bisect_right
n=int(input())
v=list(map(int,input().split()))
xp = {}
for i in v:
    if i < 0:
        if abs(i) in xp:
            xp[abs(i)] = 0
        else:
            xp[abs(i)] = xp.get(abs(i), 0)
    else:
        if i in xp:
            if xp[i] != 0:
                xp[i] += 1
        else:
            xp[i] = xp.get(i, 0) + 1
valids = []
for k, v1 in xp.items():
    if v1 != 0:
        valids += [k] * v1
valids.sort()
ans = 0
mod = int(10 ** 9)+ 7
for i in range(n):
    if v[i] > 0:
        r = bisect_right(valids, v[i])
        if len(xp) - r >= 3:
            ans += 1
print(ans % mod)


