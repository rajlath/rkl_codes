from math import sqrt 

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def lcm(a, b):
    return (a * b) // gcd(a, b)
    
def prime_factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result   
    
  
def factors(n):
    return [x for x in range(1, n+1) if  n%x==0]
    
def factorial(n)    :
    if n == 1: return 1
    else:return n * factorial(n-1)

def fibo(n)    :
    if n <= 1: return 1
    else: return fibo(n-1) + fibo(n-2)
    
