'''
No Repeat
Time limit: 1000 ms
Memory limit: 256 MB

You are given a string SS of size NN. Find the first character of SS that occurs only once in the entire string. If there is no such character, output -1−1.

Standard input
The first line contains an integer NN.

The second line contains SS.

Standard output
Print the answer on the first line.

Constraints and notes
1 \leq N \leq 1001≤N≤100
SS consists of lowercase letters of the English alphabet
Input	Output
7
nothotn
h
6
ccaabb
-1

'''
lens = int(input())
s = input()
cache = []
repeat= set()
for i in s:
    if i in cache:
        cache.remove(i)
        repeat.add(i)
    elif i in repeat:
        continue
    else:
        cache.append(i)



print( -1 if len(cache)==0 else cache[0])