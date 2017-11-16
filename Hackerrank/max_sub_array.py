'''
Sample Input

1
5 7
3 3 9 9 5
Sample Output

6

'''


for _ in range(int(input())):
    noe, mods = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    max_so_far = -1 * 10000
    current_max= -1 * 10000
    max_sum = 0
    
    for i in range(1, noe):
        current_max = max(current_max, current_max + arr[i]) % mods
        max_so_far  = max(max_so_far, current_max) % mods
        if arr[i] > 0: max_sum += arr[i] 
        
    
    print(max_so_far)
    

    
    
       
