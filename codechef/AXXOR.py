
def myeval(s):
    si = s.replace("+","|").replace("-","|").replace("*","|")
    sid= [int(x) for x in si.split("|")]
    print(sid)
    print(si)
    ops = []
    for i, v in enumerate(s):
        if v in ["+","-","*"]:
            ops.append(v)
    sid1 = []
    for i in range(len(ops)):
        if ops[i] == "*":
            sid1.append(sid[i]*sid[i+1])
       







print(myeval("2+3*6"))


