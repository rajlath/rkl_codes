'''
Input1:
0 1 2 3 4 5 6
0 2 2 3 4 5 6

Output1:
mech

Input2:
4 5 6 7 8 9 3
1 2 3 4 5 6 7

Output2:
cse

Input3:
7 6 5 4 3 2 1
1 2 3 4 5 6 7

Output3:
draw

'''
cses = sum([int(x) for x in input().strip().split()])
mecs = sum([int(x) for x in input().strip().split()])
if cses > mecs:print("cse")
elif mecs > cses:print("mech")
else:print("draw")

