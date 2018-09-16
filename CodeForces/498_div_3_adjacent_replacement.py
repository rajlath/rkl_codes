noe = int(input())
arr = [int(x) for x in input().split()]
for i, v in enumerate(arr):
    if v%2==0:arr[i]-=1
print(*arr)