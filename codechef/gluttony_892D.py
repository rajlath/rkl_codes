'''
shuffle an array of integer such that new
new array formed by shuffling will not have any
subset whose sum is equal to sum of same indexed subset
of the original array

Examples
input
2
1 2
output
2 1
input
4
1000 100 10 1
output
100 1 1000 10


'''
n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
shifted_sorted_a = [sorted_a[-1]] + sorted_a[:-1]
for i in range(len(a)):
    pos_in_sorted = sorted_a.index(a[i])
    print(shifted_sorted_a[pos_in_sorted], end=" ")