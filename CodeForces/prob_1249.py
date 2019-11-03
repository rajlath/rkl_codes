nbq = int(input())
nbs = int(input())
skill = sorted([int(x) for x in input().split()])
teams = []
for i in skill:
    if len(teams) ==  0:
        teams.append([i])
    else:
        added = False
        for j in teams:
            if abs(j[-1] - i) > 1:
                j.append(i)
                added = True
                break
        if not added:
            teams.append([i])
print(len(teams))




