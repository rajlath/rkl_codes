#copied
import operator
q=int(input())
s={}
for i in range(1, q+1):
    t, d = map(int, input().split())
    s[i] = t+d
s= sorted(s.items(), key=operator.itemgetter(1))
 
for x in s:
    print(x[0], end=' ')
