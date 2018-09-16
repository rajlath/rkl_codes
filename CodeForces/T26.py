'''
7
4
1 3
2 5
1 2
5 6
4
1
7
4
2
'''
from collections import OrderedDict
noc = int(input())
nod = int(input())
cnt = OrderedDict()
cnts= {i:0 for i in range(100005)}

for i in range(nod):
    lc, rc = [int(x)-1 for x in input().split()]
    print(lc, rc)
    for i in range(lc, rc+1):
        cnts[i] += 1
noq = int(input())
for i in range(noq):
    print(cnts[int(input())])




