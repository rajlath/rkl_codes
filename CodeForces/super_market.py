'''
3 5
1 2
3 4
1 3
1.66666667
2 1
99 100
98 99
output
0.98989899
'''
n, m = [int(x) for x in input().split()]
mins = int(10e9 + 7)
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    mins = min(mins, a/b*m)
print('{0:.8f}'.format(mins))