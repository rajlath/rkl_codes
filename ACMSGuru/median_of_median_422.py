'''
sample input
sample output
6 4 5
7 9 8
1 2 3
5

sample input
sample output
1 2 2
4 3 2
2 3 4
3
'''
ab = []
for i in range(3):
    a= (sorted([int(x) for x in input().split()]))
    ab.append(a[1])
print(sorted(ab)[1])
