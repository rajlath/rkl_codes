
print([len(x) for x in "100110000111110".split("0")])
mod = int(10e9 + 7)
nb_test = int(input())
for _ in range(nb_test):
    n = int(input())
    a = ((n * (n + 1)) // 2) % mod
    print(a)