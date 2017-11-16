import sys
nos = int(input())
arr = [int(x) for x in input().split()]
sums = sum(arr)
maxs = 0
suml = arr[0]
sumr = sums - suml
for i in range(1, nos):
    maxs = max(maxs, (suml + arr[i]) * (sumr - arr[i]))
print(maxs)    
    
