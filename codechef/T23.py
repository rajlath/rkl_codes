from math import gcd
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    div = 0
    for i in arr:
        div = gcd(div, i)
    print(("NO", "YES")[div == 1])

