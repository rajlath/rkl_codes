'''
from functools import reduce
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n ** 0.5)+1) if n%i == 0)))

def next_smallest_prime_palindrome(n):
    for i in range(n, int(10e8)+1):
        i_s = str(i)
        if i_s == i_s[::-1]:
            f = factors(i)
            print(f)
            if len(f) == 2:
                return i

print(next_smallest_prime_palindrome(9989900))
'''
'''
867. Prime Palindrome

Difficulty: Medium
Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself,
and it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right
as it does from right to left.

For example, 12321 is a palindrome.

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101


Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
'''
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def is_palin(lst):
            if len(lst)==1:return True
            i = 0
            j = len(lst)-1
            while i < j:
                if lst[i] != lst[j]: return False
                i+=1
                j-=1
            return True
        def get_digits(n):
            return [x for x in str(n)]
        def is_prime(n):
            if n <= 1: return False
            if n <= 3: return True
            if not n%2: return False
            if not n%3: return False
            i = 5
            while i * i <= n:
                if not n%i or not n%(i+2):return False
                i += 6
            return True

        if N < 100:
            i = N
            while True:
                if is_prime(i) and is_palin(get_digits(i)):
                    return i
                i += 1
        else:
            i = N
            while True:
                lst = get_digits(i)
                if is_prime(i):
                    if not len(lst) % 2:
                        i = pow(10, len(lst))
                        continue
                    if is_palin(lst):return i

#python 2 solution
#
class Solution(object):
    def __init__(self):
        self.primes = [2, 3, 5, 7]

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = len(str(N))
        a = 10**((d-1)//2)
        b = 10*a
        while True:
            s = str(a)
            n = int(s + s[-1-(d%2)::-1])
            if n >= N and self.is_prime(n):
                return n
            a += 1
            if a == b:
                if d % 2: a /= 10
                else: b *= 10
                d += 1


    def is_prime(self, x):
        if x < 2: return False
        while self.primes[-1]**2 < x:
            self.primes.append(self.next_prime())
        for p in self.primes:
            if p * p > x: break
            if x % p == 0: return False
        return True

    def next_prime(self):
        p = self.primes[-1] + 2
        while not self.is_prime(p):
            p += 2
        return p
        


print(Solution().primePalindrome(8))


