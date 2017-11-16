import math
def trailing_zero(n):
    cnt = 0
    i = 5
    while n//i >= 1:
        cnt += 1
        i*= 5
    return cnt 
    
def zeros(n):
    if n == 0:return 0
    k = int(math.log(n)/math.log(5))
    m = 5 ** k
    return int(n*(m-1)/(4*m))
    
def factorial(n)    :
    if n == 0: return 0
    if n == 1: return 1
    return n * (factorial(n-1))
    
print(factorial(29))    
  
    
for i in range(5, 100)    :
    print(i, zeros(i))
    
