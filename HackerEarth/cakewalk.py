'''
2
7
34 67 87 23 45 67 33
4
345 678 5654 876
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    print(sum([1 for x in arr if x%2]))

4 2 5 1 3 6
4 5 2 6 3 1
output
1 2 4 5 3 6
2l 12 2f 

example 2
input
19 13 1 69
19 13 69 1
output
1 13 19 69