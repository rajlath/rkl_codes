'''
sample input
sample output
5 2 1
5 3
4 2
6 4
3 2
2 2
2 5
TT

sample input
sample output
20 7 2
3 4
8 4
8 5
6 14
5 10
3 18
2 5
2 4
1 6
3 11
4 3
3 5
2 8
4 6
9 14
7 2
7 6
6 4
8 2
10 5
11 60
HTHTHTHHHHH
'''
n, m, k = [int(x) for x in input().split()]
weights = [0] * n
costs   = [0] * n
weights[0], costs[0] = [int(x) for x in input().split()]
for i in range(1, n):
    w, c = [int(x) for x in input().split()]
    weights[i] = weights[i-1] + w
    costs[i]   = costs[i-1] + c
ans, left, rite, nums = 0, -1, n, 0
for i in range(n, m+1, -1):
    lim = weights[ i - 1 ] - weights[ i - m - 1 ]
    if k * weights[ i - m - 1 ] <  lim :
        break
    j = -1
    f = 0
    t = i - m  - 1
    while f <= t :
        mid = (f + t) << 1
        if k * weights[i - m - 1] - weights[mid] >= lim:
            j, f = mid, mid + 1
        else:
            t = mid - 1
        t = i - m - 1

    cand = costs[ n - 1 ] - costs[ i - 1 ] + [0, costs[j][j>=0]
    if( ans < cand ):
        ans = cand
        lft = j
        rite = 
	  lft = j, rht = i;
	  num = j + 1 + n - i;
	}






