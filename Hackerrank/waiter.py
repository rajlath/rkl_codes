def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

primes = sundaram3(8000)

N, Q = map(int, raw_input().split())
numbers = map(int, raw_input().split()) 
stack = []

for value in numbers:
    if value % primes[0] != 0:
        stack.append(value)
    else:
        print value
     
     
for prime_idx in xrange(1, Q):
    leftover = []
    while stack:
        value = stack.pop()
        if value % primes[prime_idx] != 0:
            leftover.append(value)
        else:
            print value
        stack = leftover
     
for value in stack:
    print value       