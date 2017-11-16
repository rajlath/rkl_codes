'''
5
popcorn
corn
killme
mekill
gameofthrones
thronesofgame
ilovesports
sportiloves
opposite
road

3
0
0
0
10

6
0
0
0
14
'''
for _ in range(int(input())):
    a = list(input())
    b = list(input())
    diff = 0
    for x in a:
        if x in b:b.remove(x)
        else:
            diff += 1
    diff += len(b)
    print(int(diff))            
    
    
