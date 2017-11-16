import re
def isPrime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True
    
    
n = int(input())
for i in range(1, n+1):
	if  isPrime(i) and  isPrime(n-i) and i< n-i and i!=1 :
		print( i, n-i)
		break
		
            
