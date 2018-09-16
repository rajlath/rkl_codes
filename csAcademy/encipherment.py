'''
Encipherment
Time limit: 1000 ms
Memory limit: 256 MB

You are given a string SS and a permutation PP of the lowercase English alphabet. You are supposed to encode SS by the means of the following method: for every character cc in SS, we'll find its' order in the English alphabet; let it be ii. We will then replace cc with P_iP
​i
​​ .

Standard input
The first line contains SS.

The second line contains 2626 lowercase letters representing PP.

Standard output
Print the encoded string on the first line of the output.

Constraints and notes
1 \leq |S| \leq 1001≤∣S∣≤100
SS only consists of lowercase English letters
Input	Output	Explanation
csacademy
chtyvsduiaklqegonwmrzpxbfj
tmctcyvqf
Since 'c' is the third letter of the alphabet, its encoding will be 't'. The same for the rest of the letters.



'''
from string import ascii_lowercase as lc
text = input()
alpha= input()
ans = "".join([alpha[lc.index(x)] for x in text])
print(ans)





