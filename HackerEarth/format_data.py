'''
1
AFE DG D454 [1+5]
  AFE   12-DG    D454 [1++*B5]
 '''
from string import ascii_uppercase as uc

caps = [ord(i) for i in uc]
digs = [ord(str(i)) for i in range(10)]
oths = [x for x in range(256)]
oths = list(set(oths) - set(caps) - set(digs))
#print(caps, digs, oths)
spc  = 32
for _ in range(int(input())):
    ins  = "".join(input().split(" "))
    outs = ""
    outs += ins[0]
    ins  = ins[1:]
    for i in ins:
        curr = ord(i)
        last = ord(outs[-1])
        if curr in caps:
            if last in caps:
                outs += i
            else:
                outs += " "
                outs += i
        elif curr in digs:
            if last in digs:
                outs += i
            else:
                outs += " "
                outs += i
        else:
            if last in oths:
                outs += i
            else:
                outs += " "
                outs += i

    print(outs)



