'''
Examples
inputCopy
5 8
outputCopy
>
inputCopy
10 3
outputCopy
<
inputCopy
6 6
outputCopy
=
from math import *
x,y=map(int,input().split())
p=y*log(x)
q=x*log(y)
if(p<q):
    print('<')
elif(p>q):
    print('>')
else:
    print('=')
'''
from math import log
a, b = [int(x) for x in input().split()]
ans = 2
if b*log(a) > a*log(b) : ans = 1
if b*log(a) < a*log(b) : ans = 0
print(["<", ">", "="][ans])
