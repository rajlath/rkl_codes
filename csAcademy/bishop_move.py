'''
Move the Bishop
Time limit: 1000 ms
Memory limit: 128 MB

On a chessboard of size 8 \times 88×8 there is a bishop on cell (R_1, C_1)(R
​1
​​ ,C
​1
​​ ). You want to move the bishop to cell (R_2, C_2)(R
​2
​​ ,C
​2
​​ ), using the minimum number of moves.

A bishop is a chess piece which has no restrictions in distance for each move, but is limited to diagonal movement. Basically, in a move you can take the bishop to any cell that shares a diagonal with the initial cell.

Standard input
The first line contains 44 integers R_1, C_1, R_2, C_2R
​1
​​ ,C
​1
​​ ,R
​2
​​ ,C
​2
​​ .

Standard output
If there is no solution output -1−1.

Otherwise, print the minimum number of moves on the first line.

Constraints and notes
1 \leq R_1, C_1, R_2, C_2 \leq 81≤R
​1
​​ ,C
​1
​​ ,R
​2
​​ ,C
​2
​​ ≤8
Input	Output	Explanation
3 2 6 5
1
The start position is labeled with S

The finish one with F

The path from S to F with #



3 2 3 8
2


3 2 4 4
-1
There's no path from the start position the finish one.

'''
x1, y1, x2, y2 = [int(x) for x in input().split()]
ans = 2
if x1 == x2 and y1 == y2:ans = 0
elif (x1+y1)%2 != (x2+y2)%2:ans=-1
elif abs(x1 - x2) == abs(y1 - y2):ans = 1
print(ans)
