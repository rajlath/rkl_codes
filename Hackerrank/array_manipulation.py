def find_max(n, m, a, b, k):
    arr = [0] * (n+1)
    for i in range(m):
        lowerbound = a[i]
        upperbound = b[i]
        arr[lowerbound-1] += k[i]
        arr[upperbound-1] -= k[i]

    print(arr)
    sums = 0
    res  = -10e9
    for i in range(n):
        sums += arr[i]
        res  =  max(res, sums)

    return res

n, m = [int(x) for x in input().split()]

arr = [0] * n
for i in range(m):
    x, y, z = [int(x) for x in input().split()]
    arr[x-1] += z
    if y < len(arr):
        arr[y-1] -= z

maxs = -10e12
sums = 0
for i in arr:
    sums += i
    maxs = max(maxs, sums)
print(maxs)




