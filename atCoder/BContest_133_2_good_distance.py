N, D = [int(x) for x in input().split()]
grid = []
for _ in range(N):
    grid.append([int(x) for x in input().split()])
count = 0    
for i in range(N - 1):
    for j in range(i+1, N):
        curr_dist = 0
        for k in range(D):
            curr_dist += (grid[i][k] - grid[j][k]) * (grid[i][k] - grid[j][k])
        for k in range(128):
            if curr_dist == (k * k):
                count += 1
                break
print(count)            
            
            