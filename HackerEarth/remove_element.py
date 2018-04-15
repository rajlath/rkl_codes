import math
mods = 1000000007

mult = [0]*100000
mult[0] = 1
mult[1] = 1

for i in range(2, 100000):
    mult[i] = (mult[i-1]*i)%mods


for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    arr = sorted(arr, reverse=True)

    cost = 0
    for i in range(noe):
        cost += arr[i]*mult[i+1]%mods
    print(cost%mods)





