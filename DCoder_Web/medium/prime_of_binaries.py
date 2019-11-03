def is_prime(n):
    if n == 2 or n == 3 or n == 5:return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:return False
    for i in range(6, n+1, 6):
        if n % i == 0:return False
    return True

ins = int(input(), 2)
print(ins)
print(["Not Prime", "Prime"][is_prime(ins)])