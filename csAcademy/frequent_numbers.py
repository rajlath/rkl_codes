'''
Frequent Numbers
Time limit: 1000 ms
Memory limit: 128 MB

You are given an array of NN integers and another integer KK. How many numbers appear in the array at least KK times?

Standard input
The first line contains two integers NN and KK.

The second line contains NN integers, representing the elements of the array.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq K \leq N \leq 10001≤K≤N≤1000
The array elements are integers between 11 and 10001000
Input	Output
3 1
1 1 1
1
5 2
1 2 3 2 1
2
6 3
1 2 2 3 3 3
1

'''
from collections import Counter
noe, k = [int(x) for x in input().split()]
arr = Counter([int(x) for x in input().split()])
cnt = 0
for i in arr:
    cnt += arr[i] >= k
print(cnt)


