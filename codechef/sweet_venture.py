def bit_len(n):
    return len(bin(n)) -2



import math
for _ in range(int(input())):
    nins = int(input())
    nlen = bit_len(nins)
    n    = int(math.pow(2, nlen) - 1)


    print(n - nins)
