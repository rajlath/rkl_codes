from math import gcd
def arr_gcd(arr):
    gCD = arr[0]
    for i in range(1, len(arr)):
        gCD = gcd(gCD, arr[i])
        if gCD == 1:return "YES"
    return "NO"

for _ in range(int(input()))    :
    lens = int(input())
    arrs = [int(x) for x in input().split()]
    print(arr_gcd(arrs))

