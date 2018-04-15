from operator import mul
from functools import reduce
fib = [1,1]
for i in range(2, 10000):
    fib.append( ( 5 * fib[i-1] + 3 * fib[i - 2]) % 1000)
noe = int(input())
arr = [int(x) for x in input().split()]
pro = 1
for i in arr:
    pro = (pro * i)%600
#k   = reduce(mul, [int(x) for x in input().split()])
print(fib[k])

