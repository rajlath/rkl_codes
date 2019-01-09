# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

nb_animal, nb_legs, nb_horns = [int(x) for x in input().split()]
for i in range(nb_horns+1):
    nb_rams = (nb_horns - i) // 2
    nb_chic = nb_animal - i - nb_rams
    if nb_chic < 0:continue
    if nb_chic * 2 + (i + nb_rams) * 4 == nb_legs:       
        break
print(i)    
    
        
        
    
            
            
    