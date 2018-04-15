from collections import deque

surround = [(-2, -1, "UL"), (-2, 1, "UR"), (0, 2, "R"), (2, 1, "LR"), (2, -1, "LL"), (0, -2, "L")]

def printShortestPath(n, i_start, j_start, i_end, j_end):
    limit = range(0,n)
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    path = [[[] for _ in range(n)] for _ in range(n)]
    q = deque([(i_start, j_start)])
    dist[i_start][j_start] = 0
    while len(q) > 0:
        i, j = q.popleft()
        if i == i_end and j == j_end:
            print(dist[i][j])
            print(*path[i][j])
            return
        for dx, dy, name in surround:
            if i+dx in limit and j+dy in limit and dist[i+dx][j+dy] == -1:
                q.append((i + dx, j + dy))
                dist[i + dx][j + dy] = dist[i][j] + 1
                path[i + dx][j + dy] = path[i][j] + [name]
    print("Impossible")


if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = [int(x) for x in input().split()]
    printShortestPath(n, i_start, j_start, i_end, j_end)

'''
LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LL LL LL LL LL LL LL LL LL LL LL LL
LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LR LL LL LL LL LL LL LL LL LL LL LL LL
'''