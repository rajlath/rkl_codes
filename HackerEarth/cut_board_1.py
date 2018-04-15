'''
100 100 50 49
NO

100 100 49 49
NO
'''
#!/bin/python3

import os
import sys


#
# Complete the fillBoard function below.
#
def fillBoard(n, m, x, y):
    board = []
    domino=[]
    board.append("-"*x + "X"*(m-x))
    for i in range(n - 2):
        board.append("X" * m)
    board.append("X"*(m - y)+ "-"*y)
    canbe = True
    i = 0
    j = 0
    while i < m:
        while j < n:
            if board[i][j] == "X":
                print(i, j)
                if j + 1 < m and board[i][j+1] == "X":
                    domino.append([i, j, i, j+1])
                    j +=1
                elif i+1 < n and board[i+1][j] == "X":
                    i += 1
                    domino.append([i, j, i+1, j])
                else:
                    canbe = False
                    break
            else:
                j += 1
        if canbe == False:
            break
        else:
            i += 1
    print(domino)












if __name__ == '__main__':
    nmxy = input().split()

    n = int(nmxy[0])

    m = int(nmxy[1])

    x = int(nmxy[2])

    y = int(nmxy[3])

    fillBoard(n, m, x, y)