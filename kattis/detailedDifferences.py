nb_test = int(input())
for _ in range(nb_test):
    src = input()
    tgt = input()
    print(src)
    print(tgt)
    print("".join(["." if x == y else "*" for x, y in zip(src, tgt) ]))