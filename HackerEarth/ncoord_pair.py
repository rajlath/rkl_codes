#copied
def f(a,b):
    t=a[0][0]-b[0][0]
    if t!=0:
        return t
    t=a[0][1]-b[0][1]
    if t!=0:
        return t
    return a[1]-b[1]
d={}
for _ in xrange(input()):
    x,y=map(int,raw_input().split())
    try:
        d[(x,y)]+=1
    except KeyError:
        d[(x,y)]=1
z=[]
for i in d:
    z.append([i,d[i]])
z.sort(cmp=f)
for i in z:
    print i[0][0],i[0][1],i[1]
    
n = input()
a = sorted([map(int, raw_input().split()) for _ in xrange(n)])
i = 0
while i < n:
    p = a[i]
    k = 0
    while i < n and p == a[i]:
        k += 1
        i += 1
    print p[0], p[1], k    
