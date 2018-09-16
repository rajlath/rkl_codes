import math
for _ in range(int(input())):
        N, B = [int(x) for x in input().split()]
        print(math.ceil( (N - (N//B)) + (N%B==0) ))
