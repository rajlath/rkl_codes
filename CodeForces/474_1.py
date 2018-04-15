s = input()
ans = "YES"
if "ab" not in s and "bc" not in s:
   ans = "NO"
else:
    bindex = s.index("ab")
    cindex = s.index("bc")
    if bindex > cindex:
        ans = "NO"

print(ans)


'''
if aindex == -1:
ans = "YES"
if aindex >bindex or cindex < bindex or cindex < aindex:
    ans = "No"
else:
    acnt = s.count("a")
    bcnt = s.count("b")
    ccnt = s.count("c")
    if ccnt < acnt or ccnt < bcnt:
       ans = "NO"
print(ans)
'''


