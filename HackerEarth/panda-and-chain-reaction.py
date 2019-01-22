mod = int(10 ** 6 + 3)
nb_test = int(input())
for _ in range(nb_test):
    n, x    = [int(x) for x in input().split()]
    has = x
    for i in range(n):
        has += (has * i)%mod
    print(has)