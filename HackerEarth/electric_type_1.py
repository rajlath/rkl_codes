'''
5
1 2 2 1 3
'''
from collections import defaultdict

noe = int(input())
arr = [int(x) for x  in input().split()]
cnt = {}
unique = [0] * noe

for i in range(noe-2, -1, -1):
    curr = arr[i+1]
    if  curr in cnt:
        unique[i] = unique[i+1]
    else:
        unique[i] = unique[i+1] + 1
        cnt[curr] = True
visited = {}
ans = 0
for i in range(noe):
    curr = arr[i]
    if curr not in visited:
        ans += unique[i] 
        visited[curr] = True
print(ans)               
        

            
        
        

