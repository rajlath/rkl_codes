# Python 3 Program to find sum of
# Fibonacci numbers in O(Log n) time.

MAX = 1000

# Create an array for memoization
f = [0] * MAX

# Returns n'th Fibonacci number
# using table f[]
def fib(n):

    n = int(n)

    # Base cases
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return (1)

    # If fib(n) is already computed
    if (f[n] == True):
        return f[n]

    k = (n+1)/2 if (n & 1) else n/2

    # Applying above formula [Note value n&1
    # is 1 if n is odd, else 0].
    f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) if (n & 1) else (2 * fib(k-1) + fib(k)) * fib(k)
    return f[n]

# Computes value of first Fibonacci numbers
def calculateSum(n):

    return fib(n+2) - 1

print(calculateSum(2000))