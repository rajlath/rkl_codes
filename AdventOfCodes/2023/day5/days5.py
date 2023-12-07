from collections import defaultdict

mapd = defaultdict(dict)

def buildmaps(arrs):
    all_maps = []
    
    for ln in arrs:
        if "-" in ln:
            maps = ln.split(" ")[0].split("-")
            all_maps.append(maps[2])            
            src,_,tgt = maps
            mapd[src][tgt] = []
        else:
            mapd[src][tgt].append([int(x) for x in ln.split()])
    return mapd, all_maps            
                
            
    
with  open("input.txt")  as f:
    lines = f.readlines()
seeds = [int(x.strip()) for x in lines[0].split(":")[1].split(" ") if x!=""]

maplines  = [x.strip() for x in lines[1:] if x != "\n"]
mapd, all_map = buildmaps(maplines)




min_loc = 1e9
for seed in seeds:
    current = "seed"
    value = seed

    for trg in all_map:
            for trg_start, src_start, length in mapd[current][trg]:
                if src_start <= value < src_start + length:
                    value = trg_start + (value - src_start)
                    break

            current = trg

            min_loc = min(min_loc, value)

print(min_loc)

