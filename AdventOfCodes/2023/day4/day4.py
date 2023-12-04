with open("input.txt") as f:
    lines = f.read().splitlines()
cards = [1 for x in range(len(lines))]    
res_part_1 = 0    
for index, line in enumerate(lines):
    data = line.split(":")
    wins, alls = data[1].split("|")
    wins = list(map(int, wins.strip().split()))
    alls = list(map(int, alls.strip().split()))    
    matching = set(wins) & set(alls)
    if matching:        
        res_part_1 += (2 ** (len(matching) - 1))
        for x in range(index+1, index+len(matching)+1):
            cards[x] += cards[index]
            
print(res_part_1)
print(sum(cards))     # answer for part_2  
       