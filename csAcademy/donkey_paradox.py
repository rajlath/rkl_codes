'''
Donkey Paradox
Time limit: 1000 ms
Memory limit: 128 MB

On a field represented as a matrix of NN rows and MM columns there is a donkey and two haystacks.

The donkey is really hungry and he wants to get to a haystack as fast as possible. He can walk in four directions: up, down, left or right. The paradox of the donkey is that if the two haystacks are equally close to him he won't be able to decide which one to choose and he will starve to death.

You are given the cells of the haystackes, but you don't know where the donkey is. Compute the number of cells where the donkey will starve if he's there.

Standard input
The first line contains the two integers NN and MM.

The second line contains two integers representing the row and the column of the first haystack.

The third line contains two integers representing the row and the column of the second haystack.

Standard output
Output a single number representing the number of cells where the donkey will starve if he's there.

Constraints and notes
2 \leq N, M \leq 2002≤N,M≤200
The haystacks and the donkey are situated in three different cells.
The donkey takes into consideration only shortest routes to the haystacks.
Input	Output	Explanation
6 6
2 5
4 4
0
There are no cells equally close to the two haystacks.

5 5
2 4
5 3
5
The donkey will starve if he is one of these cells:

(3, 1)(3,1)
(3, 2)(3,2)
(3, 3)(3,3)
(4, 4)(4,4)
(4, 5)(4,5)
4 4
1 3
2 4
10
(1,4)(1,4)
(2,1)(2,1)
(2,2)(2,2)
(2,3)(2,3)
(3,1)(3,1)
(3,2)(3,2)
(3,3)(3,3)
(4,1)(4,1)
(4,2)(4,2)
(4,3)(4,3)
4 4
2 1
1 2
10
(1,1)(1,1)
(2,2)(2,2)
(2,3)(2,3)
(2,4)(2,4)
(3,2)(3,2)
(3,3)(3,3)
(3,4)(3,4)
(4,2)(4,2)
(4,3)(4,3)
(4,4)(4,4)
'''
N, M = [int(x) for x in input().split()]
poss = [ [0 for i in range(M)] for j in range(N)]
x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
starv = 0
for i in range(N):
    for j in range(M):
        x, y = i, j
        if (abs(i - x1) + abs(j - y1)) == (abs(i - x2) + abs(j - y2)):
            starv += 1
print(starv)
