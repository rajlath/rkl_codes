import math
def proper_divisors(n):
    if n == 1:return 1
    sums = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if i == n / i:
                sums += i
            else:
                sums += i + n // i
        return sums
for _ in range(int(input()))                 :
    print(proper_divisors(int(input())))
