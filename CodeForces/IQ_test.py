#http://codeforces.com/problemset/problem/25/A

'''
input
5
2 4 7 8 10
output
3
input
4
1 2 1 1
output
2
'''

n=input()
d=[int(i)%2 for i in input().split()]
print(d.index(d.count(1)==1)+1)
