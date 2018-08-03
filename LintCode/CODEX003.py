'''
###Sample Input :
this is fun

###Sample Output:
tothohisos isos fofunon
'''
from string import ascii_letters as al
s = input()
a = ''
for x in s:
    if x in al and x not in "aeiou":
         a += x+'o'+x
    else:
        a += x
print(a)