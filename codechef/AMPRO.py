'''
Input:
Amal Kumar Perera

Output:
A.K.Perera
'''
s = [x for x in input().split()]
name = ([x[0].upper() for x in s[:-1]])
name = name +[s[-1].title()]

print(".".join(name))