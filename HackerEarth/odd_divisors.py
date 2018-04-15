from functools import lru_cache

@lru_cache(maxsize=None)
def oddDivisorSum(n):
    """Return the sum of odd divisors of n."""
    while n % 2 == 0:
        n //= -n & n
    sum = 0
    for k in range(1, int(n ** .5) + 1, 2):
        if n % k == 0:
            sum += k
            if n // k != k:
                sum += n // k
    return sum

for _ in range(int(input())):
    print(oddDivisorSum(int(input())))
