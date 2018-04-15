'''
inputCopy
5
RUURU
output
3
inputCopy
17
UUURURRRUUURURUUU
output
13
'''
import re
rep = {"RU": "D", "UR": "D"}
rep = dict((re.escape(k), v) for k, v in rep.items())
pattern = re.compile("|".join(rep.keys()))
noe = int(input())
s = input()

while "RU" in s or "UR" in s:
    s = pattern.sub(lambda m: rep[re.escape(m.group(0))], s)
print(len(s))



