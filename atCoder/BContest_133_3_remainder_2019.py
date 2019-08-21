L, R = [int(x) for x in input().split()]
if R - L >= 2019:
    print(0)
else:
    mins = 2019
    L%= 2019
    R%= 2019
    for i in range(L, R):
        for j in range(i+ 1, R+1):
            mins = min(mins, (i * j) % 2019)
print(mins)            
            
    