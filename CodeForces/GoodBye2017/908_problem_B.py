'''
B. New Year and Buggy Bot

time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

Bob programmed a robot to navigate through a 2d maze.
The maze has some obstacles. Empty cells are denoted by the character '.', where obstacles are denoted by '#'.
There is a single robot in the maze. It's start position is denoted with the character 'S'.
This position has no obstacle in it. There is also a single exit in the maze. It's position is denoted with the
character 'E'. This position has no obstacle in it.
The robot can only move up, left, right, or down.

When Bob programmed the robot, he wrote down a string of digits consisting of the digits 0 to 3, inclusive.
He intended for each digit to correspond to a distinct direction, and the robot would follow the directions in order
to reach the exit. Unfortunately, he forgot to actually assign the directions to digits.
The robot will choose some random mapping of digits to distinct directions.
The robot will map distinct digits to distinct directions.
The robot will then follow the instructions according to the given string in order and chosen mapping.
If an instruction would lead the robot to go off the edge of the maze or hit an obstacle, the robot will crash and break
down. If the robot reaches the exit at any point, then the robot will stop following any further instructions.
Bob is having trouble debugging his robot, so he would like to determine the number of mappings of digits to directions
that would lead the robot to the exit.

Input
The first line of input will contain two integers n and m (2 ≤ n, m ≤ 50), denoting the dimensions of the maze.
The next n lines will contain exactly m characters each, denoting the maze.
Each character of the maze will be '.', '#', 'S', or 'E'.
There will be exactly one 'S' and exactly one 'E' in the maze.
The last line will contain a single string s (1 ≤ |s| ≤ 100) — the instructions given to the robot.
Each character of s is a digit from 0 to 3.

Output
Print a single integer, the number of mappings of digits to directions that will lead the robot to the exit.

Examples
input
5 6
.....#
S....#
.#....
.#....
...E..
333300012
output
1
input
6 6
......
......
..SE..
......
......
......
01232123212302123021
output
14
input
5 3
...
.S.
###
.E.
...
3
output
0
Note
For the first sample, the only valid mapping is , where D is down, L is left, U is up, R is right.
'''
from itertools import permutations
rows, cols = [int(x) for x in input().split()]
grid = [input() for _ in range(rows)]
route= input()
directions = [[0, 1],[-1, 0],[0, -1],[1, 0]]
begin_exit = [[-1, -1],[-1, -1]]

#get start and exit
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            begin_exit[0][0] = i
            begin_exit[0][1] = j
        elif grid[i][j] == "E":
            begin_exit[1][0] = i
            begin_exit[1][1] = j

ans = 0

for d in permutations(directions):
    x, y = begin_exit[0][0], begin_exit[0][1]
    for r in route:
        dr = d[int(r)]
        x += dr[0]
        y += dr[1]
        if x == begin_exit[1][0] and y ==  begin_exit[1][1]:
            ans += 1
            break
        if not 0 <= x < rows or not 0 <= y < cols or grid[x][y] == "#":
           break

print(ans)











