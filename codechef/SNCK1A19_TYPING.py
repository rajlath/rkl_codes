
# -*- coding: utf-8 -*-
# @Date    : 2018-10-20 07:38:09
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


nb_test = read_int()
for _ in range(nb_test):
    nb_words = read_int()
    tot_time = 0
    for _ in range(nb_words):
        curr = read_str()
        last = ["r", "l"][curr[0] in "dk"]
        curr_time = 2
        this_time = 0
        done = []
        for i in curr[1:]:
            if i in "dk":
                if last == "l":
                    this_time = 4
                else:
                    this_time = 2
                last = "l"
            else:
                if last == "r":
                    this_time = 4
                else:
                    this_time = 2
                last = "r"
            curr_time += this_time

        print(curr_time, curr, done)
        if curr in done:
            tot_time += curr_time//2
        else:
            tot_time += curr_time
        done.append(curr)


    print(done)
    print(tot_time)














