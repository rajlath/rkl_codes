'''
input
5
100 98 100 100
100 100 100 100
100 100 99 99
90 99 90 100
100 98 60 99
output
2
'''
from collections import defaultdict
n = int(input())
ranks_dict = defaultdict(list)
for i in range(n):
    ranks_dict[sum(int(x) for x in input().split())].append(i+1)
ranks_score = sorted(ranks_dict, reverse=True)
#print(ranks_score)
rank = 0
for i in ranks_score:
    if 1 in sorted(ranks_dict[i]):
        print(rank+1)
        break
    else:rank += len(ranks_dict[i])



