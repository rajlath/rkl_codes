n, m = [int(x) for x in input().split()]
min_left, min_rite = 120, 120
found = False
for i in range(n):
    if found:
        input()
    else:
        s = input()
        if "B" in s:
            x1, y1 = i, s.find("B")
            x2, y2 = i, s.rfind("B")
            length = y2 - y1 + 1
            midx    = x1 + (length )//2 + 1
            midy    = y1 + (length )//2 + 1
            print(midx, midy)
            found = True




