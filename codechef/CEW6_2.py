'''
Input:

2

010 101

11 11


Output:

11

121
'''
for i in range(int(input())):
    a, b = [x for x in input().split()]
    a1 = a.count("1")
    b1 = b.count("1")
    if a1 > 0:
        a1i = int("1" * a1)
    else:
        a1i = 0
    if b1 > 0:
        b1i = int("1" * b1)
    else:
        b1i = 0
    print(a1i * b1i)
