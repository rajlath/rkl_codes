from string import ascii_uppercase as uc
import  re

def convert_1(r, c):
    d, m = divmod(int(c), 26)
    rets = uc[d - 1] + uc[m - 1]
    rets += str(r)
    return rets

def convert_2(c, r):
    col = int(c)
    cols = uc[col // 26 - 1] + uc[col % 26 - 1]
    rets = "R" + str(r) + "C" + cols
    return rets





reg1 = re.compile(r"R\d+C\d+")
reg2 = re.compile(r"([A-Z]+)(\d+)")
reg3 = re.compile(r"\d+")

for _ in range(int(input())):
    exp = input()
    if reg1.match(exp):
        row, col = re.findall(reg3, exp)
        #print(row, col)
        print(convert_1(row, col))
    else:
        matches = reg2.match(exp)
        row, col = matches.group(1), matches.group(2)
        print(convert_2(row, col))
        #print(row, col)
for n in range(int(input())):
    x = input();a=b=0
    for c in x:
        if '0' <= c<='9':b=10*b+int(c)
        elif b:
            a,b=x[1:].split('C');b=int(b);v=""
            while b: b-=1;v=chr(65+b%26)+v;b//=26
            print(v+a);break
        else:a=26*a+ord(c)-64
    else:print("R%dC%d" % (b, a))
