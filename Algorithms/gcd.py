#from math import gcd


def gcd(a, b):
    '''
    this assumes that a is greater then b
    '''
    if a%b == 0:return b
    gcd(b, a%b)

a, b = [36, 12]
a, b = max(a, b), min(a, b)
print(gcd(a, b))

