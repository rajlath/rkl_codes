'''
input
3
1 1 0
1 1 1
1 0 0
output
2
input
2
1 0 0
0 1 1
output
1
'''
ans = 0
for _ in range(int(input())):
    ans += sum([int(x) for x in input().split()]) > 1
print(ans)    