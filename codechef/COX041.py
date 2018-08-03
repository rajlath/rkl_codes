'''
Input
3 3
000
111
222

Output
YES
Input
3 3
000
000
111

Output
NO
Input
3 3
000
111
002

Output
NO
'''
n, m = [int(x) for x in input().split()]
flag = [input() for _ in range(n)]
f = 0
t = -1
for i in range(n):
    for j in range(m):
        if j != 0 and flag[i][j-1] != flag[i][j]:
            f = 1
            break
    if flag[i][0] ==  t:
        f = 1
        break
    t = flag[i][0]
if f == 1:
    print("NO")
else:
    print("YES")



