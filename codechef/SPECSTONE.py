space=int(input())
dist,no=map(int,input().split())
planets=map(int,input().split())
planets=list(planets)
planets.append(dist)
count=0
for a,i in enumerate(planets):
    if space>=i:
        discvr=i
        count=1
    elif (a+1!=no+1) and(discvr+space)>=planets[a+1]:
        continue
    elif (discvr+space)>=i:
        discvr=i
        count+=1
        #print(discvr,count)
print(count)