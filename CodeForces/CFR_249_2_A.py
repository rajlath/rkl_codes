nb_groups, max_ride = [int(x) for x in input().split()]
groups = [int(x) for x in input().split()]
need = 0
while groups:
    curr = max_ride
    while groups and curr >=groups[0]:
        curr -= groups.pop(0)
    need += 1
print(need)
