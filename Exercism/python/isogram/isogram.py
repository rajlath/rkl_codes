def is_isogram(string):
    string = "".join(x.lower() for x in string if x.isalpha())
    return len(set(string)) == len(string)


