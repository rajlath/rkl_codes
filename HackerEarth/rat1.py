'''
3 3 2
O*O
OOO
*OO
2 2
1 1
1 2
'''
def printSolution( sol ):

    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def isSafe( maze, x, y ):
    if x >= 0 and x < maze[0] and y >= 0 and y < maze[0] and maze[x][y] == 1:
        return True
    return False

def solveMaze( maze, x, y ):
    sol = [ [ 0 for j in range(4) ] for i in range(4) ]
    if solveMazeUtil(maze, x, y, sol) == False:
        print("Solution doesn't exist");
        return False
    printSolution(sol)
    return True

def solveMazeUtil(maze, x, y, sol,n,m):

    if x ==  - 1 and y == N - 1:
        sol[x][y] = 1
        return True


    if isSafe(maze, x, y) == True:
        sol[x][y] = 1


        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True
        if solveMazeUtil(maze, x-1, y, sol) == True:
            return True
        if solveMazeUtil(maze, x, y - 1, sol) == True:
            return True

        sol[x][y] = 0
        return False

n, m, q = [int(x) for x in input().split()]
maze = []
for i in range(n):
    maze.append([x for x in input().split()])
for _ in range(q):
    x, y = [int(x) for x in input().split()]
    print(solveMaze(maze, x, y))


