'''
1 7 3

correct solution
'''

a, b, c = [int(x) for x in input().split()]

if a == b :print("YES")
elif a > b and c > 0 or a < b and c < 0:print("NO")
elif c == 0: print(["NO", "YES"][a == b])
else:print(["NO", "YES"][(b - a)%c == 0])    

