from math import floor, log10
from time import time
def is_palindrome_1(x):
    if x < 0 :return False
    num_digs = int(floor(log10(x))+1)
    msd_mask = int(pow(10, num_digs-1))
    for i in range(num_digs//2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True

def is_palindrome_2(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

st = time()
print(is_palindrome_1(1234567))
print(time() - st)
st = time()
print(is_palindrome_2(12345678909876543211234567890987654321))
print(time() - st)