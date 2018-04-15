'''
Sample Input:
3
4 1
2 3 4 4
5 3
9 9 1 1 9
2 1
2 2
Sample Output:
5
9
-1
'''
from collections import Counter
for _ in range(int(input())):
    noe, repeat = [int(x) for x in input().split()]
    arr = Counter([int(x) for x in input().split()])
    cnt = 0
    sums = 0
    for k in arr:
        if arr[k]==repeat:
            sums += k
            cnt += 1
    print(sums if cnt>0 else -1)
