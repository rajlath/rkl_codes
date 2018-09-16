'''
B. Obtaining the String

You are given two strings s  and t . Both strings have length n and
consist of lowercase Latin letters.
The characters in the strings are numbered from 1  to n .
You can successively perform the following move any number of times (possibly, zero):
swap any two adjacent (neighboring) characters of s (i.e. for any i = {1,2,…,n − 1 }
 you can swap s i and s i + 1).
You can't apply a move to the string t.
The moves are applied to the string s  one after another.

Your task is to obtain the string t  from the string s.
Find any way to do it with at most 10 4 such moves.
You do not have to minimize the number of moves, just find any sequence
of moves of length 10 4  or less to transform s  into t .

Input
The first line of the input contains one integer n  (1≤n≤50) — the length of strings s and t.
The second line of the input contains the string s consisting of n lowercase Latin letters.
The third line of the input contains the string t consisting of n lowercase Latin letters.

Output
If it is impossible to obtain the string t using moves, print "-1".
Otherwise in the first line print one integer k — the number of moves to transform s to t.
Note that k must be an integer number between 0 and 10 4 inclusive.

In the second line print k  integers c j  (1≤cj<n), where cj means that on the j-th move you swap characters
s cj  and s cj + 1.

If you do not need to apply any moves, print a single integer 0
In the first line and either leave the second line empty or do not print it at all.

Examples
inputCopy
6
abcdef
abdfec
outputCopy
4
3 5 4 5
inputCopy
4
abcd
accd
outputCopy
-1

Note In the first example the string s changes as follows: "abcdef"→ "abdcef"→ "abdcfe"→ "abdfce"→ "abdfec".
In the second example there is no way to transform the string s into the string t through any allowed moves.
'''
n=[int(k) for k in input().split(" ")][0]
s=input()
t=input()


res=[]
if sorted(s)!=sorted(t):
    print -1
else:
    for i in range(n):
        j=i
        while s[j]!=t[i]:
            j+=1
        for k in range(j-1,i-1,-1):
            res+=[k+1]
        s=s[:i]+s[j]+s[i:j]+s[j+1:]
    print (len(res))
    print (" ".join([str(k) for k in res]))









