fibonacci = {}
def get_fib(n):
    if n < 2: return n
    if n in fibonacci: return fibonacci[n]
    fibs = get_fib(n-1) + get_fib(n-2)
    fibonacci[n] = fibs
    return fibs



print(get_fib(123))

