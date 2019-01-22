import math

t = int(input())
while(t > 0):
    n = int(input())
    factor = math.floor(n / 12)
    mod = n%12

    arrangement = {
        1: "WS",
        2: "MS",
        3: "AS",
        4: "AS",
        5: "MS",
        6: "WS",
        7: "WS",
        8: "MS",
        9: "AS",
        10: "AS",
        11: "MS",
        0: "WS",
    }

    seat_num = {
        1: 12,
        2: 11,
        3: 10,
        4: 9,
        5: 8,
        6: 7,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        0: 1,
    }
    result = 0
    if mod == 0:
        result = 12*(factor-1) + seat_num.get(mod)
    else:
        result = 12*factor + seat_num.get(mod)

    print("%d %s" %(result, arrangement.get(mod)))
    t = t - 1