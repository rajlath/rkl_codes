'''
8
atuongih
'''
vowels ="aeiou"
svowel = set()
has_all = "NO"
_ = input()
for i in list(input()):
    print(i)
    if i in vowels and i not in svowel:
        svowel.add(i)
        if len(svowel)==5:
            has_all = "YES"
            break
print(has_all)            
