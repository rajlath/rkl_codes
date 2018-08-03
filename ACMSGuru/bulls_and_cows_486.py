'''
sample input
sample output
5071
6012
1 1

sample input
sample output
4321
4321
4 0
'''
a = input()
b = input()
cows = 0
bulls = 0
for i,v  in enumerate(a):
    if b[i] == v:
        cows += 1
    elif v in b:
        bulls += 1
print(cows, bulls)