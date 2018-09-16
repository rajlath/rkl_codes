for _ in range(int(input())):
    days = 0
    D,A, M, B, X = [int(x) for x in input().split()]
    months = 0
    X -= D
    m, d = divmod(X, ((A*M) +B))
    #print(m, d)
    months += m * (M + 1)
    X -= m * (A * M + B)
    m, d = divmod(X, A)
    months += m + (d > 0)
    print(months)






