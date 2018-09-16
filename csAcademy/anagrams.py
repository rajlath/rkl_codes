'''
Anagrams
Time limit: 1000 ms
Memory limit: 128 MB

You are given a list of NN words (strings containing only lower case letters of the English alphabet). We consider two words to be equivalent if they contain the same letters, i.e. we can rearrange the letters of one word in order to obtain the other word.

Compute the size of the largest subset of equivalent words.

Desired solution
You should assume the input is quite large (there are about 10^510
​5
​​  letters in total).

Standard input
The first line contains a single integer value NN.

Each of the following NN lines contains a single string, representing one of the words.

Standard output
The output should contain a single integer representing the size of the largest subset of equivalent words.

Constraints and notes
1 \leq N \leq 10^51≤N≤10
​5
​​
The sum of lengths of all the words is a number between 11 and 10^510
​5
​​ .
The strings contain only lower case letters of the English alphabet.
Input	Output	Explanation
6
cats
caller
dogs
cellar
parrots
recall
3
caller, cellar and recall are (the only) equivalent words.

8
disease
burned
viewer
praised
despair
burden
diapers
review
3
praised, despair and diapers form the largest set

'''
from collections import defaultdict
sames = defaultdict(list)
n = int(input())
lens = []
for i in range(n):
    s = input()
    s = "".join(sorted(s))
    #print(s)
    sames[s] = sames.get(s, 0) + 1
#print(sames)
print(max(sames.values()))



