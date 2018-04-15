
from collections import Counter
noe = int(input())
arr = [1 if int(x)%2 else -1 for x in input().split()]
pre=0
ans=0
M = {0:1}
for i in range(noe):
    pre += arr[i]
    if pre in M and M[pre]>0:
        ans += M[pre]
    M[pre] = M.get(pre, 0)+1
print(ans)




