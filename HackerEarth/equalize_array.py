'''
2
2 2 2 2
2 4
3 2 3 2
2 6 7
'''
from functools import reduce
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)
    
def arr_lcm(arr):
    ans = arr[0]
    for i in range(len(arr)):
        ans = (arr[i] * ans / gcd(arr[i], ans))
    return int(ans)    
    

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)
    
for _ in range(int(input())):
    ins = [int(x) for x in input().split()] 
    n = ins[0]
    primes = sorted(set(lcmm(ins[1:])))
    arr = [int(x) for x in input().split()]
    alcm = arr_lcm(arr)
    
    can = True
    for i in range(n):
        val = alcm / arr[i]
        for j in range(len(primes)):
            if val == 1:
                break
            while (val % primes[j] == 0):
                val = val/primes[j]
        if val!=1:can=False
    print("She can" if can else "She can't")            
                    
    
      
    
    
    
    
