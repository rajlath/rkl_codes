import math
n, m = [int(x) for x in input().split()]
edges = []
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    edges.append([a - 1, b - 1, c])
d = [math.inf] * n
p = [math.inf] * n
for i in range(n):
    x = -1
    for z in edges:
        a, b, c = z
        if d[a] + c < d[b]:
            d[b] = d[a] + c
            p[b] = a
            x = b
print(x)
if x == -1:
    print(-1)
else:
    for i in range(n):
        x = p[x]
    o = x
    ar = [1] * o
    x = p[x]
    ar.append(x)
    while x != 0:
        x = p[x]
        ar.append(x)
    a = a[::-1]
    print("YES")
    print(*a)

