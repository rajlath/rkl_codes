'''
n = 3
cost = 0

for i in range(-1, 10):
    n = n + (i+1)*n
    cost += n
    print(i, cost)
    0 9
1 27
2 99
3 459
4 2619
5 17739
6 138699
7 1227339
8 12113739
9 131864139

a = [3,9, 27]
x = 3
for i in range(10):
    a.append(a[-1]*x + a[-1]-a[-2])
    x += 1
print(a)


j = 1
value =  n + (j-1)*n       = n j = 2
value  = n + (j-1)*n       =2n j = 3
value  = 2n + (j-1)*2n     =6n j = 4
value  = 6n + (j-1)*6n     =24n  j = 5
value  = 24n + (j-1) * 24n  = 120n j = 6
value  = 120n+ (j-1) * 120n = 720n j = 7
value  = 720n + (j-1)*720n  =

1
2
3 3
'''
import math
mods = int(10e9 +7)
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    cost = 0
    mult = 1
    j  = 1
    for x in arr:
        cost += mult*(x)%mods
        mult =  (mult * (j+1))%mods
        j += 1

    print(cost)


'''
1 2 3 4
1*1  2 * 1*2  3 * 1 * 2 * 3     4 * 1 * 2 * 3 * 4
1 4 18 96






