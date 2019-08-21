t=int(input())
for _ in range(t):
    n=int(input())
    south=[-1]*n
    east=[-1]*n
    grid=[[0]*n for i in range(n)]
    for row in range(n):
        s=input()
        e=-1
        for column in range(n):
            if s[column]=="#":
                if row>south[column]:
                    south[column]=row
                e=column
                grid[row][column]=1
        east[row]=e
    tot=0
    for row in range(n):
        for col in range(n):
            if row>south[col] and col>east[row]:
                tot+=1
    print(tot)