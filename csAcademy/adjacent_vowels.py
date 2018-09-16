'''
Adjacent Vowels
Time limit: 1000 ms
Memory limit: 256 MB

You are given a string SS consisting of NN lowercase letters of the English alphabet. Count the number of adjacent pairs of vowels.

In this problem, we consider there are 55 letters that represent vowels: a, e, i, o and u.

Standard input
The first line contains a single integer NN.

The second line contains the string SS.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq N \leq 10001≤N≤1000
Input	Output	Explanation
5
aeoui
4
(ae)oui(ae)oui

a(eo)uia(eo)ui

ae(ou)iae(ou)i

aeo(ui)aeo(ui)

7
abaebio
2
ab(ae)bioab(ae)bio

abaeb(io)abaeb(io)

7
abcdefg
0
6
aabbcc
1
(aa)bbcc(aa)bbcc
'''
lens = int(input())
s = list(input())
stack = ["-"]
cnt = 0
for i in s:
    if i in "aeiou" and stack[-1] in "aeiou":
        cnt += 1
    stack.append(i)
print(cnt)

