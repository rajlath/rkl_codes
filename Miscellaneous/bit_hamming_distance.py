def hamming_dist(a, b):
    z = a ^ b
    z = bin(z)[2:]
    return z.count("1")


def sum_pair_hamming_dist(a):
    




print(hamming_dist(1, 4))