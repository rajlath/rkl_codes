def nearest_prime(n):
    incr = -1
    multiplier = -1
    count = 1
    while True:
        if prime(n):
            return n
        else:
            n = n + incr
            multiplier = multiplier * -1
            count = count + 1
            incr = multiplier * count

print(nearest_prime(30))