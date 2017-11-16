for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    grid = []
    for i in range(n):
        grid.append([x for x in input().split()])
    cnt = 0
    for i in range(n)   :
        for j in range(n):
            if grid[i][j]== "P":                                                       
                for x in range(j+1, j+k+1):                    
                    if x >=n:break                    
                    if grid[i][x] == "T":
                        print(i, x)
                        grid[j][x]="C"
                        cnt += 1
                        break
    print(cnt)                    
                        
