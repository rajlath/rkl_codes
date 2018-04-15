'''
input
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output
16
'''

minutes, limits = [int(x) for x in input().split()]
theorems = [int(x) for x in input().split()]
behave   = [int(x) for x in input().split()]
max_lecture = sum(x for i, x in enumerate(theorems) if behave[i])
start = 0
tmp   = max_lecture
for x in range(start, minutes-limits+ 1):
    curr = behave[x:x+limits]
    curr_sum = sum([theorems[x] for x in curr if not x ])
    print(curr, curr_sum)


