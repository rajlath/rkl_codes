R=lambda:map(int,raw_input().split())+[0]
a=[R(),R(),R(),[0]*4]
for i in (0,1,2):print ''.join(map(lambda j:"10"[(a[i][j]+a[i-1][j]+a[i][j+1]+a[i+1][j]+a[i][j-1])&1],(0,1,2)))
