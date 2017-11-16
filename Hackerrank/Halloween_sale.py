#!/bin/python3

import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if s < p:return 0
    cnt = 0    
    while p >= m:
        s -= p
        cnt += 1
        if s <= 0:
            break
        p-=d
        p = max(p, m)
    cnt += s // m
    return cnt
        
            
        

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
