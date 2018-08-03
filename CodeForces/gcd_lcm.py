def gcd(a, b):
    if a % b == 0:return b
    else:return gcd(b, a%b)


def lcm(a, b):
    return (a * b) // gcd(a, b)

print(gcd(2, 6), lcm(2, 6))