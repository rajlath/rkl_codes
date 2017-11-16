#31.35
from math import factorial as fact
from math import floor 
import sys

def combo(n,c):
    return fact(n) / (fact(c) * fact(n - c))

def answer(n):
    return sum(
        (-1) ** k * combo(n, k) * combo(n + floor(9*n/2) - 10*k - 1, n-1)
        for k in range(int(floor((9 * n / 20) + 1)))
    ) 
        
test_cases = open(sys.argv[1], 'r')
for tests in test_cases:
    print answer(int(tests))
