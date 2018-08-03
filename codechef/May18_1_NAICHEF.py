'''
2
5 1 1
1 1 1 1 1
2 1 1
1 2
'''
from collections import Counter
for _ in range(int(input())):
    n, a, b = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arrc= Counter(arr)
    ans = (arrc[a] / n) * (arrc[b] / n)
    print(ans)
