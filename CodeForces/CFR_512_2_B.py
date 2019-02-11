n,d=map(int,input().split())
q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    if(y+x-d>=0 and y+x-2*n+d<=0 and (y-d-x)*(y-x+d)<=0):
        print('YES')
    else:
        print('NO')