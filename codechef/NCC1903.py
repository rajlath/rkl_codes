from itertools import accumulate
nb_test = int(input())
for _ in range(nb_test):
    can_do = int(input())
    assign = int(input())
    pages  = [int(x) for x in input().split()]
    done   = 0
    count  = 0
    for i in range(assign):
        done += pages[i]
        if can_do >= done:
            count += 1
    print(count)


