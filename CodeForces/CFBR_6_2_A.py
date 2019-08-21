a, b, c, d = sorted([int(x) for x in input().split()])
sided = b + c
sidec = a + b
if d < sided or c < sidec:print("TRIANGLE")
else:
    if d == sided or c == sidec:print("SEGMENT")
    else:print("IMPOSSIBLE")
