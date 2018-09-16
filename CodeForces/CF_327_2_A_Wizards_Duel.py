
# -*- coding: utf-8 -*-
#! @Date    : 2018-09-05 13:15:44
#! @Author  : raj lath (oorja.halt@gmail.com)
#! @Link    : "https://codeforces.com/contest/591/problem/A"
#! @Version : 1.0.0

import os
from sys import stdin

max_val=int( 10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

def main():
    distance = read_int()
    harry    = read_int()
    wmnb     = read_int()
    print( "{0:.4f}".format(distance * (harry / (harry + wmnb))))

if __name__ == "__main__":
    main()

