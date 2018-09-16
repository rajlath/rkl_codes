import math
def prime_factors(n):
    f = []
    while n%2==0:
        f.append(2)
        n//=2
    for i in range(3, int(math.sqrt(n))+1, 2)    :
        while n%i==0:
            f.append(i)
            n//=i
    if n > 2:f.append(n)
    return f

#print(prime_factors(9013456))
from collections import defaultdict
for i in range(int(input())):
    noe = int(input())
    dic = defaultdict(list)
    fac = {int(x):prime_factors(int(x)) for x in input().split()}
vals = sorted(fac.keys(), reverse=True)

for _ in range(int(input())):
    a, b , k = [int(x) for x in input().split()]
    af = prime_factors(a)
    bf = prime_factors(b)

    pa, pb = 0, 0
    for i in vals:
        if fac[i][k-1] == af[k-1] :pa = i
        if fac[i][k-1] == bf[k-1] :pb = i
    print(["Alice", "Bob"][pa < pb])





