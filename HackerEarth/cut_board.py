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
    cells_count = n*m - x - y
    if cells_count % 2 == 0:
        print("YES")
        k = cells_count//2
        print(k)
        board = []
        board.append(list("X"*x+"_"*(m-x)))
        for _ in range(n-2):
            board.append(list("_"*m))
        board.append(list("_"*(m-y)+"X"*y))

        count = 1
        for y1 in range(n,-1,-1):
            for x1 in range(m):
                if board[y1][x1] == "_":
                    if x1+1 < m and board[y1][x1+1] == "_":
                        x2 = x1+1
                        y2 = y1
                        board[y1][x1] = str(count)
                        board[y2][x2] = str(count)
                        count += 1
                        print(y1+1,x1+1,y2+1,x2+1)
                    elif y1-1 < n and board[y1-1][x1] == "_":
                        x2 = x1
                        y2 = y1-1
                        board[y1][x1] = str(count)
                        board[y2][x2] = str(count)
                        count += 1
                        print(y2+1,x2+1,y1+1,x1+1)
                    else:

        #for l in board:
        #    for i in l:
        #        print("{:>3}".format(i), end='')
        #    print("\n")
    else:
        print("NO")



if __name__ == '__main__':
    nmxy = input().split()

    n = int(nmxy[0])

    m = int(nmxy[1])

    x = int(nmxy[2])

    y = int(nmxy[3])

    fillBoard(n, m, x, y)