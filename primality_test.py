import math
from random import randint
import time

def naive_primality(number):
    if number == 1: return False
    if number == 2 or number == 3:return True
    if number % 2 == 0 or number % 3 == 0:return False
    i = 5

    while i * i < number:
        if number % i == 0:return False
        i += 6
    return True

def Fermat_Test(number):
    if number > 1:
        for _ in range(5):
            random_number = randint(2, number) - 1
            if pow(random_number, number - 1, number) != 1:
                return False
        return True
    else:return False
for _ in range(1000):
    curr = randint(2, 1000000) - 1
    ans1 = naive_primality(curr)
    ans2 = Fermat_Test(curr)
    if ans1 != ans2:
        print(ans1, ans2, curr)


