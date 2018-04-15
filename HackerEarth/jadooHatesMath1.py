n,r,i=100000,range,input
p=[0]*n
for i in r(n):
    for j in r(i*i,n):
        p[j]+=1
for _ in r(int(input())):
    x=int(input())
    while True:
        if not p[x]:
            print(x)
            break
        x+=1


