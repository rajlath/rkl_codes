from datetime import datetime
def fibo_1(n):
    '''
    recursively find nth fibonacci number
    '''
    if n < 2 : return n
    return fibo_1(n - 1) + fibo_1(n - 2)

def fibo_2(n):
    '''
    iteratively find nth fibonacci number
    '''
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


from math import floor
def fibo_3(n):
    '''
    approximation process to find nth fibonacci, reliable upto 70th fibo
    '''
    sq5 = 5 ** 0.5
    phi = (1 + sq5) / 2
    return int(floor(phi ** n / sq5))



def fibo_4(n)    :
    '''
    using recurrance relationship
    '''
    def fib_pair(n):
        if n == 0: return (0, 1)
        else:
            (x, y) = fib_pair(n - 1)
            return (x+y, x)
    (x, y) = fib_pair(n)
    return x

def fibo_5(n, cache={0:1, 1:1}):
    if n in cache: return cache[n]
    res = fibo_5(n - 1, cache) + fibo_5(n - 2, cache)
    cache[n] = res
    return res

print(fibo_1(10))
s = datetime.now()
print(fibo_2(70))
print(datetime.now() - s)
s = datetime.now()
print(fibo_3(70))
print(datetime.now() - s)
s = datetime.now()
print(fibo_4(70))
print(datetime.now() - s)
s = datetime.now()
print(fibo_5(69))
print(datetime.now() - s)
