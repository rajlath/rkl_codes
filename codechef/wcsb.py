nb_test = int(input())
for _ in range(nb_test):
    nb_elem, nb_qry = [int(x) for x in input().split()]
    elements = [int(x) for x in input().split()]
    xors = [0]
    for i in elements:
        xors.append(i ^ xors[-1])
    for _ in range(nb_qry):
        l, r = [int(x) for x in input().split()]
        print(xors[r]^xors[l-1]^(2 ** 31 - 1))