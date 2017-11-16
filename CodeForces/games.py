'''
4
100 42
42 100
5 42
100 5
'''
n=int(input())
a,b=zip(*(input().split()for _ in ' '*n))

print(sum(a.count(x)for x in b))
