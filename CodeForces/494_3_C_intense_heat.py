from itertools import accumulate
n, k = [int(x) for x in input().split()]
arr  = [0] + [int(x) for x in input().split()]

asu   = list(accumulate(arr))
print(asu)
maxs  = -10e8
for i in range(k, n+1):
    for j in range(k, n+1):
        avg = (asu[j] - asu[j-i])/i
        maxs = max(maxs, avg)
print(maxs)


