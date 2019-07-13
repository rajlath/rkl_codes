def CorrectPath(s):
    import random
    loop = True
    while loop:
        escapeRoute=[]
        traceRoute=[]
        x=1
        y=5
        success = True
        for i in s:
            if i=="?":i=random.choice("lrud")
            if i=="u":y+=1
            elif i=="d":y-=1
            elif i=="r":x+=1
            elif i=="l":x-=1
            if (x,y) in traceRoute:
                success = False
                break
            else: traceRoute.append((x,y))
            escapeRoute.append(i)
            if x==6 or x==0 or y==0 or y==6:
                success = False
                break
        if x==5 and y==1 and success:
            loop = False

    return "".join(escapeRoute)

# keep this function call here
print(CorrectPath("???rrurdr?"))