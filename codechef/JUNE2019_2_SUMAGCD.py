from math import gcd
mods  = 1000000007
nb_Test = int(input())
for _ in range(nb_Test):
    N = int(input())
    arr = sorted(set([int(x) for x in input().split()]))
    lens = len(arr)
    ans = None
    if   lens == 1:ans = 2 * arr[0]
    elif lens == 2:ans = arr[0] + arr[1]
    else:
        ultimate    = arr[-1]
        penultimate = arr[-2]
        arr_gcd = 0
        for x in range(lens - 2):
            arr_gcd = gcd(arr_gcd, arr[x])
        ulti_gcd = gcd(arr_gcd, ultimate)
        penu_gcd = gcd(arr_gcd, penultimate)
        ans = max(ultimate + penu_gcd, penultimate + ulti_gcd)
    print(ans)    
