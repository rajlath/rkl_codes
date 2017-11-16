def count_set_bits(n):
    return bin(int(n))[2:].count("1")
    
for _ in range(int(input())):
    available, choose = [int(x) for x in input().split()]
    cakes = [int(x) for x in input().split()]
    set_count = []
    for i in cakes:
        set_count.append(count_set_bits(i))
    
    print(sum((sorted(set_count, reverse = True)[:choose])))
