'''
inputCopy
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output
16
'''

minutes, k = [int(x) for x in input().split()]
Nos_lect   = [int(x) for x in input().split()]
behaviou   = [int(x) for x in input().split()]

maxs = int(-10e12)
lect = 0
noksum = sum([x for i, x in enumerate(Nos_lect) if behaviou[i]==1])





