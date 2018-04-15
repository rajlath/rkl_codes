'''
3
4
2 5 6 4
8
88 80 82 81 84 86 85 87
4
2 4 3 1
'''
for _ in range(int(input())):
    nos = int(input())
    roll = [int(x) for x in input().split()]
    roll = sorted(roll)
    found = False
    for i in range(1, nos):
        if roll[i] != roll[i-1]+1:
            print(roll[i] - 1)
    if not found:print(roll[-1]+1)









