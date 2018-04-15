s = input()
bindex = s.index("b")
cindex = s.index("c")
aindex = s.index("a")
ans = "Yes"
if aindex > bindex or cindex < bindex or cindex < aindex:
    ans = "No"
else:
    acnt = s[:bindex].count("a")
    bcnt = s[bindex:cindex].count("b")
    ccnt = s[cindex:].count("c")
    if ccnt in [acnt, bcnt]:
       ans = "Yes"
    else:
        ans = "No"
print(ans)