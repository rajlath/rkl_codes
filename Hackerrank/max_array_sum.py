noe = int(input())
arr = [int(x) for x in input().split()]
inc = 0
exc = 0
tmp = 0
for i in range(noe):
    tmp = inc
    inc = max(arr[i] + exc, tmp)
    exc = tmp
    #print(inc, exc, tmp)
print(max(inc, exc))