'''
Examples
inputCopy
mew
outputCopy
3
inputCopy
wuffuw
outputCopy
5
inputCopy
qqqqqqqq
outputCopy
0
'''
s = input()
'''
left=len(s)
for i in range(len(s)-1, -1, -1):
    if s[i] != s[0]:
        break
    else:left -=1
print(left)
'''
if s != s[::-1]:print(len(s))
elif len(set(s)) == 1: print(0)
else: print(len(s) - 1)
