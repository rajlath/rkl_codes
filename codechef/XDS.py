
'''def ii():
    return int(input())
def mi():
    return map(int,input().split())
def li():
    return list(mi())


for _ in range(ii()):
    n=ii()
    b=int(n**.5)
    a=n//b
    c=n-a*b
    #print(a,b,c)
    if c!=0:
        A='X'*a+(b-c)*'D'+'X'+c*'D'
    else:
        A='X'*a+'D'*b
    print(A)
'''

for _ in range(int(input())):
    z = int(input())
    sqr = int((z ** 0.5))
    a,c = divmod(z, sqr)
    print(['X'*a+(sqr-c)*'D'+'X'+c*'D', 'X'*a+'D'*sqr][c==0])