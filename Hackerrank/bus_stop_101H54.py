'''
4
0 10 40 100
20 10
3
0 0 4
15 10 1
40 2 16
'''
bus_stops_cnt = int(input())
bus_stops_loc = [int(x) for x in input().split()]
waiting_time, speed = [int(x) for x in input().split()]
for i in range(int(input())):
    pos, time, walk_speed = [int(x) for x in input().split()]


    #person to take optimal busstop

    left = -1
    rite = bus_stops_cnt

    while rite - left > 1:
        mid = (left + rite) >> 1
        if bus_stops_loc[mid] < pos:
            left = mid
        else:
            rite = mid
    opt_loc = mid

    if opt_loc != pos:
        left_time = abs(pos - bus_stops_loc[left]) * walk_speed + abs(bus_stops_loc[-1] - bus_stops_loc[left]) * speed
        rite_time = abs(pos - bus_stops_loc[rite]) * walk_speed + abs(bus_stops_loc[-1] - bus_stops_loc[rite]) * speed
        print(min(left_time, rite_time))
    else:
        print(abs(bus_stops_loc[-1] - bus_stops_loc[opt_loc]) // speed)






