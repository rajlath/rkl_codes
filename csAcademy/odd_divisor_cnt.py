'''
You are given two integers AA and BB. Count how many numbers in the interval [A, B][A,B] have an odd number of divisors.

Standard input
The first line contains the two integers AA and BB.

Standard output
Output a single number representing the number of values having an odd number of divisors.

Constraints and notes
1 \leq A \leq B \leq 10001≤A≤B≤1000
Input	Output
1 10
3
5 15
1
50 120
3
'''

a, b = [int(x) for x in input().split()]
res = 0
for i in range(a, b+1):
    divcnt = 0
    for j in range(1, i+1):
        divcnt +=  i%j==0
    res += divcnt % 2
print(res)