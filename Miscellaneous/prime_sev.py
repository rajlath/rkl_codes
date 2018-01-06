import time
def prime_seive(n):
	'''
	create all primes numbers upto n
	'''
	primes = [False,False,True] + [True,False]*(n-3//2)
	for p in range(3, int(n ** 0.5)+1, 2):
		if primes[p]:
			for j in range(p*p, n, 2 * p):
				primes[j] = False
	#return [p for p in range(2,n) if primes[p]],primes
	return primes
now = time.time()	
prime = prime_seive(10000000)
print(time.time() - now)

				
		
