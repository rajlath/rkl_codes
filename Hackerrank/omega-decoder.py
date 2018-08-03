'''
Sample Input 0

"Hello World"
Sample Output 0

"oW"
Sample Input 1

"My $ame i" khan"
Sample Output 1

"y$"k"
'''
s = input()[1:-1]
s = [x for x in s.split()]
t = ''
for i,v in enumerate(s):
    t += s[i][[-1, 0][i%2]]
print('"'+t+'"')