#!/bin/python3

import sys

if __name__ == "__main__":
    nos = int(input().strip())
    choice = "-1"
    mins = 1e9
    for a0 in range(nos):
        s, n = input().strip().split(' ')        
        s, n = [str(s), int(n)]
        
        cn4 = str(n).count("4")
        cn7 = str(n).count("7")
        
        if cn4 == cn7 and cn4+cn7 == len(str(n)) and cn4 != 0:
            if n < mins:
                choice = s
          
    print(choice )         
