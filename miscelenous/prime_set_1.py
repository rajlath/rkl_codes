class prime_set(set):
     """A PrimeSet object acts like the set of prime numbers:
     ps = prime_set()
     13 in ps  //True
     list(ps)  //[2, 3, 5, 7, 11, 13] have list upto 13 now
     """
     instance = None
     def __new__(cls):
        if cls.instance is None:
            cls.instance = super(prime_set, cls).__new__(cls)
        return cls.instance
        
     def __init__(self):
        super(prime_set, self).__init__()
        self.max = 1            # Highest number sieved to so far.
        self.set = set()        # Set of primes up to self.max. 
        
     def __iter__(self):
        return iter(self.set)

     def __len__(self):
        return len(self.set)

     def __contains__(self, key):
        try:
            key = int(key)
        except ValueError:
            return False
        if key > self.max:
            self.find_primes(key)
        return key in self.set
        
     def find_primes(self, n):
        """Sieve for primes from self.max + 1 up to and including n."""
        if n <= self.max:
            return
        sieve = [True] * (n - self.max)
        for p in self:
            for i in range(p - 1 - self.max % p, len(sieve), p):
                sieve[i] = False
        for p, isprime in enumerate(sieve):
            if isprime:
                p += self.max + 1
                self.set.add(p)
                for i in range(p * p - self.max - 1, len(sieve), p):
                    sieve[i] = False
        self.max = n
        
ps = prime_set()
print(53 in ps)
print(sorted(list(ps)))
