'''
Input:
2
3
0 1 1
3
0 1 2

Output:
2
1
'''
for _ in range(int(input())):
    noe = int(input())
    cor = [int(x) for x in input().split()]
    print(noe - max(cor))