
'''
5 2
1 1 2 1 2
1 2
1 3
2 4
2 5
'''

from sys import setrecursionlimit
from collections import defaultdict

 
setrecursionlimit(1000000)
 
n, k = map(int, raw_input().strip().split())
color = [0] + map(int, raw_input().strip().split())
data, vis = defaultdict(list), [False]*(n+1)
 
for N in xrange(n-1):
    u, v = map(int, raw_input().strip().split())
    data[u].append(v)
    data[v].append(u)
s, ans = defaultdict(list), [-1]*(n+1)


 
def dfs(x):
    vis[x] = True
    s[color[x]].append(x)
    print(s, data[x], vis)
    for i in data[x]:
        if not vis[i]:
            if len(s[color[i]]) >= k:
                ans[i] = s[color[i]][len(s[color[i]])-k]
            dfs(i)
    s[color[x]].pop()
    
 
dfs(1)
 
for i in xrange(1, n+1): print ans[i],
