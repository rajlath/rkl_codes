def solve(ar,sums, k1):
    csum = 0
    i = 1
    for x in ar:
        if x > sums:return False
        if csum + x > sums:
            csum = x
            i += 1
        else:
            csum += x
    return i <= x


n, k = [int(x) for x in input().split()]
arrs = [int(x) for x in input().split()]
arsum = sum(arrs)
l = 0
i = arsum // 2
while i >= 1:
    while l + i < arsum and not solve(arrs, l + i, k):
        l += i
    i //= 2
print(l + 1)
