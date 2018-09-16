import math
import random

def finding_prime_1(number):
    '''
    simple brute force upto number
    '''
    num = abs(number)
    if num < 4:return True
    for x in range(2, num):
        if not num % x : return False
    return True

def finding_prime_2(number):
    '''
    brute force upto sqrt(number)
    '''
    limit = int(number ** 0.5)
    if number < 4 : return True
    for x in range(2, limit+ 1):
        if not number % x:return False
    return True

def finding_prime_3(number)    :
    '''
    using random number : fermat
    '''
    if number <= 102:
        for x in range(2, number):
            if pow(x, number-1, number) != 1:return False
        return True
    for _ in range(100)        :
        x = random.randint(2, number - 1)
        if pow(x, number - 1, number) != 1:return False
    return True




from datetime import datetime
n = 32416190072
#print(finding_prime_1(n))
s = datetime.now()
print(finding_prime_2(n))
print(datetime.now() - s)
s = datetime.now()
print(finding_prime_3(n))
print(datetime.now() - s)