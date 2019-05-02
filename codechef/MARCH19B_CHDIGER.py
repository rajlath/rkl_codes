
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 08:56:02
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


nb_test = RI()
for _ in range(nb_test):

    N, d = RWI()
    d = int(d)

    N = [int(x) for x in N]
    lens = len(N)
    mins = min(N)
    mins_pos = N.index(mins)
    ans = [min(mins, d)]
    curr_pos = mins_pos + 1
    have_it = False

    while curr_pos < lens:
        curr = N[curr_pos]
        for j in range(curr_pos + 1, lens):
            if curr > N[j]:
                curr = N[j]
                mins_pos = J
                have_it = True
        if have_it:
            curr_pos = mins_pos + 1
            have_it = False
        else:
            curr_pos += 1
        if mins <= d:
            ans.append(mins)
        else:
            break
    ans = ans + (len(N) - len(ans)) * [d]
    print(''.join(map(str, ans)))



