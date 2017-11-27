'''
SAMPLE INPUT
?ba??b
SAMPLE OUTPUT
ababab
Explanation
Words ababab, ababbb, bbabab and bbabbb could be written on paper. The first in alphabetical order is ababab.
'''

sl = [x for x in input().split()]
for i, v in enumerate(sl):
    if v in ["a", "b"]:continue
    if sl[i-1] == "a" or sl[i+1] == "a": sl[i] = "b"
    else:sl[i] = "a"
print("".join(sl))
