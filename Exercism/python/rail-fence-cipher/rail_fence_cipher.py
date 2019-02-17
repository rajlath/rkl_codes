
def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    if 0: # debug
        for rail in fence:
            print( ''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]


def encode(message, rails):
    return ''.join(fence(message, rails))


def decode(encoded_message, rails):
    rng = range(len(encoded_message))
    pos = fence(rng, rails)
    return ''.join(encoded_message[pos.index(n)] for n in rng)
