
s = "rishabh"
s1= s[::-1]
ans = 1
for i in s:
    print(ord(i) - ord('a'))
    ans *=  (ord(i) - ord('a') + 1)
print(ans)

import math

def stirling(n):
    # http://en.wikipedia.org/wiki/Stirling%27s_approximation
    return math.sqrt(2*math.pi*n)*(n/math.e)**n

def npr(n,r):
    return (stirling(n)/stirling(n-r) if n>20 else
            math.factorial(n)/math.factorial(n-r))

def ncr(n,r):    
    return (stirling(n)/stirling(r)/stirling(n-r) if n>20 else
            math.factorial(n)/math.factorial(r)/math.factorial(n-r))

print(npr(26,1)*npr(26,2)*npr(26,3)*npr(26,4)*npr(26,5)*npr(26,6))       
   
