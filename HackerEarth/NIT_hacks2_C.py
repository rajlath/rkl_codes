
# -*- coding: utf-8 -*-
# @Date    : 2018-10-18 18:53:31
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

mods = int(1e9)+7
nums = [1, 1]
nb_test = read_int()
for i in range(nb_test):
    n = read_int() % mods
    print(n)
    if n < len(nums):
        print("Case {}: {}".format(i+1, nums[i]))
    else:
        lens = len(nums)
        for x in range(lens-1, n):
            curr = ((2 * nums[x-1]) + (3 * nums[x-2]) + (n * pow(7, n))) % mods
            nums.append(curr)
            print("Case {}: {}".format(i+1, curr))




