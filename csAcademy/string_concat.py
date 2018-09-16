#https://csacademy.com/contest/archive/task/string-concat/
'''
Input	Output
6       3 4
c
def
abcdef
abc
ab
c
'''
nos = int(input())
words = []
for _ in range(nos):
    words.append(input())
for i in range(nos):
    ok = False
    for j in range(nos):
        for k in range(nos):
            if j == k:continue
            ok =  words[i] == words[j][k]
print(i+1 if ok else '', end=" ")



