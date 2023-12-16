def get_hash(strs, current = 0):
    for c in strs:
        current += ord(c)
        current *= 17
        current  = current % 256
    return current

data = open("input.txt").readline()


buckets = [{} for _ in range(256)]
for step in data.strip().split(","):
    if step.endswith("-"):
        key = step[:-1]
        buckets[get_hash(key)].pop(key, None)
    elif "=" in step:
        key = step[: step.index("=")]
        buckets[get_hash(key)][key] = int(step[step.index("=") + 1 :])
print(sum(
        (i + 1) * sum((j + 1) * n for j, n in enumerate(bucket.values()))
        for i, bucket in enumerate(buckets)
    ))

        
       

        

        
        