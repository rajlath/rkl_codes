nb_Test = int(input())
for _ in range(nb_Test):
    curr = input()
    counts = sorted([curr.count(i) for i in set(curr)], reverse=True)
    lens = len(curr)
    uniq_ch = len(set(curr))
    sames = 0
    for i in range(uniq_ch, -1, -1):
        if lens % i == 0:
            sames = i
            break
    ops = 0
    for i in range(sames):
        ops += abs(counts[i] - sames)
    print(ops)







