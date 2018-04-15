from math import factorial
for _ in range(int(input())):
    n = int(input())
    box, rest = divmod(n, 7)
    somersault = 7 * factorial(box) + rest
    print(somersault)