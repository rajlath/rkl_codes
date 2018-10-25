
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 08:00:37
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


nb_friends, nb_bottels, lts_in_bottles, nb_limes,limes_cut, salt_qty, ml_per_toast, gm_salt = read_ints()
can_be = min( nb_bottels*lts_in_bottles // ml_per_toast, nb_limes * limes_cut, salt_qty//gm_salt)
print(can_be // nb_friends)