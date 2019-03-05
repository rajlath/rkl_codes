def fact(n):
    if n == 1:return n
    return n * fact(n - 1)



for _ in range(int(input())):
    print( fact(int(input())) % 10)
