'''
5 2
1 0 1 1 0
1 2
0 1 4
'''

noe, noq = [int(x) for x in input().split()]
s = [x for x in input().split()]

for i in range(noq):
    arr = [int(x) for x in input().split()]
    if arr[0] == 1:
        s[arr[1]-1] = ["1","0"][int(s[arr[1]-1])]  
    print(s)         
    if arr[0] == 0:
        
        r = int(arr[2])
        if s[r-1]==0:print("EVEN")
        else:print("ODD")
        
