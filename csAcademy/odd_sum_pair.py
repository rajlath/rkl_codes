'''
Odd Sum
Time limit: 1000 ms
Memory limit: 256 MB

You are given an array AA of NN integers. Count the number of ways you can choose a pair (i, j)(i,j), 1 \leq i <j \leq N1≤i<j≤N, i \neq ji≠j, such that A_i + A_jA
​i
​​ +A
​j
​​  is odd.

Standard input
The first line contains a single integer NN.

The second line contains NN integers representing the elements of AA.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq N \leq 1001≤N≤100
1 \leq A_i \leq 1001≤A
​i
​​ ≤100
Input	Output
4
1 2 3 4
4
4
1 1 3 3
0
5
1 1 1 2 2
6
'''
noe = int(input())
arr = [int(x) for x in input().split()]
odds= sum([1 for x in arr if x%2==1])
print(odds * (noe - odds))