import bisect
from itertools import accumulate
n,q=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a=list(accumulate(a))
s=0
b = [int(x) for x in input().split()]
for x in b:
    s+=x
    if s>=a[-1]:
        print (n)
        s=0
    else:
        print (n-bisect.bisect(a,s))