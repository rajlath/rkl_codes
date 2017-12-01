'''
Find and list all four-digit numbers in decimal notation that have the property that the sum of
their four digits equals the sum of their digits when represented in hexadecimal (base 16) notation
and also equals the sum of their digits when represented in duodecimal (base 12) notation.
For example, the number 2991 has the sum of (decimal) digits 2 + 9 + 9 + 1 = 21. Since 299
1 = 1*1728 + 8*144 + 9*12 + 3, its duodecimal representation is 1893, and these digits also sum
up to 21. But in hexadecimal, 2991 is BAF16, and 11 + 10 + 15 = 36, so 2991 should be rejected
by your program.
The next number (2992), however, has digits that sum to 22 in all three representations (including
BB016), so 2992 should be on the listed output. (We don’t want decimal numbers with fewer
than four digits—excluding leading zeros—so that 2992 is the first correct answer.)

input : an integer number
output : consecutive specialized four_digit number counted for input

'''
from sys import stdin, stdout

import string
def int2base(integer, base):
        if not integer: return '0'
        sign = 1 if integer > 0 else -1
        alphanum = string.digits + string.ascii_lowercase
        nums = alphanum[:base]
        res = ''
        integer *= sign
        while integer:
                integer, mod = divmod(integer, base)
                res += nums[mod]
        return ('' if sign == 1 else '-') + res[::-1]
conv = {"0":0, "1":1, "2":2,"3":3, "4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
def sum_digits(n):
    ns = str(n)
    while (len(ns)>2):
        n = sum([conv[x] for x in ns])
        ns = str(n)
    return ns

#print(int2base(2991, 12))
#print(sum_digits(1893))

cnt = int(stdin.readline())
start = 2990
done = 0
while done < cnt:
    start += 1
    a = sum_digits(start)
    b = sum_digits(int2base(start, 12))
    c = sum_digits(int2base(start, 16))
    if a == b == c:
         print(start)
         done += 1






