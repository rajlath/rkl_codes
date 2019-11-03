from itertools import accumulate
for _ in range(int(input())):
    n, p = [int(x) for x in input().split()]
    powers = list(accumulate(sorted([int(x) for x in input().split()])))
    cando = 0
    for i in powers:
        if i <= p:
            cando += 1
    print(cando)