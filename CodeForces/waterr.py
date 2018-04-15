'''
input
3
5 1
3
3 3
1 2 3
4 1
1
output
3
1
4
'''
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    alls = [0] * a
    arr = [int(x) for x in input().split()]
    for i in arr:
        alls[i-1] = 1
    maxs = 1
    cnt  = 0
    for i in alls:
        if i :
            maxs = max(maxs, cnt)
            cnt = 0
        else:
            cnt += 1
    print(maxs)

