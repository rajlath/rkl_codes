'''
A. Polycarp's Pockets
time limit per test 1 second
memory limit per test 256 megabytes
input standard input
output standard output

Polycarp has n coins, the value of the i -th coin is a i .Polycarp wants to distribute all the coins between his pockets,
but he cannot put two coins with the same value into the same pocket.
For example, if Polycarp has got six coins represented as an array
a = [1,2,4,3,3,2] ,he can distribute the coins into two pockets as follows:[1,2,3],[2,3,4].

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.

Input
The first line of the input contains one integer
n (1≤n≤100) — the number of coins.

The second line of the input contains
n  integers a 1,a 2,…,a n (1≤ai≤100) — values of coins.

Output
Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the
same value are put into the same pocket.

Examples
input
6
1 2 4 3 3 2
output
2
input
1
100
output
1
'''
from collections import Counter
noe = int(input())
print(max(Counter([int(x) for x in input().split()]).values()))
