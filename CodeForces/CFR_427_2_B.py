k = int(input())
ins = sorted([int(x) for x in input()])
sums= sum(ins)
i = 0
while sums < k:
    sums += (9 - ins[i])
    i += 1
print(i)
