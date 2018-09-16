def count_inversions(a):
    res = 0
    counts = [0]*(len(a)+1)
    rank = { v : i+1 for i, v in enumerate(sorted(a)) }
    for x in reversed(a):
        i = rank[x] - 1
        while i:
            res += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(a):
            counts[i] += 1
            i += i & -i
    return res
from sys import stdin
nots = int(stdin.readline().strip())
for _ in xrange(nots):
    lens = int(stdin.readline().strip())
    arrA = [int(x) for x in stdin.readline().split()]
    arrB = sorted(arrA)
    arrC = [0]*lens
    #print(arrB, arrA)
    for i in xrange(lens):
        B = arrB[i]
        #print(B)
        arrC[i] = B * abs(arrA.index(B) - i)
        #print(arrC[i])
    print(count_inversions(arrC))

