from bisect import bisect_left as bl
from bisect import bisect_right as br

for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    lhs, rhs = [], []
    low, hi = 0, 0

    for i in range(n):
        for j in range(n):
            lhs.append(a[i] ** 2 + a[j])
            rhs.append(a[i] ** 2 + a[j] ** 2)

    lhs.sort()
    rhs.sort()

    ans = 0

    for i in range(len(lhs)):

        low = bl(rhs, lhs[i])
        hi = br(rhs, lhs[i])
##        print(lhs[i], low, hi)

        ans += (hi - low)

    print(ans)