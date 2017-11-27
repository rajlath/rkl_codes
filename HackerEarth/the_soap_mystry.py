noe = int(input())
prices = [int(x) for x  in input().split()]
prices = sorted(prices)
for _ in range(int(input())):
    mins = prices[0]
    maxs = prices[-1]
    pc = int(input())
    l, r = 0, noe-1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if prices[mid] < pc:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    if ans == -1:print(0)
    else:print(ans+1)
