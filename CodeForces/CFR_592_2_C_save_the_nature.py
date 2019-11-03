def calc(arr, lens, x, a, y, b):
    ans = 0
    cx, cy, cxy = 0, 0, 0
    for i in range(1, lens + 1):
        cxy += i % a == 0 and i % b == 0
        cx  += i % a == 0
        cy  += i % b == 0
    for i in range(cxy):
        ans += arr[i] * (x + y)
    for i in range(cx ):
        ans += arr[cxy + i] * x
    for i in range(cy ):
        ans += arr[cxy + cx + i] * y
    return ans

q = int(input())
for _ in range(q):
    lens = int(input())
    arrs = sorted([int(x)//100 for x in input().split()], reverse=True)
    print(arrs)
    x, a = [int(x) for x in input().split()]
    y, b = [int(x) for x in input().split()]
    k = int(input())

    if x < y:
        (x, a) , (y, b)  = (y, b), (x, a)
    print(x, a, y, b, k)
    left = 0
    rite = lens
    while rite - left > 1:
        mid = (left + rite    ) // 2
        if calc(arrs,mid, x, a, y, b) >= k:
            rite = mid
        else:
            left = mid
    print([rite, -1][rite > lens])


