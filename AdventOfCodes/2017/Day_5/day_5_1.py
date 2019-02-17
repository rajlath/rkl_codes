def is_Valid(s):
    done = []
    words= s.split()
    #print(words)
    for word in words:
        word = sorted(word)
        if word in done:
            return False
        done.append(word)
    return True

valid = 0
with open("input.txt") as f:
    for line in f:
        words = line.split()
        words = [''.join(sorted(word)) for word in words]
        valid += len(words) == len(set(words))
print(valid)



