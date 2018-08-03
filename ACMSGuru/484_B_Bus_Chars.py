'''
6
10 8 9 11 13 5
010010011101
'''
n=int(input())

i=iter(sorted(zip(map(int,input().split()),range(1,n+1))))
s,o=[],[]
for c in input():
 if c=='0':
  x=next(i)[1];o.append(x);s.append(x)
 else:o.append(s.pop())
 print(o, s)
print(*o)
