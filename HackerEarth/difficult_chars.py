'''
SAMPLE INPUT 
1
oomar
SAMPLE OUTPUT 
z y x w v u t s q p n l k j i h g f e d c b r m a o
'''
from string import ascii_lowercase as lc
alpha_count = dict(zip(lc, [0]*26))
for _ in range(int(input())):
    ins = input()
    for i in ins:
        alpha_count[i]+=1
alpha_count = sorted(alpha_count.items(), key=lambda x: (-x[1],x[0]), reverse=True)
print(' '.join(['{0}'.format(k, v) for k,v in alpha_count]))       


