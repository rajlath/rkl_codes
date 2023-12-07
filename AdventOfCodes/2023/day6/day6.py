import re
def get_valid_times(secs, dist):
    covered = 0
    can_do = 0
    speed = 0
    indx = 0
    slens = len(secs)
    result_1 = 1
    for indx in range(slens):
        to_cover = dist[indx]
        in_time  = secs[indx]
        for idx in range(in_time):
            need = (secs[indx] - indx) * idx
            if need > to_cover:
                can_do += 1
                
        result_1 *= can_do
    return result_1    
            
        
        
    


with open("input.txt") as f:
    data = f.readlines()
    times = list(map(int,re.findall(r"\d+",data[0].split(":")[1].strip())))    
    distance = list(map(int,re.findall(r"\d+",data[1].split(":")[1].strip())))

print(get_valid_times(times, distance)    )
    