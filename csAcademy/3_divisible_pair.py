'''
3-divisible Pairs
Time limit: 1000 ms
Memory limit: 128 MB

You are given an array of NN positive integers. Compute the number of pairs of integers in the array that have the sum divisible by 33.

Standard input
The first line contains one integer NN.

The second line contains NN integers representing the elements of the array.

Standard output
Output a single number representing the number of pairs that have the sum divisible by 33.

Constraints and notes
1 \leq N \leq 10^51≤N≤10
​5
​​
The elements of the array are integers between 11 and 10^510
​5
​​ .
Input	Output
5
1 4 2 3 3
3
4
3 3 3 6
6
8
1 1 7 2 11 3 6 9
9



'''

n = int(input())
a = [int(x) for x in input().split()]
d = {i:0 for i in range(3)}
for i in a:d[i%3] += 1
print( (d[0] * (d[0]-1))//2 + d[1] * d[2] )
