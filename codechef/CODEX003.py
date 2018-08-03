'''
###Sample Input :
this is fun

###Sample Output:
tothohisos isos fofunon
'''
s = input()
o = ''
for i in s:
    if i in "AEIOU " or i in "aeiou ":
        o+=i
    else:o += i +"o"+i
print(o)