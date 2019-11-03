'''
Sample Input:
3
5 3 0 1
4
10 2 4 6
3 1 7 6
4 3 1 5 9 7
10 4 4 6
3 1 7 6
4 3 1 5 9 7
Sample Output:
3
2
3
'''
nb_Test = int(input())
for _ in range(nb_Test):
    nb, ns, x, y = [int(i) for i in input().split()]
    invalids = set()
    if x != 0:
        invalids.update([int(x) for x in input().split()])
    if y != 0:
        invalids.update([int(x) for x in input().split()])
    print(min(ns, (nb - len(invalids))))


