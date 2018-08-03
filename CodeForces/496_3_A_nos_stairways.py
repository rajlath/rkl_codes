nos = int(input())
steps = [int(x) for x in input().split()]
nosw = 0
indx = [i for i,v in enumerate(steps) if v == min(steps)] + [nos]

print(len(indx) - 1)
for i in range(1, len(indx)):
    print(indx[i] - indx[i-1], end=" ")




