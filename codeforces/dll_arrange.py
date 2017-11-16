n=int(input())
l=[[]]
for i in range(n):
    l.append([int(j) for j in input().split()])
p=-1
for i in range(1,n+1):
    if l[i][0]==0:
        k=i
        while l[k][1]!=0:
            k=l[k][1]
        if p!=-1:
            l[i][0]=p
            l[p][1]=i
        p=k
for i in range(1,n+1):
    print (l[i][0],l[i][1])
