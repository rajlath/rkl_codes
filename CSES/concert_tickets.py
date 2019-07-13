
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 17:45:47
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


nb_tickets, nb_customer = RMI()
ticket_price = sorted(RMI())
will_pay = RMI()
can_have= 0
i = 0
j = 0








