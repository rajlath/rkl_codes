'''
6
10
10
10
01
10
10
'''

from itertools import groupby
alls = []
for _ in range(int(input())):
    alls.append(input())
cnt = 0    
for k in groupby(alls):
    cnt += 1
print(cnt)       
