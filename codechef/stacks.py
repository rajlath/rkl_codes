
# cook your dish here
'''
def binarysearch(a, size, n):
    low, high = 0, size-1
    ans = size
    while low <= high:
        mid = (low+high)//2
        if a[mid] > n:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans


tcase = int(input())
while tcase > 0:
    tcase -= 1
    n = int(input())
    l = list(map(int, input().split()))
    result = sorted(l[:])
    size = 0
    for i in range(n):
        k = binarysearch(result, size, l[i])
        result[k] = l[i]
        if k == size:
            size += 1
    print(size, end=" ")
    for i in range(size):
        print(result[
'''
from bisect import bisect_left
for _ in range(int(input())):
    lens = int(input())
    arrs = [int(x) for x in input().split()]
    rets = []
    for i in arrs:
        pos = bisect_left(rets, i + 1)
        if pos == len(rets):
            rets.append(i)
        else:
            rets[pos] = i
    rets = [len(rets)] + rets
    print(*rets)




'''

        from bisect import bisect_left
for i in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = []
    for j in ar:
        k = bisect_left(ans, j+1)
        if k == len(ans):
            ans.append(j)
        else:
            ans[k] = j

    print(len(ans), *ans)i], end=" ")
    print()
'''
