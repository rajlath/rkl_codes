nb_Test = int(input())
for _ in range(nb_Test):
    nb_elem, treshold = [int(x) for x in input().split()]
    elems = [int(x) for x in input().split()]
    left = -1
    rite = int(10e9 + 7)
    while rite - left > 1:
        mid  = (rite + left) >> 1
        print(mid)
        sums = sum([max(x - mid, 0) for x in elems])
        if sums >= treshold:
            left = mid
        else:
            rite = mid
    #print(left)
    sums = sum([max(x - left, 0) for x in elems])
    print(left,sums)







