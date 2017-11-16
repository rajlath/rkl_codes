from math import gcd
def is_valid_rat(a, b, c):
    if a<=0 or b<=0 or c<=0:return False
    (a, b, c) = sorted([a, b, c])
    if a + b  <= c: return False
    
    p1 = a
    p2 = c - b
    div = gcd(p1, p2)
    p1 /= div
    p2 /= div
    
    q1 = c + b
    q2 = a
    div = gcd(q1, q2)
    q1/=div
    q2/=div
 
    return p1 == q1 and p2 == q2
    
for _ in range(int(input())):
    (a, b, c, x) = [int(x) for x in input().split()]
    if is_valid_rat(a+x, b+x,c) or is_valid_rat(a+x, b, c+x) or is_valid_rat(a, b+x, c+x):
        print("YES")
    else:
        print("NO")    
