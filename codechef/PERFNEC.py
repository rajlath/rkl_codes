'''
1 2 2 3 4
3
2 0
1 -2
3 6
'''
max_cost = int(10e12)
S,G,Q,R,D = [int(x) for x in input().split()]
cost = [[max_cost for x in range(402)] for y in range(201)]

for i in range(100):
    for j in range(100 - i):
        for  k in range(100-(i+j)):
            for l in range(100 -(i+j+k)):
                for m in range(100 - (i+j+k+l)):
                    counts = i + j + k + l + m
                    price  = i * S + j * G + k * Q + l * R + m * D
                    beauty = i * (-2) + (-j) + l + m * 2
                    cost[counts][beauty+200] = min(cost[counts][beauty], price )
                print(i, j, k, l, m)
Q = int(input())
for i in range(Q):
    x, y = [int(x) for x in input().split()]
    print([-1,cost[x][y]][cost[x][y] != max_cost])


