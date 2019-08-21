for _ in range(int(input())):
    has = input()[::-1]
    chk = input()[::-1]
    indx = chk.index("1")
    print(has.index('1', indx) - indx)


'''
1
1010101010101
11110000
10101010
2
'''
