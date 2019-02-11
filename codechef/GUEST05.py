nb_test = int(input())
for _ in range(nb_test):
    nb_flow = int(input())
    ins = sorted([int(x) for x in input().split()])
    out = sorted([int(x) for x in input().split()])
    needed = 0
    in_indx = 0
    ou_indx = 0
    maxs = 0
    while in_indx < nb_flow and ou_indx < nb_flow:
        if ins[in_indx] < out[ou_indx]:
            needed += 1
            in_indx += 1
        else:
            needed -= 1
            ou_indx += 1
        maxs = max(maxs, needed)
    print(maxs)


