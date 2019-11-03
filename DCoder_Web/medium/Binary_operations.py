a, b = [x for x in input().split()]
ai = int(a, 2)
bi = int(b, 2)
print(bin(ai + bi)[2:])
print(bin(ai * bi)[2:])