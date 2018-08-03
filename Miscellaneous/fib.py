def fib(n):
    '''
    prints nth fibonacci numbers in sequence
    param  : n  Int
    return : array of int which are fibonacci numbers
    '''
    f = 0
    g = 1
    fibs = []
    for i in range(n+1):
        fibs.append(f)
        f += g
        g =  f - g
    return fibs[n]

#print(fib(10))

def sum_till_n(n):
    sums = 0
    for i in range(n+1):
        for j in range(i):
            sums+=1
    return sums

#print(annon(10))

def recursive_sum_till(n):
    sums = 0
    for i in range(n+1):
        for j in range(n+1):
            sums += 1
    return sums

#print(recursive_sum_till(100))

