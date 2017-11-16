'''
13
14 16
30 31
45 46
19 20
15 17
66 67
75 76
95 97
29 30
37 38
0 2
36 37
8 9
'''
cnt = 0
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    cnt += (b-a)>2
print(cnt)    
