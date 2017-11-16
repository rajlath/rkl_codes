'''
3
0 1 2 3 4 5
6 7 8 9 0 1
2 3 4 5 6 7

3
0 1 3 5 6 8
1 2 4 5 7 8
2 3 4 6 7 9


'''
cubes = {}
for _ in range(int(input())):
    ins = [int(x) for x in input().split()]
    for i in ins:
        cubes[i] = cubes.get(i, 0) + 1
 
ans = 0 

for i in range(10):
    if i == 0:
        if i in cubes:
            if cubes[i] < 1:                
                ans = 0
                break
    else:
        if i in cubes:            
            if cubes[i] < 2:
                ans = i * 10 + (i-1)
                break
        else:
            ans = i-1      
            
print(ans)            
        

    
