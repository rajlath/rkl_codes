from math import log10, floor
maxs = 1000005
fcts = [0, 0]
for i in range(2, maxs-1):
    fcts.append(fcts[i-1] + log10(i))
#print([floor(x) for x in fcts[:10]])
for i in range(int(input()))    :
    n = int(input())
    print(floor(n * fcts[n]) + 1)
