from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    gc_d =  gcd(arr[0], arr[1])
    for i in range(2,n):
        gc_d = gcd(gc_d, arr[i])
    print([-1, n][gc_d == 1])
