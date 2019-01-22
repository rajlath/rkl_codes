N,M =[int(n) for n in input().split()]
A=[int(n) for n in input().split()]
B=[int(n) for n in input().split()]
pair=[]
maxi=max(B)
mini=min(A)
i=A.index(mini)
j=B.index(maxi)
for y in range(M):
    pair.append((i,y))
for y in range(N):
    if y!=i:
        pair.append((y,j))
for i in pair:
    print("%d %d"%(i[0],i[1]))