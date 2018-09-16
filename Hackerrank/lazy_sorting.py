from math import factorial
from collections import Counter
#check whether arr is sorted or not
#if all(x<=y for x,y in zip(A,A[1:])): return True
noe = int(input())
arr = [int(x) for x in input().split()]
arrc= Counter(arr)
ans = factorial(noe)
if arr == sorted(arr):
    print(0)
elif len(arrc) == 1:
        print(0)
else:
    for v in arrc.values():
        ans /= factorial(v)
    print("{:6f}".format(ans))




