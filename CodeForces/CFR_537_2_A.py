'''
ins = [c in "aeiou" for c in input()]
out = [c in "aeiou" for c in input()]
print(["No", "Yes"][ins == out])
'''
vowels = 'aeiou'
ins = input()
out = input()
ans = "Yes"
if len(ins) != len(out):
    ans = "No"
else:
    for i, v in zip(ins, out)    :
        if i in vowels and v in vowels  or i not in vowels and v not in vowels:
            continue
        else:
            ans = "No"
            break
print(ans)