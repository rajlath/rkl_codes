import math
def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def fun(num):
    while not is_prime(num):num += 1
    return num

print(fun(int(input())))

b(-1) a(1) b[0] a[2] b[-2] a[-1]