'''
Sample Input

5
20 7 8 2 5
Sample Output

2
'''

lens = int(input())
indices = {}
prices = [int(x) for x in input().split()]
for i, x in enumerate(prices):
    indices[prices[i]] = i
prices = sorted(prices)

min_loss = 10e9
i = lens - 1
while i > 0:
    if prices[i] - prices[i-1] < min_loss:
        if indices[prices[i]] < indices[prices[i-1]]:
            min_loss = prices[i] - prices[i-1]
    
    i -= 1

    
print(min_loss)            

        
        



