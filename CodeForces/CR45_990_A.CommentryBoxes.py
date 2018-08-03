'''
Examples
inputCopy
9 7 3 8
outputCopy
15
inputCopy
2 7 3 7
outputCopy
14
inputCopy
30 6 17 19
outputCopy
0
'''
n, m, make, breaks = [int(x) for x in input().split()]
extra = n % m
require = min((extra * breaks), (m - extra) * make)
print(require)
