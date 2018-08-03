def gcd(a, b):
    if b == 0:return a
    return gcd(b, a%b)

def unique_prime_divisor(a, b):
    while a != 1:
        a_gcd = gcd(a, b)
        if a_gcd == 1:
            break
        a //= a_gcd
    return a
def has_same_prime_divisor(a, b)        :
    gcd_value = gcd(a, b)
    x = unique_prime_divisor(a, gcd_value)
    if x != 1:
        return False
    y = unique_prime_divisor(b, gcd_value)
    return y == 1

def solution(a, b):
    count = 0
    for x, y in zip(a, b):
        if has_same_prime_divisor(x, y):
            count += 1
    return count



print(solution([15,10,9],[75, 30, 5]))
