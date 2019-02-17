def is_pangram(sentence):
    return len(set([x.lower() for x in sentence if x.isalpha()])) == 26


#print(is_pangram('abcdefghijklmnopqrstuvwxyz'))