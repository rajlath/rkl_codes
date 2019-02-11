from math import ceil
x, y=map(int, input().split())
t=input()
a=ceil(sum([ceil(int(i)/y) for i in t.split()])/2)
print(a)