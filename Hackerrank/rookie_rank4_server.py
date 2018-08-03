'''
5
1 2 3 4 8
1 1 1 1 1
'''
n = int(input())
pos = [int(x) for x in input().split()]
hite= [int(x) for x in input().split()]

c  = [0] * n
b  = [0] * n

left = 1
b[0] = 1
for i in range(n):
    if b[i] == 0:
        left = 0
        break
    for j in range(i+1,n):
        if pos[i] + hite[i] >= pos[j]: b[j] = 1

c[n-1] = 1
rite = 1
for i in range(n-1, -1, -1):
    if c[i] == 0:
        rite = 0
        break
    for j in range(i-1, -1, -1):
        if pos[i] - hite[i] <= pos[j]:
            c[j] = 1
if rite and left : print("Both")
elif rite and not left:print("RIGHT")
elif not rite and left:print("LEFT")
else:print("NONE")
