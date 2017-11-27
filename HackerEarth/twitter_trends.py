'''
SAMPLE INPUT
10
Donald Trump becomes the 45th #US President
Potentially habitable exoplanet #ProximaB discovered
#RogerFederer wins #US Open for 5th time
#GravitationalWaves detection successful
Traces of liquid water discovered on #Mars
Life Could Survive on Exoplanet #ProximaB
Go go #RogerFederer
Ten ways #ProximaB is different from Earth
ISRO becomes 4th space agency to reach #Mars
#RogerFederer beats #Nadal
#ProximaB
#RogerFederer
#Mars

#US
#GravitationalWaves
'''
trends = {}
for _ in range(int(input())):
    s = [x for x in input().split() if x[0]=="#"]
    for i in s:
        trends[i] = trends.get(i, 0) + 1
trend_cnt = sorted(trends.items(), key=lambda x: (-x[1],x[0]))
i = 0
for k,v in trend_cnt:
    print(k)
    i += 1
    if i == 5:
        break
