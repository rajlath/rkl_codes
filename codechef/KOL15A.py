'''
Input:
1
ab1231da

Output:
7
'''
for _ in range(int(input())):
    print(sum(int(x) for x in input() if x.isdigit()))