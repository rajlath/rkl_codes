'''
10
41
13 18 14 16 16 4 13 11 11 3 0 13 1 7 5 11 14 1 1 3 9 0 13 18 16 1 16 12 16 0 11 13 5 7 1 6 13 1 7 0 14 
13 7 6 13 14 11 12 9 8 3 3 19 4 10 5 0 8 11 0 3 15 18 12 17 1 13 19 0 5 13 4 10 5 14 8 5 19 17 8 6 0 
40
5 18 19 16 16 6 14 5 11 10 6 2 19 11 17 17 16 9 4 4 12 15 6 15 17 0 17 0 14 5 12 2 18 5 19 10 11 0 8 11 
12 3 7 18 8 16 11 18 12 5 1 12 6 16 14 1 3 10 5 5 10 5 8 2 16 11 9 1 10 10 8 15 0 0 13 15 6 4 11 6 
7
18 3 6 15 2 0 15 
10 3 19 6 7 7 19 
17
12 9 9 17 18 3 11 10 5 19 0 11 16 13 1 0 18 
11 14 6 18 0 18 7 17 12 15 2 7 17 12 3 1 6 
30
15 8 19 7 1 7 12 14 3 10 6 7 13 18 5 9 2 13 3 13 12 14 18 12 11 9 2 4 2 11 
6 13 7 9 19 13 0 19 2 17 1 11 7 1 2 19 4 0 16 6 17 14 2 19 2 6 19 16 19 12 
13
18 12 19 17 13 15 18 14 19 13 14 11 10 
9 16 4 16 8 12 5 0 12 8 5 18 12 
18
14 16 14 11 8 0 10 10 4 16 15 2 7 11 19 16 5 19 
9 15 14 18 18 4 6 14 17 4 13 11 7 1 15 5 10 9 
16
1 18 19 16 8 14 12 5 15 0 8 1 9 2 13 3 
15 16 10 7 10 6 15 3 14 14 14 2 10 9 16 0 
28
2 3 9 16 16 9 13 7 7 2 15 4 10 7 4 18 12 8 10 5 11 15 10 17 10 3 16 17 
8 9 11 19 14 12 3 8 5 14 6 8 7 0 11 5 1 6 17 13 8 7 15 1 17 7 13 11 
37
18 3 10 18 8 15 14 7 2 9 14 10 13 4 13 4 15 9 15 16 16 5 18 14 4 1 6 13 11 3 4 3 10 18 3 16 14 
5 10 15 17 10 0 7 15 0 8 14 7 8 9 13 14 10 4 10 14 16 16 0 16 0 10 8 18 10 19 2 7 11 6 16 3 5 

Tie
Rupam
Ankit
Tie
Ankit
Rupam
Ankit
Ankit
Rupam
Rupam

Rupam
Rupam
Ankit
Tie
Ankit
Rupam
Ankit
Ankit
Rupam
Rupam
'''
import operator
for _ in range(int(input())):
    noe = int(input())
    rupam = sorted([int(x) for x in input().split()])
    ankit = sorted([int(x) for x in input().split()])    
    rupam_count  = {}        
    ankit_count  = {}
    
    
    
    for i, v in enumerate(rupam):        
        rupam_count[i] = rupam_count.get(i, 0) + 1         
        ankit_count[ankit[i]] = ankit_count.get(ankit[i], 0) + 1
    
   
    rupam_max = max(rupam_count.keys())
    ankit_max = max(ankit_count.keys())
    
    if rupam_count[rupam_max] > ankit_count[ankit_max]:
        print("Rupam")
    elif ankit_count[ankit_max] > rupam_count[rupam_max]:
        print("Ankit")    
    else:
        print("Tie")    
    
    
        
        
