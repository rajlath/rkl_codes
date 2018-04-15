from collections import defaultdict as df
import heapq
import sys
sys.setrecursionlimit(1000000)

n,m=[int(x) for x in raw_input().split()]
C=df(list)
for i in range(m):
    a,b=[int(x) for x in raw_input().split()]
    C[a].append(b)
    C[b].append(a)

print(C)
U,V=[int(x) for x in raw_input().split()]
H=[0]*(n+1)
v=[0]*n
H=[0]*n


def bfs(root):
    q=[root]
    v[root]=1
    while len(q)>0:
        node=q[0]
        for i in C[node]:
            if v[i]==0:
                v[i]=1
                H[i]=H[node]+1
                q.append(i)
        q.pop(0)
bfs(U)

H1=H[:]
H=[0]*(n+1)
v=[0]*n
bfs(V)



H2=H[:]
print H1,H2
for _ in range(input()):
    a=input()
    if H1[a]+H2[a]==H1[V]:
        print "YES"
    else:
        print "NO"