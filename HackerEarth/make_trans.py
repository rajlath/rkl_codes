s,b,a=input(),"Invalid Input","GCTA"
if all(x in a for x in s):b=s.translate(str.maketrans(a,"CGAU"))
print(b)
p = print
try:
    a += "CGAU"["GCTA".find(x)] for x in input()
    p(a)
except:
    p("Invalid Input")