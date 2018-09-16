s = "31464141346530336F666E697278383657696E646F77735F4E543445464B4A3034312D504F544B534544"
r = ""
for i in range(0,len(s), 2):
    curr = s[i:i+2]
    r += str(int(curr, 16))
print(r)