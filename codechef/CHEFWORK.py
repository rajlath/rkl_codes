'''
Example Input
5
1 3 4 6 8
1 2 1 2 3
'''

noe = int(input())
cost = [int(x) for x in input().split()]
types= [int(x) for x in input().split()]
T = int(10e12)
A = int(10e12)
TA= int(10e12)
for i, v  in enumerate(types):
    if v==1:T = min(T, cost[i])
    elif v==2:A=min(A, cost[i])
    else:TA = min(TA, cost[i])
print(min(T+A, TA))