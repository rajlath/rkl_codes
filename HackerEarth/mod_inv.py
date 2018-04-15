'''
def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1
a, b = [int(x) for x in input().split()]
print(modInverse(a, b))
'''
import math
print(math.log10(224))

