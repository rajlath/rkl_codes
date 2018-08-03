import math
import timeit
def sqrt(c):
    if not c < 0:
        err = 1e-15
        t = c
        while abs(t - c/t) > err * t:
            t = (c/t + t)/2
        return t
st = timeit.timeit()
print(sqrt(-123456789123456789123456789123456789))
print(timeit.timeit() - st)
st = timeit.timeit()
print(math.sqrt(-123456789123456789123456789123456789))
print(timeit.timeit() - st)