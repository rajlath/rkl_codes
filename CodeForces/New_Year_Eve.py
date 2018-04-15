n, k = [int(x) for x in input().split()]
if k == 1:
    print(n)
else:
    ns = bin(n)[2:]
    ns = ns.replace("0", "1")
    print(int(ns, 2))