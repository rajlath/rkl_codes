'''
input
6 3
output
Yes
input
4 2
output
No
input
1000 1001
output
Yes
'''
a, b = [int(x) for x in input().split()]
if a == 0 and b == 0:
    print("Yes")

elif (a - (b - 1))%2 == 0:
    print("Yes")
else:
    print("No")
