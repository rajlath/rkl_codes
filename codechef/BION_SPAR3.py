
# -*- coding: utf-8 -*-
# @Date    : 2019-03-17 21:39:40
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
R = 0
C = 0
def isValid(x,y1,y2):
    return ((x >= 0 and x < R and y1 >=0
        and y1 < C and y2 >=0 and y2 < C))

def get_max_util(arr,mem, x, y1, y2):
    if not isValid(x, y1, y2):return min_val
    if x == R - 1 and y1 == 0 and y2 == C - 1:
        if y1 == y2:return arr[x][y1]
        else:
            arr[x][y1] + arr[x][y2]
    if x == R - 1: return min_val
    if mem[x][y1] != -1:return mem[x][y1][y2]



def getMax(arr):
    mem = mem=[[[-1 for i in range(C)] for i in range(C)] for i in range(R)]
    return getMaxUtil(arr, mem, 0, 0, C-1)

nb_test = RI()
for _ in range(nb_test):
    R, C = RMI()




