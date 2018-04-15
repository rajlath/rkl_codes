n,m,nq=[int(i) for i in input().split()]
arr=[]
for i in range(n):
    arr.append([x for x in input()])

distances=[[0 for i in range(m)] for j in range(n)]
sx, sy = [int(x) for x in input().split()]
distances[sx][sy]=0
vis={}
q=[(sx,sy)]
while len(q)!=0:
    curr=q[0]
    rem=q.pop(0)
    vis[curr]=True
    r=curr[0]
    c=curr[1]

    if r-1>=0 and arr[r-1][c]=="O":
        if vis.get((r-1,c),-1)==-1 or vis[(r-1,c)]!=True:
            q.append((r-1,c))
            distances[r-1][c]=distances[r][c]+1
    if r+1<n and arr[r+1][c]=="O":
        if vis.get((r+1,c),-1)==-1 or vis[(r+1,c)]!=True:
            q.append((r+1,c))
            distances[r+1][c]=distances[r][c]+1
    if c-1>=0 and arr[r][c-1]=="O":
        if vis.get((r,c-1),-1)==-1 or vis[(r,c-1)]!=True:
            q.append((r,c-1))
            distances[r][c-1]=distances[r][c]+1
    if c+1<m and arr[r][c+1]=="O":
        if vis.get((r,c+1),-1)==-1 or vis[(r,c+1)]!=True:
            q.append((r,c+1))
            distances[r][c+1]=distances[r][c]+1
    #for i in x:
        #print(i)
#print(distances)
for _ in range(nq):
    a, b = [int(x) for x in input().split()]
    print(distances[a-1][b-1])