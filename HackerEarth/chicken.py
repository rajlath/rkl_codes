'''
inputCopy
3 2 6
output
6.5
inputCopy
4 2 20
outputv
20.0
'''
from fractions import Fraction
cuts, visit, total_time = [int(x) for x in input().split()]
if cuts % visit == 0:
    ans = float(total_time)
else:
    extra = Fraction(cuts % visit, total_time * 2)
    normal= Fraction(cuts, total_time)
    ans   = 