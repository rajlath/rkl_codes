'''
SAMPLE INPUT 
2
1
4
SAMPLE OUTPUT 
1
5

1 1 3 5 11 21 43 85 171 341



for _ in range(int(input())):
    n = int(input())
    sweets = [0,1,1,3]
    ans = sweets[3]
    if n == 1: print(1)
    elif n == 2: print(1)
    elif n == 3: print(3)
    else:
        for i in range(4, n+1):
            if i & 1:
                ans = (ans * 2 + 1)%1000000007
            else:
                ans = (ans * 2 - 1)%1000000007
        print(ans)            
 '''  
mod = 1000000007  

def power(a, b):
    tmp = a
    res = 1
    while b:
        if b%2:
            res = (res * a)%mod
        a = (a * a) % mod
        b//=2
    if n%2:res-=1
    else:res= (res+1)%mod
    return res%mod
    
m = [0,1,1]
for _ in range(int(input()))    :
    n = int(input())
    if n in [1,2]:print(1)
    else:
        if len(m)>(n):
            if m[n]!=0:
                print(m[n]) 
        for x in range(len(m)-1,n+1):m.append(0)        
        ans = (power(2, n)) % mod
        m[n-1] = ans
        print(ans%mod)
        
    
 
       

            
        
