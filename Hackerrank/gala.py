'''3
1
1
2
1 2
3
1 2 3
'''
from itertools import combinations,permutations
from fractions import Fraction
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1:
        print(arr[0])
    elif n == 2:
        a, b = int(arr[0]), int(arr[1])
        print("%d/%d" % (a+b, max(a, b)))
    else:
        arr = sorted(arr, reverse=True)[:3]
        arrp = list(permutations(arr))
        sums = 0
        maxs  = max(arr)
        for i in arrp:
            a, b, c = [x for x in i] 
            if a == min(i) or a == max(i):
                sums+= c
                
            else:
                sums += (b+c)
                
        print(Fraction(sums, 6))        
                
                
            
            
            
        
