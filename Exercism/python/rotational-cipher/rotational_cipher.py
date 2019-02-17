def rotate(text, key):
    rets = ''
    for i in text:
        if i.isupper():
            rets += chr((((ord(i) - ord("A")) + key) % 26) + ord("A"))
        elif i.islower():
            rets += chr((((ord(i) - ord("a")) + key) % 26) + ord("a"))
        else:
            rets += i
    return rets


#print(rotate('OMG', 5))
