for _ in range(int(input())):
    lens = int(input())
    arrs = []
    for _ in range(lens):
        arrs.append([int(x) for x in input().split()])
    collected = arrs[0][0]
    x, y = 0, 0
    while True:
        x1, y1 = x + 1, y
        x2, y2 = x , y + 1
        if x1 == lens -1 and y1 == lens - 1:
            collected += arrs[x1][y1]
            break
        if x2 == lens - 1 and y2 == lens - 1:
            collected += arrs[x2][y2]
            break
        curr1, curr2 = 0, 0
        if 0 <= x1 < lens and 0 <= y1 < lens:
            curr1 = arrs[x1][y1]
        if 0 <= x2 < lens and 0 <= y2 < lens:
            curr2 = arrs[x2][y2]
        if curr1 > curr2:
            collected += curr1
            x, y = x1, y1
        else:
            collected += curr2
            x, y = x2, y2

    print(collected)



