for _ in range(int(input())):
    N, A, B = [int(x) for x in input().split()]
    A1 = bin(A)[2:].count("1")
    B1 = bin(B)[2:].count("1")
    if (A1 + B1) <= N:
        print(int('1'*(A1+B1)+'0'*(N-A1-B1),base=2))
    else:
        print(int('1'*(N-(A1+B1-N))+'0'*(A1+B1-N),base=2))
