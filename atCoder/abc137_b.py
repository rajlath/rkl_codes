from collections import Counter
def get_hash(a):
    hash = 1
    ca = Counter(a)
    for x in ca:
        hash += ord(x) * ca[x]
    return hash

lens = int(input())
hashes = [''.join(sorted(input())) for _ in range(lens)]
ansv = Counter(hashes).values()
ans = sum([x//2 * 2 for x in ansv ])
print(ans)
