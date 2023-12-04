import re

with open('input.txt') as f:
    games = f.read().splitlines()

result_1 = 0 
result_2 = 0   
for game in games:
    game, sets = game.split(':')
    id = re.findall(r"\d+", game)[0]
    mr =  max(int(nos) for nos, col in  re.findall(r"(\d+) (red)", sets))
    mg =  max(int(nos) for nos, col in  re.findall(r"(\d+) (green)", sets))
    mb =  max(int(nos) for nos, col in  re.findall(r"(\d+) (blue)", sets))
    if mr <= 12 and mg <= 13 and mb <= 14:
        result_1 += int(id)
    result_2 += (mr * mg * mb )
    
print(result_2)       
        
            