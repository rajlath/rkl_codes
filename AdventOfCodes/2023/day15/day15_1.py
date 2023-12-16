def get_hash(strs, current = 0):
    for c in strs:
        current += ord(c)
        current *= 17
        current  = current % 256
    return current 

sample = open("input.txt").readline().split(",")
hash_val = sum([get_hash(sam) for sam in sample])
print(hash_val)


