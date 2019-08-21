###Input:
#key = [9,20,21,9,2,28,26,14,14,12,0,11,16,4,10,5,1,6,27,6,25,23,20,13,4]
#crypttext = "HACKER"


def build_key_matrix(key):
    x = 0
    y = 0
    key_mat = []
    for i in range(16):
        for j in range(16):
            key_mat.append(key[x] ^ y)
            x += 1
            y += 1
            if x == len(key):x = 0
    return key_mat

key = [int(x) for x in input().strip().split(",")]
crypttext = input().strip()
key_mat = build_key_matrix(key)
decoded = ''
for i in range(len(key)):
    decoded += chr(key_mat[i] ^ ord(crypttext[i%len(crypttext)]))
print(decoded)

'''
decoded = ''
for i in range(len(key)):


key_mat = build_key_matrix(key)
pt_mat = [x for x in plaintext]
pt_mat = pt_mat + ['0'] * max(0, (256 - len(plaintext)))
pt_mats = []
x = 0
for i in range(16):
    current = []
    for j in range(16):
        current.append(pt_mat[x])
        x += 1
    pt_mats.append(current)

cyphertext = "HACKER"
def build_crypt_matrix(ciphertexts):
    x = 0
    ct_mat = []
    for i in range(16):
        current = []
        for j in range(16):
            current.append(cyphertext[x])
            x += 1
            if x == len(cyphertext):x = 0
        ct_mat.append(current)
    return ct_mat

ct_mat = build_crypt_matrix(cyphertext)

decoded = ''





decoded = []
for i in range(16):
    current = []
    for j in range(16):
        current.append(chr(key_mat[i][j] ^ ord(ct_mat[i][j])))
    decoded.append(current)
print(decoded)
'''
