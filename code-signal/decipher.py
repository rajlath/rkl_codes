def decipher(cipher):
    if cipher == "":return ""
    cipher = list(cipher)
    ret = ''
    i = 0
    ch= cipher.pop(0)
    while cipher:
        if len(ch)>0:
            if int(ch) not in range(97, 124):
                ch += cipher.pop(0)
            else:
                ret += chr(int(ch))
                if cipher:ch=cipher.pop(0)
    if ch:ret += chr(int(ch))
    return ret

print(decipher("10197115121"))
