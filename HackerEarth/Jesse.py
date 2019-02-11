from fractions import gcd
fibo = [0, 1 ,1]
mods = 10 ** 9 + 7
for i in range(3,1000004):
    fibo.append((fibo[-1] % mods + fibo[-2] % mods) % mods)
for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    if m != n and abs(m - n) <= 2:
        print(1)
    else:
        print(fibo[gcd(m, n)])