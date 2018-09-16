'''
Two Coins
Time limit: 1000 ms
Memory limit: 256 MB

You are given NN coins, where the ii-th coin has a value of v_iv
​i
​​ , for each ii between 11 and NN. How many different amounts can you pay using exactly 2 coins?

Standard input
The first line contains an integer NN, the number of coins.

The second line contains NN integers representing the values of the NN coins.

Standard output
Print the answer on the first line of the output.

Constraints and notes
1 \leq N \leq 101≤N≤10
1 \leq v_i \leq 101≤v
​i
​​ ≤10, for each ii, where 1 \leq i \leq N1≤i≤N
Input	Output	Explanation
4
2 2 1 3
3
The amounts that can be paid ar
'''
n = int(input())
c = [int(x) for x in input().split()]
sums = set()
for i in range(n):
    for j in range(i+1, n):
        sums.add(c[i] + c[j])

print(len(sums))

