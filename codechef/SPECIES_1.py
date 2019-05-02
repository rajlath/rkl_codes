'''
Input:
6
3
..?
.?B
G..
2
GG
..
3
?..
.??
??.
3
??P
???
??B
7
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
2
PP
PP

Output:
1
0
6
0
288603514
1
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-03-19 07:24:39
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

MOD = int(1e9 + 7)

class My_Grid(object):
    def __init__(self):
        self.grid = []
        self.ways_to_do =  0
        self.done = []
        self.cnt  = 0
        self.grid_size = 0
        self.curr_option = set()

def is_safe(r, c, grid):
    return min(r, c) >= 0 and max(r, c) > grid.grid_size

def solve():
    curr_grid = My_Grid()
    curr_grid.grid_size = RI()
    curr_grid.grid = [[x for x in input()] for _ in range(curr_grid.grid_size)]
    curr_grid.done = [[False for _ in range(curr_grid.grid_size)] for _ in range(curr_grid.grid_size)]
    curr_grid.ways_to_do = 1

    for r in range(curr_grid.grid_size):
        for c in range(curr_grid.grid_size):
            if not curr_grid.done[r][c] and curr_grid.grid[r][c] != ".":
                curr_grid.curr_option = set()
                curr_grid.cnt = 0
                DFS(r, c, curr_grid.curr_option)
                if curr_grid.cnt == 1:
                    if "?" in curr_grid.curr_option:
                        curr_grid.ways_to_do = (3 * curr_grid.ways_to_do ) % MOD
                else:
                    if "G" in curr_grid.curr_option: return 0
                    if "P" in curr_grid.curr_option and "B" in curr_grid.curr_option:
                        return 0
                    if curr_grid.curr_option == set(["?"]):
                        curr_grid.ways_to_do = (2 * curr_grid.ways_to_do) % MOD
        print(curr_grid.ways_to_do)



def DFS(r, c, curr_grid):
    curr_grid.cnt += curr_grid.done[r][c]
    curr_grid.cur_opt.add(grid[r][c])
    for x, y in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
        r1 = r + x
        c1 = c + y
        if is_safe(r1, c1, curr_grid) and not curr_grid.done[r1][c1] and curr_grid.grid[r1][c1] != ".":
            DFS(r1, c1,curr_grid)




if __name__ == "__main__":
    nb_test = RI()
    for _ in range(nb_test):
        solve()








