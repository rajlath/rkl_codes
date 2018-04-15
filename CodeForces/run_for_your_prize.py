'''
Examples
input
3
2 3 9
output
8
input
2
2 999995
output
5
'''

input()
#print(max(min(x-1,10**6-x)for x in map(int,input().split())))
lst = [min(x-1,10**6-x)for x in map(int,input().split())]
print(lst)


