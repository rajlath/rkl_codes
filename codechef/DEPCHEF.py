nb_Test = int(input())
for _ in range(nb_Test):
    nb_soldiers = int(input())
    powers    = [int(x) for x in input().split()]
    shields   = [int(x) for x in input().split()]
    powers = [powers[-1]] + powers + [powers[0]]
    #print(powers)
    best_shields = int(-10e18)
    for i in range(1, nb_soldiers+1):
        curr = [powers[i-1], powers[i+1], powers[i-1]+powers[i+1]]
        if max(curr) < shields[i-1]:
            best_shields = max(best_shields , shields[i-1])
    if best_shields == int(-10e18):
        print(-1)
    else:
        print(best_shields)





