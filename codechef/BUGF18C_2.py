nots = int(input())
for _ in range(nots):
    start, end = [int(x) for x in input().split()]
    if end < start:
        print(start - end)
    for i in range(start, 0, -1):
        if i * 3 == end:
            print( 1 + start - i)
            






