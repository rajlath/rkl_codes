from sys import stdin

nb_bldgs, nb_query = [int(x) for x in stdin.readline().split()]
bldgs_heights      = [int(x) for x in stdin.readline().split()]
nexts              = [-1] * nb_bldgs
stacks             = []
stacks.append(0)
for i in range(1, nb_bldgs):
    while stacks and bldgs_heights[i] > bldgs_heights[stacks[-1]]:
        nexts[stacks[-1]] = i
        stacks.pop()
    stacks.append(i)


z = 1
for i in range(2, nb_bldgs):
    if bldgs_heights[i] <= bldgs_heights[i-1]: z = 0
ans = 0
for _ in range(nb_query):
    x, y = [int(x) for x in stdin.readline().split()]
    x = (x + ans)%nb_bldgs
    y = (y + ans)%nb_bldgs
    if x > y:
        x, y = y, x
    if z:
        ans = y + 1 - x
    else:
        p = 1
        i = x
        while True:
            if nexts[i] == -1 or nexts[i] > y:break
            p += 1
            i = nexts[i]
        ans = p
    print(ans)
