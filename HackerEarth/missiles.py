'''
3
3
3 3 1 3 2
2 2 1 2 2
3 1 1 2 3
'''
n = int(input())
field = [[0 for x in range(n)] for y in range(n)]
nom = int(input())
for _ in range(nom):
    p,a1,a2,b1,b2 = [int(x) for x in input().split()]
    i, j = a1-1, a2-1


    for x in range(i,b1):
        for y in range(j, b2):
            field[x][y] ^= p


print(field)

