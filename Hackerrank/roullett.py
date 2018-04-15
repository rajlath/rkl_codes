#!/bin/python3

import sys

def revisedRussianRoulette(n, doors):
    # Complete this function
        lst = ""
        for i in range(n):
            lst += str(doors[i])
        #lst = "".join(map(str, doors))
        a, b =  lst.count("1") - lst.count('11'), lst.count('1')
        return a, b



if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))

    if doors:
        result = revisedRussianRoulette(n, doors)
        print (" ".join(map(str, result)))
    else:
        print("0 0")
'''
10
0 1 03
1 1 1

'''


