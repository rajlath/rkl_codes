from fractions import gcd
from functools import reduce
for i in range(int(input())):
    res = "She can"
    n, x, y, z = [int(x) for x in input().split()]  
    prime = list(set([x, y, z]))
    print(prime)    
    gc = [int(x) for x in input().split()]
    lcm = gc[0]
    for i in gc:
        lcm = (i*lcm)/gcd(i, lcm)
    for i in gc:
        val = lcm/i
        for j in range(3):
            if val == 1:break
            while val % prime[j] == 0:
                val = val/prime[j]
                
        if val != 1:
            res = "She can't"
            break 
            
            
    print(res)                 
        
        
'''
5
10 5 7 2
3125 1 5764801 1 78125 1 1 117649 343 5
10 3 7 3
61 12 93 11 62 3 42 52 81 96
10 7 5 3
1225 5 1 1 1 343 15 390625 105 7
10 7 2 7
51 9 6 41 7 62 22 71 100 99
10 3 2 2
41 24 20 71 38 35 45 72 21 94

She can
She can't
She can
She can't
She can't

She can't
She can't
She can't
She can't
She can't
''' 

       
