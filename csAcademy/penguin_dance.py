n, p, t = [int(x) for x in input().split()]
dance   = [0,0,0,0,1,-1,1,1,1]
a = 0
m   = 0
ans = -1
for i in range(t+1):
   a += dance[m]
   m = (m+1)%9
if p < a or p > a + n:
    print(-1)
else:
    print(p-a+1)

import heapq

