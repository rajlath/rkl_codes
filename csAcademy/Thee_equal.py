'''
Three Equal
Time limit: 1000 ms
Memory limit: 256 MB

You are given an array AA of NN integers between 00 and 22. With cost 11 you can apply the following operation A_i = ((A_i + 1)\ \% \ 3)A
​i
​​ =((A
​i
​​ +1) % 3).

Find the minimum cost to make all elements equal.

Standard input
The first line contains one integer NN.

The second line contains NN integers representing the elements of the array AA.

Standard output
Output a single number representing the minimum cost to make all elements of AA equal.

Constraints and notes
1 \leq N \leq 10^31≤N≤10
​3
​​
The elements of the array AA are integers between 00 and 22.
Input	Output
4
1 0 0 2
3
3
1 2 2
1
3
1 1 1
0
'''
from collections import Counter
lens = int(input())
s = [int(x) for x in input().split()]
sc = Counter(s)
ans = lens
for i in range(3):
    ans = min(ans, sc[(i+1)%3] * 2 + sc[(i+2) % 3])
print(ans)    