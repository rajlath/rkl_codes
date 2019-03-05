'''
a, b = [int(x) for x in input().split()]
if b < a:
    a, b = b, a
for i in range(a + 1, b + 2):
    print(i)
    '''
a, b = [int(x) for x in input().split()]
for i in range(min(a,b) + 1, max(a, b) + 2)    :
    print(i)