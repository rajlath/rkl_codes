'''
5
2 3
2 3
5 1
4 3
5 3
'''
for i in range(int(input())):
    have, power = [int(x) for x in input().split()]
    days = 1
    while have > 0:
        have -= days ** power
        if have <= 0:
            break
        days += 1
    print(days-1)




