ins = input()
indx= ins.find("00000")
if indx != -1:
    ins = ins[:indx]
print(sum([int(x) for x in ins]) // 3)
