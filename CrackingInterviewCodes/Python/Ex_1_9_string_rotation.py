'''
1.9 String Rotation:
Assume you have a method isSubstring which checks if one word is a substring
of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
using only one call to isSubstring
(e.g., "waterbottle" is a rotation of"erbottlewst").



params s1 : string :Source string
params s2 : string :String to check
return boolean True if string is a rotation of source else False
'''

# Adding s1 to itself and check if SS contains s2
def string_rotation(src, tgt):
    if len(src) != len(tgt):return False
    src += src
    return tgt in src

print(string_rotation("waterbottle","erbottlewat" ))
print(string_rotation("rajkumarlath", "lathrajkumar"))
print(string_rotation("rajkumarlath", "lathrajkuma"))

