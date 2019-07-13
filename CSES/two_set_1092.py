
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 11:29:58
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


n = RI()
sums = (n * (n + 1))// 2
if sums % 2:
    print("NO")
else:
    sums //= 2
    answer = []
    done = 0
    todo = 0
    curr = n
    while True:
        answer.append(curr)
        done += curr
        curr-=1
        todo = sums - done
        if todo < 1:break
        if todo <= curr:
            answer.append(todo)
            break
    print("YES")
    print(len(answer))
    print(*answer)
    print(n - len(answer))
    for j in range(curr, 0, -1):
        if j == todo:continue
        print(j, end= " ")

