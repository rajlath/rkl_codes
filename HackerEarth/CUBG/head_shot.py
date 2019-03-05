import math
nb_Test = int(input())
for _ in range(nb_Test):
    d, h = [int(x) for x in input().split()]
    tanO = d / h
    O =  math.atan(tanO)
    print(round( O * (180 / math.pi)))