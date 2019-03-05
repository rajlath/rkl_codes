mods = 1000000007

def fast_exp(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mods
        base = (base * base) % mods
        exp >>= 1
    return res % mods
nb_test = int(input())
for _ in range(nb_test):
    curr = int(input())
    if curr == 1:
        print(0)
        continue
    e = (curr * (curr - 1)) // 2
    print(int(fast_exp(2, e - 1)))
