from math import gcd
nb_test = int(input())
for _ in range(nb_test):
    a,b = [int(x) for x in input().split()]
    ans = a + b - gcd(a, b)
    print(ans)
