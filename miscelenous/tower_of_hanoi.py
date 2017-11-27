'''
SAMPLE INPUT
2
3
4 3
1 4
3 2
5
5 6
4 3
1 2
7 5
3 4

SAMPLE OUTPUT
5
12
'''
import operator
for _ in range(int(input())):
    nos = int(input())
    tower = []
    for i in range(nos):
        lst = [int(x) for x in input().split()]
        tower.append(lst)
    tower = sorted(tower, reverse=True)
    ans = [0]*nos
    print(tower)
    for x in range(nos):
        ans[i] = tower[x][1]

    max_h = 0
    for i in range(nos):
        for j in range(i, nos):
            print(i, j, tower[i][0], tower[j][0],tower[i][1],tower[j][1] )
            if tower[i][0] > tower[j][0] and tower[i][1] > tower[j][1]:
                ans[i] = max((ans[j] + tower[i][1]), ans[i])
    max_h  = max(max_h, ans[i])

    print(max_h)





