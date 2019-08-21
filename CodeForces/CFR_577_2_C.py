n, m = [int(x) for x in input().split()]
arrs = sorted([int(x) for x in input().split()])[n//2:]
left = 0
rite = 10 ** 10
while rite - left > 1:
    mid = (left + rite) // 2
    need = 0
    for vals in arrs:
        need += max(0, mid - vals)
    if need > m:
        rite = mid
    else:
        left = mid
print(left)