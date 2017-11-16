'''
2
6 3
arjit
tijra
genius
chanda
ashish
arjit
4 2
bond
coder
bond
lol
'''
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    lens = [0] * 1000
    can_be = True
    for _ in range(n):
        lens[len(input())] += 1
    for l in lens:
        if l%k != 0:
            can_be = False
            break
    print(["Not possible","Possible"][can_be])            

