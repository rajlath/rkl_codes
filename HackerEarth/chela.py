r,i=range,input
def p(n):
    for i in r(2,int(n**0.5)+1):
        if n%1==0:return 0
    return 1
for _ in r(i()):
    n=i()
    while 1:
        n+=1
        if p(n):
            print(n)
            break
