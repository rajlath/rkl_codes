'''
18
    14 16 20 2
'''
def countSetBits( n ):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Function that return count of
# flipped number
def FlippedCount(a , b):

    # Return count of set bits in
    # a XOR b
    return countSetBits(a^b)

M, N = [int(x) for x in input().strip().split()]
Ns   = [int(x) for x in input().strip().split()]
count = 0
for i in Ns:
    count += FlippedCount(M, i)
print(count)


