'''
2
5
2 4 2 5 6
4
2 2 2 2
'''

for _ in range(int(input())):
    noe = int(input())
    edist = sorted([int(x) for x in input().split()])
    
    will_die =0
    dist = 1
    killed = 0
    for i in edist:
        if i < dist:
            will_die = True
            break
        else:
            killed+=1
            dist+=1
        if killed%6==0:dist+=1    
            
    if will_die:
        print("Goodbye Rick")
        print(killed)
    else:
        print("Rick now go and save Carl and Judas")         
    
    
