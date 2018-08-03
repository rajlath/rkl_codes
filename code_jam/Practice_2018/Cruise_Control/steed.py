'''
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
'''

for _ in range(int(input())):
    destination, no_of_horses = [int(x) for x in input().split()]
    ann_speed = int(10e12)
    for i in range(no_of_horses):
        pos, speed = [int(x) for x in input().split()]
        a = destination * speed
        b = destination - pos
        ann_speed = min(ann_speed, destination * speed / (destination - pos))

    print("{:.6f}".format(ann_speed))


