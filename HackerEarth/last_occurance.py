'''
1
5
2 2 3 3 1
3
2
3
5

for _ in range(int(input())):
    pos_dic = {}
    _ = input()
    arr = input().split()
    for i,v in enumerate(arr):
        pos_dic[v] = pos_dic.get(v, 0)
        pos_dic[v] = i
    print(pos_dic)    
    for i in range(int(input())):
        print(pos_dic.get(input(), -1))
'''
import sys
from collections import defaultdict
t = int(sys.stdin.readline())
while t:
    noe = sys.stdin.readline()
    arr = sys.stdin.readline().strip().split()
    dc  = defaultdict(list)
    indx = 0
    for i, v in enumerate(arr):        
        dc[v].append(i) 
    qry = int(sys.stdin.readline())    
    while qry:
        cur = sys.stdin.readline().strip()
        if cur in dc:
            print(dc[cur][-1] + 1)
        else:
            print(-1)
        qry -= 1
    t -= 1            


