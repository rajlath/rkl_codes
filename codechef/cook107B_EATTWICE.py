from collections import defaultdict
nb_Test = int(input())
for _ in range(nb_Test):
    nb_dish, nb_days = [int(x) for x in input().split()]
    days = defaultdict(list)
    for i in range(nb_dish):
        day, taste = [int(x) for x in input().split()]
        days[day].append(taste)
    tastiness = []
    for i, v in days.items():
        tastiness.append(max(v))
    tastiness = sorted(tastiness, reverse=True)
    print(tastiness[0] + tastiness[1])
