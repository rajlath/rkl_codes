for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    ans = n
    s = 0
    k = sum(a)
    for i in range(n):
        s += a[i]
        if i - k >= 0:
            s -= a[i - k]
        ans = min(ans, k - s)
    s = 0
    k = n - k
    for i in range(n):
        s += 1 - a[i]
        if i - k >= 0:
            s -= 1 - a[i - k]
        ans = min(ans, k - s)
    print(ans)

