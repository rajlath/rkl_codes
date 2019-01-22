
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 20:02:56
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


nb_test  = int(input())
for _ in range(nb_test):
    player = [0] * 100
    nb_over, nb_player = read_ints()
    for i in range(nb_player):
        player[i] = -1
        score = input()
        striker = 0
        non_str = -1
        wicket = 2
        player[striker] = 0
        player[non_str] = 0
        count = 0
        for j in range(len(score)):
            if count == 6:
                player[striker], player[non_str] = player[non_str], player[striker]
                count = 0
            if score[j] == "0":
                player[striker] += 0
            elif score[j] == "1":
                player[striker] += 1
                player[striker], player[non_str] = player[non_str], player[striker]
            elif score[j] == "2":
                player[striker] += 2
            elif score[j] == "3":
                player[striker] += 3
                player[striker], player[non_str] = player[non_str], player[striker]
            elif score[j] == "4"    :
                player[striker] += 4
            elif score[j] == "6"    :
                player[striker] += 6
            elif score[j] == 'w':
                player[striker] = 0
                wicket += 1
            count += 1
        print("Case {} :".format(i+1))
        for y in range(nb_player):
            if i == striker:
                print("Player "+str(i+1)+":"+str(player[i+1]))
            elif i == non_str:
                print("Player "+str(i+1)+":"+str(player[i+1]))
            elif player[i] == -1:
                print("Player "+str(i+1)+": DNB")
            else:
                print("Player "+str(i+1)+":"+str(player[i+1]))





