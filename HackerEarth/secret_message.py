import string
uppers = list(string.ascii_uppercase)
lowers = list(string.ascii_lowercase)
digits = list(string.digits)

for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    dec  = input()
    enc  = ""
    for i in dec:
        if i in uppers:
            enc += uppers[(uppers.index(i) + k) % 26]
        elif i in lowers:
            enc += lowers[(lowers.index(i)+ k) % 26]
        elif i in digits:
            enc += digits[(digits.index(i) + k) % 10]
        else:
            enc += i
    print(enc)
