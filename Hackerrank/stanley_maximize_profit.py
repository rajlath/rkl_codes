'''
Sample Input 0

5 10 3
2 3 4 1 5
1 3 2 4 5
Sample Output 0

250
n, m, k where 
n is the number of currencies excluding bitcoin,
m is the amount of bitcoins Ron has and
k is the conversion rate of bitcoin w.r.t dollar.
'''
nos_currency, nos_btcoin, dollar_per_btcoin = [int(x) for x in input().split()]
price_other = [int(x) for x in input().split()]
btcoin_multiple = [int(x) for x in input().split()]
max_value = nos_btcoin * dollar_per_btcoin
for i, v in enumerate(price_other):
    max_value = max(max_value, (nos_btcoin * btcoin_multiple[i] * v))
print(max_value)    



