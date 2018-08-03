'''
sample input
sample output
4 2
1 2
2 1 3
2 4 2
1 3
1
4

sample input
sample output
4 1
3 4 3 2
3 1 3 4
3 1 2 4
3 1 2 3
0
'''
'''
from collections import defaultdict
users , user = [int(x) for x in input().split()]
pal = []
palofpal = []
for i in range(users):
    pals = [int(x) for x in input().split()]
    pal.append(pals[1:])
user = user - 1

for i in range(len(pal[user])):
    curr_pal = pal[user][i]
    for j in range(len(pal[curr_pal - 1])):
        curr_fof = pal[curr_pal-1][j]
        if curr_fof != user + 1 and curr_fof not in pal[user] and curr_fof not in palofpal:
            palofpal.append(curr_fof)
if len(palofpal) > 0:
    print(len(palofpal))
    print(*palofpal)
else:
    print(0)
'''
n, x = [int(x) for x in input().split()]
p = [[None]]
for i in range(n):
    curr = [int(x) for x in input().split()]
    p.append([y for y in curr[1:]])


isf = [False] * (n + 1)
isff= [False] * (n + 1)
for i in range(len(p[x])):

    isf[p[x][i]] = True
    for j in range(1, len(p[p[x][i]])):
        isf[p[x][i]] = True
        for j in range(len(p[p[x][i]])):
            isff[p[p[x][i]][j]] = True
fof = []
for i in range(1, n+1):
    if i != x and not isf[i] and isff[i]:
        fof.append(i)
if len(fof) > 0:
    print(len(fof))
    print(*fof)
else:
    print(0)











