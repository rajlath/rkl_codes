from collections import deque
n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
z = deque(sorted([(c[i], i) for i in range(n)]))
for _ in range(m):
    t, d = [int(x) for x in input().split()]
    ans = 0
    t -= 1
    k = min(d, a[t])
    a[t]-= k
    ans += k * c[t]
    d -= k
    while d > 0 and z:
        curr = z[0]
        k = min(a[curr[1]], d)
        a[curr[1]] -= k
        d -= k
        ans += curr[0] * k
        if not a[curr[1]]:
            z.popleft()
    if not d:
        print(ans)
    else:
        print(0)