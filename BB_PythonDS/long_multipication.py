
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 10:20:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : Benjamin Baka PythonDSandAlgo Examples
# @Version : 1.0.0
from math import log10, ceil
def karatsuba(x,y):
    '''
    multipication of very big numbers using recursion
    implements karatsuba algorithm
    @param int : a
    @param int : b
    @return int
    '''

    # The base case for recursion
    if x < 10 or y < 10:
        return x*y
    #sets n, the number of digits in the highest input number
    n = max(int(log10(x)+1), int(log10(y)+1))
    # rounds up n/2
    n_2 = int(ceil(n / 2.0))
    #adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1
    #splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    #applies the three recursive steps
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd
    #performs the multiplication
    return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc)))

def main():
    print(karatsuba(123456789123456789, 98765439876543))
    print(123456789123456789 * 98765439876543)
    y, n = test()
    print("failed {} and ok {}".format(y, n))

import random
def test():
    failed, ok = 0,0
    for i in range(1000):
        x = random.randint(1,10**5)
        y = random.randint(1,10**5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            failed += 1
        else:
            ok +=  1
    return (failed, ok)



if __name__ == "__main__":
    main()




