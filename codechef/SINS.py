'''
Sample Input:
3
5 3
10 10
4 8

Sample Output:
2
20
8
'''
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    choc = 0
    while True:
        if a == b:break
        if a == 0 or b == 0:break
        if a > b:
            a, b = a-b, b
            choc += b
        if b > a:
            a, b = a, b-a
            choc += a
    print(a + b)