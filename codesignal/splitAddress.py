import re
def splita(a):
    #return re.match(r"(http[s]?)://(.*).com/(.*)?", a).groups()
    #return re.fullmatch(r"(http[s]?)://(.*).com/(.*)?", a).groups()

    #rets=re.match(r"(http[s]?)://(.*).com/(.*)?", a)
    #return rets.groups()
    h=(a[:a.index(":")])
    p=a[a.index("://")+3:a.index(".com")]
    e=a[a.index(".")+5:]
    ans= [h,p]
    if e:ans +=[e]
    return ans
    '''
    l = [i for i in a]
    p = ''.join(l)[:l.index(":")]
    d = ''.join(l)[l.index(":")+3:l.index(("."))]
    d = a.split("://")[1].split(".")[0].split("/")[0]
    if len(a) > l.index(".") + 5:
        e= ''.join(l)[l.index(".")+5:]
        return [p,d,e]
    else:return [p,d]


    print(l, p, d)
    '''

print(splita("http://stackoverflow.com/questions"))
