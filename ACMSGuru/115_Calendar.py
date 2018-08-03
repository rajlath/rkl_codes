day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

d, m = [int(x) for x in input().split()]
if 0 < m < 13 and d <= day_in_month[m] and m != 0 and d != 0:
    day_number = d
    for i in range(1, m):
        day_number += day_in_month[i]
    day_number %= 7
    if day_number:
        print(day_number)
    else:print(7)
else:
    print("Impossible")

