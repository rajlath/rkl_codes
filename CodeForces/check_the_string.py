'''
Examples
 input
aaabccc
outputCopy
YES
 input
bbacc
outputCopy
NO
 input
aabc
outputCopy
YES
'''

import re
r = re.compile(r"^(a+)(b+)(c+)$")
s = input()
ans = "NO"
m = re.match(r, s)
if m:
   if len(m.group(1))==len(m.group(3)) or len(m.group(2))==len(m.group(3)):
       ans = "YES"
print(ans)


