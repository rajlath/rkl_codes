import re
x=re.findall('([AEIOUaeiou]{2,})',input())
for a in x:
    if len(a)>1:
        print(a)