for _ in range(int(input())):
    G, D, M, F = [int(x) for x in input().split()]
    ans = min([G, D, F])
    sums = sum([G, D, M, F])
    if ans * 4 <= sums:
        print(ans)
    else:
        while ans * 4 > sums:
            ans -= 1
        print(ans)