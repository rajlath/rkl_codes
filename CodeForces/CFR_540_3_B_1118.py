n = int(input())
a = [int(x) for x in input().split()] 
odd_even = [0, 0]
ans = 0
for k, v in enumerate(a):
    odd_even[k%2] += v
odd_even[0] -= a[0]    
ans += odd_even[0] == odd_even[1]
for i in range(1, n):
    odd_even[i%2] -= a[i]
    odd_even[i%2] += a[i-1] 
    ans += odd_even[0] == odd_even[1]
print(ans)    


