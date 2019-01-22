nb_cashier = int(input())
peoples = [int(x) for x in input().split()]
mins = int(1e6)
for i in range(nb_cashier):
    curr = sum([int(x) * 5 for x in input().split()])
    curr += peoples[i] * 15
    mins = min(mins, curr)
print(mins)    
    
    
    