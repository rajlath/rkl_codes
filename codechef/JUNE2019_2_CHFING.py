mods  = 1000000007
nb_Test = int(input())
for _ in range(nb_Test):
    N, K = [int(x) for x in input().split()]
    d = N - 1
    a = K - 1
    if d > a:print(a%mods)
    else:
        n = a // d
        n += (a % d) > 0
        ans = (n * (2 * a - (n - 1) * d )) // 2
        print(ans % mods)
