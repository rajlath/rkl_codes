
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:29:00
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
from itertools import accumulate
day = ["NONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
nb_test = int(input())
for _ in range(nb_test):
    nb_topic = int(input())
    days = list(accumulate([int(x) for x in input().split()]))
    i = 0
    while nb_topic > 0:
        i = 0
        for d in days:
            nb_topic -= d
            if nb_topic <= 0:
                print(day[i])
                break
            i +=1





