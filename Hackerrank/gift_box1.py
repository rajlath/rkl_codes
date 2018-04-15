#!/bin/python3

import os
import sys

def giftBoxes(g, c):
    s = list(g + '.')
    n = len(s)
    pi = [0]
    for i in range(1, n):
        j = pi[-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi.append(j)
    pi.append(0)
    print(pi)
    count = 0
    for char in c:
        s.append(char)
        j = pi[-1]
        while j > 0 and s[-1] != s[j]:
            j = pi[j - 1]
        if s[-1] == s[j]:
            j += 1
        pi.append(j)
        if pi[-1] == len(g):
            for _ in range(len(g)):
                s.pop()
                pi.pop()
            count += 1
        #print(s, count)
    return count

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        g = input()
        c = input()
        result = giftBoxes(g, c)

        print(result)

