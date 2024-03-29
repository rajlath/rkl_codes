'''
A permutation of size n is an array of size n such that each integer from 1 to n occurs exactly once in this array.
An inversion in a permutation p is a pair of indices (i, j) such that i > j and ai < aj. For example,
a permutation [4, 1, 3, 2] contains 4 inversions: (2, 1), (3, 1), (4, 1), (4, 3).

You are given a permutation a of size n and m queries to it. Each query is represented by two indices l and r
denoting that you have to reverse the segment [l, r] of the permutation. For example, if a = [1, 2, 3, 4] and
a query l = 2, r = 4 is applied, then the resulting permutation is [1, 4, 3, 2].

After each query you have to determine whether the number of inversions is odd or even.

Input
The first line contains one integer n (1 ≤ n ≤ 1500) — the size of the permutation.
The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ n) — the elements of the permutation.
These integers are pairwise distinct.

The third line contains one integer m (1 ≤ m ≤ 2·105) — the number of queries to process.

Then m lines follow, i-th line containing two integers li, ri (1 ≤ li ≤ ri ≤ n) denoting that i-th query is to
reverse a segment [li, ri] of the permutation. All queries are performed one after another.

Output
Print m lines. i-th of them must be equal to odd if the number of inversions in the permutation after i-th query is odd,
and even otherwise.

Examples
input
3
1 2 3
2
1 2
2 3
output
odd
even
input
4
1 2 4 3
4
1 1
1 4
1 4
2 3
output
odd
odd
odd
even
Note
The first example:

after the first query a = [2, 1, 3], inversion: (2, 1);
after the second query a = [2, 3, 1], inversions: (3, 1), (3, 2).
The second example:

a = [1, 2, 4, 3], inversion: (4, 3);
a = [3, 4, 2, 1], inversions: (3, 1), (4, 1), (3, 2), (4, 2), (4, 3);
a = [1, 2, 4, 3], inversion: (4, 3);
a = [1, 4, 2, 3], inversions: (3, 2), (4, 2).
'''


from sys import stdin, stdout
input, print = stdin.readline, stdout.write
n = int(input())
a = [int(i) for i in input().split()]
c = 0
for i in range(n):
    for j in range(i + 1, n):
        c += int(a[i] > a[j])
c %= 2
q = int(input())
for i in range(q):
    l, r = [int(i) for i in input().split()]
    c ^= (r - l) * (r - l + 1) // 2 % 2
    print("odd\n" if c else "even\n")