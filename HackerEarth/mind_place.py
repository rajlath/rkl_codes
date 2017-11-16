'''
SAMPLE INPUT 
5 5
-10 -5 -3 4 9
-6 -2 0 5 10
-4 -1 1 6 12
2 3 7 8 13
100 120 130 140 150
3
0
-2
170
SAMPLE OUTPUT 
1 2
1 1
-1 -1
'''
n, m= [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
for i in range(int(input()))   :
    needed = int(input())    
    r = m - 1
    c = 0
    while True:
        if needed < matrix[0][0] or needed > matrix[n-1][m-1] or r < 0 or c > n-1:
            print("-1 -1") 
            break          
        elif matrix[c][r] == needed:
            print(c, r)
            break        
        else:
            if needed < matrix[c][r]: r-= 1
            else: c+=1
        
                
            
    
    
    
    
