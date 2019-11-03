def substitutionCipherDecryption(contents, signature, encryptedSignature):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    text = ["*"] * 26
    for i in range(26):
        if alpha[i] in signature:
            text[i] =encryptedSignature[signature.index(alpha[i])]
    for i in alpha:
        if i not



substitutionCipherDecryption("issomtoqmvjts","alice","james")


'''
plaintext alphabet:  abcdefghijklmnopqrstuvwxyz
                     jbecsdfgmhiaklnopqrtuvwxyz
                     j e s     m   a

                    james
                    alice
ciphertext alphabet: j*e*s***m**a**************

'''