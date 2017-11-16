'''
SAMPLE INPUT 
6
1 2 2 1 2 3
5
0 1
0 2
1 2
1 3
0 3
SAMPLE OUTPUT 
1
1
1
2
2
'''
import sys
noe = int(input())
arr = sys.stdin.readline().split()
arrs = set()
dcnt = {}
maxcnt = 0
#for i in arr:dcnt[i] = 0

for i in arr:    
    dcnt[i] = dcnt.get(i, 0) + 1
    maxcnt = max(maxcnt, dcnt[i])
    
for i in dcnt:arrs.add(dcnt[i])
#print(dcnt, arrs, maxcnt)    
for i in range(int(input())):
    ops, val = sys.stdin.readline().split()
    ops, val = int(ops), int(val)
    if ops == 0:
        if val <= maxcnt:
            for i in arr:
                if dcnt[i] >= val:
                    print(i)
                    break
        else:
            print("0") 
    else:
        if val in arrs:
            
            for i in arr:
                
                if dcnt[i] == val:
                    print(i)
                    break
        else:
            
            print("0")                        
    
