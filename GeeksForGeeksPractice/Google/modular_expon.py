def modpow(x, n, m):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return modpow(x * (x % m), n // 2, m) % m
    elif n % 2 == 1:
        return (x * modpow(x * (x % m), (n - 1) // 2, m)) % m

print(modpow(10, 9, 6))
