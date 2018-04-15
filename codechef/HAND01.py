'''
 for i in range (a):
        if(str1[i]=='!'):
            b=b+'*'
        elif(str1[i]=='?'):
            b=b+'-'
        elif(str1[i]=='%'):
            b=b+'+'
        elif(str1[i]=='$'):
            b=b+'/'
        else:
            b=b+str1[i]
'''
dicts = {"!":"*", "?":"-","%":"+","$":"/"}
for _ in range(int(input())):
    print(eval("".join([dicts[x] if x in dicts else x for x in input()])))