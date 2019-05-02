import math

def primeFactors(n):
    facts = set()
    while n % 2 == 0:
        facts.add(2)
        n = n // 2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
           facts.add(i)
           n //= i

    if n > 2:
        facts.add(n)
    return facts

print(primeFactors(5))
f = math.factorial(5)
sums =  (5  * 6)  // 2
print(f, sums, f% sums)
print(primeFactors(sums))