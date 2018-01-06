'''
4
1 2 1
1 3 2
3 4 -1
-1 -4 5 6
'''
from collections import defaultdict

def dfs(cur, par):
    global sub
    sub[cur] = 1
    for i in gr[cur]:
        if i[0] != par:
            dfs(i[0], cur)
            sub[cur] += sub[i[0]]



gr = defaultdict(list)
noe = int(input())
sub = [0] * (noe+10)

for _ in range(noe-1):
    p1, p2, p = [int(x) for x in input().split()]
    gr[p1-1].append((p2-1, p))
    gr[p2-1].append((p1-1, p))
a = [int(x) for x in input().split()]
dfs(0, -1)
for i in range(noe):
    print(sub[i])


