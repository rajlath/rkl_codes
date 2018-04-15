def prime_factors(n, unique=False):
    '''
    prime factors of an integer
    param n : integer number
    unique  : return only unique factors
    rets list of factors
    '''
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n//=2
    ends = int(n ** 0.5) + 1
    for i in range(3, ends, 2):
        while n % i == 0:
            factors.append(i)
            n//=i
    if n > 2:
        factors.append(n)
    if unique:
        return list(set(factors))
    else:
        return factors

pf = []
for i in range(2, 100):






