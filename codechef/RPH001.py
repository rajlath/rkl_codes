'''
1
21 1
'''
for _ in range(int(input())):
    a, b = [x for x in input().split()]
    answ = int(str(int(str(a)[::-1]) + int(str(b)[::-1])   )[::-1])
    print(answ)