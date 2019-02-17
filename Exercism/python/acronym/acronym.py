
from string import punctuation
from re import split
def abbreviate(words):
    lst = [x.strip(punctuation) for x in split("[ -]", words) if x !='']
    return "".join(x[0].upper() for x in lst)

