f=lambda:map(int,input().split())
n,p,q,r=f()
a=b=c=-10**19
d=list(f())
for i in range(n):
    a=max(a,d[i]*p)
    b=max(b,a+d[i]*q)
    c=max(c,b+d[i]*r)
    print(a, b, c)
print(c)
