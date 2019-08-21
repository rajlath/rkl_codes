
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 10:55:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


confuse = "Wait, what?"

def did_x_win(board, x):
    score = 0
    #check rows
    for i in range(3):
        score += len(set(board[i])) == 1 and board[i][0] == x
        # diag1
        score += board[0][0] == board[1][1] == board[2][2] == x
        score += board[0][2] == board[1][1] == board[2][0] == x
     #check cols
    board = list(zip(*board))
    for i in range(3):
        score += len(set(board[i])) == 1 and board[i][0] == x
    return score > 0

board = []
cnt_x, cnt_o = 0, 0
x_won, o_won = False, False
for i in range(3):
    board.append([x for x in input()])
    cnt_x += board[i].count("X")
    cnt_o += board[i].count("O")
score = 0
answer = ''
o_won = did_x_win(board, "O")
x_won = did_x_win(board, "X")
#print(o_won, x_won)
if cnt_x < cnt_o:answer = confuse
elif cnt_x > (cnt_o + 1) : answer = confuse
elif o_won + x_won > 1:answer = confuse
elif x_won  and cnt_x != (cnt_o + 1):answer = confuse
elif x_won:answer = "X won."
elif o_won and cnt_x != cnt_o:answer = confuse
elif o_won:answer = "O won."
elif cnt_x + cnt_o == 9:answer = "It's a draw."
elif cnt_x == cnt_o:answer = "X's turn."
else:answer = "O's turn."
print(answer)








