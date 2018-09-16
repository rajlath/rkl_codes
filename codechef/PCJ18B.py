for _ in range(int(input())):
    n = int(input())
    if n == 1: print(1)
    else:
        sqr = sum([((n - i) + 1) ** 2 for i in range(3, n, 2)])
        sqr+=  (n ** 2 + (n%2))
        print(sqr)

