from string import ascii_lowercase as al
alpha = al + al[::-1]
#print(alpha[alpha.index('o') + 26])

def encode(plain_text):
    decoded = ''
    for i in plain_text:
        if i.isalnum():
            if i.isdigit():
                decoded += i
            else:
                decoded += alpha[alpha.index(i.lower()) + 26]
    rets = []
    for i in range(0, len(decoded), 5):
        rets.append(decoded[i:i+5])
    return " ".join(rets)


def decode(ciphered_text):
    encoded = ''
    for i in ciphered_text:
        if i.isalnum():
            if i.isdigit():
                encoded += i
            else:
                encoded += alpha[alpha.index(i.lower()) + 26]
    return encoded


#print(decode("gvhgr mt123 gvhgr mt"))