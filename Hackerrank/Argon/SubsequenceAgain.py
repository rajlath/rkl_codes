'''
Subsequence Again
You are provided with a string  and an integer . You have to find another string  which satisfies the following conditions:

 must be a subsequence of .
Every character in  must occur at least  times.
The length of  must be as large as possible.
If there are multiple strings for  with largest possible length, pick the lexicographically smallest one.
For example, let's say the string is  hackerrank and .

image

The solution for this is  akrrak. Here  is a subsequence of , it contains the characters ,  and  repeated at least  times. And, it is the only longest possible subsequence that satisfies the conditions.

Input Format

The first line contains a string  denoting the original string. 
The second line contains an integer .

Constraints

String  will only contain lowercase English characters.
Every input will have a valid solution.
Output Format

Print the string  on a single line.

Sample Input 0

hackerrank
2
Sample Output 0

akrrak
Explanation 0

In 'akrrak', all the characters occur exactly 2 times.

Sample Input 1

baaabaacba
3
Sample Output 1

baaabaaba
Explanation 1

In 'baaabaaba', 'a' occurs 6 times which is greater than 3 and 'b' occurs exactly 3 times.
'''

from collections import Counter
candidate = input().strip()
NoOfOccur = int(input().strip())
ccandidate= Counter(candidate)	
output = ""
for ch in candidate:			
	if ccandidate[ch] >= NoOfOccur:
		output += ch
		
print(output)	

		
	
	
	
		
		
		
		
			
		
		
