'''
5 4 4
i loser am the second
100 1 1 5 10
1 1
1 3
2 2 5
1 4
i am the second
'''
from collections import defaultdict
no_of_word, no_of_group, word_cnt_msg = [int(x) for x in input().split()]
words = [x for x in input().split()]
costs = [int(x) for x in input().split()]
groups = defaultdict(list)
for i in range(no_of_group):
    grp_cnt, *grp = [int(x) for x in input().split()]
    if len(grp)==1:
        grp_min = costs[grp[0]-1]
    else:
        grp_min = min([costs[x-1] for x in grp])
        for i in range(len(grp)):
            costs[grp[i]-1] =grp_min

print(sum([costs[words.index(x)] for x in input().split()]))

'''
n, k, m = map(int, input().split())
w = list(input().split())

lk = {}
for i in range(n):
    lk[w[i]] = i

c = list(map(int, input().split()))

m = [10**19] * k
gr = [0] * n

for i in range(k):
    g = list(map(int, input().split()))
    for j in g[1:]:
        m[i] = min(m[i], c[j - 1])
        gr[j - 1] = i

let = input().split()
res = 0
for word in let:
    res += m[gr[lk[word]]]

print(res)
'''












