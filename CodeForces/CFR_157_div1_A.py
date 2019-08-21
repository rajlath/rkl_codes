s = list(input())
if "0" in s:
    s.pop(s.index("0"))
else:s = s[:-1]
print("".join(s))
