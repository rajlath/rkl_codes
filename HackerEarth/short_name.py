'''
SAMPLE INPUT
Mohd Kafeel Khan
SAMPLE OUTPUT
M. K. Khan
'''
s = input()
lens = len(s)
spc  = s.count(" ")
had_space = True
outs = ""
for i in s:
    if spc == 0:
        outs += i
    elif i == " ":
        outs += i
        spc -= 1
        had_space = True
    else:
        if had_space:
            outs += i
            if spc >= 0:
                outs += "."
            had_space = False
print(outs)



