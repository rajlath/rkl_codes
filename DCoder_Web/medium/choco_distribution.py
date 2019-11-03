for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    n += 1
    alls, extra = divmod(m, n)
    given = [alls] * n
    for i in range(extra):
        given[i] += 1
    print(*given)