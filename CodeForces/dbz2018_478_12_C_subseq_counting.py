n,d=map(int,raw_input().split())
x=1
v=[]
for b in range(60):
    if (1<<b)&n:
        v+=[x]*b
        x+=d
        v+=x,
        x+=d
if not v:
    v+=[1]
print len(v)
print ' '.join(map(str,v))
