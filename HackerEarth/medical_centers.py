'''
SAMPLE INPUT 
4 2 5
10 51 45 24
50 77 98 12
23 62 33 65
89 41 36 78
17 23 76 54
40 50 10 30
SAMPLE OUTPUT 
3 2
'''

could_be, will_be, client_count = [int(x) for x in input().split()]
client_budget =  [[0]*could_be]
for _ in range(client_count):
    client_budget.append([int(x) for x in input().split()])

    
cost_needed = [int(x) for x in input().split()]

for x in range(could_be):
    for y in range(client_count+1):
         
        client_budget[0][x] += client_budget[y][x] 
        
         
profits = [(x - y) for x,y in zip(client_budget[0], cost_needed)]
profits_sorted = sorted(profits, reverse=True)
print(profits.index(profits_sorted[0])+1, profits.index(profits_sorted[1])+1 )

    
    
    
