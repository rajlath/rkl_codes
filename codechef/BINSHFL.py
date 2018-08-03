'''
2
2 4
1 5

2
1
'''
def count_ones(a):
    return bin(a)[2:].count("1")

for _ in range(int(input()))    :
    a, b = [int(x) for x in input().split()]
    ab, bb = '{0:07b}'.format(a), '{0:07b}'.format(b)
    print(ab, bb)

