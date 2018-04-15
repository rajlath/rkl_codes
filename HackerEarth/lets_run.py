'''
SAMPLE INPUT
4
1 2 2 4
1 2 2 3
1 2 2 2
1 2 2 1
SAMPLE OUTPUT
2
0
2
1
'''
for _ in range(int(input())):
    speed, lap1, speed_mult,for_time = [int(x) for x in input().split()]
    distance = 0
    if lap1 > for_time:
        distance = for_time * speed
    else:
        while for_time > lap1:
            distance += lap1 * speed
            for_time -= lap1
            speed = speed * -1 * speed_mult
        if for_time > 0:
            distance += lap1 * speed
    print(distance)

