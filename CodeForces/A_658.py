R=lambda:map(int,raw_input().split())
n,c=R()
def s(u,v):
    x,y=0,0
    for i in range(n):
        y+=v[i]
        x+=max(0,u[i]-y*c)
    return x
p=R()
t=R()
a,b=s(p,t),s(p[::-1],t[::-1])
print 'Limak' if a>b else 'Radewoosh' if a<b else 'Tie'