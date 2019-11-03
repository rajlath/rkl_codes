for _ in range(int(input())):
    c, x = [int(x) for x in input().split()]
    if x == 1:
        print(c)
    else:
        ans = 0
        d, m = divmod(c, x)
        ans += m
        while d:
            d, m = divmod(d, x)
            ans += m
        print(ans)


