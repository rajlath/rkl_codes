'''
1
10 7 19 4
5
15 3
17 6
10 5
20 2
15 6
'''

for _ in range(int(input())):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    cnt = 0
    for _ in range(int(input())):
        x, y = [int(x) for x in input().split()]
        if x > x1 and x < x2:
            if (y > y1 and y < y2) or (y > y2 and y < y1):cnt += 1
    print(cnt)
