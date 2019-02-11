nb_test = int(input())
for _ in range(nb_test):
    nb_areas = int(input())
    dones = [int(x) for x in input().split()]
    done_till_now = 0
    done_count    = 0
    for i in dones:
        if i == -1:
            here = done_till_now // done_count
        else:
            here = i
        print(here, end = ' ')
        done_till_now += here
        done_count += 1





