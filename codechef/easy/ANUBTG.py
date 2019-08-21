for _ in range(int(input())):
    nb_items = int(input())
    costs = sorted([int(x) for x in input().split()], reverse=True)
    
    bill  = sum([x for i, x in enumerate(costs) if i%4==0 or i%4 == 1])
    print(bill)
