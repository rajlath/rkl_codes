'''
Monotone Subarray
Time limit: 1000 ms
Memory limit: 256 MB

You are given an array AA of size NN. Consider the following definitions:

An array is non-increasing if for every ii, A_i \geq A_{i+1}A
​i
​​ ≥A
​i+1
​​ .
Similarly, it is non-decreasing if for every ii, A_i \leq A_{i+1}A
​i
​​ ≤A
​i+1
​​ .
An array is monotone if it is non-increasing or non-decreasing.
Find the longest monotone subarray.

Standard input
The first line contains a single integer NN.

The second line contains NN integers represent the elements of AA.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq N \leq 10^51≤N≤10
​5
​​
1 \leq A_i \leq 2 * 10^51≤A
​i
​​ ≤2∗10
​5
​​
Input	Output	Explanation
7
1 2 3 4 3 2 1
4
The longest monotone array is 1\ 2\ 3\ 41 2 3 4
5
3 2 1 1 2
4
3\ 2\ 1\ 13 2 1 1
7
1 2 2 2 3 3 4
7
The whole array is non-decreasing

9
3 4 2 1 1 4 5 6 3
5
1\ 1\ 4\ 5\ 61 1 4 5 6

'''
def get_length_increasing(arr):
    ans = 0
    last_high = int(10e9)
    curr_num = 0
    for i in arr:
        if last_high > i:
            ans = max(ans, curr_num)
            curr_num = 1
        else:
            curr_num += 1
        last_high = i
    ans = max(ans, curr_num)
    return ans

lens = int(input())
arrs = [int(x) for x in input().split()]
print(max(get_length_increasing(arrs), get_length_increasing(arrs[::-1])))

