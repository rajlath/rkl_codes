from random import randint
 
def isProbablyPrime(n, k = 5):
    if (n < 2 ):return False
    output = True
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):            
            return False
        print(i, a)     
    return output
    
print(isProbablyPrime(131))    
   


