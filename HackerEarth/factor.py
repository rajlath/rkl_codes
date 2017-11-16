from math import sqrt
from functools import reduce
def factors_2(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
                
print(factors_2(12345678))                
