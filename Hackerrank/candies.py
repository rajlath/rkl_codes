'''
Sample Input 0

3
1
2
2
Sample Output 0

4
Explanation 0

Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies.
Hence optimal distribution will be 1, 2, 1.

Sample Input 1

10
2
4
2
6
1
7
8
9
2
1
Sample Output 1

19
Explanation 1

Optimal distribution will be 1 2 1 2 1 2 3 4 2 1

'''
n = int(input())
candies = [0] * n
ranks   = []
candies[0] = 1
for i in range(n):
    ranks.append(int(input()))
for i in range(1, n):
    if ranks[i-1] < ranks[i]:candies[i] = candies[i-1]+1
    else: candies[i] =  1

for i in range(n-2, -1, -1):
    if ranks[i] > ranks[i+1] and candies[i] <= candies[i+1]: candies[i] = candies[i+1]+1
#print(candies)
print(sum(candies))

