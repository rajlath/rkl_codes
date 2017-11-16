'''
4
2 3 4 1
'''

gifts = {}
nos = int(input())
friends = [int(x) for x in input().split()]
for i, v in enumerate(friends):
    gifts[v] = i+1
giftss = sorted(gifts)
for i in giftss:
    print(gifts[i], end=" ")    
