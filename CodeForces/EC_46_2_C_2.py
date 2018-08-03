
n = int(input())
pos = {}
for _ in range(n):
    l, r = [int(x) for x in input().split()]
    if l in pos: pos[l] += 1
    else:pos[l] = 1
    if r+1 in pos: pos[r+1] -= 1
    else:pos[r+1] = -1
    #pos[r+1] = pos.get(r+1, -1) - 1
a = sorted(pos.items(), key = lambda x : x[0])

res = [0] * n
s = 0
for i in range(len(a)):
    if 1 <= s <= n:
        res[s-1] += a[i][0] - a[i-1][0]
    s += a[i][1]
print(*res)
'''
[(0, 1), (1, 1), (3, 1), (4, -2), (9, -1)]
n = int(input())
pos = {}
for _ in range(n):
    L, R = map(int, input().split())
    if L in pos: pos[L] += 1
    else: pos[L] = 1
    if R+1 in pos: pos[R+1] -= 1
    else: pos[R+1] = -1
a = sorted(pos.items(), key=lambda x: x[0])
print(a)
res = [0]*n
s = 0
for i in range(len(a)):
    if 1 <= s <= n:
        res[s - 1] += a[i][0] - a[i - 1][0]
    s += a[i][1]
print(*res)
'''
