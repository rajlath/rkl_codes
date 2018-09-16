'''
import collections

def sieve(n):
    m = (n-1) // 2
    b = [True]*m
    i,p,ps = 0,3,[2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i+=1; p+=2
    while i < m:
        if b[i]:
            ps.append(p)
        i+=1; p+=2
    return ps

def seive_1(n):
    primes = [True] * (n+10)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*2, n+10, p):
                primes[i] = False
        p += 1
    return primes

def Trie():
    return collections.defaultdict(Trie)


#primes = seive_1(10 ** 6)
#print(primes[:20])

nb_test = int(input())
for _ in range(nb_test):
    nb_element = int(input())
    elements   = [int(x) for x in input().split()]
    #print()
    evens = sum([1 for x in elements if x%2==0])
    odds  = nb_element - evens
    print( evens * odds // 2)
    #evens = len(set(evens))
    #print(evens, odds)
    #print(evens)

    even = 0
    odd  = 0
    for element in elements:
        if element % 2 == 0:
            even += 1
            if element == 2 or element == 0:
                continue
        else:
            odd += 1


    cnt = 0
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            curr = elements[i] ^ elements[j]
            if curr%2==0 and curr != 2 and curr != 0:
                cnt += 1
    print(cnt)



            if :
            pair1.append(elements[i]^elements[j])



    root = Trie()
    valid= 0
    pairs = []
    for element in elements:
        candidate = 0
        cur = this = root
        for i in range(32)[::-1]:
            curBit = element >> i & 1
            this = this[curBit]
            if curBit ^ 1 in cur:
                candidate += 1 << i
                pairs.append(candidate)
                cur = cur[curBit ^ 1]
            else:
                cur = cur[curBit]

        pair1 = []


        arr = pair1[:]
        count = 0
        for i in range(len(pair1)):
            if arr[i] % 2 == 0 and arr[i] != 0 and arr[i] != 2:
                count += 1
        print(count)
'''
import collections
def Trie():
    return collections.defaultdict(Trie)
nb_test = int(input())
for _ in range(nb_test):
    nb_element = int(input())
    elements   = [int(x) for x in input().split()]

    root = Trie()
    valid= 0
    for element in elements:
        candidate = 0
        cur = this = root
        for i in range(32)[::-1]:
            curBit = element >> i & 1
            this = this[curBit]
            if curBit ^ 1 in cur:
                candidate += 1 << i
                cur = cur[curBit ^ 1]
            else:
                cur = cur[curBit]
        print(candidate,end = " ")
        if candidate % 2 == 0 and candidate != 0: valid += 1
    print(valid)











