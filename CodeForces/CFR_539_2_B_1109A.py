nb_monster = int(input())
powers = [int(x) for x in input().split()]
mins = min(powers)
res = sum(powers)
for i in range(nb_monster):
    for d in range(1, powers[i]+1):
        if powers[i] % d != 0:continue
        curr = res - mins - powers[i]
        curr = mins * d + powers[i] // d
        res = min(res, curr)
print(res)