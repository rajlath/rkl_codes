'''
2
5
12 13 -4 3 2
6
15
11
13
2
3
12
6
12 3 -67 67 34 2
4
4
5
67
7
'''
import sys
for _  in range(int(input())):
    noe = int(input())
    arr = [x for x in sys.stdin.readline().strip().split()]    
    for _ in range(int(input())):
        curr = sys.stdin.readline()
        if curr in arr:
            print("Yes")
        else:
            print("No")    
        
