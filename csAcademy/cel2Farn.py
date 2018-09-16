'''
Game of Chance
Time limit: 1000 ms
Memory limit: 256 MB

Alex and Ben are investors in the stock market. Initially Alex has AA dollars and Ben has BB dollars. Every second each of the two either wins or loses 11 dollar. Decide who has more money after NN seconds.

Standard input
The first line contains three integers NN, AA and BB.

The second line contains NN integers representing the wins and losses of Alex. The integers are either 11, in case of win, or -1−1, in case of a loss.

The third line contains NN integers representing the wins and losses of Ben. The integers are either 11, in case of win, or -1−1, in case of a loss.

Standard output
If Alex has more money in the end print 11. If Ben has more money print 22. If they have the same amount print 00.

Constraints and notes
0 \leq A, B \leq 10000≤A,B≤1000
1 \leq N \leq 10001≤N≤1000
It is guaranteed neither of them will ever have a negative amount of money
Input	Output	Explanation
5 2 3
1 -1 1 1 -1
-1 1 -1 -1 -1
1
\small 2+1-1+1+1-1=32+1−1+1+1−1=3

\small 3-1+1-1-1-1=03−1+1−1−1−1=0

4 1 3
1 1 -1 -1
1 -1 -1 -1
0
\small 1+1+1-1-1=11+1+1−1−1=1
\small 3+1-1-1-1=13+1−1−1−1=1
'''
n, a, b = [int(x) for x in input().split()]
ai = [int(x) for x in input().split()]
bi = [int(x) for x in input().split()]
print([0, 1][a + sum(ai) > b + sum(bi)])





