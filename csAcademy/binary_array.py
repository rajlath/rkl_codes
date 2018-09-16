'''
Find Binary Array
Time limit: 1000 ms
Memory limit: 256 MB

You have a binary array of length NN. For each index i (1 \leq i \leq N)i(1≤i≤N) you know the number of zeroes among the positions on the left side of ii and on the right side of ii, respectively. Find the array!

Standard input
The first line contains an integer NN, the length of the binary array.

The second line contains NN integer values, where the ii-th value represents the number of zeroes among the positions on the left side of the ii-th index of the array.

The third line contains NN integer values, where the ii-th value represents the number of zeroes among the positions on the right side of the ii-th index of the array.

Standard output
The first line will contain NN bits (00 or 11), representing the binary array.

Constraints and notes
2 \leq N \leq 10^52≤N≤10
​5
​​
It is guaranteed that there is always at least one solution
Input	Output
5
0 1 1 1 2
1 1 1 0 0
01101
'''
lens = int(input())
arrL = [int(x) for x in input().split()]
arrR = [int(x) for x in input().split()]
for i in range(1, lens):
    if arrL[i] != arrL[i-1]:
        print(0, end="")
    else:
        print(1, end="")
#arr  = [0 if b != a else 1 for a, b in zip(arrL, arrL[1:])]
print( 0 if arrR[-1] != arrR[-2] else 1, end="")

