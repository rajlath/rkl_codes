'''
input
3 17 4
output
13
'''
n, k, w = [int(x) for x in input().split()]
cost = 0
for i in range(1, w+1):
    cost += n * i
if k > cost:
    print("0")
else:
    print(cost - k)       
