LIMIT = int(10e5) + 6

def seive_generation():
    '''
    prime number generation process
    Generate a counter upto LIMIT that will store number of
    primes number that itself is prime and adding 6 will also
    be a prime
    '''
    seive = [False, False] + [True] * LIMIT
    ENDS = int(LIMIT ** 0.5)
    for i in range(2, ENDS):
        if seive[i]:
            j = i * i
            while j < LIMIT:
                seive[j] = False
                j += i

    #create a counter for hexprimes
    counter = [0] * LIMIT
    counts  =  0
    for i in range(2, LIMIT - 6):
        if seive[i] and seive[i+6]:counts += 1
        counter[i] = counts
    return counter

counts = seive_generation()
nb_test = int(input())
for _ in range(nb_test):
    current = int(input())
    print(counts[current])

