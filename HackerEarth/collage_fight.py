'''
5 5
3 4 4 2 1
4 3 2 1 2
'''
an, bn = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
b = sorted(b)

for i in range(an):
    le = 0
    en = bn - 1
    f=0
    while le<=en:
        mid=(le+en)//2
        if b[mid]<=a[i]:
            le=mid+1
        else:
            en=mid-1
        f=le
    print(bn - f,end=" ")