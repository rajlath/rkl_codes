
# -*- coding: utf-8 -*-
# @Date    : 2018-10-19 07:22:47
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


masha_floor, egor_floor, curr_floor, stair_time, elev_time, door_time = read_ints()
time_for_stair =  abs(masha_floor - egor_floor) * stair_time
time_for_elev  =  abs(curr_floor - masha_floor) * elev_time
time_for_elev +=  abs(masha_floor - egor_floor) * elev_time + 3 * door_time
print(["Yes", "No"][time_for_elev > time_for_stair])