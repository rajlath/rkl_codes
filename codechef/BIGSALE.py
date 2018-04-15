'''
Example
Input:

2
2
100 5 10
100 1 50
3
10 10 0
79 79 79
100 1 100

Output:

30.000000000
3995.0081000
'''
for _ in range(int(input())):
    renos = int(input())
    loss  = 0.0
    for _ in range(renos):
        price, nos, discount = [int(x) for x in input().split()]
        incprice =  price + ((price * discount) / 100)
        salprice = incprice - ((incprice * discount) / 100)
        loss += nos * (price - salprice)
    print("%0.7f" % (loss))