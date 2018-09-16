'''
Word Permutation
Time limit: 1000 ms
Memory limit: 128 MB

Alex has a list of NN distinct words and a permutation \sigmaσ of size NN. Initially, the words in the list are sorted lexicographically. Alex changes the order of the words according to the permutation: the new position of the iith word is \sigma(i)σ(i). You are given the permuted list of words and are asked to compute the permutation \sigmaσ.

Standard input
The first line contains a single integer value NN.

Each of the following NN lines contains a single string, representing one of the words.

Standard output
The output should contain NN values representing the permutation \sigmaσ.

Constraints and notes
1 \leq N \leq 10^51≤N≤10
​5
​​
The sum of lengths of the strings is ≤ 10^510
​5
​​
The strings will contain only lower case letters of the English alphabet.
Input	Output
3
xyz
abc
foo
2 3 1
6
cloud
algorithms
complexity
development
python
java
2 1 3 4 6 5

'''
now = int(input())
words = []
for i in range(now):
    words.append(input())
wordss = sorted(words)
for i in wordss:
    print(words.index(i)+1, end=" ")




