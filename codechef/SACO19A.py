
# -*- coding: utf-8 -*-
# @Date    : 2019-01-31 13:50:36
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import defaultdict

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = int(input())
for _ in range(nb_test):
    nb_teams, nb_quaries = read_ints()
    leaders = {}
    members = defaultdict(list)
    for _ in range(nb_teams * 3):
        nos, member, status = read_strs()
        if status == "Y":
            leaders[nos] = member
        else:
            if nos in members:
                members[nos].append(member)
            else:
                members[nos]=[member]
    for _ in range(nb_quaries):
        a, b = read_strs()
        if b == '1':
            print(leaders[a])
        elif b == '2':
            print(min(members[a]))
        else:
            print(max(members[a]))












