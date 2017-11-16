'''
2
3 4
1 1 1
6 2
1 0 1 1 0 0
'''
from copy import deepcopy
for i in range(int(input())):
    nos_lan, nos_hours = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]    
    for i in range(nos_hours):
        tmp =  [0] * nos_lan        
        tmp[0] = [0, 1][arr[1]==1]
        tmp[-1]= [0, 1][arr[-1]==1]
        for i in range(1, len(tmp)-1):
            tmp[i] = [0,1][arr[i-1] == arr[i+1] == 1]        
        arr = deepcopy(tmp)  
        if set(tmp) == [0]:break
    print(" ".join(map(str,arr)))      
