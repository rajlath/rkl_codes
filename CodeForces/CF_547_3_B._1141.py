from itertools import groupby
nb_hours = int(input())
schedule = [int(x) for x in input().split()]
schedule += schedule
schedule = groupby(schedule)
maxs = 0
for i, g in schedule:
        if i == 1:
                maxs = max(maxs, len(list(g)))
print(maxs)



