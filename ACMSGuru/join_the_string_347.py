'''
6
it
looks
like
an
easy
problem
'''
n = int(input())
alls = []
for _ in range(n):
    alls.append(input())
print("".join(sorted(alls)))
