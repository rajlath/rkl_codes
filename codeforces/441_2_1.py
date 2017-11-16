def distance(n, a, b, c):
    if n == 1:
        return 0
    else:
        if a < b:
            return a + distance(n-1, a, c, b)    
        else:
            return b + distance(n-1, b, c, a)  
            
I = lambda:int(input())
n = I()
a = I()
b = I()
c = I()

print(distance(n, a, b, c))          
