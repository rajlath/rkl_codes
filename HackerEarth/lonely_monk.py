odd_even = [1,0]
n =int(input())
p = [0] * (n+10)
ans = 0
arr = [int(x) for x in input().split()]
x = 1
for i in arr:
    p[x] = p[x-1] + i    
    p[x] %= 2
    ans += odd_even[p[x]]
    odd_even[p[x]] += 1
    x+=1
    
print(ans)    
