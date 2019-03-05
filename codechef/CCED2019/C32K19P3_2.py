'''input
The experiment was started by turning the compressor on.

'''
import sys
sys.setrecursionlimit(10**5+1)

import heapq


RI = lambda : [int(x) for x in raw_input().split()]
rw = lambda : raw_input().strip()



s = rw()
C={}

for i in s:
    if i not in C:
        C[i]=0
    C[i]+=1

l = C.keys()
l=sorted(l,key = lambda x:C[x])



H = []

for i in C:
    heapq.heappush(H,(C[i],ord(i),i))

Child = {}
while len(H)>1:
    first = heapq.heappop(H)
    second = heapq.heappop(H)

    fc = first[2]
    sc = second[2]

    Child[fc+sc] = [fc,sc]
    heapq.heappush(H,(first[0]+second[0],first[1]+second[1],first[2]+second[2]))


mx = ''
for i in Child:
    if len(mx) < len(i):
        mx = i

root = mx

Code = {}
def dfs(root,cur=""):
    if len(root)==1:
        Code[root] = cur
    else:
        dfs(Child[root][0],cur+"0")
        dfs(Child[root][1],cur+"1")
dfs(root)


ss = ""
for i in s:
    ss+=Code[i]
print ss



