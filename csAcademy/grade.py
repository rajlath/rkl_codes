'''
Risk Rolls
Time limit: 1000 ms
Memory limit: 256 MB

Alena and Boris are playing Risk today. We'll call an outcome the sum of values on the faces of 11 or more rolled dice. Alena has NN possible outcomes whilst Boris has MM. In turns, each one of them will choose their best possible available outcome and play it. If Alena's outcome is strictly greater than Boris's, then Alena wins; otherwise Boris wins. Whenever one of them runs out of outcomes, the game ends.

In how many turns does Alena win? What about Boris?

Standard input
The first line contains two integers NN and MM.

The second contains NN integers, Alena's possible outcomes.

The third line contains MM integers, Boris's possible outcomes.

Standard output
Print two integers AA and BB on the first line of the output; AA represents the number of turns won by Alena and BB the number of turns won by Boris.

Constraints and notes
1 \leq N, M \leq 101≤N,M≤10
1 \leq v \leq 241≤v≤24, where vv is a possible outcome value
Input	Output	Explanation
1 3
24
1 2 3
1 0
In the first turn, Alena will play 2424, which will beat Boris's 33
3 1
2 1 3
24
0 1
This is the first sample with reversed outcomes for Alena and Boris.

2 2
10 1
5 5
1 1
4 3
3 4 5 24
9 9 9
1 2
In the first turn Alena will beat Boris because she will play 2424.

3 3
8 9 10
10 8 8
1 2
In the first turn they will play 1010 against 1010 and Boris will win. On the second turn they will play 99 versus 88 and Alena will win. The third turn is also won by Boris.
'''
turns = min([int(x) for x in input().split()])
A = 0
B = 0
ai = [int(x) for x in input().split()]
bi = [int(x) for x in input().split()]

for i in range(turns):
    at = ai.pop(ai.index(max(ai)))
    bt = bi.pop(bi.index(max(bi)))
    if at > bt: A += 1
    else: B += 1

print(A, B)

