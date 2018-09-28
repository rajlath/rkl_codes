
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 20:22:55
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

'''
1
5 2 10
1 1 1 1 1
1 2 3 2 1
'''

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = read_int()
for _ in range(nb_test):
    days, monitor, anger = read_ints()
    jack = read_ints()
    jill = read_ints()
    day_anger = [a + b for a, b in zip(jack, jill)]
    ans = "yes"
    left = 0
    rite = left + monitor
    while rite <= days-1:
        #print(left, rite)
        curr = sum(day_anger[left:rite])
        if curr >= anger:
            ans = "no"
            break
        else:
            left += 1
            rite += 1
            if rite >= days:break
            curr -= day_anger[left]
            curr += day_anger[rite]
    print(ans)


