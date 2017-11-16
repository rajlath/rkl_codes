def extended_gcd(a, b):
    if b == 0:
        return  a
    else:
        extended_gcd(b, a%b) 
        
