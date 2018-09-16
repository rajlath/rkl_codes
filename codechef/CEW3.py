for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    mn   = m + n
    ans  = "1.000000"
    if m == 1 and n == 1 or m ==1 and n == 0 or mn in (0, 1):
        ans = "0.000000"
    print(ans)