
offsets = [-11,11,9,7,5,3,1,-1,-3,-5,-7,-9]
seats   = ["WS","WS","MS","AS","AS","MS","WS","WS","MS","AS","AS","MS",]

    
for i in range(int(input()))   :
    offs = int(input())
    off  = offs % 12
    print(offs + offsets[off], seats[off])
        
'''
10
19
29
96
33
24
38
66
47
12
4

18 WS
32 MS
85 WS
28 AS
13 WS
47 MS
67 WS
39 MS
1 WS
9 AS

18 WS
32 MS
85 WS
28 AS
13 WS
47 MS
67 WS
38 MS
1 WS
9 AS
'''
