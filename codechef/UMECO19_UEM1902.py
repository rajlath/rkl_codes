import re
pat = re.compile(r"(\+?[0-9]{2}?)?[- ]?(\(?[0-9]{3}?\)?)?[- ]?([0-9]{10})")
ins = [ x for x in input().split(",")]
ans = "Valid"
for i in ins:
    m = pat.match(i)
    if m:
        isd = m.groups()[0]
        std = m.groups()[1]
        if isd is not None and std is None:
            ans = "Invalid"
            break
    else:
        ans = "Invalid"
print(ans)

