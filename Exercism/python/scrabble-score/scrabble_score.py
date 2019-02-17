def score(word):
    key = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
    val = [1] * 10 + [2] * 2 + [3] * 4 + [4] * 5 + [5] * 1 + [8] * 2 +[10] * 2
    return sum([val[key.index(x.upper())] for x in word])




