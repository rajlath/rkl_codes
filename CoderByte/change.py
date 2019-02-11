def change(a):
    if a.isupper():
        return  chr((ord(a) - ord('A') +  1)%26 + ord("A"))
    else:
        return  chr((ord(a) - ord('a') +  1)%26 + ord("a"))

from string import  ascii_letters as al
def LetterChanges(str):
    ans = [change(x) if x in al else x  for x in str]
    ans = [x.upper() if x in "AEIOUaeiou"  else x for x in ans]
    return "".join(ans)