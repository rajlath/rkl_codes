nb_monster = int(input())
powers = sorted([int(x) for x in input().split()])
curr = powers[0]
mins = 0
for p in powers:
    for j in range(1, int(p ** 0.5) + 1):
        if p % j == 0:
            cand = (curr + p) - (p // j + curr * j)
            mins = max(mins, cand)
print(sum(powers) - mins)

