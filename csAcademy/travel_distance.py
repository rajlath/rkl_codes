'''
Travel Distance
Time limit: 1000 ms
Memory limit: 256 MB

Alex has decided to go on a new adventure. Initially, we can consider he is situated at coordinates (0, 0)(0,0). At each step, he will move 11 unit in one of the four cardinal directions, denoted by NN, EE, SS and WW.

Find the Manhattan distance between his final position and the starting one.

Standard input
The first line contains a string representing Alex's moves. The string will contain only the characters NN, EE, SS or WW.

Standard output
Print the answer on the first line.

Constraints and notes
The length of the input string will be between 11 and 1\,0001000.
Input	Output
NES
1
SSSEEE
6
NSEW
0
NWNSSSWNW
3
'''
x, y = 0, 0
s = input()
for i in s:
    if   i == "N": x += 1
    elif i == "S": x -= 1
    elif i == "E": y += 1
    elif i == "W": y -= 1
print(abs(x) + abs(y))
