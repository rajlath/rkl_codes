'''
1
4
2 2 3 7
'''
for i in range(int(input())):
    nos = int(input())
    choc= [int(x) for x in input().split()]
    mins = min(choc)
    res = 10e9
    for i in range(-5, 1):
        temp = 0
        for j in range(nos):
            delta = choc[j] - i - mins
            temp += delta/5 + delta%5/2 + delta%5%2
        res = min(int(temp), res)
    print(res)
