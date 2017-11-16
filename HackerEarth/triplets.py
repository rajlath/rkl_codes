'''
10 5
1 10 4 3 2 5 0 1 9 5
'''

noe, m = [int(x) for x in input().split()]
arr    = [int(x) for x in input().split()]

dp = [0]*m
for i in range(noe):
    dp[arr[i]%m] += 1
    
    
ans = 0
for i in range(m):	
    a1 = dp[i]
    a2 = a1 -1
    a3 = a2 -1
    if a3 <= 0:continue
    if 3 * i % m == 0:
        ans += 1 * a1 * a2 * a3 //6
        
for i in range(m):
    for j in range(i+1,m):
        k = (3 * m - i - j)% m
        if k <= j:continue
        ans += 1 * dp[i]*dp[j]*dp[k]
        
for i in range(m):
    for j in range(m):
        if i == j:continue
        if (2 * i + j)%m == 0:
            ans += 1 * dp[i] * (dp[i] - 1) // 2 * dp[j]          

print(ans)   
  
   
        
     
    
