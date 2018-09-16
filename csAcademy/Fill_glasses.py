'''
Balanced Number
Time limit: 1000 ms
Memory limit: 128 MB

You are given a positive number NN. We say the frequency of cc is equal to the number of digits of NN equal to cc.

NN is balanced if the frequency of all cc (0 \leq c \leq 90≤c≤9) is the same. Decide whether NN is balanced or not.

Standard input
The first line contains a single integer NN.

Standard output
If NN is balanced output 11, otherwise output 00.

Constraints and notes
The number of digits of NN is between 11 and 10001000
NN does not have leading zeroes, but NN can be 0
Input	Output	Explanation
1234567890
1
The number has all digits exactly once.

12345678905
0
55 occurs twice, while all the others only once.

1337
0
Several digits don't occur at all, for example 22 or 99.



'''
from collections import Counter
n = input()
freq = [0] * 10
for i in n:
    freq[int(i)] += 1
ans = 1
for i in freq:
    if i != freq[0]:
        ans = 0
        break
print(ans)

