'''
input
3
4
940
4444
output
Case #1: 3 1
Case #2: 930 10
Case #3: 3333 1111
'''
nb_test = int(input())
for indx in range(nb_test):
    ins = input()
    lens = len(ins)
    less = []
    more = []
    for i in range(lens):
        l = ins[lens - i - 1]
        if l == "4":
            less.append('3')
            more.append('1')
        else:
            less.append(l)
            more.append('0')
    while more[-1] == "0":more.pop()
    less = less[::-1]
    more = more[::-1]
    ansa = int(''.join(less))
    ansb = int(''.join(more))
    print("Case #{}: {} {}".format(indx+1, ansa, ansb))




