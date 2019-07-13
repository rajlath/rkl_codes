import bisect
input()
t=[]
for i in map(int,input().split()):
    p=bisect.bisect(t,i)
    print(p)
    if p==len(t):t+=i,
    t[p]=i
    print(t)

print(len(t))