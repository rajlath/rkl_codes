for i in range(int(input())):
    nol = int(input())
    mw  = 2 * nol - 1
    forms = '{:^'+str(mw)+'}'
    
    for i in range(1, nol+1):
        print(forms.format("*"*(2*i -1)))
        
import re
print(len(re.findall("\d+", "sadw96aeafae4awdw2wd100awd")))

