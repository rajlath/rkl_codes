#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rinfo
#
# Created:     02/08/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from collections import Counter
from collections import namedtuple
from math import log10
import math
def main(x, y):
    if x < 10 or y < 10:return x * y
    n = max(len(str(x)), len(str(y)))
    n_2 = [n // 2 , n//2+1][n%2 > 0]
    n = n if n % 2 == 0 else n + 1
    '''
    print(n_2, n)
    n = max(int(log10(x) + 1), int(log10(y) + 1))
    n_2 = int(math.ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1
    print(n_2, n)
    '''
    a, b = divmod(x, 10 ** n_2)
    c, d = divmod(y, 10 ** n_2)
    ac = main(a, c)
    bd = main(b, d)
    ad_bc = main((a+b), (c+d)) - ac -bd
    return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc)))





import random
if __name__ == '__main__':
    for i in range(1):
        x = random.randint(1, 10**12)
        y = random.randint(1, 10**12)
        expected  = x * y
        result    = main(x, y)
        ans = result == expected
        if not ans:
            print("{} * {} = {} and expected {}".format(x, y, result, expected))
    print("OK")
    print("{} * {} = {} and expected {}".format(x, y, result, expected))


