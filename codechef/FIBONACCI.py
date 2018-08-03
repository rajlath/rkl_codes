a,b=map(int,input().split())
x,y=0,1
for i in range(b-2):
    t=x+y;x,y=y,t
c=y//a*a
d=c+a
print([c,d][y>(c+d)//2])