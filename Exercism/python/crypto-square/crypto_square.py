from math import ceil

def encode(clear_text):
    """Encipher a message using a crypto square"""
    if len(clear_text) == 0: return ''
    clear_text = [c for c in clear_text.lower() if c.isalnum()]
    square_size = int(ceil(len(clear_text)**0.5))
    cipher_text = [clear_text[i::square_size] for i in range(square_size)]
    cols = len(cipher_text[0])
    for i in range(len(cipher_text)):
        if len(cipher_text[i]) != cols:
            cipher_text[i] += [' '] * (cols - len(cipher_text[i]))
    return ' '.join([''.join(text) for text in cipher_text])
#print(encode("chill out"))