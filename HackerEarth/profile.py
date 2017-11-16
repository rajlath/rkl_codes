size = int(input())
no_of_pics = int(input())
for i in range(no_of_pics):
    w, h = [int(x) for x in input().split()]
    if w<size or  h<size:
        print("UPLOAD ANOTHER")
        continue
    elif w>=180 and  h>=180:
        if w == h :
            print("ACCEPTED")
            continue
    print("CROP IT")
    
            
'''
SAMPLE INPUT 
1
8
2 2
1 1
1 2
2 1
11 11
11 12
12 11
12 12

CROP IT
CROP IT
CROP IT
CROP IT
CROP IT
CROP IT
CROP IT
CROP IT

ACCEPTED
ACCEPTED
CROP IT
CROP IT
ACCEPTED
CROP IT
CROP IT
ACCEPTED
'''                
            
             
        
