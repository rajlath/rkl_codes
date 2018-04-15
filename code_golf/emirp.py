r,s=[x for x in range(1,1001) if str(x)==str(x)[::-1]],lambda a:int(a**0.5)
def p(n):
    for i in range(3,s(n),2):
            if n%i==0:
                return 0
print(*["\n"+str(x) for x in r if p(x)!=0 and int(str(x)[::-1]) in r ])



