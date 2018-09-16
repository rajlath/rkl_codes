def fib(a, cache={0:0,1:1}):
    if a in cache: return cache[a]
    res = fib(a-1, cache) + fib(a-2, cache)
    cache[a] = res
    return res

print(fib(70))