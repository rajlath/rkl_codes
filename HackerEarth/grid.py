n,m,q = [int(x) for x in input().split()]
s = []
for i in range(n):
    s.append(input())
Q = []
lvl = 0
visited = [[0 for x in range(m+10)] for y in range(n+10)]
level   = [[0 for x in range(m+10)] for y in range(n+10)]

xy = [int(x) for x in input().split()]
Q.append((xy[0], xy[1]))
while len(Q) > 0:
    x = Q[-1]
    Q.pop()
    a, b = x[0], x[1]
    print(a, b)
    if a<0 or a > n-1 or b < 0 or b < m-1 or visited[a][b] or s[a][b] == "*":
        visited[a][b] = True
        level[a][b] = lvl

    Q.append((a+1, b))
    Q.append((a-1, b))
    Q.append((a, b+1))
    Q.append((a, b-1))

    lvl += 1

for _ in range(q):
    a, b = [int(x)-1 for x in input().split() ]
    print(level[a][b])






