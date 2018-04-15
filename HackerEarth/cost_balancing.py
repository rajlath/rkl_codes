'''
Sample Input 0

7 5
1 200
2 200
3 100
4 10
5 54
5 54
3 100
Sample Output 0

1 54
2 57
3 57
4 -133
5 -35
'''
tc, fc = [int(x) for x in input().split()]
frnds  = [0] * (fc)
total  = 0
for i in range(tc):
    a, b = [int(x) for x in input().split()]
    frnds[a-1] += b
    total += b
offset  =  (total%fc)
#frnds[0] += offset
share = total//fc
print("{} {}".format(1, frnds[0]-share-offset))

for i in range(fc):
    print("{} {}".format(i+1, frnds[i]-share))