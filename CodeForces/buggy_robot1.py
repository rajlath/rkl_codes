moves = int(input())
comms = input()
x = 0
y = 0
for i in comms:
    if i == "L":x-=1
    if i == "R":x+=1
    if i == "U":y+=1
    if i == "D":y-=1
print(moves - (abs(x) + abs(y)))
