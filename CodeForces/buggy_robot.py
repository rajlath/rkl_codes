"""
input
4
LDUR
output
4
input
5
RRRUU
output
0
input
6
LLRRRR
output
4
U — move from the cell (x, y) to (x, y + 1);
D — move from (x, y) to (x, y - 1);
L — move from (x, y) to (x - 1, y);
R — move from (x, y) to (x + 1, y).
"""
input()
comms = input()
x, y = 0, 0
cnt = 0
done = False
for i in comms:
    cnt += 1
    if i == "U":
        x , y = x, y+1              
    elif i == "D":
        x , y = x, y-1        

    elif i == "L":
        x, y = x-1, y
    elif i == "R":
        x, y = x+1, y 
        
    if x == y == 0:
        done= True
        break 
print(cnt if done else 0)                
        
