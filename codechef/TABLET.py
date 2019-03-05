nb_test = int(input())
for _ in range(nb_test):
    nb_frnds = int(input())
    will_see = sorted([int(x) for x in input().split()])
    joined = 0
    for i in will_see:
        if i <= joined:
            joined += 1
    print(joined)





