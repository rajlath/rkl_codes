for i in range(int(input())):
    r,t = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l=range(len(a)+1)
    b = [sum(a[i:j])for i in l[:-1]for j in l[i:]]
    print(max([x//r for x in b if x%r==0]))




