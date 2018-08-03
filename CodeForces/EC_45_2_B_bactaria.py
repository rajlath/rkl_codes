R=lambda:map(int,input().split())
n,m=R()
c={}
for x in R():
    c[x]=c.get(x,0)+1
a=0
b=sorted(c)[::-1]
while b:
    x=b.pop()

    if not b or b[-1]>x+m:
        print(x)
        a+=c[x]

print(a)