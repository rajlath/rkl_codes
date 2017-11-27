'''
https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/prefpref/

Find the maximal length of some prefix of the string S which occurs in strings T as subsequence.

SAMPLE INPUT
digger
biggerdiagram
SAMPLE OUTPUT
3
'''

t = input()
s = input()

cnt = 0
idx = 0

for v in t:
    cui = s.find(v, idx+1)
    if cui == -1:break
    if cui >= idx:
        idx = cui
        cnt +=1
print(cnt)


