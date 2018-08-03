'''
3
3 1 2
'''
n = int(input())
a = [int(x) for x in input().split()]
cnt = 1
while True:
    for i in range(n):
        if a[i+1]<a[i]:
            j = i+ 1
            for x in range(j, n):
                if a[x+1] > a[x]:
                    break
            

