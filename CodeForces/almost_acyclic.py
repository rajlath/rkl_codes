N = 500
cnt = 0
g = [0] * N

n, m = [int(x) for x in input().split()]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    u-=1
    v-=1
    g.append(v)

for _ in range(u):


