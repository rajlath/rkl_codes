'''
Example

Input:
bidhan


Output:
nbidha
Explanation

The rotations of string bidhan are

bidhan,
idhanb,
dhanbi,
hanbid,
anbidh and
nbidha.
'''
s = input()
indx = s.index(max(s))
ans  = s[indx:] + s[:indx]
print(ans)
