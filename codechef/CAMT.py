
from collections import defaultdict
notr, noed = [int(x) for x in input().split()]
d = defaultdict(list)
for _ in range(noed):
    x, y = [int(x) for x in input().split()]
    d[x].append(y)
for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    c = 1
    def count_bad(a, d):
        global c
        if a in d:
            for branch in d[a]:
                c += 1
                count_bad(branch, d)
        return c

    print(count_bad(y, d))


'''
def func(d,a):
    global c
    if a in d.keys():
        for element in d[a]:
            c=c+1
            func(d,element)

c=1
n,m=map(int,input().split())
d={}
for i in range (m):
    a,b=map(int,input().split())
    if a in d.keys():
        d[a].append(b)
    else:
        d[a]=[]
        d[a].append(b)
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    c=1
    func(d,y)
    print (c)
'''



