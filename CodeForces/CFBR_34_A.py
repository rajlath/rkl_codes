n=int(input())
a=list(map(int,input().split()))
x,y,h=-1,-1,1001
for i in range(n):
    k=abs(a[i]-a[(i+1)%n])
    if k<h:
        h=k
        x=i
        y=(i+1)%n
print("{} {}" .format(x+1,y+1))