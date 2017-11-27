'''
SAMPLE INPUT
int t; //variable t
t->a=0;  //t->a does something
return 0;
SAMPLE OUTPUT
int t; //variable t
t.a=0;  //t->a does something
return 0;
'''
from sys import stdin

for lines in stdin:
    done = False
    outs =""
    first = False
    for i in range(len(lines)-1):
        if done:
            outs +=lines[i]
        else:
            if lines[i] == lines[i+1] == "/":
                done = True
                outs += "/"
                i += 1
            elif lines[i] == "-" and lines[i+1] == ">":
                outs += "."
                i += 1
            else:
                outs += lines[i]

    print(outs)
