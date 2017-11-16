from collections import defaultdict
nos_owl, nos_connection = [int(x) for x in input().split()]
friends = defaultdict(list)
for _ in range(nos_connection):
    self, friend = [int(x) for x in input().split()]
    friends[self].append(friend)
nos_fight = int(input()) 
 
for i in range(nos_fight):
    found = False 
    fighter1, fighter2 = [int(x) for x in input().split()]    
    if fighter1 in friends:
        for x in friends[fighter1]:
            if x == fighter2:
                print("TIE")
                found = True
                break
            elif x > fighter2:
                    print(fighter1)
                    found=True
                    break
    if not found:
        if fighter1>fighter2:
            print(fighter1)       
        else:
            print(fighter2)    
                
                    
      
    
