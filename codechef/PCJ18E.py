
import  math
for i in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    arr1 = sorted(arr)
    c = 0
    for i in arr:
        if arr1[c] is i:
            c += 1
    print(noe - c)

