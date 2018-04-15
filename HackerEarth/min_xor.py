def maxXor(arr):
    min_xor = int(10e9)
    base  = 1
    tbase = 1
    val = 1
    variance = 0
    while base < len(arr):
        while (tbase+variance < len(arr)):
            val = base ^ (tbase + variance)
            min_xor = min(min_xor, val)
            variance += 1
        print(min_xor)
        base += 1
        variance = 0
    return min_xor

print(maxXor([5,2,3]))