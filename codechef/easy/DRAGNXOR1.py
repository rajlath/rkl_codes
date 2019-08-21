def cnt(a):
    c = 0
    while a:
        c += a & 1
        a >>= 1
    return c

for _ in range(int(input())):
    n, a, b = [int(x) for x in input().split()]
    print(bin(a), bin(b))
    a, b = cnt(a), cnt(b)
    print(a, b)
    if (a + b) <= n:
        print(int('1'*(a+b)+'0'*(n-a-b),base=2))
    else:
        print(int('1'*(n-(a+b-n))+'0'*(a+b-n),base=2))
