a = input()
b = input()

#

for i in range(len(a) - len(b)+1 ):
    x = a[i:i+len(b)]
    #print(set(x).intersection(b))
    a1 = sorted(x)
    b1 = sorted(b)
    print(a1, b1)
    print(sum([c1!=c2 for c1,c2 in zip(sorted(x), sorted(b))]), end=" ")
    print(x, b)


