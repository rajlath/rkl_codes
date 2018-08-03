'''
Examples
inputCopy
3
101
outputCopy
Yes
inputCopy
4
1011
outputCopy
No
inputCopy
5
10001
outputCopy
No
'''
noe = int(input())
ins = "0"+input()+"0"
print("NO" if ("11" in ins or "000" in ins ) else "YES")
