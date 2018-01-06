def sum_divisors(n):
    """Return a list of the sums of divisors for the numbers below n.

    >>> sum_divisors(10) # https://oeis.org/A000203
    [0, 1, 3, 4, 7, 6, 12, 8, 15, 13]

    """
    result = [1] * n
    result[0] = 0
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m    # (B)
                    result[i] *= m          # (B)
                last_m = m
                p_power *= p
    return result
    
print(sum_divisors(20))    
