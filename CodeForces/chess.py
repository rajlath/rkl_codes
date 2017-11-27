'''
Examples
input
3
1
1
2
output
YES
input
2
1
2
output
NO
'''
last = [1,2]
result = "YES"
for _ in range(int(input())):
    nexts = int(input())
    if nexts not in last:
        result = "NO"
        break
    else:
        if nexts == 1:
            last = [1, 3]
        elif nexts == 2:
            last = [2, 3]
        else:
            last = [3, 1]
print(result)

