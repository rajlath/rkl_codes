from math import gcd
n = int(input())
for i in range(n - 1):
    if gcd(n, i) == 1:
        a = i
print(a)        
