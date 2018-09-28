
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 09:24:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

'''
2
5 10
3 5 3 2 1
4 6
10 8 6 4
'''
nb_test = read_int()
for _ in range(nb_test):
    nb_people, have_amt = read_ints()
    need_amt = read_ints()
    answer = ''
    for i in range(nb_people):
        result = have_amt >=need_amt[i]
        if result:
            have_amt -= need_amt[i]
            answer += "1"
        else:answer += "0"

    print(answer)
